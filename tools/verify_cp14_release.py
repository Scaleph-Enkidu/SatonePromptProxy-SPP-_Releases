#!/usr/bin/env python3
"""Verify the CP14-9 release assets before and after GitHub publication."""

import argparse
import hashlib
import json
import pathlib
import zipfile


ROOT = pathlib.Path(__file__).resolve().parents[1]
PAIR = "AIChat_v1.16.23_SPP_v5.8.26"
PACKAGE = ROOT / "packages" / PAIR
MANIFEST = ROOT / "releases" / f"{PAIR}.json"
AI_NAME = "AIChat_v1.16.23.zip"
SPP_NAME = "SatonePromptProxy_v5.8.26.zip"


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_zip(path, required):
    with zipfile.ZipFile(path) as archive:
        assert archive.testzip() is None, f"Corrupt ZIP: {path}"
        names = set(archive.namelist())
        assert required <= names, f"Missing ZIP entries: {required - names}"
        assert not any(name.startswith("/") or ".." in pathlib.PurePosixPath(name).parts for name in names)
        sums = json.loads(archive.read("SHA256SUMS.json"))
        for name, expected in sums.items():
            if isinstance(expected, dict):
                expected = expected.get("sha256")
            if expected:
                assert hashlib.sha256(archive.read(name)).hexdigest() == expected, name
        return archive


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--assets-dir", type=pathlib.Path)
    args = parser.parse_args()
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    directory = args.assets_dir if args.assets_dir else PACKAGE
    for name in (AI_NAME, SPP_NAME):
        path = directory / name
        expected = manifest["assets"][name]
        assert path.stat().st_size == expected["size_bytes"], name
        assert sha256(path) == expected["sha256"], name
    verify_zip(directory / AI_NAME, {"AIChat.dll", "AIChat.pdb", "BUILD_INFO.json", "README.md"})
    with zipfile.ZipFile(directory / SPP_NAME) as archive:
        verify_zip(directory / SPP_NAME, {"SatonePromptProxy.exe", "mayuri-voice/refs/MAY_1158_Neutral.wav", "BUILD_INFO.json"})
        wav = archive.read("mayuri-voice/refs/MAY_1158_Neutral.wav")
        assert hashlib.sha256(wav).hexdigest() == manifest["included_neutral_wav_sha256"]
    print("CP14-9 release assets verified")


if __name__ == "__main__":
    main()
