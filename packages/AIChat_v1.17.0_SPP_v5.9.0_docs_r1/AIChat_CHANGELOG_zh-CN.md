# AIChat 1.17.0：版本与改动

正式配对 **SatonePromptProxy 5.9.0**，用户于2026-10-01确认测试完成并批准发布。此文件为**文档修订 1**：补齐玩家可独立阅读的说明，**不修改 AIChat DLL 或 SPP EXE**，程序运行版本仍为1.17.0/5.9.0。

## 本版实际变化

- **文字玩家不必等待麦克风环境。** 未安装或未启用语音模块时，两个语音按钮深灰锁定并说明原因，文字输入和正常空闲抬头继续可用；加载中与真正就绪分别显示对应状态。
- **状态更可靠。** 兼容旧 SPP 的可选安装字段，处理过期状态和重启后的重新确认，修正锁定按钮仍误显示可用悬停效果的问题；原版剧情门禁继续优先。
- **本地回忆无需 Python。** 配对SPP将关键词Recall内置于Go主程序；语义回忆使用独立选装的E5 int8/ONNX组件，不把模型或语音环境当作文字前置。
- **待结算提示更准确。** 超时或待结算时提示查看SPP与日志，不再承诺一次重启必然补完记忆整理，也不要求重复发送同一请求。
- **程序和大模型独立分发。** 约11MB配对主程序可独立使用；约94MB语义组件另下载，已有同一组件可校验复用。主程序更新时保留模型、缓存和个人资料。

## 继续保留的能力

本版沿用聊天Dock与历史、游戏原生字幕/动画、原版台词同步、按存档判定剧情知识、三档Memory、关系与情绪显示、Meta演出、F8按住说话/持续通话、TTS单段预取和此前稳定性修正。这些属于既有能力，本次文档修订没有新增或重写其运行逻辑。

聪音回复在整轮播放或字幕展示完成后写入历史，原版剧情、自语和点击台词按ID幂等同步。原版共同经历叠加需要可靠Steam身份；身份不可用不代表已有AI对话和独立AI关系被删除。

## 安装与更新的影响

先完成文字，再按需求选装ONNX、聪音TTS、玩家ASR；各阶段不依赖后续，ONNX不是语音前置。语义组件放SPP EXE同层，AIChat DLL/PDB放游戏 `BepInEx/plugins`，避免同时加载两份插件。

设置先编辑草稿，再点击“保存并应用配置”；服务显示“（正在使用）”后才按新连接发消息。语音共用SPP代理地址 `http://127.0.0.1:11435`，不要把供应商聊天URL填进语音地址。

升级前停机、备份。覆盖程序时保留AIChat CFG/history、SPP配置/凭据、记忆与归档、旧数据库、模型、缓存、Persona/profiles及声线。文档修订1不要求重新配置连接、删除档案或重新下载同一模型。

## 已知限制与验证边界

- 配对SPP的大WAL冷启动仍慢：5万条合成历史的WAL重放与档案投影约**495.12秒**，整管线观察峰约**944MB**；“350MB”只针对既定worker+向量持续查询作用域，不代表整套SPP。文档修订1没有新增启动加速。
- 自动化和隔离解压验收使用固定程序与指定输入；用户本机确认通过，仍不能保证所有硬件、云端供应商、麦克风/声线组合或每条玩家语料都表现相同。
- 程序继续沿用原受测DLL/EXE；补写正文和重新封装文档不能被理解为新运行代码通过全套测试。出现问题请保留日志和资料，先按安装指南排查。

完整使用方法见[AIChat 包内 README 完整正文](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.17.0_SPP-v5.9.0-docs-r1/AIChat_README_zh-CN.md)，详细步骤见 [本包安装指南](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/main/docs/INSTALL.zh-CN.md)和[语音设置](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/main/docs/VOICE_SETUP.zh-CN.md)。正式版本入口仍为 [AIChat 1.17.0 + SPP 5.9.0 Release](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/tag/AIChat-v1.17.0_SPP-v5.9.0)；附件校验与文档修订信息以 [最新下载与校验说明](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/main/docs/DOWNLOADS.zh-CN.md)为准。
