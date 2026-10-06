[简体中文](../zh-CN/PACKAGE_INSTALL.md) | [English](PACKAGE_INSTALL.md) | [日本語](../ja/PACKAGE_INSTALL.md)

# N15 documentation package: installation and rollback

**AIChat 1.18.28 + SPP 5.10.8**, documentation revision **docs_r1, 2026-10-06**. This revises the documentation of the released N15 runtime; it is not a new unpublished runtime candidate. The original archive remains, and every non-document runtime member is unchanged.

The root `README.md` has three language entrances. `AIChat/README.md` and `SatonePromptProxy/README.md` provide component entrances. Full offline text lives in `docs/zh-CN`, `docs/en`, `docs/ja`. External downloads, web status pages and source links still need their corresponding services/network.

1. Exit game/SPP and back up the old binaries, entire personal SPP folder and game `BepInEx/config`.
2. Put AIChat DLL/PDB in `BepInEx/plugins`. New SPP users need its entire folder; users already on the same SPP 5.10.8 from N9–N14 do not need a different EXE.
3. If moving to a new SPP directory, use [memory import](UPGRADE.md) with the old directory's absolute path; do not erase it first.
4. Refresh the Relaxed whitelist to `752,50,51`, or back up/regenerate only the plugin CFG. Regeneration resets paths, API settings, thresholds, keys and emotion display.
5. Confirm log version 1.18.28 and follow the [checklist](PACKAGE_CHECKLIST.md). Full prerequisites and voice instructions are in [installation](INSTALL.md).

For rollback, stop services and restore the matching old DLL/PDB, SPP and complete pre-upgrade configuration/data. Reading or replacing documentation alone needs no save migration. `BUILD_INFO.json` retains the original N15 seal; `DOCUMENTATION_REVISION.json` records changed document members, original archive hash and unchanged-file proof.
