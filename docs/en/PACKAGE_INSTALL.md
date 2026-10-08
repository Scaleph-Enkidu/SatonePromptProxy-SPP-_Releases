[简体中文](../zh-CN/PACKAGE_INSTALL.md) | [English](PACKAGE_INSTALL.md) | [日本語](../ja/PACKAGE_INSTALL.md)

# Installation and rollback

**AIChat 1.18.30 + SPP 5.10.10 · 2026-10-08**

This release combines nine fixes across memory import, voice echo filtering, exit cleanup and date-based recall. Update both AIChat and SPP. The three-language guides and package entry points are updated together.

Exit the game and SPP. Back up the entire old SPP directory and plugin configuration before replacing AIChat DLL/PDB and SPP. When moving SPP, follow the [upgrade guide](UPGRADE.md) to import memory. A previously corrected Relaxed whitelist needs no further reset. GitHub’s automatic Source code ZIP is not an installer. TTS, ASR and semantic models remain optional external components.

The root and both component README files provide Chinese, English and Japanese entry points, with full guides in their respective `docs/zh-CN`, `docs/en` and `docs/ja` directories. Preserve the complete SPP directory on a new installation. Put AIChat DLL/PDB in the game’s `BepInEx/plugins`; keep one AIChat DLL and store backups elsewhere. For rollback, stop services and restore the old programs together with the complete pre-upgrade data backup. `BUILD_INFO.json` records this version’s sources, binaries and per-file hashes.

[Install](INSTALL.md) · [Upgrade](UPGRADE.md) · [Checks](PACKAGE_CHECKLIST.md)
