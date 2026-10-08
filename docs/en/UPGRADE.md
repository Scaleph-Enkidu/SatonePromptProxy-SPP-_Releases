[简体中文](../zh-CN/UPGRADE.md) | [English](UPGRADE.md) | [日本語](../ja/UPGRADE.md)

# Upgrade and rollback

[Home](README.md) · [Installation](INSTALL.md) · [Backup scope](DATA_AND_PRIVACY.md)

**AIChat 1.18.30 + SPP 5.10.10**. This release combines nine fixes across memory import, voice echo filtering, exit cleanup and date-based recall. Update both AIChat and SPP. The three-language guides and package entry points are updated together.

## 1. Back up before changing files

Exit the game, SPP and related voice services. Copy the **entire old SPP runtime directory**, including `local_v1`, `memory_profiles`, configuration, credentials, persona and legacy files. Back up the game's `BepInEx\config` and current AIChat DLL/PDB. Keep DLL backups outside `plugins`.

## 2. Install in a new SPP directory and import

Extract the new SPP to a separate directory. Replace the game's single AIChat DLL/PDB with the new pair. Start the game/new SPP; in the SPP/persona-memory settings, use the old-version memory inheritance/import action and enter the **absolute path of the old SPP directory**. The importer reads the old directory and backs up the destination. Verify the selected profile and history after completion. Keep the original backup until the new installation is confirmed.

Set the new SPP EXE path and check all external TTS/ASR/model paths. A directory move alone does not automatically migrate memories. Do not replace your personal configuration blindly with an example. See [portable deployment](PORTABLE_DEPLOYMENT.md).

## 3. Refresh the old N15 animation setting

N15 removes cup/tea actions **256,751,753,755,52** from the Relaxed pool. Existing CFG values are retained by BepInEx, so replacing the DLL alone is insufficient.

Prefer the targeted edit in `BepInEx\config\com.username.chillaimod.cfg`:

```text
Relaxed=256,751,753,755,52
```

becomes:

```text
Relaxed=752,50,51
```

Edit only the Relaxed portion of `StablePoseOverrides`, keep other entries, save, and restart the game. Alternatively, after backing it up, delete **only** `com.username.chillaimod.cfg` so it regenerates. This resets plugin keys, API settings, thresholds, paths and the emotion-display switch; reconfigure them, including the SPP path. It does not erase SPP memories.

Do not delete `BepInEx.cfg`, `BepInEx/core`, `AIChatSatoneUX.history`, `SatoneInputHistory.v2.jsonl`, `AIChat.spp-*.json` or old memory directories to refresh this one setting.

## 4. Check and roll back

Confirm `Loading [AIChat Remake 1.18.30]` in `BepInEx\LogOutput.log`, inspect F9 connection/path settings and the imported profile in Dashboard. Try several relaxed conversations; cup props should not remain on the fixed path. [Package checks](PACKAGE_CHECKLIST.md) distinguish the tested whitelist path from the standard pool that previously had static review only.

For rollback, stop services and restore the matching old program **and full pre-upgrade data backup**. Newer records are not guaranteed to be understood by an older version. A documentation-only package requires no data migration by itself.
