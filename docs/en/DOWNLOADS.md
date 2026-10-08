[简体中文](../zh-CN/DOWNLOADS.md) | [English](DOWNLOADS.md) | [日本語](../ja/DOWNLOADS.md)

# Downloads and SHA-256 verification

**AIChat 1.18.30 + SPP 5.10.10**

This release combines nine fixes across memory import, voice echo filtering, exit cleanup and date-based recall. Update both AIChat and SPP. The three-language guides and package entry points are updated together.

- [ZIP](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.18.30_SPP-v5.10.10/SatoneMod_AIChat_1.18.30_SPP_5.10.10_Windows_x64.zip)
- [SHA-256](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.18.30_SPP-v5.10.10/SatoneMod_AIChat_1.18.30_SPP_5.10.10_Windows_x64.zip.sha256)
- [Manifest](../../releases/AIChat_v1.18.30_SPP_v5.10.10.json)
- [ONNX (optional)](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.17.1_SPP-v5.9.1-license-r1/Satone_Semantic_E5_small_int8_ORT_1.30.0_Windows_x64.zip)

Exit the game and SPP. Back up the entire old SPP directory and plugin configuration before replacing AIChat DLL/PDB and SPP. When moving SPP, follow the [upgrade guide](UPGRADE.md) to import memory. A previously corrected Relaxed whitelist needs no further reset. GitHub’s automatic Source code ZIP is not an installer. TTS, ASR and semantic models remain optional external components.

```powershell
Get-FileHash .\SatoneMod_AIChat_1.18.30_SPP_5.10.10_Windows_x64.zip -Algorithm SHA256
```

SHA-256 = `.sha256` = manifest `package_sha256`.

[Release notes](releases/AIChat_v1.18.30_SPP_v5.10.10.md) · [Archive](RELEASE_ARCHIVE.md)
