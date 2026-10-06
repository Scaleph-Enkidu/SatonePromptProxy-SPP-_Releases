[简体中文](../zh-CN/DOWNLOADS.md) | [English](DOWNLOADS.md) | [日本語](../ja/DOWNLOADS.md)

# Downloads and SHA-256 verification

[← Home](README.md)

Current pair: **AIChat 1.18.28 + SPP 5.10.8**. Use the trilingual documentation revision below; it changes guides only and retains every original N15 runtime file. Existing N15 users can read the guides without reinstalling. Refresh the old Relaxed whitelist as described in [UPGRADE](UPGRADE.md).

- [Trilingual program package (about 43 MB)](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.18.28_SPP-v5.10.8-docs-r1/SatoneMod_AIChat_1.18.28_SPP_5.10.8_Windows_x64_docs_r1.zip)
- [Original N15 archive (about 39 MB, original hash retained)](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.18.28_SPP-v5.10.8/SatoneMod_AIChat_1.18.28_SPP_5.10.8_Windows_x64.zip)
- [Optional ONNX (about 94 MB)](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.17.1_SPP-v5.9.1-license-r1/Satone_Semantic_E5_small_int8_ORT_1.30.0_Windows_x64.zip)
- [Documentation-revision manifest](../../releases/AIChat_v1.18.28_SPP_v5.10.8_docs_r1.json)

Exit game/services before updating. Do not substitute GitHub's automatic Source code ZIP for the installer. TTS runtime/weights and ASR environment/model are external; Neutral reference audio is included. See [installation](INSTALL.md) and [voice](VOICE_SETUP.md).

## Verification

```powershell
Get-FileHash .\SatoneMod_AIChat_1.18.28_SPP_5.10.8_Windows_x64_docs_r1.zip -Algorithm SHA256
```

The PowerShell result must match the adjacent `.sha256` file and manifest `package_sha256`. A documentation revision changes the ZIP hash; DLL/PDB/EXE and other runtime bytes remain identical.

[SHA-256](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.18.28_SPP-v5.10.8-docs-r1/SatoneMod_AIChat_1.18.28_SPP_5.10.8_Windows_x64_docs_r1.zip.sha256)

See the [archive](RELEASE_ARCHIVE.md) for older versions, withdrawn assets and dated test scope.
