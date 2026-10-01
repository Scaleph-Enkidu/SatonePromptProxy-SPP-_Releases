# SatonePromptProxy 5.9.1：版本与改动

正式配对 AIChat 1.17.1，发布日期 2026-10-01。

- Start_Text_Chat.bat 在当前控制台运行同目录 SPP，启动失败保留错误、返回码并等待按键。
- Verify_Semantic_Recall.bat、Enable_Semantic_Recall.bat、Disable_Semantic_Recall.bat 使用稳定的 ASCII 命令和 CRLF，修正 Windows cmd 对旧脚本的解析问题。
- 最新四阶段安装正文覆盖双击 EXE 启动、BAT 备用入口、语义组件 Verify/Enable 排错，以及旧语音输入复制/导出/移除的真实 UI 入口。
- 配对 AIChat 的同步、中文提示、TTS 异常折叠、独立聊天背景及分区修正统一发布。

SPP 应用标识增加到 5.9.1，重新构建程序；除版本标识外，服务核心源码沿用原受测逻辑。本次没有新增记忆迁移、模型版本、FPS 修复或大 WAL 加速。ONNX 模型继续独立选装，已安装同一组件可以复用。

先退出 SPP 和游戏，备份 EXE/BAT，覆盖程序与工具；保留 config.json、连接/凭据、记忆/关系/聊天、models、缓存和 GPT-SoVITS/Fun-ASR/语音目录。[完整教程](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/AIChat-v1.17.1_SPP-v5.9.1/docs/INSTALL.zh-CN.md)和[正式配对发布](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/tag/AIChat-v1.17.1_SPP-v5.9.1)。
