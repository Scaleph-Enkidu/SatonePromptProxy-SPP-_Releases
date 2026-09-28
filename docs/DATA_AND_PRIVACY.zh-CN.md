# 配置、聊天记录与隐私

[返回首页](../README.md) · [安装步骤](INSTALL.zh-CN.md)

当前配对为 AIChat **1.16.23** 与 SPP **5.8.26**（2026-09-28）。以下旧版证据段落保留历史来源；新连接模式的 Key、记忆和服务商行为以本节补充为准。

OpenAI、DeepSeek 与中转站各自使用独立的 Key／模型草稿；点击“保存并应用配置”后才切换。AIChat 的本机 CFG 可保存这些草稿，SPP 还会将已保存连接的凭据写入 SPP 目录的 `connection_credentials.v1.json`。两处都属于敏感个人文件，不应随安装包、日志或截图公开。聊天内容按当前选择的服务发送给对应服务商；切换公司不会自动删除本地档案或旧服务商可能保存的远端数据。

## 为什么换了 AIChat.dll 还能看到旧接口和聊天？

因为程序文件与玩家数据分开保存。游戏加载新版 DLL 后，仍会读取同一游戏目录下的旧 CFG 和历史文件。**看到旧数据，不能证明密钥或聊天内容被写进了 DLL。**

源码中配置键为 `Config.Bind("1. LLM", "API_Key", ...)`，保存按钮执行 `Config.Save()`；历史路径由 `Path.Combine(Paths.ConfigPath, "AIChatSatoneUX.history")` 构成。原文证据和固定提交链接见[核查记录](MAINTAINER_STATUS.zh-CN.md)。

## 数据具体保存在哪里

以下使用默认路径；自定义 SPP config.json 可以改变部分文件位置。

| 数据 | 默认位置 | 需要注意什么 |
|---|---|---|
| AIChat API URL、API Key、模型、界面设置、服务路径 | `游戏目录\BepInEx\config\com.username.chillaimod.cfg` | **API Key 按普通配置字符串持久化，未见加密包装**；能读取文件的人可能取得密钥 |
| AIChat 窗口聊天历史 | `游戏目录\BepInEx\config\AIChatSatoneUX.history` | 内容使用 Base64 编码，不是加密；是 UI 显示历史，不是全部模型记忆 |
| AIChat 调试日志 | `游戏目录\BepInEx\LogOutput.log` | 包含识别结果、模型回复和 TTS 请求等敏感内容 |
| SPP 配置 | `SPP目录\config.json` | 包含上游地址、本机路径、声线设置等；标准模板没有 API Key 字段 |
| SPP 已保存连接凭据 | `SPP目录\connection_credentials.v1.json` | 含连接的 API Key，应与 AIChat CFG 一起私下备份，不要公开 |
| SPP 配置备份 | 如 `config.json.before_v5.8.23` | 也是个人配置，不应公开分发 |
| 角色设定 | config.json 的 `persona_file` 指向的 TXT，当前默认 `SatonePersona_v4.5.txt` | 用户修改后可能含私人设定；与三个记忆档案独立 |
| 档案数据 | `SPP目录\memory_profiles\记忆1\`、`记忆2\`、`记忆3\` | 含记忆、关系、归档、召回索引、会话状态及恢复文件；默认文件夹是中文“记忆1”，接口 ID 才是 memory1 |
| 长期记忆与 AI 关系 | 档案内 `SatoneMemory.json`、`SatoneRelationship.json` | 可包含个人信息和关系推断 |
| 完整本地对话归档 | 档案内 `SatoneArchive.jsonl`、`SatoneChat.txt` | 不应作为公开故障附件 |
| 本地检索数据库 | 档案内 `SatoneRecall.db` | 同样应视为私人聊天数据 |
| 远端会话关联状态 | 档案内 `conversation_state.json` 与相关事务/恢复文件 | 不是“完整云端数据的离线副本” |
| 原版共同经历账本 | `SPP目录\OriginalGameProgress.json` 及 `.prev` 等 | 记录原版进度、派生账户标识等；不是可以随意公开的通用模板 |
| 本机路径缓存 | `SPP目录\runtime_paths.json` | 可能暴露电脑用户名与目录；迁移后可自动重新发现，不是加密凭据库 |
| 用量记录与程序日志 | `usage_stats.json`、`SatonePromptProxy_v5.8.26.log`、Embedding 日志等 | 可能含费用、模型、对话内容与本机路径 |
| 游戏自身存档 | 由游戏管理 | 不等于上述 Mod 配置或 SPP 记忆；不要误删 |

旧版本或关闭 memory_profiles 的安装还可能在 SPP 根目录保留同名记忆、关系、归档与状态文件。备份与清理时不能只看新档案目录。

## API Key 会经过哪里

旧 OpenAI 云模式下，AIChat 从本地 CFG 读取 Key，经本机 SPP 调用对应上游。新版按服务商保存的连接则由 SPP 使用 `connection_credentials.v1.json` 中的当前凭据；AIChat 本机草稿也可能留有 Key。请同时保护这两处。

SPP 的常规 `config.json` 没有 Key 字段，但这**不代表整个 SPP 目录没有密钥**；新版连接凭据文件另行保存 Key。旧 `OPENAI_API_KEY` 环境变量回退仍只适用于相应旧路径。

界面的“显示 API Key”开关只改变显示方式。用星号遮挡可以减少截图泄漏，**不能加密磁盘上的配置文件**。其他在同一电脑/账户下运行、可以读取该目录的软件，仍可能读到它。

API URL 通常只是地址，本身不等于秘密；但若你自行把密钥放进 URL 参数，URL 也会变成敏感信息。改用第三方上游还意味着该服务会接收鉴权和聊天内容，不能只改地址却继续沿用官方服务的隐私预期。

## 聊天是否只保存在本地

不是。选择 OpenAI、DeepSeek 或中转站时，当前对话和所需上下文会发送给该服务。旧 OpenAI 云模式使用远端会话项目；新版 SPP 本地连接以本地档案为主要记录，但服务商仍可能按其政策保存 API 请求。本地另有完整归档、摘要、关系和日志。

OpenAI [数据控制文档](https://developers.openai.com/api/docs/guides/your-data)对 `/v1/conversations` 及其 items 的保留说明原文为：

> “Until deleted”

因此，删除本地 UI 历史、删 DLL、切换记忆档案或删除本地 SPP 文件夹，都不能被表述为“已经删除全部云端记录”。要删除远端会话，应按所用 API 平台的会话及数据删除机制处理。本文不把本地 reset 操作当作完整远端隐私删除承诺。

在本文的本地语音部署下，麦克风音频由本机 Fun-ASR 处理，识别文字再进入在线聊天；SPP 的 ASR 脚本会暂存本轮 WAV，正常处理后在 finally 中删除。异常退出遗留的临时文件、系统备份或其他软件行为不在此保证范围内。

## 普通玩家应该怎么做

1. 正常更新 DLL 时保留自己的配置，不必因为旧记录还在就认定泄漏。
2. 不把个人 CFG、整个 BepInEx/config、整个 SPP 运行目录或私人备份发给别人。
3. 分享日志前检查姓名、住址、完整聊天、Key、Authorization/Bearer、电脑用户名和私人路径。日志记录了原文，不等于日志适合公开。
4. 如果 Key 已经出现在公开仓库、截图或不可信人的文件中，去服务商平台撤销并重新创建；只删除当前截图或 GitHub 文件不能保证历史副本消失。
5. 本地 11435 只监听 loopback，可减少直接网络暴露，但多个本地管理端点没有独立登录。它不是抵御本机其他程序的安全边界，不能无鉴权转发到局域网或公网。

## 备份与更换电脑

先停止游戏与所有相关服务，再做私人备份：

- AIChat 的 CFG 和 history。
- SPP 的 config.json、实际使用的人格文件、**整个 memory_profiles**、原版进度账本和相邻恢复/备份文件、usage_stats.json。
- 旧版遗留在根目录的记忆/关系/归档/状态文件，以及需要保留的私人日志。
- GPT-SoVITS 配置、声线权重和参考录音；Fun-ASR 模型及环境需要迁移或重新安装。

SPP Dashboard 的 Backup 按钮不等于备份了游戏目录、所有模型和原版进度账本。当前 `createBackupZip` 的显式清单没有包含 AIChat CFG/history，也未列出根目录 OriginalGameProgress.json；应额外备份这些文件。

换电脑后修正绝对路径，继续使用能访问旧远端会话的 API 项目/密钥，并重新通过 Steam 游戏运行时验证原版身份。Python 虚拟环境可能含原路径，不保证直接搬文件夹即可运行。

## 禁用与彻底清理不是同一件事

- 只禁用：移出 DLL、停止服务，保留个人数据。
- 重置 AIChat 本地显示与设置：停机备份后移走该 CFG 和 history，下次会按默认值重建；不会因此重置 SPP 或删除云端会话。
- 完整个人数据清理：还需要处理 SPP 各档案、根目录遗留文件、日志、备份和远端会话。先确认要丢弃哪些记忆，不能把“删除 DLL”当成全部清理。

## 当前发行包是否携带作者的个人数据

源码与 CI 打包脚本显示：AIChat 包使用新构建的 DLL、版本说明和 BUILD_INFO；SPP 在独立 staging 目录复制程序、模板、默认人格等，并检查没有 config.json 与 runtime_paths.json。检查到的 AIChat 默认 Key 是占位符，不是实际用户密钥。

本次 CP14-9 分发包为 AIChat 1.16.23 与 SPP 5.8.26。打包检查已核对 ZIP 文件清单和 SHA256：没有个人 CFG、运行用 config.json、runtime_paths.json、聊天 history、memory_profiles 或日志文件。SPP 包额外包含默认参考音频 `mayuri-voice/refs/MAY_1158_Neutral.wav`；示例模板保留。

这支持“本次分发包未夹带上述个人运行文件”的判断，但不等于完整二进制安全审计，也不能证明用户本机目录从未被其他方式分享。更换 DLL 后读取旧配置和历史，仍应按本页前述的本地数据位置解释。
