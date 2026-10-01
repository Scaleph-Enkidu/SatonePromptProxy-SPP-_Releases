# AIChat 1.17.1：版本与改动

正式配对 SatonePromptProxy 5.9.1，发布日期 2026-10-01。

- 原版进度在连接、配置切换或服务恢复后及时重同步；首次绑定前显示同步状态，成功后刷新好感度。
- 模型切换结果显示中文「切换成功」，TTS 参考音频的异常名称与原因集中在「异常原因」折叠。
- 窗口和历史记录框各有独立背景透明度，0.00 完全透明、1.00 完全不透明。
- 「自定义聊天背景颜色」包含 R/G/B 和明度；仅作用于历史记录框。设置分组、历史框、标题和输入操作区保留分区与原尺寸。
- 历史提示为「（历史记录仅显示最近50句对话）」，左上角标题为「AIChat Remake控制台」。
- 配对包合入最新四个 BAT 与四阶段教程，包含语义脚本排错、SPP 日志窗口说明和旧语音输入恢复。

继续保留原有聊天、原生字幕/动画、三档记忆、关系/情绪、Meta 演出、F8 按住说话及持续通话。升级时退出游戏，备份并覆盖 DLL/PDB，plugins 中只保留一份 AIChat.dll；保留配置、关系、记忆、记录、模型与语音目录。

掉帧根因和 SPP 大档冷启动耗时仍未解决。本地构建/UI/同步回归与封包不等于全部游戏场景已实测。详见 [本包教程](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/AIChat-v1.17.1_SPP-v5.9.1/docs/INSTALL.zh-CN.md)和[完整发布页](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/tag/AIChat-v1.17.1_SPP-v5.9.1)。
