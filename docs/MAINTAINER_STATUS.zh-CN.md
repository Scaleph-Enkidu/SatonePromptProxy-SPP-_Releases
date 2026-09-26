# 教程核查记录与公开发布前待办

[返回首页](../README.md)

日期：2026-09-26。本文供维护者更新教程使用，普通玩家可直接读[安装页](INSTALL.zh-CN.md)。

## 核查到的仓库状态

| 仓库 | 可见性 | main / develop 快照 | 已发布版本 |
|---|---|---|---|
| Scaleph-Enkidu/SatoneAIChat_Remake | private | 两分支均为 `aeaa1b33598d68ead0b3d1353b3793e5df399cc2` | Release `AIChat-v1.16.14`，非草稿、非预发布 |
| Scaleph-Enkidu/SatonePromptProxy | private | 两分支均为 `916c61a71973f825266be7140d84c45afbd6bcaa` | Release `SPP-v5.8.23`，非草稿、非预发布 |
| Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases | private | 本次文档更新前 main 为 `262e21f2d69d93bcae9311eec2906503730a8b22` | 核查时无 Release |

本次只把教程写入指定发布库，不改变上述可见性，不向发布库复制私人源码、玩家数据或游戏资产，不创建二进制 Release。未来状态变化后应更新本表及玩家下载清单。

AIChat README 的“当前正式版本 1.16.9”和候选条目没有完全同步到新 Release；SPP 文档也残留旧阶段文字。教程按正式 Release、源代码和最新配对说明判断，没有把这些旧条目继续写给新玩家。

## 关键依据与原文摘录

以下固定提交链接来自私有源库；没有权限的读者可能看不到。玩家教程应保持自足，不能要求普通玩家靠阅读这些源码才能安装。

### AIChat 配置与历史

来源：[AIMod.cs](https://github.com/Scaleph-Enkidu/SatoneAIChat_Remake/blob/aeaa1b33598d68ead0b3d1353b3793e5df399cc2/AIChat/AIMod.cs)、[SatoneConversation.cs](https://github.com/Scaleph-Enkidu/SatoneAIChat_Remake/blob/aeaa1b33598d68ead0b3d1353b3793e5df399cc2/AIChat/Satone/SatoneConversation.cs)。

```csharp
_apiKeyConfig = Config.Bind("1. LLM", "API_Key", "sk-or-v1-PasteYourKeyHere", "API Key");
Config.Save();
_satoneHistoryPath = Path.Combine(Paths.ConfigPath, "AIChatSatoneUX.history");
string encoded = Convert.ToBase64String(Encoding.UTF8.GetBytes(e.Text ?? string.Empty));
```

这些是不同位置的原文摘录，省略了周围代码。配置经 BepInEx 持久化，历史另存且采用可逆编码。换 DLL 后保留旧配置是预期行为。当前界面用 PasswordField 遮挡密钥，不是磁盘加密。

### SPP 鉴权、监听、档案与备份

来源：[main.go](https://github.com/Scaleph-Enkidu/SatonePromptProxy/blob/916c61a71973f825266be7140d84c45afbd6bcaa/main.go)、[relationship_queue.go](https://github.com/Scaleph-Enkidu/SatonePromptProxy/blob/916c61a71973f825266be7140d84c45afbd6bcaa/relationship_queue.go)。

```go
auth := strings.TrimSpace(r.Header.Get("Authorization"))
lastAuth = auth
if ip == nil || !ip.IsLoopback() {
    log.Fatalf("For safety, listen must be loopback only, got %q", cfg.Listen)
}
```

关系恢复任务的源码注释：

> “The API key is supplied by the next authenticated request and is never written to disk.”

该注释针对 SPP 恢复任务，不应扩大为“整个 Mod 不在磁盘保存 Key”。AIChat 的 CFG 仍保存 Key。

`fixedMemoryProfiles()` 定义接口 ID `memory1` 与目录名 `记忆1`；教程按真实目录描述。`createBackupZip()` 明确列出人格、usage、config 和 memory_profiles，未包括游戏内 AIChat 配置，也未列出根目录 OriginalGameProgress.json。

### Release 打包范围

来源：[AIChat 工作流](https://github.com/Scaleph-Enkidu/SatoneAIChat_Remake/blob/aeaa1b33598d68ead0b3d1353b3793e5df399cc2/.github/workflows/build-v1.16.0.yml)、[SPP 工作流](https://github.com/Scaleph-Enkidu/SatonePromptProxy/blob/916c61a71973f825266be7140d84c45afbd6bcaa/.github/workflows/release.yml)。

SPP 的原文检查：

```sh
test ! -e "$STAGE/config.json"
test ! -e "$STAGE/runtime_paths.json"
```

SPP 使用明确文件清单复制到 release-stage，未复制 tools/windows 下的 BAT。两个工作流都没有把玩家的已运行目录直接压缩。本次检查的是工作流、模板和源码，没有对实际发布 ZIP 的所有字节做安全扫描。

### 外部组件

| 内容 | 一手资料 |
|---|---|
| BepInEx 安装方法和已存在的 x64 附件 | [官方安装文档](https://docs.bepinex.dev/articles/user_guide/installation/index.html)、[5.4.23.5 Release](https://github.com/BepInEx/BepInEx/releases/tag/v5.4.23.5) |
| GPT-SoVITS Windows 包、模型与 API | [官方 README](https://github.com/RVC-Boss/GPT-SoVITS)、[api_v2.py](https://github.com/RVC-Boss/GPT-SoVITS/blob/main/api_v2.py)、[tts_infer.yaml](https://github.com/RVC-Boss/GPT-SoVITS/blob/main/GPT_SoVITS/configs/tts_infer.yaml)、[官方整合包列表](https://huggingface.co/lj1995/GPT-SoVITS-windows-package/tree/main) |
| Fun-ASR 的模型加载方式与依赖 | [官方仓库](https://github.com/QwenAudio/Fun-ASR)、[requirements.txt](https://github.com/QwenAudio/Fun-ASR/blob/main/requirements.txt)、[原版模型卡](https://huggingface.co/FunAudioLLM/Fun-ASR-Nano-2512) |
| 模型整包下载方法 | [Hugging Face 官方指南](https://huggingface.co/docs/huggingface_hub/guides/download) |
| API Key、模型与账单 | [OpenAI Quickstart](https://developers.openai.com/api/docs/quickstart)、[GPT-6 Luna](https://developers.openai.com/api/docs/models/gpt-6-luna)、[生产使用建议](https://developers.openai.com/api/docs/guides/production-best-practices) |
| 云端会话保留 | [OpenAI 数据控制](https://developers.openai.com/api/docs/guides/your-data)，Conversations 表格的原文为 “Until deleted” |

上游会更新，因此以上动态链接不是依赖锁定文件。正式发布前应固定实际验证过的包版本和哈希，记录 Windows、驱动、Python、Torch、FunASR、Transformers 版本。

## 公开面向普通玩家前需要补齐什么

| 优先级 | 缺项 | 验收方式 |
|---|---|---|
| 必须 | 玩家无需私库权限即可取得配对 Mod 包 | 从未登录 GitHub 的浏览器打开下载链接并下载；在下载页标清当前版本 |
| 必须 | 实际 Release ZIP 内容核查 | 检查文件清单与哈希，不含个人 CFG、config.json、history、memory_profiles、日志、备份或凭据 |
| 必须 | 已验证的 Fun-ASR 全新环境 | 用干净 Windows 建环境、完整下载模型、成功加载、F8/持续通话测试；保存精确依赖版本，不只写 pip install 成功 |
| 必须（复现演示声音） | 声线 `.ckpt/.pth` 的准确原链接、版本、许可和参考录音来源 | 列出准确文件名、来源、GPT-SoVITS 版本，能从零取得并生成相同类型的声音 |
| 必须 | 解决默认 MAY WAV 不存在的初次安装问题 | 提供合法可取得的录音与相应配置，或提供清楚的自有参考音频流程；Neutral 实测通过 |
| 必须 | 新手从零实测一次 | 只有 Steam 游戏、没有旧 CFG/缓存/模型的环境，按教程完成；将测试边界写实 |
| 建议 | 实际 GUI 截图 | Steam 定位目录、正确文件层级、F9 配置、服务就绪状态；截图前清除 Key 与私人聊天 |
| 建议 | 降低手工配置成本 | 之后另行实现干净配置向导/依赖安装器；本次仅写教程，没有伪称已实现 |
| 建议 | 统一源库 README 版本状态 | 避免正式 Release 与旧候选说明相互矛盾 |
| 建议 | 扩大备份范围并复测 | 明确包含 AIChat CFG/history 与 OriginalGameProgress 账本；不得把私人备份当安装包 |
| 建议 | 密钥与日志保护 | 另行设计 Windows 凭据保护、导出脱敏、日志开关和本地端点鉴权；现状在隐私页明示 |

本次任务的完成标准是“形成可审阅、依据明确、缺项可见的教程并写入指定仓库”，不是未经实测就宣布已经实现零基础一键安装。
