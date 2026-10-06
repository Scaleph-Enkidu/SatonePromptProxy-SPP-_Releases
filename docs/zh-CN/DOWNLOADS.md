[简体中文](DOWNLOADS.md) | [English](../en/DOWNLOADS.md) | [日本語](../ja/DOWNLOADS.md)

# 下载与 SHA-256 校验

[← 首页](README.md)

当前程序配对 **AIChat 1.18.28 + SPP 5.10.8**。推荐下面的三语文档修订包；它只更新说明，所有运行文件与原 N15 相同。已经安装 N15 的用户可直接阅读文档，无需重装。旧 CFG 必须按[升级指南](UPGRADE.md)刷新 Relaxed 白名单。

- [三语主程序包（约 43 MB）](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.18.28_SPP-v5.10.8-docs-r1/SatoneMod_AIChat_1.18.28_SPP_5.10.8_Windows_x64_docs_r1.zip)
- [原 N15 包（约 39 MB，原始哈希不变）](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.18.28_SPP-v5.10.8/SatoneMod_AIChat_1.18.28_SPP_5.10.8_Windows_x64.zip)
- [可选 ONNX（约 94 MB）](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.17.1_SPP-v5.9.1-license-r1/Satone_Semantic_E5_small_int8_ORT_1.30.0_Windows_x64.zip)
- [本次文档修订清单](../../releases/AIChat_v1.18.28_SPP_v5.10.8_docs_r1.json)

退出游戏与服务后再更新。不要使用 GitHub 自动生成的 Source code ZIP 代替安装包。TTS 环境、声线权重、ASR 环境/模型另装，主包包含默认 Neutral 参考音频。详见[安装](INSTALL.md)与[语音](VOICE_SETUP.md)。

## 校验步骤

```powershell
Get-FileHash .\SatoneMod_AIChat_1.18.28_SPP_5.10.8_Windows_x64_docs_r1.zip -Algorithm SHA256
```

PowerShell 计算结果必须与同目录 `.sha256` 文件及 manifest 的 `package_sha256` 一致。文档修订的 ZIP 哈希会变化；DLL/PDB/EXE 等运行文件逐字节保持不变。

[SHA-256](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.18.28_SPP-v5.10.8-docs-r1/SatoneMod_AIChat_1.18.28_SPP_5.10.8_Windows_x64_docs_r1.zip.sha256)

旧版本、已下架附件和历史测试范围见[归档](RELEASE_ARCHIVE.md)。
