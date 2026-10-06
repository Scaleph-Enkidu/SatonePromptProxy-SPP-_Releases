[简体中文](AIChat_README.md) | [English](../en/AIChat_README.md) | [日本語](../ja/AIChat_README.md)

# AIChat 1.18.28：包内说明

[文档首页](README.md) · [完整安装](INSTALL.md) · [升级](UPGRADE.md)

这是《Chill with You: Lo-Fi Story》Windows / Steam 版的游戏端插件，需与 SPP 5.10.8 配对。当前支持中文、英文、日文界面与字幕；发音支持取决于外部声线与模型。

退出游戏，安装 BepInEx 5.4.23.5 x64 并运行游戏一次。将包内 `AIChat/AIChat.dll`、`AIChat.pdb` 放入游戏 `BepInEx/plugins`，只保留一个 AIChat DLL，备份放在插件目录外。F9 打开控制台，设置并应用 SPP EXE 路径和 LLM 连接。Enter 发送，Shift+Enter 换行；F8 按住说话需另装 ASR。持续通话默认关闭，需主动开启。

N15 修复 Relaxed 端杯残留。旧配置必须将 `StablePoseOverrides` 的 Relaxed 部分改为 `Relaxed=752,50,51`，或备份后仅删除 `com.username.chillaimod.cfg` 重新配置。不要删除整套 BepInEx 配置或记忆。N14 的 409 参考策略刷新修复保留。详见[更新记录](releases/AIChat_v1.18.28_SPP_v5.10.8.md)。

窗口显示最近 50 句不等于只保存 50 句。三档记忆、人格、好感度、情绪、剧情同步与 Meta 演出见[系统说明](README.md#systems)。云端 API 需要自己的额度；TTS、ASR 与 ONNX 分别选装。先阅读[硬件负担](HARDWARE.md)、[隐私与备份](DATA_AND_PRIVACY.md)及[授权范围](LICENSE_SCOPE.md)。

本 `docs_r1` 只修订文档，没有重编译 DLL/PDB。原构建证据与本次逐文件比对分别保留，不能把文档更新当成新一轮实机测试。
