from __future__ import annotations

import base64
import datetime as dt
import hashlib
import hmac
import http.client
import json
import mimetypes
import os
import tempfile
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import quote, urlparse


EMPTY_SHA256 = hashlib.sha256(b"").hexdigest()
DEFAULT_ACCOUNT_ID = "e49bd1edd9fe4f9384b9cae226f7bf8a"
DEFAULT_ENDPOINT_URL = f"https://{DEFAULT_ACCOUNT_ID}.r2.cloudflarestorage.com"
DEFAULT_CONFIG_PATH = Path("raw") / "r2-storage.json"
DEFAULT_RAW_SOURCE_DIR = Path("raw") / "sources"
DEFAULT_STATE_DIR = Path(".genealogy") / "raw-cloud"
DEFAULT_RAW_CLOUD_MANIFEST_PATH = Path("raw") / "r2-raw-sources.json"
DEFAULT_DERIVED_ASSET_MANIFEST_PATH = Path("raw") / "r2-derived-assets.json"
DEFAULT_DERIVED_ASSET_KEY_PREFIX = "derived"
LEGACY_REMOTE_MANIFEST_KEYS = (
    "_manifests/raw-sources-cloud-manifest.json",
    "_manifests/derived-assets-cloud-manifest.json",
)
DEFAULT_DERIVED_ASSET_ROOTS = (
    Path("raw") / "codex-conversion-jobs",
    Path("raw") / "assets",
    Path("research") / "_assets",
)
TEXT_OR_CODE_SUFFIXES = {
    ".csv",
    ".html",
    ".htm",
    ".json",
    ".jsonl",
    ".log",
    ".md",
    ".py",
    ".ps1",
    ".rtf",
    ".toml",
    ".tsv",
    ".txt",
    ".xml",
    ".yaml",
    ".yml",
}
DERIVED_ASSET_MEDIA_TYPE_PREFIXES = ("image/", "audio/", "video/")
DERIVED_ASSET_MEDIA_TYPES = {
    "application/pdf",
    "application/octet-stream",
}


@dataclass(frozen=True)
class RawCloudConfig:
    endpoint_url: str
    bucket: str
    access_key_id: str
    secret_access_key: str
    prefix: str = ""
    account_id: str = DEFAULT_ACCOUNT_ID
    raw_dir: Path = DEFAULT_RAW_SOURCE_DIR
    state_dir: Path = DEFAULT_STATE_DIR
    timeout_seconds: int = 120


@dataclass(frozen=True)
class RawCloudFile:
    path: str
    key: str
    bytes: int
    sha256: str
    media_type: str


def read_env_file(path: Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        name, value = line.split("=", 1)
        name = name.strip()
        value = value.strip().strip('"').strip("'")
        if name and name not in os.environ:
            os.environ[name] = value


def read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return path


def load_raw_cloud_config(
    root: Path,
    *,
    env_file: Path | None = None,
    config_file: Path | None = None,
    endpoint_url: str | None = None,
    account_id: str | None = None,
    bucket: str | None = None,
    prefix: str | None = None,
    raw_dir: Path | None = None,
    state_dir: Path | None = None,
    require_credentials: bool = True,
) -> RawCloudConfig:
    root = root.resolve()
    env_path = env_file if env_file is not None else root / ".env.r2"
    if not env_path.is_absolute():
        env_path = root / env_path
    read_env_file(env_path)

    config_path = config_file if config_file is not None else root / DEFAULT_CONFIG_PATH
    if not config_path.is_absolute():
        config_path = root / config_path
    config = read_json(config_path)

    resolved_account_id = (
        account_id
        or os.environ.get("R2_ACCOUNT_ID")
        or str(config.get("account_id") or "")
        or DEFAULT_ACCOUNT_ID
    )
    resolved_endpoint = (
        endpoint_url
        or os.environ.get("R2_ENDPOINT_URL")
        or str(config.get("endpoint_url") or "")
        or f"https://{resolved_account_id}.r2.cloudflarestorage.com"
    )
    resolved_bucket = bucket or os.environ.get("R2_BUCKET") or str(config.get("bucket") or "")
    access_key_id = os.environ.get("R2_ACCESS_KEY_ID") or os.environ.get("AWS_ACCESS_KEY_ID") or ""
    secret_access_key = os.environ.get("R2_SECRET_ACCESS_KEY") or os.environ.get("AWS_SECRET_ACCESS_KEY") or ""
    resolved_prefix = prefix if prefix is not None else os.environ.get("R2_PREFIX", str(config.get("prefix") or ""))
    resolved_raw_dir = raw_dir or Path(str(config.get("raw_dir") or DEFAULT_RAW_SOURCE_DIR.as_posix()))
    resolved_state_dir = state_dir or Path(str(config.get("state_dir") or DEFAULT_STATE_DIR.as_posix()))

    missing = []
    if require_credentials:
        if not resolved_bucket:
            missing.append("R2_BUCKET")
        if not access_key_id:
            missing.append("R2_ACCESS_KEY_ID")
        if not secret_access_key:
            missing.append("R2_SECRET_ACCESS_KEY")
    if missing:
        raise ValueError(
            "Missing R2 configuration: "
            + ", ".join(missing)
            + ". Put these in .env.r2 or export them before running upload, verify, or restore."
        )

    return RawCloudConfig(
        endpoint_url=resolved_endpoint,
        bucket=resolved_bucket,
        access_key_id=access_key_id,
        secret_access_key=secret_access_key,
        prefix=normalize_prefix(resolved_prefix),
        account_id=resolved_account_id,
        raw_dir=resolved_raw_dir,
        state_dir=resolved_state_dir,
    )


def normalize_prefix(prefix: str) -> str:
    prefix = prefix.replace("\\", "/").strip("/")
    return f"{prefix}/" if prefix else ""


def normalize_key(key: str) -> str:
    return key.replace("\\", "/").lstrip("/")


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with open(long_fs_path(path), "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def file_size(path: Path) -> int:
    return os.stat(long_fs_path(path)).st_size


def long_fs_path(path: Path) -> str:
    value = os.path.abspath(os.fspath(path))
    if os.name != "nt":
        return value
    if value.startswith("\\\\?\\"):
        return value
    if value.startswith("\\\\"):
        return "\\\\?\\UNC\\" + value.lstrip("\\")
    return "\\\\?\\" + value


def relative_posix(path: Path, root: Path) -> str:
    rel = os.path.relpath(os.path.abspath(os.fspath(path)), os.path.abspath(os.fspath(root)))
    return Path(rel).as_posix()


def path_to_key(path: Path, root: Path, prefix: str) -> str:
    return f"{prefix}{relative_posix(path, root)}"


def scan_files(path: Path) -> list[Path]:
    files: list[Path] = []
    with os.scandir(long_fs_path(path)) as entries:
        for entry in entries:
            child = path / entry.name
            if entry.is_dir(follow_symlinks=False):
                files.extend(scan_files(child))
            elif entry.is_file(follow_symlinks=False) and entry.name != ".gitkeep":
                files.append(child)
    return files


def iter_raw_files(root: Path, raw_dir: Path) -> list[Path]:
    root = root.resolve()
    raw_root = raw_dir if raw_dir.is_absolute() else root / raw_dir
    if not raw_root.exists():
        raise FileNotFoundError(raw_root)
    return sorted(scan_files(raw_root), key=lambda path: relative_posix(path, root).lower())


def build_raw_cloud_manifest(
    root: Path,
    config: RawCloudConfig,
    *,
    limit: int | None = None,
) -> dict[str, Any]:
    root = root.resolve()
    files = []
    raw_files = iter_raw_files(root, config.raw_dir)
    if limit is not None and limit > 0:
        raw_files = raw_files[:limit]
    for path in raw_files:
        rel = relative_posix(path, root)
        media_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        files.append(
            RawCloudFile(
                path=rel,
                key=path_to_key(path, root, config.prefix),
                bytes=file_size(path),
                sha256=file_sha256(path),
                media_type=media_type,
            )
        )

    return {
        "version": 1,
        "created": dt.datetime.now(dt.timezone.utc).isoformat(),
        "purpose": "Cloud object inventory for immutable raw genealogy source originals.",
        "storage": {
            "provider": "cloudflare-r2",
            "account_id": config.account_id,
            "endpoint_url": config.endpoint_url,
            "bucket": config.bucket,
            "prefix": config.prefix,
        },
        "manifest_path": DEFAULT_RAW_CLOUD_MANIFEST_PATH.as_posix(),
        "raw_source_root": config.raw_dir.as_posix(),
        "files": [file.__dict__ for file in files],
    }


def raw_cloud_state_path(root: Path, config: RawCloudConfig, name: str) -> Path:
    state_dir = config.state_dir if config.state_dir.is_absolute() else root.resolve() / config.state_dir
    return state_dir / name


def write_raw_cloud_inventory(
    root: Path,
    config: RawCloudConfig,
    *,
    limit: int | None = None,
    out: Path | None = None,
) -> Path:
    manifest = build_raw_cloud_manifest(root, config, limit=limit)
    output = out or (root.resolve() / DEFAULT_RAW_CLOUD_MANIFEST_PATH)
    if not output.is_absolute():
        output = root.resolve() / output
    return write_json(output, manifest)


def is_derived_media_asset(path: Path) -> bool:
    if not path.is_file() or path.name == ".gitkeep":
        return False
    if path.suffix.lower() in TEXT_OR_CODE_SUFFIXES:
        return False
    media_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    if media_type.startswith(DERIVED_ASSET_MEDIA_TYPE_PREFIXES):
        return True
    return media_type in DERIVED_ASSET_MEDIA_TYPES


def iter_derived_asset_files(
    root: Path,
    asset_roots: tuple[Path, ...] = DEFAULT_DERIVED_ASSET_ROOTS,
) -> list[Path]:
    root = root.resolve()
    files: list[Path] = []
    for asset_root in asset_roots:
        resolved_root = asset_root if asset_root.is_absolute() else root / asset_root
        if not resolved_root.exists():
            continue
        files.extend(path for path in resolved_root.rglob("*") if is_derived_media_asset(path))
    return sorted(files)


def derived_asset_key(path: Path, root: Path, prefix: str) -> str:
    rel = path.resolve().relative_to(root.resolve()).as_posix()
    asset_prefix = normalize_prefix(DEFAULT_DERIVED_ASSET_KEY_PREFIX)
    return f"{prefix}{asset_prefix}{rel}"


def build_derived_asset_manifest(
    root: Path,
    config: RawCloudConfig,
    *,
    limit: int | None = None,
) -> dict[str, Any]:
    root = root.resolve()
    files = iter_derived_asset_files(root)
    if limit is not None and limit > 0:
        files = files[:limit]

    entries = []
    for path in files:
        rel = path.resolve().relative_to(root).as_posix()
        media_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        entries.append(
            RawCloudFile(
                path=rel,
                key=derived_asset_key(path, root, config.prefix),
                bytes=path.stat().st_size,
                sha256=file_sha256(path),
                media_type=media_type,
            )
        )

    return {
        "version": 1,
        "created": dt.datetime.now(dt.timezone.utc).isoformat(),
        "purpose": "Cloud object inventory for binary source-prep derivatives. JSON, Markdown, and code remain in GitHub.",
        "storage": {
            "provider": "cloudflare-r2",
            "account_id": config.account_id,
            "endpoint_url": config.endpoint_url,
            "bucket": config.bucket,
            "prefix": config.prefix,
        },
        "manifest_path": DEFAULT_DERIVED_ASSET_MANIFEST_PATH.as_posix(),
        "asset_roots": [path.as_posix() for path in DEFAULT_DERIVED_ASSET_ROOTS],
        "files": [entry.__dict__ for entry in entries],
    }


def write_derived_asset_inventory(
    root: Path,
    config: RawCloudConfig,
    *,
    limit: int | None = None,
    out: Path | None = None,
) -> Path:
    manifest = build_derived_asset_manifest(root, config, limit=limit)
    output = out or (root.resolve() / DEFAULT_DERIVED_ASSET_MANIFEST_PATH)
    if not output.is_absolute():
        output = root.resolve() / output
    return write_json(output, manifest)


class R2Client:
    def __init__(self, config: RawCloudConfig) -> None:
        self.config = config
        parsed = urlparse(config.endpoint_url)
        if parsed.scheme != "https" or not parsed.netloc:
            raise ValueError("R2 endpoint_url must be an https URL")
        self.host = parsed.netloc
        self.region = "auto"
        self.service = "s3"

    def head_object(self, key: str) -> dict[str, str] | None:
        response = self._request("HEAD", key, payload_hash=EMPTY_SHA256)
        if response.status == 404:
            response.close()
            return None
        if response.status >= 300:
            body = response.read().decode("utf-8", errors="replace")
            response.close()
            raise RuntimeError(f"HEAD {key} failed with HTTP {response.status}: {body[:500]}")
        headers = {name.lower(): value for name, value in response.getheaders()}
        response.close()
        return headers

    def put_file(self, path: Path, key: str, sha256: str) -> None:
        content_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        metadata_path = base64.urlsafe_b64encode(path.as_posix().encode("utf-8")).decode("ascii")
        size = file_size(path)
        headers = {
            "content-length": str(size),
            "content-type": content_type,
            "x-amz-meta-local-sha256": sha256,
            "x-amz-meta-local-size": str(size),
            "x-amz-meta-local-path-b64": metadata_path,
        }
        with open(long_fs_path(path), "rb") as handle:
            response = self._request("PUT", key, headers=headers, body=handle, payload_hash=sha256)
            body = response.read().decode("utf-8", errors="replace")
            status = response.status
            response.close()
        if status >= 300:
            raise RuntimeError(f"PUT {key} failed with HTTP {status}: {body[:500]}")

    def delete_object(self, key: str) -> bool:
        response = self._request("DELETE", key, payload_hash=EMPTY_SHA256)
        body = response.read().decode("utf-8", errors="replace")
        status = response.status
        response.close()
        if status == 404:
            return False
        if status >= 300:
            raise RuntimeError(f"DELETE {key} failed with HTTP {status}: {body[:500]}")
        return True

    def list_objects(self, prefix: str = "", max_keys: int = 1000) -> list[str]:
        keys: list[str] = []
        continuation: str | None = None
        while True:
            query = {
                "list-type": "2",
                "prefix": normalize_key(prefix),
                "max-keys": str(max_keys),
            }
            if continuation:
                query["continuation-token"] = continuation
            response = self._request("GET", "", query=query, payload_hash=EMPTY_SHA256)
            body = response.read()
            status = response.status
            response.close()
            if status >= 300:
                raise RuntimeError(f"LIST {prefix} failed with HTTP {status}: {body.decode('utf-8', errors='replace')[:500]}")
            root = ET.fromstring(body)
            namespace = ""
            if root.tag.startswith("{"):
                namespace = root.tag.split("}", 1)[0] + "}"
            keys.extend(element.text or "" for element in root.findall(f".//{namespace}Contents/{namespace}Key"))
            truncated = (root.findtext(f"{namespace}IsTruncated") or "").lower() == "true"
            continuation = root.findtext(f"{namespace}NextContinuationToken")
            if not truncated or not continuation:
                break
        return keys

    def put_json(self, data: dict[str, Any], key: str) -> None:
        payload = json.dumps(data, indent=2, ensure_ascii=False).encode("utf-8")
        payload_hash = hashlib.sha256(payload).hexdigest()
        headers = {
            "content-length": str(len(payload)),
            "content-type": "application/json; charset=utf-8",
            "x-amz-meta-local-sha256": payload_hash,
            "x-amz-meta-local-size": str(len(payload)),
        }
        response = self._request("PUT", key, headers=headers, body=payload, payload_hash=payload_hash)
        body = response.read().decode("utf-8", errors="replace")
        status = response.status
        response.close()
        if status >= 300:
            raise RuntimeError(f"PUT {key} failed with HTTP {status}: {body[:500]}")

    def get_json(self, key: str) -> dict[str, Any]:
        response = self._request("GET", key, payload_hash=EMPTY_SHA256)
        body = response.read()
        status = response.status
        response.close()
        if status >= 300:
            raise RuntimeError(f"GET {key} failed with HTTP {status}: {body.decode('utf-8', errors='replace')[:500]}")
        return json.loads(body.decode("utf-8"))

    def get_file(self, key: str, output: Path) -> None:
        response = self._request("GET", key, payload_hash=EMPTY_SHA256)
        status = response.status
        if status >= 300:
            body = response.read().decode("utf-8", errors="replace")
            response.close()
            raise RuntimeError(f"GET {key} failed with HTTP {status}: {body[:500]}")
        output.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile(delete=False, dir=output.parent) as tmp:
            tmp_path = Path(tmp.name)
            for chunk in iter(lambda: response.read(1024 * 1024), b""):
                tmp.write(chunk)
        response.close()
        os.replace(tmp_path, output)

    def _request(
        self,
        method: str,
        key: str,
        *,
        query: dict[str, str] | None = None,
        headers: dict[str, str] | None = None,
        body: Any = None,
        payload_hash: str,
    ) -> http.client.HTTPResponse:
        request_path = self._request_path(key)
        query_string = canonical_query_string(query or {})
        full_request_path = f"{request_path}?{query_string}" if query_string else request_path
        signed_headers = self._signed_headers(method, request_path, query_string, headers or {}, payload_hash)
        connection = http.client.HTTPSConnection(self.host, timeout=self.config.timeout_seconds)
        connection.request(method, full_request_path, body=body, headers=signed_headers)
        return connection.getresponse()

    def _request_path(self, key: str) -> str:
        normalized = normalize_key(key)
        bucket_path = "/" + quote(self.config.bucket, safe="")
        if not normalized:
            return bucket_path
        return bucket_path + "/" + quote(normalized, safe="/~")

    def _signed_headers(
        self,
        method: str,
        request_path: str,
        query_string: str,
        headers: dict[str, str],
        payload_hash: str,
    ) -> dict[str, str]:
        now = dt.datetime.now(dt.timezone.utc)
        amz_date = now.strftime("%Y%m%dT%H%M%SZ")
        date_stamp = now.strftime("%Y%m%d")
        all_headers = {name.lower(): value for name, value in headers.items()}
        all_headers["host"] = self.host
        all_headers["x-amz-content-sha256"] = payload_hash
        all_headers["x-amz-date"] = amz_date

        canonical_headers = "".join(f"{name}:{normalize_header(value)}\n" for name, value in sorted(all_headers.items()))
        signed_header_names = ";".join(sorted(all_headers))
        canonical_request = "\n".join(
            [
                method,
                request_path,
                query_string,
                canonical_headers,
                signed_header_names,
                payload_hash,
            ]
        )
        credential_scope = f"{date_stamp}/{self.region}/{self.service}/aws4_request"
        string_to_sign = "\n".join(
            [
                "AWS4-HMAC-SHA256",
                amz_date,
                credential_scope,
                hashlib.sha256(canonical_request.encode("utf-8")).hexdigest(),
            ]
        )
        signing_key = aws_signature_key(self.config.secret_access_key, date_stamp, self.region, self.service)
        signature = hmac.new(signing_key, string_to_sign.encode("utf-8"), hashlib.sha256).hexdigest()
        all_headers["authorization"] = (
            "AWS4-HMAC-SHA256 "
            f"Credential={self.config.access_key_id}/{credential_scope}, "
            f"SignedHeaders={signed_header_names}, "
            f"Signature={signature}"
        )
        return all_headers


def normalize_header(value: str) -> str:
    return " ".join(str(value).strip().split())


def canonical_query_string(query: dict[str, str]) -> str:
    return "&".join(
        f"{quote(str(name), safe='-_.~')}={quote(str(value), safe='-_.~')}"
        for name, value in sorted(query.items())
    )


def aws_signature_key(secret_key: str, date_stamp: str, region_name: str, service_name: str) -> bytes:
    key_date = hmac.new(("AWS4" + secret_key).encode("utf-8"), date_stamp.encode("utf-8"), hashlib.sha256).digest()
    key_region = hmac.new(key_date, region_name.encode("utf-8"), hashlib.sha256).digest()
    key_service = hmac.new(key_region, service_name.encode("utf-8"), hashlib.sha256).digest()
    return hmac.new(key_service, b"aws4_request", hashlib.sha256).digest()


def upload_raw_to_cloud(
    root: Path,
    config: RawCloudConfig,
    *,
    dry_run: bool = False,
    force: bool = False,
    limit: int | None = None,
) -> dict[str, Any]:
    manifest = build_raw_cloud_manifest(root, config, limit=limit)
    summary: dict[str, Any] = {
        "action": "upload",
        "dry_run": dry_run,
        "total_files": len(manifest["files"]),
        "total_bytes": sum(item["bytes"] for item in manifest["files"]),
        "uploaded": 0,
        "skipped": 0,
        "planned": 0,
        "errors": [],
    }
    manifest_path = write_raw_cloud_inventory(root, config, limit=limit)

    if dry_run:
        summary["planned"] = len(manifest["files"])
        write_json(raw_cloud_state_path(root, config, "last-upload-plan.json"), {"summary": summary, "manifest": manifest})
        return summary

    client = R2Client(config)
    root = root.resolve()
    for item in manifest["files"]:
        local_path = root / item["path"]
        try:
            remote = client.head_object(item["key"])
            remote_sha = (remote or {}).get("x-amz-meta-local-sha256", "")
            remote_size = int((remote or {}).get("content-length", "-1"))
            if not force and remote_sha == item["sha256"] and remote_size == item["bytes"]:
                summary["skipped"] += 1
                continue
            client.put_file(local_path, item["key"], item["sha256"])
            summary["uploaded"] += 1
        except Exception as exc:  # pragma: no cover - exercised only against live object storage
            summary["errors"].append({"path": item["path"], "key": item["key"], "error": str(exc)})

    manifest["upload_summary"] = summary
    write_json(manifest_path, manifest)
    write_json(raw_cloud_state_path(root, config, "last-upload-report.json"), {"summary": summary, "manifest": manifest})
    return summary


def upload_derived_assets_to_cloud(
    root: Path,
    config: RawCloudConfig,
    *,
    dry_run: bool = False,
    force: bool = False,
    limit: int | None = None,
    out: Path | None = None,
) -> dict[str, Any]:
    manifest = build_derived_asset_manifest(root, config, limit=limit)
    summary: dict[str, Any] = {
        "action": "asset-upload",
        "dry_run": dry_run,
        "total_files": len(manifest["files"]),
        "total_bytes": sum(item["bytes"] for item in manifest["files"]),
        "uploaded": 0,
        "skipped": 0,
        "planned": 0,
        "errors": [],
    }
    manifest_path = write_derived_asset_inventory(root, config, limit=limit, out=out)

    if dry_run:
        summary["planned"] = len(manifest["files"])
        write_json(
            raw_cloud_state_path(root, config, "last-derived-asset-upload-plan.json"),
            {"summary": summary, "manifest": manifest},
        )
        return summary

    client = R2Client(config)
    root = root.resolve()
    for item in manifest["files"]:
        local_path = root / item["path"]
        try:
            remote = client.head_object(item["key"])
            remote_sha = (remote or {}).get("x-amz-meta-local-sha256", "")
            remote_size = int((remote or {}).get("content-length", "-1"))
            if not force and remote_sha == item["sha256"] and remote_size == item["bytes"]:
                summary["skipped"] += 1
                continue
            client.put_file(local_path, item["key"], item["sha256"])
            summary["uploaded"] += 1
        except Exception as exc:  # pragma: no cover - exercised only against live object storage
            summary["errors"].append({"path": item["path"], "key": item["key"], "error": str(exc)})

    manifest["upload_summary"] = summary
    write_json(manifest_path, manifest)
    write_json(
        raw_cloud_state_path(root, config, "last-derived-asset-upload-report.json"),
        {"summary": summary, "manifest": manifest},
    )
    return summary


def cleanup_remote_json_manifests(config: RawCloudConfig) -> dict[str, Any]:
    client = R2Client(config)
    deleted: list[str] = []
    missing: list[str] = []
    errors: list[dict[str, str]] = []
    for key in LEGACY_REMOTE_MANIFEST_KEYS:
        object_key = f"{config.prefix}{normalize_key(key)}"
        try:
            if client.delete_object(object_key):
                deleted.append(object_key)
            else:
                missing.append(object_key)
        except Exception as exc:  # pragma: no cover - exercised only against live object storage
            errors.append({"key": object_key, "error": str(exc)})
    remaining: list[str] = []
    try:
        remaining = client.list_objects(f"{config.prefix}_manifests/")
    except Exception as exc:  # pragma: no cover - exercised only against live object storage
        errors.append({"key": f"{config.prefix}_manifests/", "error": f"list failed: {exc}"})
    return {
        "action": "cleanup-manifests",
        "deleted": deleted,
        "missing": missing,
        "remaining": remaining,
        "errors": errors,
    }


def verify_raw_cloud(
    root: Path,
    config: RawCloudConfig,
    *,
    limit: int | None = None,
) -> dict[str, Any]:
    manifest = build_raw_cloud_manifest(root, config, limit=limit)
    client = R2Client(config)
    issues = []
    verified = 0
    for item in manifest["files"]:
        try:
            remote = client.head_object(item["key"])
            if remote is None:
                issues.append({"path": item["path"], "key": item["key"], "issue": "missing_remote_object"})
                continue
            remote_size = int(remote.get("content-length", "-1"))
            remote_sha = remote.get("x-amz-meta-local-sha256", "")
            if remote_size != item["bytes"]:
                issues.append(
                    {
                        "path": item["path"],
                        "key": item["key"],
                        "issue": "size_mismatch",
                        "local": item["bytes"],
                        "remote": remote_size,
                    }
                )
                continue
            if remote_sha != item["sha256"]:
                issues.append(
                    {
                        "path": item["path"],
                        "key": item["key"],
                        "issue": "sha256_metadata_mismatch",
                        "local": item["sha256"],
                        "remote": remote_sha,
                    }
                )
                continue
            verified += 1
        except Exception as exc:  # pragma: no cover - exercised only against live object storage
            issues.append({"path": item["path"], "key": item["key"], "issue": "request_failed", "error": str(exc)})

    report = {
        "action": "verify",
        "created": dt.datetime.now(dt.timezone.utc).isoformat(),
        "total_files": len(manifest["files"]),
        "verified": verified,
        "issues": issues,
    }
    write_json(raw_cloud_state_path(root, config, "last-verify-report.json"), report)
    return report


def restore_raw_from_cloud(
    root: Path,
    config: RawCloudConfig,
    *,
    manifest_path: Path | None = None,
    force: bool = False,
    limit: int | None = None,
) -> dict[str, Any]:
    root = root.resolve()
    client = R2Client(config)
    if manifest_path is not None:
        source_manifest_path = manifest_path if manifest_path.is_absolute() else root / manifest_path
        manifest = json.loads(source_manifest_path.read_text(encoding="utf-8"))
    else:
        local_manifest_path = root / DEFAULT_RAW_CLOUD_MANIFEST_PATH
        if not local_manifest_path.exists():
            raise FileNotFoundError(
                f"Missing GitHub-tracked raw cloud manifest: {local_manifest_path}. "
                "Run raw-cloud inventory/upload from a workspace with raw cache first."
            )
        manifest = json.loads(local_manifest_path.read_text(encoding="utf-8"))

    files = list(manifest.get("files", []))
    if limit is not None and limit > 0:
        files = files[:limit]

    restored = 0
    skipped = 0
    errors = []
    for item in files:
        rel = Path(item["path"])
        if rel.is_absolute() or not rel.as_posix().startswith(config.raw_dir.as_posix().rstrip("/") + "/"):
            errors.append({"path": item.get("path", ""), "issue": "unsafe_restore_path"})
            continue
        output = root / rel
        if output.exists() and not force:
            if file_sha256(output) == item.get("sha256"):
                skipped += 1
                continue
            errors.append({"path": item["path"], "issue": "local_file_differs_use_force"})
            continue
        try:
            client.get_file(item["key"], output)
            downloaded_sha = file_sha256(output)
            if downloaded_sha != item.get("sha256"):
                errors.append(
                    {
                        "path": item["path"],
                        "issue": "downloaded_sha256_mismatch",
                        "expected": item.get("sha256"),
                        "actual": downloaded_sha,
                    }
                )
                continue
            restored += 1
        except Exception as exc:  # pragma: no cover - exercised only against live object storage
            errors.append({"path": item["path"], "key": item["key"], "issue": "request_failed", "error": str(exc)})

    report = {
        "action": "restore",
        "created": dt.datetime.now(dt.timezone.utc).isoformat(),
        "total_files": len(files),
        "restored": restored,
        "skipped": skipped,
        "errors": errors,
    }
    write_json(raw_cloud_state_path(root, config, "last-restore-report.json"), report)
    return report
