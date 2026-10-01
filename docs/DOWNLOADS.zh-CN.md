# 下载清单：AIChat 1.17.1 + SPP 5.9.1

[返回首页](../README.md) · [四阶段安装教程](INSTALL.zh-CN.md)

更新日期：2026-10-01。首次安装先下载配对主程序包，包含 AIChat、SPP、最新四个 BAT 与完整教程。语义模型仍为独立选装，同一模型已安装时可以复用。GitHub 自动生成的 Source code ZIP 不是安装包。

| 附件 | 用途 | 安装位置 |
|---|---|---|
| [SatoneMod_AIChat_1.17.1_SPP_5.9.1_Windows_x64.zip](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.17.1_SPP-v5.9.1/SatoneMod_AIChat_1.17.1_SPP_5.9.1_Windows_x64.zip)（约 11 MB） | AIChat 1.17.1 + SPP 5.9.1 配对主程序 | DLL/PDB 放到游戏 BepInEx/plugins，SPP 整目录放到固定运行位置 |
| [Satone_Semantic_E5_small_int8_ORT_1.30.0_Windows_x64.zip](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.17.1_SPP-v5.9.1/Satone_Semantic_E5_small_int8_ORT_1.30.0_Windows_x64.zip)（约 94 MB） | 按意思查找历史对话的可选模型 | models 放在 SPP EXE 旁，按教程 Verify → Enable → 重启 |

主程序包含默认 Neutral 参考音频；GPT-SoVITS、Fun-ASR、声线及识别权重按需另装。ONNX 不是 TTS/ASR 的前置条件。

已安装用户先退出游戏和 SPP，备份程序文件，再覆盖 DLL/PDB、SPP EXE、BAT 和说明。保留 config.json、连接凭据、关系、记忆、聊天记录、models、缓存和语音目录；不要覆盖或删除玩家资料。可分别使用两个私库的 [AIChat 1.17.1](https://github.com/Scaleph-Enkidu/SatoneAIChat_Remake/releases/tag/AIChat-v1.17.1) / [SPP 5.9.1](https://github.com/Scaleph-Enkidu/SatonePromptProxy/releases/tag/SPP-v5.9.1) 组件包。

[本次正式 Release](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/tag/AIChat-v1.17.1_SPP-v5.9.1) · [SHA-256 与包内文件清单](../releases/AIChat_v1.17.1_SPP_v5.9.1.json)。原版本和原模型下载保留。程序更新后游戏掉帧根因仍未确定，不将 BAT 调整描述为 FPS 修复。

```powershell
Get-FileHash -LiteralPath '.\SatoneMod_AIChat_1.17.1_SPP_5.9.1_Windows_x64.zip' -Algorithm SHA256
```

四个阶段与旧语音输入恢复见[完整教程](INSTALL.zh-CN.md)。
