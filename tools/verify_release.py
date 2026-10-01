"""Verify immutable release assets, including the text-first pair and ONNX add-on."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import stat
import zipfile

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = "releases/AIChat_v1.17.0_SPP_v5.9.0.json"
SEMANTIC_PREFIX = "models/multilingual-e5-small/"
SEMANTIC_FILES = {
    "model.onnx": "dd476dd0c2514e9b9be83aeb3853fac0763e0bdf4a71645407587d77c48a2d88",
    "tokenizer.json": "0b44a9d7b51c3c62626640cda0e2c2f70fdacdc25bbbd68038369d14ebdf4c39",
    "onnxruntime.dll": "7e39e2bdbba836d98071ef28620735ba36a47c554cf794585269aecc50fab0da",
    "onnxruntime_providers_shared.dll": "b9b7ab9e2a8b08ee7ae4a7ac1c8bfd44a741f17ad8d0f764953140a57de0b796",
}
SEMANTIC_LICENSES = {
    "MODEL_CARD.md": ("0038de97aee16258cecbad7ffda4b4febd6953e747a00e0ddbc8e6ed241e9c1c", 497538),
    "E5_MIT_LICENSE": ("904dc4d8749877f1dba1cda48200d2462dccbeb7c134d5e4ef6fa75e0198c8fe", 1104),
    "ORT_LICENSE": ("c250d6278f0b47a6439fb7592b08b58a55eb9f535aa49a1db63211c3f982b674", 1094),
    "ORT_ThirdPartyNotices.txt": ("c53a76501ef60db6f865f20599f220761201ac4057683acefdab37d861b86622", 344457),
}
SEMANTIC_METADATA = {
    "platform": "windows-amd64", "runtime": "ORT CPU 1.30.0",
    "model": "intfloat/multilingual-e5-small",
    "model_revision": "614241f622f53c4eeff9890bdc4f31cfecc418b3",
    "source_file": "onnx/model_qint8_avx512_vnni.onnx",
}
SEMANTIC_SOURCES = {
    "MODEL_CARD.md": "https://huggingface.co/intfloat/multilingual-e5-small/raw/614241f622f53c4eeff9890bdc4f31cfecc418b3/README.md",
    "E5_MIT_LICENSE": "https://raw.githubusercontent.com/microsoft/unilm/master/LICENSE",
}
PAIR_BINARIES = {"AIChat": "AIChat/AIChat.dll", "SPP": "SatonePromptProxy/SatonePromptProxy.exe"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def sha256_file(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def safe_path(name):
    require(isinstance(name, str) and name, "Empty or invalid asset path")
    path = PurePosixPath(name)
    require(not path.is_absolute() and ".." not in path.parts and "\\" not in name
            and ":" not in name and not any(ord(c) < 32 for c in name)
            and all(p not in ("", ".") and not p.endswith((".", " ")) for p in name.split("/")),
            "Unsafe path: " + name)
    require(not any(re.fullmatch(r"(?i)(con|prn|aux|nul|com[1-9]|lpt[1-9])(\..*)?", p)
                    for p in path.parts), "Windows reserved path: " + name)
    return path


def check_no_player_data(name):
    path = safe_path(name)
    lower = name.lower()
    basename = path.name.lower()
    forbidden_names = {"config.json", "runtime_paths.json", "connections.v1.json",
                       "connection_credentials.v1.json", "originalgameprogress.json",
                       "usage_stats.json", "conversation_state.json", ".env",
                       "credentials", "credentials.json", "api_key.txt", "api_keys.json",
                       "satonememory.json", "satonerelationship.json", "satonearchive.jsonl", "satonechat.txt"}
    require(basename not in forbidden_names and not basename.startswith((".env.", "config.json.",
            "connection_credentials.", "originalgameprogress.json."))
            and not lower.endswith((".cfg", ".history", ".log", ".db", ".sqlite", ".sqlite3",
                                    ".db-wal", ".db-shm", ".writer.lock", ".pem", ".key"))
            and not any(p.lower() in {"memory_profiles", "backups", "logs", ".git", ".aws", ".ssh"}
                        for p in path.parts), "Player data or credentials in ZIP: " + name)


def check_archive(archive, expected_members):
    names = archive.namelist()
    require(isinstance(expected_members, list) and len(expected_members) == len(set(expected_members)),
            "Invalid ZIP member manifest")
    for name in expected_members:
        safe_path(name)
    require(len(names) == len(set(names)), "Duplicate ZIP member")
    require(len(names) == len({name.casefold() for name in names}), "Windows path collision")
    require(sorted(names) == sorted(expected_members), "Unexpected ZIP contents")
    for entry in archive.infolist():
        check_no_player_data(entry.filename)
        require(not entry.is_dir(), "Unexpected directory entry: " + entry.filename)
        require(not stat.S_ISLNK(entry.external_attr >> 16), "Symlink ZIP member")
        require(not entry.flag_bits & 1, "Encrypted ZIP member")
    require(archive.testzip() is None, "Corrupt ZIP")


def check_file_hashes(archive, info, info_path):
    hashes = info.get("files_sha256")
    require(isinstance(hashes, dict), "Missing files_sha256")
    require(set(archive.namelist()) == set(hashes) | {info_path}, "Unmanifested or missing ZIP files")
    require(info_path not in hashes, "Metadata cannot hash itself")
    for name, expected in hashes.items():
        safe_path(name)
        require(isinstance(expected, str) and re.fullmatch(r"[0-9a-f]{64}", expected), "Invalid file SHA256")
        require(digest(archive.read(name)) == expected, "Packaged file hash mismatch: " + name)


def check_pair(archive, asset):
    info = json.loads(archive.read("BUILD_INFO.json"))
    for key in ("versions", "source_commits"):
        require(set(asset[key]) == set(PAIR_BINARIES), "Invalid paired " + key)
        require(info[key] == asset[key], "Paired " + key + " mismatch")
    require(all(isinstance(sha, str) and re.fullmatch(r"[0-9a-f]{40}", sha)
                for sha in asset["source_commits"].values()), "Invalid tested source commit")
    require(set(asset["binaries_sha256"]) == set(PAIR_BINARIES.values()), "Invalid paired binary hashes")
    check_file_hashes(archive, info, "BUILD_INFO.json")
    for binary in PAIR_BINARIES.values():
        data = archive.read(binary)
        require(data[:2] == b"MZ", "Invalid Windows binary: " + binary)
        require(digest(data) == asset["binaries_sha256"][binary], "Tested binary mismatch: " + binary)
    require(not any(name.startswith("SatonePromptProxy/models/") or name.endswith(".onnx")
                    or PurePosixPath(name).name in SEMANTIC_FILES for name in archive.namelist()),
            "Optional models must remain in the separate component")


def check_semantic(archive):
    metadata_path = SEMANTIC_PREFIX + "COMPONENT.json"
    info = json.loads(archive.read(metadata_path))
    require(all(info.get(k) == v for k, v in SEMANTIC_METADATA.items()), "Unsupported semantic component metadata")
    expected = {SEMANTIC_PREFIX + name for name in SEMANTIC_FILES}
    expected |= {SEMANTIC_PREFIX + "licenses/" + name for name in SEMANTIC_LICENSES}
    expected |= {metadata_path, SEMANTIC_PREFIX + "licenses/provenance.json", "语义组件安装说明.md"}
    require(set(archive.namelist()) == expected, "Missing license or unsupported semantic payload")
    check_file_hashes(archive, info, metadata_path)
    for name, expected_sha in SEMANTIC_FILES.items():
        require(digest(archive.read(SEMANTIC_PREFIX + name)) == expected_sha, "Unsupported semantic asset: " + name)
    proof = json.loads(archive.read(SEMANTIC_PREFIX + "licenses/provenance.json"))
    require(isinstance(proof, list) and len(proof) == len(SEMANTIC_LICENSES), "Invalid license provenance")
    require({item["file"] for item in proof} == set(SEMANTIC_LICENSES), "Missing license provenance")
    for item in proof:
        expected_sha, expected_size = SEMANTIC_LICENSES[item["file"]]
        data = archive.read(SEMANTIC_PREFIX + "licenses/" + item["file"])
        require(digest(data) == expected_sha and len(data) == expected_size, "Changed semantic license")
        require(item["sha256"] == expected_sha and item["bytes"] == expected_size, "License provenance mismatch")
        if item["file"].startswith("ORT_"):
            require(item.get("source_archive_sha256") == "c6ba983baf5681af108599675d2a89c2d145512d02de28aed0bff177cd0ba949",
                    "ORT license source mismatch")
        else:
            require(item.get("url") == SEMANTIC_SOURCES[item["file"]], "License source URL mismatch")


def check_legacy(archive, asset):
    info = json.loads(archive.read("BUILD_INFO.json"))
    for key in ("source_commit", "version", "component"):
        require(info[key] == asset[key], "Legacy BUILD_INFO mismatch: " + key)
    if asset.get("workflow_run") is not None:
        require(str(info.get("workflow_run")) == str(asset["workflow_run"]), "Workflow run mismatch")


def verify_manifest(manifest_path, assets_dir=None, expected_tag=None):
    manifest_path = Path(manifest_path)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
    schema = manifest.get("schema_version", 1)
    require(schema in (1, 2), "Unsupported manifest schema")
    if expected_tag is not None:
        require(manifest["release_tag"] == expected_tag, "Release tag mismatch")
    if assets_dir is None:
        directory = ROOT / str(safe_path(manifest["package_directory"]))
    else:
        directory = Path(assets_dir)
    assets = manifest["assets"]
    require(isinstance(assets, list) and assets, "No release assets")
    require(len({a["name"].casefold() for a in assets}) == len(assets), "Duplicate release asset")
    if schema == 2:
        roles = [a.get("role") for a in assets if a["name"].endswith(".zip")]
        require(set(roles) == {"paired_program", "semantic_component"} and len(roles) == 2,
                "Expected one program pair and one semantic component")
    required_files = set()
    for asset in assets:
        require(len(safe_path(asset["name"]).parts) == 1, "Asset must be a flat filename")
        check_no_player_data(asset["name"])
        path = directory / asset["name"]
        require(path.stat().st_size == asset["size"], "Size mismatch: " + path.name)
        require(sha256_file(path) == asset["sha256"], "SHA256 mismatch: " + path.name)
        required_files.add(path.name)
        if path.suffix != ".zip":
            continue
        with zipfile.ZipFile(path) as archive:
            check_archive(archive, asset["zip_members"])
            if schema == 1:
                check_legacy(archive, asset)
            elif asset["role"] == "paired_program":
                check_pair(archive, asset)
            else:
                check_semantic(archive)
        checksum_name = asset["checksum_file"]
        require(len(safe_path(checksum_name).parts) == 1, "Unsafe checksum filename")
        checksum = (directory / checksum_name).read_text(encoding="utf-8-sig").split()
        require(checksum == [asset["sha256"], asset["name"]], "Checksum file mismatch: " + path.name)
        required_files.add(checksum_name)
        print("Verified " + path.name + ": " + asset["sha256"])
    if assets_dir is not None and schema == 2:
        required_files.add(manifest_path.name)
        actual = {p.name for p in directory.iterdir()}
        require(actual == required_files, "Missing or unrecorded release attachment")
        require((directory / manifest_path.name).read_bytes() == manifest_path.read_bytes(),
                "Uploaded manifest differs from repository manifest")
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=ROOT / DEFAULT_MANIFEST)
    parser.add_argument("--assets-dir", type=Path)
    parser.add_argument("--tag")
    args = parser.parse_args()
    verify_manifest(args.manifest, args.assets_dir, args.tag)
    print("All release assets match the recorded original files.")


if __name__ == "__main__":
    main()
