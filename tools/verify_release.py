"""Verify the original distribution packages before publishing or on a rerun."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import zipfile

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("--assets-dir", type=Path)
args = parser.parse_args()
manifest = json.loads((ROOT / "releases/AIChat_v1.16.14_SPP_v5.8.23.json").read_text())
directory = args.assets_dir or ROOT / manifest["package_directory"]

for asset in manifest["assets"]:
    path = directory / asset["name"]
    data = path.read_bytes()
    assert len(data) == asset["size"], f"Size mismatch: {path.name}"
    assert hashlib.sha256(data).hexdigest() == asset["sha256"], f"SHA256 mismatch: {path.name}"
    if path.suffix != ".zip":
        continue
    with zipfile.ZipFile(path) as archive:
        assert archive.testzip() is None, f"Corrupt ZIP: {path.name}"
        names = archive.namelist()
        assert len(names) == len(set(names)), f"Duplicate ZIP member: {path.name}"
        assert sorted(names) == sorted(asset["zip_members"]), f"Unexpected ZIP contents: {path.name}"
        for name in names:
            member = PurePosixPath(name)
            assert not member.is_absolute() and ".." not in member.parts and "\\" not in name
            lower = name.lower()
            assert not lower.endswith((".cfg", ".history", ".log")), f"Runtime data: {name}"
            assert member.name.lower() not in ("config.json", "runtime_paths.json")
            assert not any(p.lower() in ("memory_profiles", "backups", "logs") for p in member.parts)
        info = json.loads(archive.read("BUILD_INFO.json"))
        assert info["source_commit"] == asset["source_commit"]
        assert info["version"] == asset["version"]
        assert str(info["workflow_run"]) == str(asset["workflow_run"])
    checksum = (directory / asset["checksum_file"]).read_text().split()
    assert checksum == [asset["sha256"], asset["name"]], f"Checksum file mismatch: {path.name}"
    print(f"Verified {path.name}: {asset['sha256']}")

print("All release assets match the recorded original files.")
