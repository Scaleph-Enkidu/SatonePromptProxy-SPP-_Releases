"""Build the N15 documentation-only revision; never rebuild or alter runtime payloads."""
from pathlib import Path, PurePosixPath
import argparse
import hashlib
import json
import posixpath
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
LANGUAGES = ("zh-CN", "en", "ja")
ORIGINAL_DIR = "packages/AIChat_v1.18.28_SPP_v5.10.8"
ORIGINAL_NAME = "SatoneMod_AIChat_1.18.28_SPP_5.10.8_Windows_x64.zip"
ORIGINAL_SHA256 = "5c13266e6ec9d1f7e775bb305d1734099b845acc91ecb27902c5290b9bb2f45e"
REVISION_DIR = ORIGINAL_DIR + "_docs_r1"
REVISION_NAME = ORIGINAL_NAME.replace(".zip", "_docs_r1.zip")
MANIFEST = "releases/AIChat_v1.18.28_SPP_v5.10.8_docs_r1.json"
REVISION = "DOCUMENTATION_REVISION.json"
REPLACED = {
    "00_安装与回滚.md",
    "01_N15实机验证清单.md",
    "SatonePromptProxy/docs/INSTALL.zh-CN.md",
    "SatonePromptProxy/docs/PORTABLE_DEPLOYMENT.md",
}
WEB = "https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/main/"
LINK = re.compile(r"(!?\[[^\]\n]*\]\()([^\s)]+)(\))")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def gateway(prefix, page, title):
    return (f"# {title}\n\n" + " · ".join(
        f"[{label}]({prefix}docs/{lang}/{page})"
        for lang, label in zip(LANGUAGES, ("简体中文", "English", "日本語"))
    ) + "\n\nAIChat 1.18.28 + SPP 5.10.8 · docs_r1 · 2026-10-06\n").encode("utf-8")


def document_payload():
    """Bundle canonical guides; non-bundled repository assets remain explicit web links."""
    result = {}
    for folder in ("docs", "licenses", "releases"):
        for path in sorted((ROOT / folder).rglob("*")):
            if path.is_file() and path.relative_to(ROOT).as_posix() != MANIFEST:
                name = path.relative_to(ROOT).as_posix()
                result[name] = path.read_bytes()
    for name in ("LICENSE", "NOTICE", "LICENSE_SCOPE.zh-CN.md"):
        result[name] = (ROOT / name).read_bytes()
    result["README.md"] = gateway("", "README.md", "Satone Mod · 聪音 Mod · 聡音 Mod")
    result["AIChat/README.md"] = gateway("", "AIChat_README.md", "AIChat")
    result["SatonePromptProxy/README.md"] = gateway("", "SPP_README.md", "SatonePromptProxy")
    # Preserve known package entry paths, but make each a three-language entrance.
    result["00_安装与回滚.md"] = gateway("", "PACKAGE_INSTALL.md", "安装 / Installation / 導入")
    result["01_N15实机验证清单.md"] = gateway("", "PACKAGE_CHECKLIST.md", "检查 / Checks / 確認")
    result["SatonePromptProxy/docs/INSTALL.zh-CN.md"] = gateway("../", "INSTALL.md", "安装 / Installation / 導入")
    result["SatonePromptProxy/docs/PORTABLE_DEPLOYMENT.md"] = gateway("../", "PORTABLE_DEPLOYMENT.md", "迁移 / Moving / 移設")
    # Avoid circular ZIP-hash metadata: this internal proof has no outer ZIP hash.
    available = set(result) | {REVISION}
    for name, data in list(result.items()):
        if not name.endswith(".md"):
            continue
        if name.startswith(("AIChat/", "SatonePromptProxy/")):
            continue  # Component-local entrances resolve after the copies below.
        text = data.decode("utf-8-sig").replace("\r\n", "\n")
        def replace(match):
            target = match.group(2)
            if re.match(r"[A-Za-z][A-Za-z0-9+.-]*:", target) or target.startswith("#"):
                return match.group(0)
            path, sep, anchor = target.partition("#")
            absolute = posixpath.normpath(posixpath.join(posixpath.dirname(name), path))
            if absolute in available:
                return match.group(0)
            if absolute == MANIFEST:
                absolute = REVISION
                relative = posixpath.relpath(absolute, posixpath.dirname(name) or ".")
                return match.group(1) + relative + match.group(3)
            return match.group(1) + WEB + absolute + (sep + anchor if sep else "") + match.group(3)
        result[name] = LINK.sub(replace, text).encode("utf-8")
    # Each component remains readable after being copied out of the paired archive.
    shared = {name: data for name, data in result.items()
              if name.startswith(("docs/", "licenses/", "releases/"))
              or name in ("LICENSE", "NOTICE", "LICENSE_SCOPE.zh-CN.md")}
    for component in ("AIChat", "SatonePromptProxy"):
        for name, data in shared.items():
            if component == "AIChat" and name == "LICENSE":
                continue  # Preserve the original runtime archive's legal bytes.
            result[f"{component}/{name}"] = data
    return result


def build():
    original_path = ROOT / ORIGINAL_DIR / ORIGINAL_NAME
    assert sha(original_path.read_bytes()) == ORIGINAL_SHA256, "Original archive changed"
    with zipfile.ZipFile(original_path) as source:
        original = {info.filename: source.read(info) for info in source.infolist() if not info.is_dir()}
    assert REPLACED <= original.keys()
    payload = {name: data for name, data in original.items() if name not in REPLACED}
    additions = document_payload()
    assert not (set(additions) & set(payload)), "Document payload would replace protected content"
    payload.update(additions)
    unchanged = {name: sha(data) for name, data in original.items() if name not in REPLACED}
    changes = {name: {"original_sha256": sha(original[name]), "revision_sha256": sha(payload[name])} for name in sorted(REPLACED)}
    proof = {
        "schema_version": 1,
        "kind": "documentation_revision",
        "revision": "N15-docs-r1-trilingual",
        "release_tag": "AIChat-v1.18.28_SPP-v5.10.8-docs-r1",
        "generated_on": "2026-10-06",
        "versions": {"AIChat": "1.18.28", "SPP": "5.10.8"},
        "new_binaries_built": False,
        "languages": list(LANGUAGES),
        "original_package": f"{ORIGINAL_DIR}/{ORIGINAL_NAME}",
        "original_package_sha256": ORIGINAL_SHA256,
        "original_build_info_scope": "BUILD_INFO.json is retained verbatim as evidence of the original N15 candidate. Its pre-publication label, pre-rewrite commit IDs and old document hashes describe that original archive, not this documentation revision. Runtime hashes remain valid.",
        "unchanged_original_members_sha256": unchanged,
        "replaced_document_members": changes,
        "added_document_members_sha256": {name: sha(data) for name, data in sorted(additions.items()) if name not in REPLACED},
    }
    for prefix in ("", "AIChat/", "SatonePromptProxy/"):
        payload[prefix + REVISION] = json_bytes(proof)
    target = ROOT / REVISION_DIR
    target.mkdir(parents=True, exist_ok=True)
    output = target / REVISION_NAME
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, data in sorted(payload.items()):
            info = zipfile.ZipInfo(name, date_time=(2026, 10, 6, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data, compresslevel=9)
    digest = sha(output.read_bytes())
    (target / (REVISION_NAME + ".sha256")).write_text(f"{digest}  {REVISION_NAME}\n", encoding="utf-8", newline="\n")
    manifest = dict(proof, package_directory=REVISION_DIR, package_file=REVISION_NAME,
                    package_sha256=digest, package_bytes=output.stat().st_size,
                    zip_members_sha256={name: sha(data) for name, data in sorted(payload.items())})
    (ROOT / MANIFEST).write_bytes(json_bytes(manifest))
    print(json.dumps({"package": str(output), "bytes": output.stat().st_size, "sha256": digest,
                      "unchanged_original_members": len(unchanged), "members": len(payload)}))


def anchors(text):
    result = set(re.findall(r'<a\s+(?:id|name)="([^"]+)"', text))
    used = {}
    fenced = False
    for line in text.splitlines():
        if re.match(r"^\s*(```|~~~)", line):
            fenced = not fenced
        if fenced or not re.match(r"^#{1,6}\s+", line):
            continue
        heading = re.sub(r"^#{1,6}\s+", "", line).strip().lower()
        heading = re.sub(r"[\[\]`*_]", "", heading)
        heading = re.sub(r"[^\w\-\s\u3400-\u9fff]", "", heading).replace(" ", "-")
        count = used.get(heading, 0)
        used[heading] = count + 1
        result.add(heading + (f"-{count}" if count else ""))
    return result


def check_links(files, names, scope):
    errors = []
    for name in scope:
        text = files[name].decode("utf-8-sig")
        text = re.sub(r"(?ms)^\s*(```|~~~).*?^\s*\1\s*$", "", text)
        for match in LINK.finditer(text):
            link = match.group(2)
            if re.match(r"[A-Za-z][A-Za-z0-9+.-]*:", link):
                continue
            path, sep, anchor = link.partition("#")
            target = posixpath.normpath(posixpath.join(posixpath.dirname(name), path)) if path else name
            if target not in names and not any(n.startswith(target.rstrip("/") + "/") for n in names):
                errors.append(f"{name}: missing {link}")
            elif sep and target.endswith(".md") and target in files and anchor not in anchors(files[target].decode("utf-8-sig")):
                errors.append(f"{name}: missing anchor {link}")
    return errors


def verify():
    files = {p.relative_to(ROOT).as_posix(): p.read_bytes() for p in (ROOT / "docs").rglob("*.md")}
    files["README.md"] = (ROOT / "README.md").read_bytes()
    scope = [name for name in files if name == "README.md" or any(name.startswith(f"docs/{lang}/") for lang in LANGUAGES)]
    names = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*") if ".git" not in p.parts}
    errors = check_links(files, names, scope)
    sets = [{p.relative_to(ROOT / "docs" / lang).as_posix() for p in (ROOT / "docs" / lang).rglob("*.md")} for lang in LANGUAGES]
    assert sets[0] == sets[1] == sets[2], "Language page coverage differs"
    for name in scope:
        if name == "README.md":
            continue
        text = files[name].decode("utf-8-sig")
        assert all(f"[{label}]" in text.splitlines()[0] for label in ("简体中文", "English", "日本語")), name
        assert not re.search(r"@[A-Z_]+@", text), f"Unexpanded placeholder in {name}"
    manifest = json.loads((ROOT / MANIFEST).read_text(encoding="utf-8"))
    path = ROOT / manifest["package_directory"] / manifest["package_file"]
    assert sha(path.read_bytes()) == manifest["package_sha256"]
    assert path.stat().st_size == manifest["package_bytes"]
    assert path.with_suffix(path.suffix + ".sha256").read_text().split() == [manifest["package_sha256"], manifest["package_file"]]
    original_path = ROOT / ORIGINAL_DIR / ORIGINAL_NAME
    assert sha(original_path.read_bytes()) == ORIGINAL_SHA256
    with zipfile.ZipFile(original_path) as source, zipfile.ZipFile(path) as archive:
        assert archive.testzip() is None
        members = archive.namelist()
        assert len(members) == len(set(n.casefold() for n in members)), "Duplicate ZIP members"
        assert set(members) == set(manifest["zip_members_sha256"])
        packed = {name: archive.read(name) for name in members}
        for name, data in packed.items():
            assert not PurePosixPath(name).is_absolute() and ".." not in PurePosixPath(name).parts
            assert sha(data) == manifest["zip_members_sha256"][name], name
        for name, data in document_payload().items():
            assert packed.get(name) == data, f"Bundled document is stale: {name}"
        for name in source.namelist():
            if name not in REPLACED:
                assert source.read(name) == packed[name], f"Protected original member changed: {name}"
        for name in ("README.md", "AIChat/README.md", "SatonePromptProxy/README.md"):
            assert all(label.encode() in packed[name] for label in ("简体中文", "English", "日本語"))
        for lang in LANGUAGES:
            for page in sets[0]:
                assert f"docs/{lang}/{page}" in packed
        package_scope = [name for name in packed if name in ("README.md", "AIChat/README.md", "SatonePromptProxy/README.md") or any(name.startswith(f"{prefix}docs/{lang}/") and name.endswith(".md") for lang in LANGUAGES for prefix in ("", "AIChat/", "SatonePromptProxy/"))]
        errors.extend(check_links(packed, set(packed), package_scope))
        for component in ("AIChat", "SatonePromptProxy"):
            prefix = component + "/"
            standalone = {name[len(prefix):]: data for name, data in packed.items() if name.startswith(prefix)}
            standalone_scope = [name[len(prefix):] for name in package_scope if name.startswith(prefix)]
            errors.extend(check_links(standalone, set(standalone), standalone_scope))
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Verified {len(sets[0])} pages per language, {len(scope)} repository pages, offline links, ZIP checksums and {len(manifest['unchanged_original_members_sha256'])} unchanged original members.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="Verify without rebuilding")
    args = parser.parse_args()
    if not args.verify:
        build()
    verify()
