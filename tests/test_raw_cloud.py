import hashlib
import json

from historic_doc_ingest.raw_cloud import (
    DEFAULT_ENDPOINT_URL,
    R2Client,
    RawCloudConfig,
    build_derived_asset_manifest,
    build_raw_cloud_manifest,
    build_raw_cloud_manifest_from_remote,
    cleanup_disposable_derived_assets_from_cloud,
    load_raw_cloud_config,
    raw_cloud_manifest_item_matches_source_filter,
    restore_raw_from_cloud,
    restore_derived_asset_from_cloud,
    upload_derived_assets_to_cloud,
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
    low_value_crop = tmp_path / "raw" / "codex-conversion-jobs" / "job-one" / "extracted-images" / "page-0001" / "handwritten-marginalia.png"
    input_crop = tmp_path / "raw" / "codex-conversion-jobs" / "job-one" / "extracted-images" / "page-0001" / "_gemini-input-crops" / "zoom.png"
    vault_page_image = tmp_path / "research" / "_assets" / "conversions" / "source-one" / "page-images" / "page-0001.jpg"
    page_markdown = tmp_path / "raw" / "codex-conversion-jobs" / "job-one" / "page-markdown" / "page-0001.md"
    staged_source = tmp_path / "raw" / "codex-conversion-jobs" / "job-one" / "source" / "record.pdf"
    raw_original = tmp_path / "raw" / "sources" / "record.pdf"
    page_image.parent.mkdir(parents=True)
    crop.parent.mkdir(parents=True)
    low_value_crop.parent.mkdir(parents=True, exist_ok=True)
    input_crop.parent.mkdir(parents=True)
    vault_page_image.parent.mkdir(parents=True)
    page_markdown.parent.mkdir(parents=True)
    staged_source.parent.mkdir(parents=True)
    raw_original.parent.mkdir(parents=True)
    page_image.write_bytes(b"fake jpg")
    crop.write_bytes(b"fake png")
    low_value_crop.write_bytes(b"marginalia png")
    input_crop.write_bytes(b"temporary zoom crop")
    vault_page_image.write_bytes(b"vault page image")
    page_markdown.write_text("# Page 1\n", encoding="utf-8")
    staged_source.write_bytes(b"%PDF staged")
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
    }
    assert (
        paths["raw/codex-conversion-jobs/job-one/extracted-images/page-0001/signature.png"]["key"]
        == "archive/derived/raw/codex-conversion-jobs/job-one/extracted-images/page-0001/signature.png"
    )
    assert manifest["manifest_path"] == "raw/r2-derived-assets.json"


def test_remote_raw_cloud_manifest_lists_r2_raw_sources(monkeypatch, tmp_path) -> None:
    class FakeClient:
        def __init__(self, config):
            self.config = config

        def list_objects(self, prefix):
            assert prefix == "archive/raw/sources/"
            return [
                "archive/raw/sources/B.pdf",
                "archive/raw/sources/A image.jpg",
                "archive/derived/raw/codex-conversion-jobs/job/page-images/page-0001.jpg",
            ]

        def head_object(self, key):
            return {
                "content-length": "123",
                "content-type": "application/pdf" if key.endswith(".pdf") else "image/jpeg",
                "x-amz-meta-local-sha256": f"sha-for-{key.rsplit('/', 1)[-1]}",
            }

    monkeypatch.setattr("historic_doc_ingest.raw_cloud.R2Client", FakeClient)
    config = RawCloudConfig(
        endpoint_url=DEFAULT_ENDPOINT_URL,
        bucket="genealogy",
        access_key_id="test",
        secret_access_key="test",
        prefix="archive/",
    )

    manifest = build_raw_cloud_manifest_from_remote(tmp_path, config)

    paths = [item["path"] for item in manifest["files"]]
    assert paths == ["raw/sources/A image.jpg", "raw/sources/B.pdf"]
    assert manifest["source"] == "remote-r2-list"
    assert manifest["files"][0]["key"] == "archive/raw/sources/A image.jpg"
    assert manifest["files"][0]["sha256"] == "sha-for-A image.jpg"


def test_raw_cloud_restore_filters_manifest_to_requested_source(monkeypatch, tmp_path) -> None:
    restored = []
    keep_bytes = b"keep source"
    skip_bytes = b"skip source"
    manifest_path = tmp_path / "raw" / "r2-raw-sources.json"
    manifest_path.parent.mkdir(parents=True)
    manifest_path.write_text(
        json.dumps(
            {
                "files": [
                    {
                        "path": "raw/sources/keep.pdf",
                        "key": "archive/raw/sources/keep.pdf",
                        "bytes": len(keep_bytes),
                        "sha256": hashlib.sha256(keep_bytes).hexdigest(),
                    },
                    {
                        "path": "raw/sources/skip.pdf",
                        "key": "archive/raw/sources/skip.pdf",
                        "bytes": len(skip_bytes),
                        "sha256": hashlib.sha256(skip_bytes).hexdigest(),
                    },
                ]
            }
        ),
        encoding="utf-8",
    )

    class FakeClient:
        def __init__(self, config):
            self.config = config

        def get_file(self, key, output):
            restored.append((key, output.relative_to(tmp_path).as_posix()))
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_bytes(keep_bytes)

    monkeypatch.setattr("historic_doc_ingest.raw_cloud.R2Client", FakeClient)
    config = RawCloudConfig(
        endpoint_url=DEFAULT_ENDPOINT_URL,
        bucket="genealogy",
        access_key_id="test",
        secret_access_key="test",
        prefix="archive/",
    )

    report = restore_raw_from_cloud(tmp_path, config, manifest_path=manifest_path, source="keep.pdf")

    assert report["total_files"] == 1
    assert report["restored"] == 1
    assert restored == [("archive/raw/sources/keep.pdf", "raw/sources/keep.pdf")]
    assert (tmp_path / "raw" / "sources" / "keep.pdf").exists()
    assert not (tmp_path / "raw" / "sources" / "skip.pdf").exists()


def test_raw_cloud_manifest_item_matches_source_sha_and_path() -> None:
    item = {
        "path": "raw/sources/nested/record.pdf",
        "key": "archive/raw/sources/nested/record.pdf",
        "sha256": "ABC123",
    }

    assert raw_cloud_manifest_item_matches_source_filter(item, source="record.pdf", source_sha256="abc123")
    assert raw_cloud_manifest_item_matches_source_filter(item, source="raw/sources/nested/record.pdf")
    assert not raw_cloud_manifest_item_matches_source_filter(item, source="other.pdf")
    assert not raw_cloud_manifest_item_matches_source_filter(item, source_sha256="def456")


def test_derived_asset_upload_prunes_disposable_existing_manifest_entries(monkeypatch, tmp_path) -> None:
    deleted = []

    existing = {
        "version": 1,
        "files": [
            {
                "path": "raw/codex-conversion-jobs/job/page-images/page-0001.jpg",
                "key": "derived/raw/codex-conversion-jobs/job/page-images/page-0001.jpg",
                "bytes": 123,
                "sha256": "old-sha",
                "media_type": "image/jpeg",
            },
            {
                "path": "raw/codex-conversion-jobs/job/source/source.pdf",
                "key": "derived/raw/codex-conversion-jobs/job/source/source.pdf",
                "bytes": 456,
                "sha256": "source-sha",
                "media_type": "application/pdf",
            },
            {
                "path": "raw/codex-conversion-jobs/job/extracted-images/page-0001/portrait.png",
                "key": "derived/raw/codex-conversion-jobs/job/extracted-images/page-0001/portrait.png",
                "bytes": 789,
                "sha256": "crop-sha",
                "media_type": "image/png",
            },
            {
                "path": "raw/codex-conversion-jobs/job/extracted-images/page-0001/page-0001-image-01-handwritten-marginalia.png",
                "key": "derived/raw/codex-conversion-jobs/job/extracted-images/page-0001/page-0001-image-01-handwritten-marginalia.png",
                "bytes": 321,
                "sha256": "low-value-crop-sha",
                "media_type": "image/png",
            }
        ],
    }
    manifest_path = tmp_path / "raw" / "r2-derived-assets.json"
    manifest_path.parent.mkdir(parents=True)
    manifest_path.write_text(json.dumps(existing), encoding="utf-8")

    class FakeClient:
        def __init__(self, config):
            self.config = config

        def list_objects(self, prefix):
            if prefix == "derived/raw/codex-conversion-jobs/":
                return [
                    "derived/raw/codex-conversion-jobs/job/page-images/page-0001.jpg",
                    "derived/raw/codex-conversion-jobs/job/source/source.pdf",
                    "derived/raw/codex-conversion-jobs/job/extracted-images/page-0001/portrait.png",
                    "derived/raw/codex-conversion-jobs/job/extracted-images/page-0001/page-0001-image-01-handwritten-marginalia.png",
                ]
            if prefix == "derived/research/_assets/conversions/":
                return [
                    "derived/research/_assets/conversions/source-one/page-images/page-0001.jpg",
                    "derived/research/_assets/conversions/source-one/extracted-images/page-0001/portrait.png",
                ]
            raise AssertionError(prefix)

        def delete_object(self, key):
            deleted.append(key)
            return True

    monkeypatch.setattr("historic_doc_ingest.raw_cloud.R2Client", FakeClient)
    config = RawCloudConfig(
        endpoint_url=DEFAULT_ENDPOINT_URL,
        bucket="genealogy",
        access_key_id="test",
        secret_access_key="test",
    )

    summary = upload_derived_assets_to_cloud(tmp_path, config)

    assert summary["total_files"] == 0
    assert summary["deleted_disposable"] == 4
    assert deleted == [
        "derived/raw/codex-conversion-jobs/job/page-images/page-0001.jpg",
        "derived/raw/codex-conversion-jobs/job/source/source.pdf",
        "derived/raw/codex-conversion-jobs/job/extracted-images/page-0001/page-0001-image-01-handwritten-marginalia.png",
        "derived/research/_assets/conversions/source-one/page-images/page-0001.jpg",
    ]
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert [item["path"] for item in manifest["files"]] == [
        "raw/codex-conversion-jobs/job/extracted-images/page-0001/portrait.png"
    ]


def test_disposable_derived_asset_cleanup_strips_configured_prefix(tmp_path) -> None:
    deleted = []

    class FakeClient:
        def list_objects(self, prefix):
            if prefix == "archive/derived/raw/codex-conversion-jobs/":
                return [
                    "archive/derived/raw/codex-conversion-jobs/job/page-images/page-0001.jpg",
                    "archive/derived/raw/codex-conversion-jobs/job/extracted-images/page-0001/portrait.png",
                ]
            if prefix == "archive/derived/research/_assets/conversions/":
                return ["archive/derived/research/_assets/conversions/source-one/page-images/page-0001.jpg"]
            raise AssertionError(prefix)

        def delete_object(self, key):
            deleted.append(key)
            return True

    config = RawCloudConfig(
        endpoint_url=DEFAULT_ENDPOINT_URL,
        bucket="genealogy",
        access_key_id="test",
        secret_access_key="test",
        prefix="archive/",
    )

    summary = cleanup_disposable_derived_assets_from_cloud(tmp_path, config, client=FakeClient())

    assert summary["deleted"] == 2
    assert deleted == [
        "archive/derived/raw/codex-conversion-jobs/job/page-images/page-0001.jpg",
        "archive/derived/research/_assets/conversions/source-one/page-images/page-0001.jpg",
    ]


def test_restore_derived_asset_uses_deterministic_r2_key(monkeypatch, tmp_path) -> None:
    calls = []

    class FakeClient:
        def __init__(self, config):
            self.config = config

        def get_file(self, key, output):
            calls.append((key, output.relative_to(tmp_path).as_posix()))
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_bytes(b"jpeg bytes")

    monkeypatch.setattr("historic_doc_ingest.raw_cloud.R2Client", FakeClient)
    config = RawCloudConfig(
        endpoint_url=DEFAULT_ENDPOINT_URL,
        bucket="genealogy",
        access_key_id="test",
        secret_access_key="test",
        prefix="archive/",
    )

    target = tmp_path / "raw" / "assets" / "portrait.png"
    summary = restore_derived_asset_from_cloud(tmp_path, config, target)

    assert summary["restored"] == 1
    assert calls == [
        (
            "archive/derived/raw/assets/portrait.png",
            "raw/assets/portrait.png",
        )
    ]
