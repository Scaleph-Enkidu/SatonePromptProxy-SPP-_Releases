[简体中文](DATA_AND_PRIVACY.md) | [English](../en/DATA_AND_PRIVACY.md) | [日本語](../ja/DATA_AND_PRIVACY.md)

# 配置、聊天记录与隐私

[返回首页](README.md) · [四阶段安装](INSTALL.md)

适用配对：**AIChat 1.18.28 + SPP 5.10.8**，更新于 **2026-10-01**。程序文件与个人运行数据分开保存；替换 DLL／EXE 后继续看到旧接口、Key 或聊天，通常是读取了原配置和存档，不代表它们被打入新程序包。

## 数据保存在哪里

以下为默认或常见位置；旧安装和自定义配置可能不同。**备份整个 SPP 个人运行目录最能避免遗漏新旧档案。**

| 数据 | 位置与注意事项 |
|---|---|
| AIChat 设置、连接草稿与可能保存的 Key | 游戏 `BepInEx/config/com.username.chillaimod.cfg`；按敏感文件保护 |
| AIChat 窗口历史 | 游戏 `BepInEx/config/AIChatSatoneUX.history`；Base64 不是加密，也不等于全部模型记忆 |
| 游戏插件日志 | 游戏 `BepInEx/LogOutput.log`；可能含识别文字、回复、TTS 请求与路径 |
| SPP 常规配置 | SPP 根目录 `config.json`；含地址、本机路径与服务配置 |
| 已保存连接与凭据 | `connections.v1.json` 和 **`connection_credentials.v1.json`**；后者保存 API Key，不应公开 |
| 当前人格 | `persona_file` 指向的 TXT，默认 `SatonePersona_v4.6.txt`；用户修改可能含私人设定 |
| 新本地聊天权威记录 | `local_v1/commits.jsonl`、`local_v1/active_selection.v1.json` 与相邻锁／恢复文件；不能把它们当缓存删除 |
| 新本地档案投影 | `memory_profiles/memory1/local_v1`、`memory2/local_v1`、`memory3/local_v1` 及档案内其他文件 |
| 旧版记忆、关系、归档与数据库 | 常见于 `memory_profiles/记忆1`、`记忆2`、`记忆3`，旧安装还可能在 SPP 根目录；含 `SatoneMemory.json`、`SatoneRelationship.json`、`SatoneArchive.jsonl`、`SatoneChat.txt`、`SatoneRecall.db` 等 |
| ONNX 语义缓存 | SPP 根目录 `semantic_recall_v1`；包含档案身份、交流文本摘要／指纹与向量，仍应按私人数据处理 |
| ONNX 模型文件 | `models/multilingual-e5-small`；通用模型、tokenizer、ORT、组件清单与许可，不是个人聊天存档 |
| 原版共同经历账本 | `OriginalGameProgress.json` 与相邻恢复／备份；可能含进度与派生身份 |
| 本机服务路径 | `runtime_paths.json`、`service_paths.ini` 等；可能暴露用户名和安装目录 |
| 用量、日志与备份 | `usage_stats.json`、SPP／语音日志、`config.json.before-semantic-*` 等；按个人数据保护 |
| 游戏自身存档 | 由游戏管理，独立于 Mod 配置与 SPP 记忆 |

新版本地档案的接口 ID 和文件夹名可为 `memory1/2/3`，旧版中文“记忆1/2/3”也可能继续保留；不能只备份其中一种布局。ONNX 缓存可重建，**权威 WAL 与档案、旧数据库不是可随意清理的缓存**。只索引最新 50,000 条语义记录不等于删除更旧存档。

## API Key 与聊天经过哪里

AIChat 可能在 CFG 中保留连接草稿，SPP 将已保存连接的凭据保存在 `connection_credentials.v1.json`。SPP 的标准 `config.json` 没有 Key 字段，不能由此推断整个目录没有密钥。凭据文件的 Windows 访问权限限制也不等于加密；同一账户下可读取它的软件仍可能取得内容。界面“显示 API Key”只改变显示方式。

选择云端服务时，当前对话及所需人格／记忆／上下文发给当前已应用的 API 供应商。选择中转站也会把鉴权和内容交给该站。切换服务、删本地历史、卸载 DLL 或删除 SPP 目录不会自动删除供应商可能保存的远端数据；远端删除与保留以所用服务的数据政策和操作机制为准，例如 [OpenAI 数据控制](https://developers.openai.com/api/docs/guides/your-data)。

按本教程部署的 ONNX、GPT-SoVITS 与 Fun-ASR 在本机运行。麦克风由本机 ASR 转为文字，再随聊天进入所选上游；临时 WAV 在正常处理后清理，异常退出和系统备份仍可能留下副本。自行改为远程 ASR／TTS 时，音频与文本的接收方也会改变。

## 备份、升级与更换电脑

先退出游戏、SPP 和相关服务，再私下备份：

- 游戏的 AIChat CFG、history 和需要保留的日志。
- 整个 SPP 个人运行目录，尤其是 `config.json`、连接／凭据、`local_v1`、整个 `memory_profiles`、旧根目录记忆、人格修改、原版进度账本与相邻恢复文件。
- 已安装的 `models`、`semantic_recall_v1`、参考录音和个人语音配置；GPT-SoVITS 权重、Fun-ASR 模型与环境在外部目录时另行备份。

Dashboard 的 Backup 按钮不等于备份了游戏配置、全部模型和所有新旧运行文件；不要只靠一次面板导出完成整版本回退。更新按[新目录安装与记忆继承](UPGRADE.md)操作，保留这些数据，不先删除整个旧 SPP 目录。回退需同时恢复原程序和升级前整套个人数据，不能保证旧版理解新版新写的数据。

更换电脑后修正绝对路径并重新校验语义组件；Python 虚拟环境可能引用旧路径，需要重新安装。恢复凭据时遵循相应 Windows 权限与服务商账户条件，重新验证 Steam 游戏身份。

## 分享日志与清理

求助优先给版本、组合、时间和复现步骤，再附脱敏的必要日志／状态。不要公开整个 CFG、SPP 运行目录、备份或聊天数据库；检查 Key、Authorization／Bearer、姓名、住址、完整聊天、机器用户名和私人路径。

Key 如果已经公开，去供应商平台撤销并重新创建；只删除当前截图或文件不能保证历史副本消失。默认 11435、9880、9881 使用本机地址；本地管理端点不是对同账户其他程序的安全边界，不应无鉴权转发到局域网或公网。

只禁用 Mod 可移出 DLL 并停止服务，保留个人数据。彻底清理还要另行处理本地档案、根目录旧文件、日志、备份和供应商远端数据；先确认哪些记忆要丢弃，删除 DLL 不等于全部数据删除。

## 当前发行包的边界

本次主程序配对包与选装模型包从独立封包目录生成，检查成员、CRC、逐文件 hash 与个人运行文件排除。程序包不应包含玩家 CFG、运行用 `config.json`、连接凭据、聊天 history、`local_v1`、`memory_profiles`、日志或私人备份；默认 Neutral 是发布资源。模型包为通用模型与运行库、来源清单和许可。

本次精确包身份与最终检查以[发布清单](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/AIChat-v1.17.1_SPP-v5.9.1/releases/AIChat_v1.17.1_SPP_v5.9.1.json)和[维护记录](../MAINTAINER_STATUS.zh-CN.md)为准。文件清单排除个人数据不等于完整二进制安全审计。本版本地验证的具体范围见维护记录，不扩展为所有机器、供应商或语音组合已验收。
