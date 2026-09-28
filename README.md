# 聪音 Mod：让对话延续，让关系慢慢成长

**适用于 Steam Windows 版《放松时光：与你共享 Lo-Fi 故事》**的非官方 AI 互动模组。AIChat Remake 负责游戏内聊天、字幕和操作；SatonePromptProxy（SPP）负责人格、记忆、好感度、模型连接和语音转发。玩家可打字、按住 F8 说话或自行开启持续通话。对话和记忆按档案保存在本机；调用云端模型时，相关内容会发给选用的 API 服务商。

## 当前配对版本

**AIChat 1.16.23 + SPP 5.8.26**（2026-09-28）。[下载两份完整安装包](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/tag/AIChat-v1.16.23_SPP-v5.8.26) · [从零安装](docs/INSTALL.zh-CN.md) · [文件与依赖清单](docs/DOWNLOADS.zh-CN.md) · [语音与麦克风](docs/VOICE_SETUP.zh-CN.md) · [本地数据与隐私](docs/DATA_AND_PRIVACY.zh-CN.md)。请下载 Release 中的 AIChat ZIP 和 SPP ZIP，按配对版本使用；GitHub 自动生成的 Source code ZIP 不是安装包。

OpenAI 和 DeepSeek 在游戏中各有独立的 API Key 与模型名称，点击 **“保存并应用配置”** 后才会切换，任一时刻只使用一个服务。首次配置时，OpenAI 预填 `gpt-6-luna`，DeepSeek 预填 `deepseek-flash`；输入框仍可修改，已有自定义模型不会被覆盖。这两个名称是**截至 2026-09-28 的推荐示例**，使用前请核对 [OpenAI 官方模型页](https://developers.openai.com/api/docs/models/gpt-6-luna)或 [DeepSeek 官方接口页](https://api-docs.deepseek.com/api/create-chat-completion/)。中转站另按它提供的地址和模型名称填写。

**API 用量由服务商计费。** 游戏、ChatGPT 订阅和本 Mod 下载均不包含 OpenAI／DeepSeek API 额度。请准备自己的 Key，并在服务商网站确认账户权限、价格和余额。[费用说明](docs/API_COST.zh-CN.md)中的数字是示例，不是每轮固定费用。

## 默认语音与需要另下的文件

SPP 完整包已经包含默认参考音频 `mayuri-voice/refs/MAY_1158_Neutral.wav`。完整解压并保留目录结构后，**无需再单独下载 Neutral 参考音频**。若已有 GPT-SoVITS 程序和可用运行环境，可另下载“孤独摇滚”GPT-SoVITS 声线模型的 GPT 与 SoVITS 权重，按[语音教程](docs/VOICE_SETUP.zh-CN.md)加载并试听。SPP 未附带 GPT-SoVITS 程序、声线权重或 Fun-ASR 模型；语音输入还需另装 Fun-ASR。其余情绪参考录音未随包提供，缺失时使用 Neutral 回退。旧配置若将 `emotion_tts.ref_root` 指向外部目录，需核对并改向包内目录或清空。

声音效果与所选权重、参考录音及本机环境有关，不能仅凭服务显示就绪判断；请实际生成并播放一段测试语音。默认 Neutral 音频的[原始项目](https://huggingface.co/SteinsGateSg/mayuri-voice)标注 `License: other`；“孤独摇滚”[模型项目](https://huggingface.co/lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models)标注 CC BY-NC-SA 4.0。请按各来源的条件使用外部资源。

## 功能和安装范围

- 三套独立记忆档案保存对话、长期记忆与 AI 关系；同一档案可在 OpenAI 与 DeepSeek 之间延续话题。模型每轮只接收当前所需的上下文，完整旧记录保存在本地供检索，记忆不是无限上下文。
- 聪音用日语发声并显示中文字幕。GPT-SoVITS 负责生成声音，Fun-ASR 负责识别麦克风；只用键盘聊天可暂不安装 ASR。
- 默认人格保存在 `SatonePersona_v4.5.txt`，可自行编辑；更改会影响三个档案。原版游戏经历的同步需要可验证的 Steam 身份，取不到身份时 AI 对话仍可使用。
- 完整本地语音会占用显存与内存。硬件建议、CPU 路线和未验证的边界见[运行开销说明](docs/HARDWARE.zh-CN.md)。

升级时退出游戏与 SPP，只替换程序文件；**保留自己的 `config.json`、AIChat CFG、API Key、记忆和人格文件**。首次带入旧记忆时可以选择导入或跳过；之后切换服务无需手工迁移存档。[详细步骤](docs/INSTALL.zh-CN.md)写明新装、升级、回退和日志位置。

AIChat 基于 [qzrs777/AIChat](https://github.com/qzrs777/AIChat) 修改，原项目作者与许可证随包保留。本 Mod 由 AI 辅助开发；当前配对主要功能已由维护者实机使用，1.16.23 的预填模型变更通过本地 CI，最终声音和不同设备表现仍需玩家验证。问题请发到[本库 Issues](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/issues)，附版本、复现步骤和脱敏日志，勿公开 API Key 或私人聊天记录。
