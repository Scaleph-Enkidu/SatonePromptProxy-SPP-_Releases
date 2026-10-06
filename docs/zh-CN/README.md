[简体中文](README.md) | [English](../en/README.md) | [日本語](../ja/README.md)

# 聪音 Mod：让对话延续，让关系慢慢成长

这是为 Windows / Steam 版《Chill with You: Lo-Fi Story》制作的非官方 Mod。AIChat 负责游戏内聊天、字幕、播放与操作；SatonePromptProxy（SPP）负责模型连接、人格、记忆、关系和语音转发。当前程序提供**简体中文、English、日本語**界面与字幕支持。语音能否自然读出某种语言，仍取决于所选声线和模型；本教程采用日语语音。

当前配对：**AIChat 1.18.28 + SPP 5.10.8（N15）**。本次 `docs_r1` 只更新三语文档与包内说明，程序二进制不变。

![安装后的聊天界面](../images/install-success.png)

## 安装前：运行负担与已知限制

**游戏、GPT-SoVITS、Fun-ASR 同时运行需要额外 CPU、内存和数 GB 显存。** 完整 GPU 语音以 **8 GB 显存作为评估起点，12 GB 以上更有余量**，不是经过多档设备验证的最低配置。6 GB 可尝试 TTS 用 GPU、ASR 用 CPU；4 GB 以下或集成显卡优先文字。云端聊天不会在本机加载聊天大模型，但自行部署本地模型要另算资源。

2026-09-27 的一次截图显示两个未识别具体用途的 Python 进程约 2.17 / 1.92 GiB、游戏约 0.63 GiB；不能把进程读数直接相加当作整卡峰值。历史合成存档测试中，SPP＋ONNX 在 1 万 / 5 万条记录时观察到约 **441 / 944 MB RAM**，启动约 **11.65 / 495.12 秒**，不含游戏、TTS、ASR。350 MB 门禁只针对 worker，不代表整个 SPP。

**大存档冷启动慢、部分玩家反馈的游戏掉帧原因仍未解决，尚无统一验证通过的低显存模式。** AMD／Intel GPU 不能直接照搬 NVIDIA CUDA 方案，先使用文字和 ONNX CPU 路线。三语文档主程序约 43 MB、模型约 94 MB 的下载大小不代表运行内存。完整数据与范围见[硬件说明](HARDWARE.md)。

## 安装、升级与排错

| 你要做什么 | 从这里开始 |
| --- | --- |
| 第一次安装 | [四阶段完整教程](INSTALL.md) |
| 获取程序与校验文件 | [下载清单与 SHA-256](DOWNLOADS.md) |
| 已有旧版本 | [升级、记忆继承与回滚](UPGRADE.md) |
| 选装语义回忆 | [ONNX 设置](ONNX_SETUP.md) |
| 聪音发音、麦克风与排错 | [语音进阶](VOICE_SETUP.md) |
| API 费用 | [费用计算与账单](API_COST.md) |
| 保存、迁移与隐私 | [数据和备份](DATA_AND_PRIVACY.md) · [迁移部署](PORTABLE_DEPLOYMENT.md) |
| 阅读包内说明 | [AIChat README](AIChat_README.md) · [SPP README](SPP_README.md) · [安装与回滚](PACKAGE_INSTALL.md) |

安装顺序是 **① 文字聊天 → ② 可选 ONNX → ③ 可选 TTS → ④ 可选 ASR**。文字完成即可使用；后三项分别选择，TTS／ASR 不依赖 ONNX。F9 打开聊天，Enter 发送，Shift+Enter 换行；F8 按住说话，持续通话需要主动开启。

N15 移除了 Relaxed 的端杯动作。旧用户必须刷新 `StablePoseOverrides` 中的 `Relaxed=752,50,51`，详见升级页。N14 的 SPP 参考策略刷新修复也保留。换 SPP 目录时，使用新目录中的“继承旧版本记忆”入口读取旧目录，不要删除旧记忆。

## 她会记得什么，又会如何回应

人格参考了原作 1,700 多条台词，保留聪音的自主性、表达习惯和边界。她可以亲近、开玩笑、主动分享，也可以拒绝；高好感并不等于无条件服从。26 种情绪按发言区间表达，不是固定好感加减分。

三套记忆档案分别保存聊天、长期记忆和 AI 关系，支持在不同服务与模型之间延续。同一轮只选取需要的近期交流、摘要和相关历史；关键词覆盖完整可用历史，任意 ONNX 语义回忆覆盖最新 50,000 条有效交流，较早权威记录不会因此删除。人格文件 `SatonePersona_v4.6.txt` 由三档共用。

原版剧情知识与共同经历按已确认的游戏身份和进度参与上下文；第 31 章等失联状态遵循游戏本身。身份同步失败不等于所有 AI 对话不可用，但不能凭空认定剧情进度。原作经验加值与 AI 的好感、信任、舒适、开放四维分开保存。

目前还不能完整识别窗景、服装、眼镜和摆件。围绕“为什么不看窗外”的持续追问可能引出 Meta 演出，出现回避、失联与花屏。作者曾感叹，纯文字演出比预想更恐怖。设置可关闭或重置，每次启动从阶段 1 开始；具体结局和恢复见 [Meta 说明](systems/META.md)。

<a id="systems"></a>
## 系统设计与使用说明

- [人格](systems/PERSONA.md)
- [好感度计算](systems/AFFECTION.md)
- [边界与关系修复](systems/BOUNDARIES.md)
- [26 种情绪](systems/EMOTIONS.md)
- [记忆与档案](systems/MEMORY.md)
- [历史回忆与检索](systems/RECALL.md)
- [剧情知识与共同经历](systems/STORY_KNOWLEDGE.md)
- [原版剧情协同](systems/STORY_COORDINATION.md)
- [Meta 演出](systems/META.md)
- [聊天界面与历史](systems/CHAT_UI.md)
- [回复校验与恢复](systems/RECOVERY.md)
- [模型连接与切换](systems/CONNECTIONS.md)
- [服务与进程管理](systems/SERVICES.md)
- [语音与字幕](systems/SPEECH.md)
- [语音输入与持续通话](systems/VOICE_INPUT.md)

## 可选 F10 外观采集工具

[SatoneStateCatalog](tools/STATE_CATALOG.md) 是独立小插件，用 F10 读取当前生效的外观编号并记录描述。它不解锁内容、不修改存档，也不代表聪音已经能控制场景。提供[源码构建说明](tools/BUILD_STATE_CATALOG.md)和[待观察编号](tools/OBSERVED_IDS.md)。预编译版本的构建记录与实机验证范围分开说明。

<a id="roadmap"></a>
## 未来安排

继续完善语音体验和适合不同语言的声线，建立外观描述库，并探索通过对话调整环境与道具。中英日 UI／字幕已纳入当前功能，不再列为待开发功能；中文语音等效果仍需匹配模型与后续验证。

## 版本、署名和授权

[本次三语文档修订](releases/DOCS_TRILINGUAL_20261006.md) · [N15 更新记录](releases/AIChat_v1.18.28_SPP_v5.10.8.md) · [历史与验证归档](RELEASE_ARCHIVE.md)

AIChat 基于 [qzrs777/AIChat](https://github.com/qzrs777/AIChat)，原作者 Elysia777；本项目由 Scaleph 维护，开发中使用 AI 辅助。可授权的自有内容采用 PolyForm Noncommercial 1.0.0，原作者、第三方资源和此前 MIT 授权的权利保留。见[授权范围](LICENSE_SCOPE.md)、[LICENSE](../../LICENSE) 与 [NOTICE](../../NOTICE)。GPT-SoVITS、Fun-ASR、E5、ORT、声线与录音各遵循其来源条件。
