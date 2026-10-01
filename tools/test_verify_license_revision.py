"""Regression checks for lost credits, altered runtime and false old-rights claims."""
import io
import json
from pathlib import Path
import unittest
import zipfile

import verify_release as v


class LicenseRevisionTests(unittest.TestCase):
    def setUp(self):
        root = Path(__file__).resolve().parents[1]
        self.payload = {}
        license_data = (root / "LICENSE").read_bytes()
        notice = (root / "NOTICE").read_bytes()
        scope = (root / "LICENSE_SCOPE.zh-CN.md").read_bytes()
        upstream = (root / "licenses/upstream/AIChat-MIT.txt").read_bytes()
        legacy = (root / "licenses/legacy/Release-Repository-MIT.txt").read_bytes()
        for prefix in ("", "AIChat/", "SatonePromptProxy/"):
            for name, data in [("LICENSE", license_data), ("NOTICE", notice), ("LICENSE_SCOPE.zh-CN.md", scope),
                               ("licenses/upstream/AIChat-MIT.txt", upstream), ("licenses/legacy/Release-Repository-MIT.txt", legacy)]:
                self.payload[prefix + name] = data
        original = {"AIChat/AIChat.dll": b"MZ-original-dll", "SatonePromptProxy/SatonePromptProxy.exe": b"MZ-original-exe",
                    "SatonePromptProxy/Start_Text_Chat.bat": b"original BAT", "SatonePromptProxy/third_party/LICENSE": b"original license"}
        self.payload.update(original)
        self.payload["BUILD_INFO.json"] = json.dumps({"new_binaries_built": False, "original_program_zip_sha256": "c" * 64}).encode()
        self.manifest = {"release_tag": "AIChat-v1.17.1_SPP-v5.9.1-license-r1", "new_binaries_built": False,
                         "license_revision": {"identifier": "PolyForm-Noncommercial-1.0.0", "license_sha256": v.POLYFORM_SHA256,
                                              "upstream_mit_sha256": v.UPSTREAM_MIT_SHA256, "notice_sha256": v.digest(notice),
                                              "legacy_public_mit_sha256": v.digest(legacy), "original_program_zip_sha256": "c" * 64,
                                              "unchanged_payload_sha256": {n: v.digest(data) for n, data in original.items()}}}

    def verify(self):
        stream = io.BytesIO()
        with zipfile.ZipFile(stream, "w") as archive:
            for name, data in self.payload.items():
                archive.writestr(name, data)
        with zipfile.ZipFile(stream) as archive:
            v.check_license_revision(archive, self.manifest)

    def test_valid_revision(self):
        self.verify()

    def test_changed_standard_text(self):
        self.payload["AIChat/LICENSE"] += b"New additional restriction"
        with self.assertRaisesRegex(ValueError, "PolyForm"):
            self.verify()

    def test_lost_author_even_if_manifest_updated(self):
        notice = self.payload["NOTICE"].replace(b"Scaleph", b"Anonymous")
        for prefix in ("", "AIChat/", "SatonePromptProxy/"):
            self.payload[prefix + "NOTICE"] = notice
        self.manifest["license_revision"]["notice_sha256"] = v.digest(notice)
        with self.assertRaisesRegex(ValueError, "attribution"):
            self.verify()

    def test_replaced_upstream_mit(self):
        self.payload["AIChat/licenses/upstream/AIChat-MIT.txt"] = self.payload["LICENSE"]
        with self.assertRaisesRegex(ValueError, "AIChat MIT"):
            self.verify()

    def test_lost_legacy_public_license(self):
        del self.payload["licenses/legacy/Release-Repository-MIT.txt"]
        with self.assertRaises(KeyError):
            self.verify()

    def test_altered_runtime(self):
        self.payload["SatonePromptProxy/Start_Text_Chat.bat"] += b"changed"
        with self.assertRaisesRegex(ValueError, "payload"):
            self.verify()

    def test_altered_third_party(self):
        self.payload["SatonePromptProxy/third_party/LICENSE"] = self.payload["LICENSE"]
        with self.assertRaisesRegex(ValueError, "third-party payload"):
            self.verify()

    def test_added_unproven_runtime(self):
        self.payload["AIChat/new.dll"] = b"MZ-new"
        with self.assertRaisesRegex(ValueError, "new runtime"):
            self.verify()

    def test_removed_prior_rights_statement(self):
        for prefix in ("", "AIChat/", "SatonePromptProxy/"):
            self.payload[prefix + "LICENSE_SCOPE.zh-CN.md"] = b"All prior licenses are cancelled."
        with self.assertRaisesRegex(ValueError, "prior-rights"):
            self.verify()

    def test_revision_cannot_skip_proof(self):
        del self.manifest["license_revision"]
        with self.assertRaisesRegex(ValueError, "Missing license revision"):
            self.verify()

    def test_revision_cannot_claim_new_build(self):
        self.manifest["new_binaries_built"] = True
        with self.assertRaisesRegex(ValueError, "new build"):
            self.verify()

    def test_legacy_manifest_not_relabelled(self):
        self.manifest = {"release_tag": "AIChat-v1.17.1_SPP-v5.9.1"}
        self.verify()


if __name__ == "__main__":
    unittest.main()
