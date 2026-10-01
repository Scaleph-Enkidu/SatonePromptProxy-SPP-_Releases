"""Release boundary tests use tiny supported-component fixtures, never a network."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import zipfile

import verify_release as v


class ReleaseTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.assets = self.root / "assets"
        self.assets.mkdir()
        self.manifest = self.root / "repo" / "pair.json"
        self.manifest.parent.mkdir()
        self.model_data = {name: ("fixture-" + name).encode() for name in v.SEMANTIC_FILES}
        self.license_data = {name: ("license-" + name).encode() for name in v.SEMANTIC_LICENSES}
        supported = {name: v.digest(data) for name, data in self.model_data.items()}
        licenses = {name: (v.digest(data), len(data)) for name, data in self.license_data.items()}
        self.addCleanup(patch.stopall)
        patch.object(v, "SEMANTIC_FILES", supported).start()
        patch.object(v, "SEMANTIC_LICENSES", licenses).start()

    def zip_asset(self, name, payload, metadata):
        path = self.assets / name
        with zipfile.ZipFile(path, "w", zipfile.ZIP_STORED) as archive:
            for member, data in payload.items():
                archive.writestr(member, data)
        asset = dict(metadata, name=name, size=path.stat().st_size, sha256=v.sha256_file(path),
                     checksum_file=name + ".sha256", zip_members=list(payload))
        (self.assets / asset["checksum_file"]).write_text(asset["sha256"] + "  " + name + "\n")
        return asset

    def pair(self, extra=None, incorrect_hash=False, binary_hash=None):
        payload = {"AIChat/AIChat.dll": b"MZ-pair-dll-fixture",
                   "SatonePromptProxy/SatonePromptProxy.exe": b"MZ-pair-exe-fixture",
                   "SatonePromptProxy/config.example.json": b"{}"}
        payload.update(extra or {})
        info = {"versions": {"AIChat": "1.17.0", "SPP": "5.9.0"},
                "source_commits": {"AIChat": "a" * 40, "SPP": "b" * 40},
                "files_sha256": {name: v.digest(data) for name, data in payload.items()}}
        if incorrect_hash:
            info["files_sha256"]["SatonePromptProxy/config.example.json"] = "0" * 64
        binaries = {name: v.digest(payload[name]) for name in v.PAIR_BINARIES.values()}
        if binary_hash:
            binaries["AIChat/AIChat.dll"] = binary_hash
        payload["BUILD_INFO.json"] = json.dumps(info).encode()
        return self.zip_asset("pair.zip", payload, {"role": "paired_program", "versions": info["versions"],
                              "source_commits": info["source_commits"], "binaries_sha256": binaries})

    def semantic(self, missing_license=None, bad_model=False, bad_provenance=False):
        prefix = v.SEMANTIC_PREFIX
        payload = {prefix + name: data for name, data in self.model_data.items()}
        for name, data in self.license_data.items():
            if name != missing_license:
                payload[prefix + "licenses/" + name] = data
        proof = []
        for name, (sha, size) in v.SEMANTIC_LICENSES.items():
            item = {"file": name, "sha256": sha, "bytes": size}
            if name.startswith("ORT_"):
                item["source_archive_sha256"] = "c6ba983baf5681af108599675d2a89c2d145512d02de28aed0bff177cd0ba949"
            else:
                item["url"] = v.SEMANTIC_SOURCES[name]
            proof.append(item)
        if bad_provenance:
            proof[0]["sha256"] = "0" * 64
        if bad_model:
            payload[prefix + "model.onnx"] = b"unsupported-even-with-consistent-hashes"
        payload[prefix + "licenses/provenance.json"] = json.dumps(proof).encode()
        payload["语义组件安装说明.md"] = "Optional component".encode()
        info = dict(v.SEMANTIC_METADATA, files_sha256={name: v.digest(data) for name, data in payload.items()})
        payload[prefix + "COMPONENT.json"] = json.dumps(info).encode()
        return self.zip_asset("semantic.zip", payload, {"role": "semantic_component"})

    def release(self, pair=None, semantic=None):
        manifest = {"schema_version": 2, "release_tag": "AIChat-v1.17.0_SPP-v5.9.0",
                    "assets": [pair or self.pair(), semantic or self.semantic()]}
        self.save(manifest)
        return manifest

    def save(self, manifest):
        text = json.dumps(manifest)
        self.manifest.write_text(text)
        (self.assets / self.manifest.name).write_text(text)

    def add_superseded(self, manifest, payload=None, include_members=True):
        payload = payload or {"historical.txt": b"preserved original bytes"}
        archive_path = self.assets / "old_program.zip"
        with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_STORED) as archive:
            for name, data in payload.items():
                archive.writestr(name, data)
        checksum_path = self.assets / "old_program.zip.sha256"
        checksum_path.write_text(v.sha256_file(archive_path) + "  old_program.zip\n")
        old_manifest = self.assets / "old_manifest.json"
        old_manifest.write_text('{"original_release_manifest":true}')
        records = [{"name": path.name, "size": path.stat().st_size, "sha256": v.sha256_file(path)}
                   for path in (archive_path, checksum_path, old_manifest)]
        if include_members:
            records[0]["zip_members"] = list(payload)
        # An old role must not enter current program/model role counts.
        records[0]["role"] = "paired_program"
        manifest["superseded_assets"] = records
        self.save(manifest)
        return records

    def verify(self):
        return v.verify_manifest(self.manifest, self.assets, "AIChat-v1.17.0_SPP-v5.9.0")

    def test_new_pair_and_model_without_build_info(self):
        self.release()
        self.verify()
        with zipfile.ZipFile(self.assets / "semantic.zip") as archive:
            self.assertNotIn("BUILD_INFO.json", archive.namelist())

    def test_outer_hash_damage(self):
        self.release()
        with (self.assets / "pair.zip").open("ab") as stream:
            stream.write(b"damage")
        with self.assertRaisesRegex(ValueError, "Size mismatch"):
            self.verify()

    def test_inner_hash_damage_with_valid_outer_hash(self):
        self.release(pair=self.pair(incorrect_hash=True))
        with self.assertRaisesRegex(ValueError, "Packaged file hash"):
            self.verify()

    def test_outer_hash_damage_without_size_change(self):
        self.release()
        path = self.assets / "pair.zip"
        data = bytearray(path.read_bytes())
        data[-1] ^= 1
        path.write_bytes(data)
        with self.assertRaisesRegex(ValueError, "SHA256 mismatch"):
            self.verify()

    def test_unsafe_windows_and_parent_paths(self):
        for name in ("../escape.txt", "C:/escape.txt", "folder\\escape.txt", "aux.txt", "alias."):
            with self.subTest(name=name):
                self.release(pair=self.pair(extra={name: b"untrusted"}))
                with self.assertRaisesRegex(ValueError, "path"):
                    self.verify()

    def test_private_data_with_valid_outer_and_inner_hashes(self):
        for name in ("SatonePromptProxy/config.json", "SatonePromptProxy/connection_credentials.v1.json",
                     "SatonePromptProxy/SatoneRecall.db", "AIChat/private.history",
                     "SatonePromptProxy/logs/session.txt", "SatonePromptProxy/.env"):
            with self.subTest(name=name):
                self.release(pair=self.pair(extra={name: b"private"}))
                with self.assertRaisesRegex(ValueError, "Player data"):
                    self.verify()

    def test_missing_license_even_when_manifests_agree(self):
        self.release(semantic=self.semantic(missing_license="ORT_LICENSE"))
        with self.assertRaisesRegex(ValueError, "Missing license"):
            self.verify()

    def test_unsupported_model_even_when_manifests_agree(self):
        self.release(semantic=self.semantic(bad_model=True))
        with self.assertRaisesRegex(ValueError, "Unsupported semantic asset"):
            self.verify()

    def test_license_provenance_must_agree(self):
        self.release(semantic=self.semantic(bad_provenance=True))
        with self.assertRaisesRegex(ValueError, "provenance mismatch"):
            self.verify()

    def test_tested_binary_hash_must_agree(self):
        self.release(pair=self.pair(binary_hash="0" * 64))
        with self.assertRaisesRegex(ValueError, "Tested binary"):
            self.verify()

    def test_checksum_and_uploaded_manifest(self):
        self.release()
        (self.assets / "pair.zip.sha256").write_text("0" * 64 + "  pair.zip\n")
        with self.assertRaisesRegex(ValueError, "Checksum"):
            self.verify()
        self.release()
        (self.assets / self.manifest.name).write_text("{}")
        with self.assertRaisesRegex(ValueError, "Uploaded manifest"):
            self.verify()

    def test_extra_uploaded_attachment_fails(self):
        self.release()
        (self.assets / "accidental-config.json").write_text("{}")
        with self.assertRaisesRegex(ValueError, "unrecorded release attachment"):
            self.verify()

    def test_non_ascii_attachment_and_checksum_names_rejected(self):
        for field in ("name", "checksum_file"):
            with self.subTest(field=field):
                manifest = self.release()
                manifest["assets"][0][field] = "安装包.zip" if field == "name" else "安装包.zip.sha256"
                self.save(manifest)
                with self.assertRaisesRegex(ValueError, "must be ASCII"):
                    self.verify()

    def test_crc_damage_even_with_correct_outer_hash(self):
        manifest = self.release()
        path = self.assets / "pair.zip"
        data = bytearray(path.read_bytes())
        offset = data.index(b"MZ-pair-dll-fixture")
        data[offset] ^= 1
        path.write_bytes(data)
        manifest["assets"][0]["sha256"] = v.sha256_file(path)
        self.save(manifest)
        with self.assertRaisesRegex(ValueError, "Corrupt ZIP"):
            self.verify()

    def test_schema_one_legacy_build_info(self):
        info = {"component": "spp", "version": "5.8.42", "source_commit": "c" * 40}
        asset = self.zip_asset("legacy.zip", {"BUILD_INFO.json": json.dumps(info).encode(),
                                             "config.example.json": b"{}"}, info)
        self.save({"schema_version": 1, "release_tag": "legacy", "assets": [asset]})
        v.verify_manifest(self.manifest, self.assets, "legacy")

    def test_complete_superseded_history_allowed(self):
        manifest = self.release()
        self.add_superseded(manifest)
        self.verify()

    def test_superseded_archive_without_member_list_still_scanned(self):
        manifest = self.release()
        self.add_superseded(manifest, include_members=False)
        self.verify()

    def test_superseded_hash_damage_rejected(self):
        manifest = self.release()
        records = self.add_superseded(manifest)
        records[0]["sha256"] = "0" * 64
        self.save(manifest)
        with self.assertRaisesRegex(ValueError, "Superseded SHA256 mismatch"):
            self.verify()

    def test_unrecorded_extra_beside_superseded_assets_rejected(self):
        manifest = self.release()
        self.add_superseded(manifest)
        (self.assets / "unrecorded.txt").write_text("unexpected attachment")
        with self.assertRaisesRegex(ValueError, "unrecorded release attachment"):
            self.verify()

    def test_superseded_name_collisions_rejected(self):
        for target in ("CURRENT_ZIP", "CURRENT_CHECKSUM", "CURRENT_MANIFEST", "DUPLICATE_HISTORY"):
            with self.subTest(target=target):
                manifest = self.release()
                records = self.add_superseded(manifest)
                if target == "CURRENT_ZIP":
                    records[0]["name"] = manifest["assets"][0]["name"].upper()
                elif target == "CURRENT_CHECKSUM":
                    records[0]["name"] = manifest["assets"][0]["checksum_file"]
                elif target == "CURRENT_MANIFEST":
                    records[0]["name"] = self.manifest.name
                else:
                    records.append(dict(records[0]))
                self.save(manifest)
                with self.assertRaisesRegex(ValueError, "name collision"):
                    self.verify()

    def test_current_asset_cannot_collide_with_manifest(self):
        manifest = self.release()
        manifest["assets"].append({"name": self.manifest.name, "size": 0, "sha256": "0" * 64})
        self.save(manifest)
        with self.assertRaisesRegex(ValueError, "collides with current manifest"):
            self.verify()

    def test_superseded_zip_private_files_and_unsafe_paths_rejected(self):
        for name in ("../escape.txt", "config.json"):
            with self.subTest(name=name):
                manifest = self.release()
                self.add_superseded(manifest, payload={name: b"untrusted"})
                with self.assertRaisesRegex(ValueError, "Unsafe path|Player data"):
                    self.verify()

    def test_superseded_zip_crc_and_members_checked(self):
        manifest = self.release()
        records = self.add_superseded(manifest)
        records[0]["zip_members"] = ["wrong.txt"]
        self.save(manifest)
        with self.assertRaisesRegex(ValueError, "Unexpected ZIP contents"):
            self.verify()
        records = self.add_superseded(manifest)
        path = self.assets / records[0]["name"]
        data = bytearray(path.read_bytes())
        data[data.index(b"preserved original bytes")] ^= 1
        path.write_bytes(data)
        records[0]["sha256"] = v.sha256_file(path)
        self.save(manifest)
        with self.assertRaisesRegex(ValueError, "Corrupt ZIP"):
            self.verify()

    def test_windows_case_collision(self):
        self.release(pair=self.pair(extra={"docs/readme.md": b"a", "docs/README.md": b"b"}))
        with self.assertRaisesRegex(ValueError, "Windows path collision"):
            self.verify()


if __name__ == "__main__":
    unittest.main()
