[简体中文](SPP_README.md) | [English](../en/SPP_README.md) | [日本語](../ja/SPP_README.md)

# SatonePromptProxy 5.10.8：包内说明

[文档首页](README.md) · [完整安装](INSTALL.md) · [迁移部署](PORTABLE_DEPLOYMENT.md)

SPP 与 AIChat 1.18.28 配对，负责模型代理、人格、三档记忆、关系、关键词/可选语义回忆，以及 TTS/ASR 转发。保留完整目录结构，建议放在 `D:\LofiMOD\SatonePromptProxy`。

运行 `SatonePromptProxy.exe`，看到 `127.0.0.1:11435` 的监听日志后保持窗口运行。在 F9 中配置 SPP 路径及服务商 API Key、模型，保存并应用。首次启动会从 `config.example.json` 生成 `config.json`，不要用示例覆盖个人配置。`Start_Text_Chat.bat` 启动同一个服务；其他工具和自动启动说明见[服务管理](systems/SERVICES.md)。

文字与关键词回忆不需要 Python。可选 ONNX E5 int8/ORT 模型在 CPU 上运行，约 94 MB 的组件另下，并在停机时 Verify/Enable；TTS 和 ASR 不依赖它。主包有 `mayuri-voice/refs/MAY_1158_Neutral.wav`，没有完整 GPT-SoVITS、声线权重或 Fun-ASR 模型。[语音教程](VOICE_SETUP.md)给出具体环境与测试。

游戏共用语音 URL 为 `http://127.0.0.1:11435`，SPP 转发到 TTS 9880 和 ASR 9881。路径、状态和 CPU 分支请按[安装正文](INSTALL.md)，不要把日志窗口当命令行。

升级时停机并保存整个旧 SPP 目录，在新目录导入记忆；不要把 `local_v1` 当缓存删除。人格 `SatonePersona_v4.6.txt` 由三档共用，长期关系各自独立。大存档冷启动仍慢，详见[硬件](HARDWARE.md)。API Key、聊天、向量缓存均需保护，见[数据](DATA_AND_PRIVACY.md)。

本 `docs_r1` 不改 EXE、BAT、默认配置、人格、ASR 脚本、模型或参考录音。[授权与署名](LICENSE_SCOPE.md)及原第三方许可继续保留。
