import hashlib
import json

from historic_doc_ingest.raw_cloud import (
    DEFAULT_ENDPOINT_URL,
    R2Client,
    RawCloudConfig,
    build_derived_asset_manifest,
    build_raw_cloud_manifest,
    load_raw_cloud_config,
)


def test_raw_cloud_manifest_hashes_raw_source_originals_with_stable_keys(tmp_path) -> None:
    first = tmp_path / "raw" / "sources" / "record one.txt"
    second = tmp_path / "raw" / "sources" / "nested" / "record two.txt"
    generated = tmp_path / "raw" / "chunks" / "converted" / "manifest.json"
    placeholder = tmp_path / "raw" / "sources" / ".gitkeep"
    first.parent.mkdir(parents=True)
    second.parent.mkdir(parents=True)
    generated.parent.mkdir(parents=True)
    first.write_text("source text", encoding="utf-8")
    second.write_text("more source text", encoding="utf-8")
    generated.write_text('{"chunks": []}', encoding="utf-8")
    placeholder.write_text("", encoding="utf-8")

    config = RawCloudConfig(
        endpoint_url=DEFAULT_ENDPOINT_URL,
        bucket="genealogy-raw",
        access_key_id="test",
        secret_access_key="test",
        prefix="archive/",
    )

    manifest = build_raw_cloud_manifest(tmp_path, config)

    paths = {item["path"]: item for item in manifest["files"]}
    assert set(paths) == {
        "raw/sources/nested/record two.txt",
        "raw/sources/record one.txt",
    }
    assert paths["raw/sources/record one.txt"]["key"] == "archive/raw/sources/record one.txt"
    assert paths["raw/sources/record one.txt"]["sha256"] == hashlib.sha256(b"source text").hexdigest()
    assert manifest["manifest_path"] == "raw/r2-raw-sources.json"


def test_raw_cloud_config_reads_non_secret_config_and_env_file(tmp_path, monkeypatch) -> None:
    for name in [
        "R2_ACCOUNT_ID",
        "R2_ENDPOINT_URL",
        "R2_BUCKET",
        "R2_ACCESS_KEY_ID",
        "R2_SECRET_ACCESS_KEY",
        "R2_PREFIX",
    ]:
        monkeypatch.delenv(name, raising=False)

    (tmp_path / "raw").mkdir()
    (tmp_path / "raw" / "r2-storage.json").write_text(
        json.dumps(
            {
                "account_id": "account-from-config",
                "bucket": "bucket-from-config",
                "prefix": "config-prefix",
            }
        ),
        encoding="utf-8",
    )
    (tmp_path / ".env.r2").write_text(
        "\n".join(
            [
                "R2_BUCKET=bucket-from-env",
                "R2_ACCESS_KEY_ID=access-from-env",
                "R2_SECRET_ACCESS_KEY=secret-from-env",
                "R2_PREFIX=env-prefix",
            ]
        ),
        encoding="utf-8",
    )

    config = load_raw_cloud_config(tmp_path)

    assert config.endpoint_url == "https://account-from-config.r2.cloudflarestorage.com"
    assert config.bucket == "bucket-from-env"
    assert config.access_key_id == "access-from-env"
    assert config.secret_access_key == "secret-from-env"
    assert config.prefix == "env-prefix/"
    assert config.raw_dir.as_posix() == "raw/sources"


def test_raw_cloud_request_path_uses_path_style_bucket_and_encoded_key() -> None:
    config = RawCloudConfig(
        endpoint_url=DEFAULT_ENDPOINT_URL,
        bucket="genealogy-raw",
        access_key_id="test",
        secret_access_key="test",
    )
    client = R2Client(config)

    assert (
        client._request_path("raw/sources/Camara de Senadores #1.pdf")
        == "/genealogy-raw/raw/sources/Camara%20de%20Senadores%20%231.pdf"
    )


def test_derived_asset_manifest_includes_binary_outputs_not_text_state(tmp_path) -> None:
    page_image = tmp_path / "raw" / "codex-conversion-jobs" / "job-one" / "page-images" / "page-0001.jpg"
    crop = tmp_path / "raw" / "codex-conversion-jobs" / "job-one" / "extracted-images" / "page-0001" / "signature.png"
    page_markdown = tmp_path / "raw" / "codex-conversion-jobs" / "job-one" / "page-markdown" / "page-0001.md"
    raw_original = tmp_path / "raw" / "sources" / "record.pdf"
    page_image.parent.mkdir(parents=True)
    crop.parent.mkdir(parents=True)
    page_markdown.parent.mkdir(parents=True)
    raw_original.parent.mkdir(parents=True)
    page_image.write_bytes(b"fake jpg")
    crop.write_bytes(b"fake png")
    page_markdown.write_text("# Page 1\n", encoding="utf-8")
    raw_original.write_bytes(b"%PDF raw")

    config = RawCloudConfig(
        endpoint_url=DEFAULT_ENDPOINT_URL,
        bucket="genealogy",
        access_key_id="test",
        secret_access_key="test",
        prefix="archive/",
    )

    manifest = build_derived_asset_manifest(tmp_path, config)

    paths = {item["path"]: item for item in manifest["files"]}
    assert set(paths) == {
        "raw/codex-conversion-jobs/job-one/extracted-images/page-0001/signature.png",
        "raw/codex-conversion-jobs/job-one/page-images/page-0001.jpg",
    }
    assert (
        paths["raw/codex-conversion-jobs/job-one/page-images/page-0001.jpg"]["key"]
        == "archive/derived/raw/codex-conversion-jobs/job-one/page-images/page-0001.jpg"
    )
    assert manifest["manifest_path"] == "raw/r2-derived-assets.json"
