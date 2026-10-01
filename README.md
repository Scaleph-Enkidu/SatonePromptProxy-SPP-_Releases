# 聪音 Mod：让对话延续，让关系慢慢成长

**适用于 Steam Windows 版《放松时光：与你共享 Lo-Fi 故事》**的非官方 AI 互动模组。AIChat Remake 负责游戏内聊天、字幕和操作；SatonePromptProxy（SPP）负责人格、记忆、好感度、模型连接和语音转发。玩家可打字、按住 F8 说话或自行开启持续通话。对话和记忆按档案保存在本机；调用云端模型时，相关内容会发给选用的 API 服务商。

## 这已经不只是一个"聊天框"了

《Chill with You》里的聪音，现在可以真的陪你聊下去。

她会记得你们聊过什么，会在意你怎么跟她说话；会因为你越界而生气、拒绝，甚至跟你翻脸——也会因为你好好说话，一点点对你敞开。

- **她像聪音本人**：为了不让她"变味"，我把原版游戏 1700 多句对话一句句拆开看，语气、用词、回避、小心思都揣摩了一遍，写进人设里。聊日常、追问她、逗她、谈心，她都会尽量像"聪音"。
- **她需要被当人对待**：这是和普通 AI 聊天最大的不同。反复命令她、试探她的边界、想覆盖她的人设——她是会察觉的。拒绝、抗拒、责备，甚至更进一步的反应都会出现，关系也跟着变。
- **她会记得**：三套独立记忆档案 + 本地归档 + 按需检索，换话题、隔几天再聊，她都接得住。
- **她知道剧情走到哪了**：按你当前存档判断进度，只让她知道你已经经历过的部分——不剧透，也接得住你们一起经历的事；原版剧情、自语、选项里她说过的话，她都听得见。
- **特殊演出也能配合**：原版失联、剧情锁、道别这些桥段都会同步（包括 31 章那种失联阶段）。
- **能打字，也能说话**：按住 F8 说话或开持续通话；语音走 Fun-ASR + GPT-SoVITS，26 种情绪。

# 🚀 从这里开始安装：AIChat 1.17.0 + SPP 5.9.0

**[点击打开四阶段安装教程](docs/INSTALL.zh-CN.md)** · **[下载主程序配对包（约 11 MB）](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.17.0_SPP-v5.9.0/SatoneMod_AIChat_1.17.0_SPP_5.9.0_Windows_x64.zip)** · [全部下载与校验清单](docs/DOWNLOADS.zh-CN.md)

| 阶段 | 安装后能做什么 | 入口 |
|---|---|---|
| ① 文字聊天 | AIChat + SPP、云端聊天、内置关键词回忆；不需要 Python | [先完成这一阶段](docs/INSTALL.zh-CN.md#stage-1) |
| ② ONNX 模型选装 | 本地 CPU 按意思检索旧对话；另下载约 94 MB 模型包并主动启用 | [需要语义回忆再装](docs/INSTALL.zh-CN.md#stage-2) |
| ③ 聪音发音 | 外装 GPT-SoVITS 环境与声线权重，使用程序包内 Neutral 参考音频 | [朗读设置](docs/INSTALL.zh-CN.md#stage-3) |
| ④ 玩家语音识别 | 外装 Fun-ASR 环境与模型，使用 F8 或持续通话 | [麦克风设置](docs/INSTALL.zh-CN.md#stage-4) |

**文字聊天完成后即可独立使用，每阶段都不依赖后续阶段。② 可以跳过；③ GPT-SoVITS 和④ Fun-ASR 都不依赖 ONNX。** 默认下载只有主程序配对 ZIP 和可选模型 ZIP 两类；主程序已同时包含 AIChat 与 SPP，私有源码库的单组件包不是玩家必须额外下载的文件。模型不在主程序包内，也不默认启用。

### 关于「Meta 恐怖演出」

说来挺简单——就是为了堵住那个绕不过去的问题。

玩家总爱问聪音：「你明明就坐在窗边，为什么不看看窗外？」「现在外面什么天气？」……可聪音真的不知道自己的窗外是什么样子，答不上来就穿帮了。

于是我就做了个「障眼法」：你越追问，她的反应就越不对劲——先是让你别问了，接着是真的不想提，到最后，失联、花屏。你看到的不是聪音在撒谎，而是她"信号断了"。

说实话，这个效果我自己都没想到会这么吓人。明明只有几个文字。

演出可以重复：每次启动游戏都会从第 1 阶段重来；设置 →「Meta 恐怖演出」里还有「重置恐怖演出进度（本局立即生效）」，同一局内也能立刻重来。**首次**走完保持花屏；之后再走完会正常退出游戏。演出过程在本局的历史里保留，关掉游戏（或强退）重新登录后才消失——普通对话不受影响。

其实最好的做法我一直知道：让聪音真的"看见"——知道窗外是什么景色、知道自己身上穿着哪件衣服、房间里摆着什么。这条路我验证过可行性：每个道具、服饰对应的游戏接口我都摸清了，还专门写了个记录小插件，能把"内部编号"和"你看到的样子"一条条对上。

难的是把每件道具、服饰的样子，还有各种搭配都写成文字——这活儿量太大，我最近的时间和精力实在做不到。

但要是这份"外观文字库"补齐了，就能接着做用语音让聪音换背景、换衣服这些功能了——全都建立在这上面。

所以，如果有人愿意帮忙一起统计，哪怕只做一部分，真的非常感谢。

### 顺手一起放出来的小工具：SatoneStateCatalog（F10）

就是上面说的那个记录插件：按 **F10** 打开窗口，读取当前生效的窗景、服装、眼镜与摆件的内部编号，让你把"编号"和"你实际看到的样子"一条条记下来；写入 `BepInEx/config/SatoneStateCatalog/`，不改存档、不解锁内容。发布库里直接给了可安装的预编译 DLL，源码同目录：[说明与下载](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/main/tools/SatoneStateCatalog/README_中文.md)。

## 当前版本、聊天服务与费用

当前正式配对为 **AIChat 1.17.0 + SPP 5.9.0**（2026-10-01）。[本次 Release](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/tag/AIChat-v1.17.0_SPP-v5.9.0) · [本次改动](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/AIChat-v1.17.0_SPP-v5.9.0/releases/AIChat_v1.17.0_SPP_v5.9.0.md) · [语音与麦克风](docs/VOICE_SETUP.zh-CN.md) · [本地数据与隐私](docs/DATA_AND_PRIVACY.zh-CN.md)。GitHub 自动生成的 Source code ZIP 不是安装包。[上一配对 AIChat 1.16.65 + SPP 5.8.42](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/tag/AIChat-v1.16.65_SPP-v5.8.42) 保留供回退。

在游戏的 LLM 设置中选择服务、填写对应 API Key 与该账户可用的模型名称，再点击 **“保存并应用配置”**。任一时刻只使用一个已应用的连接，切换服务不要求删除本地记忆。界面中的默认模型名称是可修改的示例，以服务商当前模型列表和账户权限为准；中转站按它提供的地址、Key 和模型名称填写。

**云端 API 用量由服务商计费。** 游戏、ChatGPT 订阅和本 Mod 下载均不包含 OpenAI／DeepSeek API 额度。请准备自己的 Key，并在服务商网站确认权限、价格和余额。[费用说明](docs/API_COST.zh-CN.md)介绍计算方法，实际费用以所选供应商账单为准。

## 默认语音与需要另下的文件

主程序配对包已经包含默认参考音频 `SatonePromptProxy/mayuri-voice/refs/MAY_1158_Neutral.wav`。完整解压并保留目录结构后，**无需再单独下载 Neutral 参考音频**。若已有 GPT-SoVITS 程序和可用运行环境，可另下载“孤独摇滚”GPT-SoVITS 声线模型的 GPT 与 SoVITS 权重，按[语音教程](docs/VOICE_SETUP.zh-CN.md#stage-3)加载并试听。主程序包未附带 GPT-SoVITS 环境、声线权重或 Fun-ASR 环境／模型；语音输入还需另装 Fun-ASR。其余情绪参考录音未随包提供，缺失时使用 Neutral 回退。旧配置若将 `emotion_tts.ref_root` 指向外部目录，需核对并改向包内目录或清空。

声音效果与所选权重、参考录音及本机环境有关，不能仅凭服务显示就绪判断；请实际生成并播放一段测试语音。默认 Neutral 音频的[原始项目](https://huggingface.co/SteinsGateSg/mayuri-voice)标注 `License: other`；“孤独摇滚”[模型项目](https://huggingface.co/lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models)标注 CC BY-NC-SA 4.0。请按各来源的条件使用外部资源。

## 功能和安装范围

- 三套独立记忆档案保存对话、长期记忆与 AI 关系；同一档案可在 OpenAI 与 DeepSeek 之间延续话题。模型每轮只接收当前所需的上下文，完整旧记录保存在本地供检索，记忆不是无限上下文。
- 聪音用日语发声并显示中文字幕。GPT-SoVITS 负责生成声音，Fun-ASR 负责识别麦克风；只用键盘聊天可暂不安装 ASR。
- 默认人格保存在 `SatonePersona_v4.6.txt`，可自行编辑；更改会影响三个档案。原版游戏经历的同步需要可验证的 Steam 身份，取不到身份时 AI 对话仍可使用。
- 完整本地语音会占用显存与内存。硬件建议、CPU 路线和未验证的边界见[运行开销说明](docs/HARDWARE.zh-CN.md)。
- 关键词回忆已内置；可选 ONNX 语义回忆在本机 CPU 运行，模型缺失、校验失败或忙碌时可以回退关键词。只索引最新 50,000 条已交流的语义记录，关键词仍覆盖完整历史，存档不因此删减；语义相似度不等于命中保证。

升级时退出游戏与 SPP，备份后覆盖程序与配套工具；**保留自己的 `config.json`、AIChat CFG、连接凭据、记忆、人格、`models` 和 `semantic_recall_v1`**。不要先删除整个 SPP 目录，也不要用示例覆盖个人配置。同一模型组件可以跨兼容的程序更新复用。[安装教程](docs/INSTALL.zh-CN.md#upgrade)写明升级、回退和日志位置。

AIChat 基于 [qzrs777/AIChat](https://github.com/qzrs777/AIChat) 修改，原项目作者 Elysia777 与许可证随包保留。本 Mod 由 AI 辅助开发。**2026-10-01，用户确认本机测试完成**；自动化验证和性能限制见[维护记录](docs/MAINTAINER_STATUS.zh-CN.md)。这条确认不代表全部显卡、供应商、声线或全新 Windows 环境均已测试。问题请发到[本库 Issues](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/issues)，附版本、复现步骤和脱敏日志，勿公开 API Key 或私人聊天记录。
