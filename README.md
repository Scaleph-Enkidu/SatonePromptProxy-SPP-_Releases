# 聪音 Mod：普通玩家安装指南

适用游戏：《放松时光：与你共享Lo‑Fi故事》（Chill with You : Lo-Fi Story）的 Steam Windows 版。

本 Mod 由 **AIChat Remake** 和 **SatonePromptProxy（SPP）** 共同工作。AIChat 在游戏里显示聊天、字幕并播放语音；SPP 管理角色设定、记忆、关系及语音服务连接。

**安装教程草稿 v3 · 核查日期 2026-09-26 · 当前配对：AIChat 1.16.14 + SPP 5.8.23。**

## 安装前先读：你需要自行支付 OpenAI API 费用

**这是开始安装前最重要的条件。当前教程使用 OpenAI API 生成聪音的回答，玩家必须准备自己的 API Key，并开通 API 计费或按 OpenAI 页面要求购买可用额度。没有可用的 API 服务，安装两个插件也不能让聪音进行 AI 对话。**

这里说的是 OpenAI API，不是登录 ChatGPT 网页。购买游戏、下载 Mod 或订阅 ChatGPT Plus/Pro，都不等于已经为这个 Mod 购买 API 用量。本教程目前没有经过验证的纯离线主聊天模型安装方案。

**推荐使用 GPT-6 Luna，在模型名称一栏准确填写 `gpt-6-luna`。** 先查看 [OpenAI 官方模型说明](https://developers.openai.com/api/docs/models/gpt-6-luna)、[API 价格](https://developers.openai.com/api/docs/pricing)与[计费页面](https://platform.openai.com/settings/organization/billing/overview)，确认自己的账户能够使用，再到 [API Key 页面](https://platform.openai.com/api-keys)创建密钥。具体付款方式、地区要求与额度以 OpenAI 页面为准。

### 大概会花多少钱

API 按处理的 token 收费，**不会按照“说一句固定扣多少钱”收费**。本页把“玩家发一条消息，聪音回复一次”记为 1 轮。人格、记忆、旧对话、好感更新、记忆整理与推理过程都会影响用量。

2026-09-26 核对的 GPT-6 Luna Standard 单价为：每百万 token，普通输入 **$0.10**、缓存命中输入 **$0.01**、写入缓存输入 **$0.125**、输出 **$0.50**。原文数值、计算公式和完整前提见[费用说明](docs/API_COST.zh-CN.md)。

下面只是**预算演算，不是实测均值或费用上限**。将主聊天和所有辅助请求均摊到每轮；人民币按 **$1 = ¥7 的示例汇率**换算，未含税费及手续费。未命中的输入全部按较高的缓存写入价计算，输出包含推理 token。

| 演算前提 | 每天 100 轮 | 连续 30 天，共 3,000 轮 | 假设有 $5 余额，每天 100 轮约能用 |
|---|---:|---:|---:|
| 每轮合计 30,000 输入、1,000 输出；90% 输入命中缓存 | $0.1145，约 ¥0.80 | $3.435，约 ¥24.05 | 43.7 天 |
| 同样的输入和输出，但没有缓存命中 | $0.425，约 ¥2.98 | $12.75，约 ¥89.25 | 11.8 天 |
| 每轮合计 50,000 输入、4,000 输出；没有缓存命中 | $0.825，约 ¥5.78 | $24.75，约 ¥173.25 | 6.1 天 |

例如，在第二种假设下，1,000 轮相当于每天 100 轮聊 10 天，约花 **$4.25 / ¥29.75**。$5 不是最低充值额或套餐，天数也不代表额度有效期。实际消耗可能超过这些例子；请以 [OpenAI 用量页](https://platform.openai.com/usage)和账单为准。

**当前 SPP 5.8.23 的内置价格表尚未包含 `gpt-6-luna`，面板显示 0 或未知不等于免费。** [费用说明](docs/API_COST.zh-CN.md)提供了本地估算表的填写方法。

## 安装难度与项目声明

**目前安装过程非常复杂，适合具有一定电脑使用经验、愿意阅读教程并自行排查问题的玩家。** 虽然不需要 Git 或编译代码，但你仍需要管理文件路径、修改 JSON/YAML 配置、安装多个程序与模型，并在命令行或日志中排查错误。完整语音和麦克风配置可能花费大量时间与心力；请在投入前判断自己是否愿意承担这些成本。

这是我为个人需求制作并主要自用的粗糙模组，目前稳定性可能存在较大问题，易用性也不佳。不同电脑、显卡驱动、游戏更新和外部服务可能导致故障。我不保证所有功能持续可用，也不承诺及时修复或提供逐台电脑的安装支持。请自行决定是否安装、备份个人数据，并自行承担安装与使用中的 API 费用、故障、数据损失及其他问题和风险。

**本项目的代码编写、修改、排错和文档整理大量使用了 OpenAI Codex。** AI 参与开发不等于代码已被充分验证；仍需要人工检查和实际使用反馈。

遇到问题欢迎在[本发布库的 Issues](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/issues)反馈。请提供 AIChat/SPP 版本、操作步骤和脱敏后的日志片段，不要上传 API Key、完整个人配置或私人聊天记录。

## 原作者与致谢

本项目中的 AIChat Remake 基于 **[qzrs777/AIChat](https://github.com/qzrs777/AIChat)** 修改而来。原项目 [MIT 许可证](https://github.com/qzrs777/AIChat/blob/main/LICENSE)的署名为 **Elysia777**，原文为 “Copyright (c) 2025 Elysia777”。

**非常感谢 AIChat 原作者与贡献者完成从 0 到 1 的工作。** 本改版是在他们已经建立的基础上，继续修改界面、功能与 SPP 配合方式。原许可证和作者署名随分发文件保留，见 [AIChat_LICENSE.txt](packages/AIChat_v1.16.14_SPP_v5.8.23/AIChat_LICENSE.txt)。本改版与 SPP 引入的问题请向本项目反馈，不应要求上游作者为这些修改负责。

## 下载这两个插件

统一入口：[AIChat 1.16.14 + SPP 5.8.23 配对发布](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/tag/AIChat-v1.16.14_SPP-v5.8.23)。

| 安装包 | 放在哪里 |
|---|---|
| [AIChat_v1.16.14.zip](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.16.14_SPP-v5.8.23/AIChat_v1.16.14.zip) | 解压取出 AIChat.dll，放到游戏的 BepInEx/plugins |
| [SatonePromptProxy_v5.8.23.zip](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.16.14_SPP-v5.8.23/SatonePromptProxy_v5.8.23.zip) | 全部解压到固定文件夹，运行 SatonePromptProxy.exe |

第一次安装还需要 BepInEx 和自己的 API 配置，请从下方“一步一步安装”开始。不要下载 Source code 作为插件包。

> **访问状态：** 两份正式包已集中到本发布库，并保留原 ZIP、SHA256 校验文件及 AIChat 原许可证。当前本发布库仍是 Private，未获得本库权限的玩家会看到 404；公开本库后，玩家无需访问两个源码仓库。后藤一里声线、Mayuri 参考音频与 26 种情绪的文件对应关系已写入语音说明；Windows 全新安装实测仍需补齐。

| 你要做什么 | 阅读哪一页 |
|---|---|
| 先了解 API 购买、模型选择和使用费用 | [API 与费用估算](docs/API_COST.zh-CN.md) |
| 第一次安装，不知道这些软件是什么 | [一步一步安装](docs/INSTALL.zh-CN.md) |
| 找文件、确认版本、检查需要额外下载什么 | [完整下载清单](docs/DOWNLOADS.zh-CN.md) |
| 让聪音发声，再让她听懂麦克风 | [语音与麦克风设置](docs/VOICE_SETUP.zh-CN.md) |
| 了解密钥、聊天记录、备份和卸载 | [本地数据与隐私](docs/DATA_AND_PRIVACY.zh-CN.md) |
| 维护教程，补齐公开发布前的缺项 | [核查依据与待办](docs/MAINTAINER_STATUS.zh-CN.md) |

## 安装前需要知道

- 两个 Mod 安装包不包含 GPT-SoVITS、Fun-ASR 模型、声线权重或参考录音。完整语音功能需要额外下载与配置。
- 本教程限定 Windows 64 位。完整本地语音流程优先在兼容 NVIDIA 显卡的电脑上验证；本项目尚未给出经过实测的最低显存或 CPU 实时性能保证。
- 请通过 Steam 启动游戏，以便读取有效身份。身份不可用时，受影响的是原版经历同步及其好感叠加，不等于所有 AI 聊天和 AI 好感都会失效。
- 更新 DLL 后仍显示旧接口和聊天记录，通常是读取了旧配置。不要向别人发送自己使用过的整个游戏目录或 SPP 目录。
- SPP 5.8.23 的新记忆整理阈值尚无游戏内长对话验收记录。正式 Release 不代表所有设备与分支都已经实测。

本仓库提供教程和两份正式插件包，不包含游戏模型、游戏音频、玩家密钥或玩家存档。外部程序、模型与录音的使用条件以原发布页为准。
