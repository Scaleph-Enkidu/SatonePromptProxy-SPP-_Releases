# 聪音 Mod：普通玩家安装指南

适用游戏：《放松时光：与你共享Lo‑Fi故事》（Chill with You : Lo-Fi Story）的 Steam Windows 版。

本 Mod 由 **AIChat Remake** 和 **SatonePromptProxy（SPP）** 共同工作。AIChat 在游戏里显示聊天、字幕并播放语音；SPP 管理角色设定、记忆、关系及语音服务连接。玩家不需要学习 Git，也不需要编译代码。

**安装教程草稿 v2 · 核查日期 2026-09-26 · 当前配对：AIChat 1.16.14 + SPP 5.8.23。**

## 下载这两个插件

统一入口：[AIChat 1.16.14 + SPP 5.8.23 配对发布](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/tag/AIChat-v1.16.14_SPP-v5.8.23)。

| 安装包 | 放在哪里 |
|---|---|
| [AIChat_v1.16.14.zip](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.16.14_SPP-v5.8.23/AIChat_v1.16.14.zip) | 解压取出 AIChat.dll，放到游戏的 BepInEx/plugins |
| [SatonePromptProxy_v5.8.23.zip](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.16.14_SPP-v5.8.23/SatonePromptProxy_v5.8.23.zip) | 全部解压到固定文件夹，运行 SatonePromptProxy.exe |

第一次安装还需要 BepInEx 和自己的 API 配置，请从下方“一步一步安装”开始。不要下载 Source code 作为插件包。

> **访问状态：** 两份正式包已集中到本发布库，并保留原 ZIP、SHA256 校验文件及 AIChat 原许可证。当前本发布库仍是 Private，未获得本库权限的玩家会看到 404；公开本库后，玩家无需访问两个源码仓库。声线准确资源说明与 Windows 全新安装实测仍需补齐。

| 你要做什么 | 阅读哪一页 |
|---|---|
| 第一次安装，不知道这些软件是什么 | [一步一步安装](docs/INSTALL.zh-CN.md) |
| 找文件、确认版本、检查需要额外下载什么 | [完整下载清单](docs/DOWNLOADS.zh-CN.md) |
| 让聪音发声，再让她听懂麦克风 | [语音与麦克风设置](docs/VOICE_SETUP.zh-CN.md) |
| 了解密钥、聊天记录、备份和卸载 | [本地数据与隐私](docs/DATA_AND_PRIVACY.zh-CN.md) |
| 维护教程，补齐公开发布前的缺项 | [核查依据与待办](docs/MAINTAINER_STATUS.zh-CN.md) |

## 安装前需要知道

- 购买游戏不包含 AI 服务额度。本教程使用玩家自己的 OpenAI API Key 和可用的 API 计费账户；不要把 ChatGPT 登录密码或网页订阅当作 API Key。
- 两个 Mod 安装包不包含 GPT-SoVITS、Fun-ASR 模型、声线权重或参考录音。完整语音功能需要额外下载与配置。
- 本教程限定 Windows 64 位。完整本地语音流程优先在兼容 NVIDIA 显卡的电脑上验证；本项目尚未给出经过实测的最低显存或 CPU 实时性能保证。
- 请通过 Steam 启动游戏，以便读取有效身份。身份不可用时，受影响的是原版经历同步及其好感叠加，不等于所有 AI 聊天和 AI 好感都会失效。
- 更新 DLL 后仍显示旧接口和聊天记录，通常是读取了旧配置。不要向别人发送自己使用过的整个游戏目录或 SPP 目录。
- SPP 5.8.23 的新记忆整理阈值尚无游戏内长对话验收记录。正式 Release 不代表所有设备与分支都已经实测。

本仓库提供教程和两份正式插件包，不包含游戏模型、游戏音频、玩家密钥或玩家存档。外部程序、模型与录音的使用条件以原发布页为准。
