[简体中文](DOWNLOADS.md) | [English](../en/DOWNLOADS.md) | [日本語](../ja/DOWNLOADS.md)

# 下载与 SHA-256 校验

**AIChat 1.18.30 + SPP 5.10.10**

本次合并两批共 9 项修复，更新记忆导入、语音回声过滤、退出清理与日期召回。需要更新 AIChat 和 SPP 两端程序；三语说明与包内入口同步更新。

- [ZIP](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.18.30_SPP-v5.10.10/SatoneMod_AIChat_1.18.30_SPP_5.10.10_Windows_x64.zip)
- [SHA-256](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.18.30_SPP-v5.10.10/SatoneMod_AIChat_1.18.30_SPP_5.10.10_Windows_x64.zip.sha256)
- [Manifest](../../releases/AIChat_v1.18.30_SPP_v5.10.10.json)
- [ONNX (optional)](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.17.1_SPP-v5.9.1-license-r1/Satone_Semantic_E5_small_int8_ORT_1.30.0_Windows_x64.zip)

退出游戏与 SPP，完整备份旧 SPP 目录和游戏插件配置后，再替换 AIChat DLL/PDB 及 SPP。若使用新 SPP 目录，按[升级指南](UPGRADE.md)继承记忆。已刷新过的 Relaxed 白名单无需再次重置。不要使用 GitHub 自动生成的 Source code ZIP 代替安装包。TTS、ASR 与语义模型仍为可选外部组件。

```powershell
Get-FileHash .\SatoneMod_AIChat_1.18.30_SPP_5.10.10_Windows_x64.zip -Algorithm SHA256
```

SHA-256 = `.sha256` = manifest `package_sha256`.

[Release notes](releases/AIChat_v1.18.30_SPP_v5.10.10.md) · [Archive](RELEASE_ARCHIVE.md)
