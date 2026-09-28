# AIChat 1.16.23 + SatonePromptProxy 5.8.26

CP14-9 配对正式安装包，2026-09-28。

## 本次更新

- OpenAI 的新配置预填 `gpt-6-luna`，DeepSeek 预填 `deepseek-flash`；界面示例标注推荐日期 2026-09-28。已有自定义模型保留，模型名称仍可手动修改。请以[OpenAI 官方文档](https://developers.openai.com/api/docs/models/gpt-6-luna)和[DeepSeek 官方文档](https://api-docs.deepseek.com/api/create-chat-completion/)为准。
- 选择公司、填写 Key 和模型先形成草稿；点“保存并应用配置”才切换。中转站按服务商提供的地址、Key 和模型填写。
- 延续先前的回复状态、语音流程、错误提示和记忆处理修复。此前 1.16.22 + 5.8.26 的主要功能由维护者实机确认正常；本次默认模型改动通过 13 项本地 CI。
- SPP 包已带 `mayuri-voice/refs/MAY_1158_Neutral.wav`。在已安装 GPT-SoVITS 程序及运行环境后，另准备“孤独摇滚”GPT／SoVITS 声线模型权重，即可用这份默认参考音频测试发声。其他情绪音频、模型权重、GPT-SoVITS 程序和 Fun-ASR 模型未包含。

## 安装与回退

请同时下载 `AIChat_v1.16.23.zip` 和 `SatonePromptProxy_v5.8.26.zip`，不要下载 GitHub 自动生成的 Source code ZIP。退出游戏与 SPP，替换 AIChat DLL／PDB，并把 SPP 包完整解压到独立目录；保留自己的 `config.json`、API Key、人格和记忆。旧 `emotion_tts.ref_root` 指向外部目录时，请核对并改向包内 `mayuri-voice/refs` 或清空。详细步骤见[安装教程](../docs/INSTALL.zh-CN.md)与[下载清单](../docs/DOWNLOADS.zh-CN.md)。回退时成对恢复原程序和备份，切换模型不要求迁移存档。

## 校验与范围

- AIChat ZIP SHA-256：`4673b76e4e3c1aba4e7b57f0054dc53ea65176e08936eeaa7f91da8c00515648`
- SPP ZIP SHA-256：`88a01fdaba7648f26db80f8ccc5d1937d2a10a98ad868770e9ff8021eecd2119`
- 包内 Neutral WAV SHA-256：`ad79cf940b28545f2034c841755fb6c5a9479b250e45763d7fecf629bf0a9970`

本地 CI 通过核心／UI／配对流程测试和 DLL／EXE 构建。1.16.23 的真实 OpenAI、DeepSeek 与语音效果仍需用户在各自机器上验证。安装包不含玩家数据或个人 Key；请勿把自己的配置和日志直接公开。
