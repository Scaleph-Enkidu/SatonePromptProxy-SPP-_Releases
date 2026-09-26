# 教程核查记录与公开发布前待办

[返回首页](../README.md)

日期：2026-09-26。本文供维护者更新教程使用，普通玩家可直接读[安装页](INSTALL.zh-CN.md)。

## 核查到的仓库状态

| 仓库 | 可见性 | main / develop 快照 | 已发布版本 |
|---|---|---|---|
| Scaleph-Enkidu/SatoneAIChat_Remake | private | 两分支均为 `aeaa1b33598d68ead0b3d1353b3793e5df399cc2` | Release `AIChat-v1.16.14`，非草稿、非预发布 |
| Scaleph-Enkidu/SatonePromptProxy | private | 两分支均为 `916c61a71973f825266be7140d84c45afbd6bcaa` | Release `SPP-v5.8.23`，非草稿、非预发布 |
| Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases | private | 搬运前教程提交 `eb87300fd0a36e8301ba4dfef55857ebeb14fb27` | 配对发布 [AIChat-v1.16.14_SPP-v5.8.23](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/tag/AIChat-v1.16.14_SPP-v5.8.23) |

本次按维护者要求，将两份最新正式安装包、原校验文件及 AIChat 许可证加入本发布库，并更新使用方法的下载入口。文件存于 `packages/AIChat_v1.16.14_SPP_v5.8.23/`，配对 Release 由 `.github/workflows/publish-pair.yml` 校验后发布，原始来源与包内文件清单见[版本清单](../releases/AIChat_v1.16.14_SPP_v5.8.23.json)。两个原 ZIP 未重新编译或重打包。

AIChat 来源为成功工作流 36241959879 的 artifact 10906530604，SPP 来源为成功工作流 36246435335 的 artifact 10907293697。两份 ZIP 的 SHA256 均与源库正式 Release 资产 digest 相同。AIChat 原 BUILD_INFO 仍记录 paired_spp 5.8.22；SPP 5.8.23 明确记录 paired_aichat 1.16.14，所以本配对继续使用原 AIChat 包。

本次没有改变三个仓库的可见性。当前普通玩家仍需要本发布库权限；公开本发布库后，二进制下载不依赖私有源库权限。私人源码、玩家数据和游戏资产未搬入本库。

AIChat README 的“当前正式版本 1.16.9”和候选条目没有完全同步到新 Release；SPP 文档也残留旧阶段文字。教程按正式 Release、源代码和最新配对说明判断，没有把这些旧条目继续写给新玩家。

## 本次首页与语音说明补充

- 首页已将付费 OpenAI API、`gpt-6-luna` 推荐、每天 100 轮的假设预算、安装难度、自用项目的稳定性与责任说明、Codex 参与和 AIChat 原作者致谢放在下载教程之前。
- AIChat 上游为 [qzrs777/AIChat](https://github.com/qzrs777/AIChat)，LICENSE 署名为 Elysia777。本仓库已有随包许可证继续保留。
- [GPT-6 Luna 官方页](https://developers.openai.com/api/docs/models/gpt-6-luna)与[价格页](https://developers.openai.com/api/docs/pricing)核实 Standard 单价为每百万输入 $0.10、缓存读取 $0.01、缓存写入 $0.125、输出 $0.50。预算假设、公式和本地价格表缺项见 [API_COST](API_COST.zh-CN.md)。
- 后藤声线：[原作者模型页](https://huggingface.co/lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models)、[v2ProPlus/gotoh-v1-3-1 文件夹](https://huggingface.co/lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models/tree/main/models/Hitori_Gotoh/v2ProPlus/gotoh-v1-3-1)。所选两个权重的文件名与历史使用记录一致；已查询上游文件元数据，未在本次下载完整权重或测试合成。
- Mayuri：[参考库](https://huggingface.co/SteinsGateSg/mayuri-voice/tree/main/refs)、[index.csv](https://huggingface.co/SteinsGateSg/mayuri-voice/blob/main/refs/index.csv)。按 SPP 5.8.23 原包的 `profiles_26.csv` 与 `config.example.json` 核对了全部 26 项来源：24 个不同 WAV 均有对应 TXT，索引时长在 3–10 秒，默认 prompt 与索引逐项相同。未在本次逐段试听或将外部音频打入插件包。
- SPP 的 `resolveVoiceProfile` 按 mapping/profiles 选择文件；`loadPromptForProfile` 先读非空 prompt，再读 WAV 旁边同名 TXT。只改 CSV 不改变运行配置。上述事实已写进玩家语音说明。

## 首页功能介绍的实现依据

2026-09-27（日本时间）补充：首页现在先介绍模组体验、长期记忆、关系、人格设定及默认存档位置，再说明 API 费用和安装条件。本次核对的源提交仍为 AIChat `aeaa1b33598d68ead0b3d1353b3793e5df399cc2` 与 SPP `916c61a71973f825266be7140d84c45afbd6bcaa`，未将宣传文字写成实机稳定性保证。

- **本地原文与按需检索：** [main.go](https://github.com/Scaleph-Enkidu/SatonePromptProxy/blob/916c61a71973f825266be7140d84c45afbd6bcaa/main.go) 的 `appendArchive` 追加写入原文；`shouldRecall` 检查当前话语中的回忆触发词，`buildRecallInstructions` 要求检索 worker 已启动，并对检索结果执行分数和长度筛选。源码摘录：

```go
f, err := os.OpenFile(p, os.O_CREATE|os.O_WRONLY|os.O_APPEND, 0600)
if !shouldRecall(userText) || !recallWorker.started {
    return "", nil, false
}
```

以上两段来自不同函数。源库 [README 的长期记忆说明](https://github.com/Scaleph-Enkidu/SatonePromptProxy/blob/916c61a71973f825266be7140d84c45afbd6bcaa/README.md)在自动整理步骤中明确写道：“本地 Archive 完全不删除。”这描述自动整理流程，不覆盖手动重置、删文件、磁盘故障等情况。首页将“近乎无限记忆”限定为本地归档可以持续积累，不承诺模型有无限上下文或保证每次召回成功。

- **档案位置：** `defaultMemoryProfilesConfig` 将根目录设为 `memory_profiles`，`fixedMemoryProfiles` 使用中文文件夹名“记忆1/2/3”；路径组合原文为 `filepath.Join(profileRootPath(), p.Folder, filepath.Base(base))`。因此不能把接口 ID `memory1` 当成默认磁盘文件夹名。关闭档案功能或使用自定义配置时，实际位置可能不同。
- **好感与关系：** [relationship.go](https://github.com/Scaleph-Enkidu/SatonePromptProxy/blob/916c61a71973f825266be7140d84c45afbd6bcaa/relationship.go)维护 Affection、Trust、Comfort、Openness 及进度字段；综合好感计算原文为 `v := a*0.50 + t*0.20 + c*0.20 + o*0.10`。关系规则随阶段改变配合与亲密交流的倾向；Persona 定义的身份、自主性和核心边界独立于关系数值。首页没有把高好感描述为无条件服从，也没有把模型评分当作真实心理测量。
- **完整人格文本与重载：** 默认文件由 `defaultPersonaFile = "SatonePersona_v4.5.txt"` 定义。`reloadPersonaNow` 替换 Persona 项目的源码注释为 “Remove all previous developer persona messages, leaving chat history untouched.”；修改人格无需清空聊天。人格全局共用而记忆档案独立，不能把三个档案宣传为三个人格。完整可编辑同样不等于模型行为可以被百分之百控制。
- **其他功能边界：** 语音、情绪参考与麦克风需要外部服务及资源；原版经历需要有效 Steam 身份。26 项参考配置、24 段不同上游录音及相关下载入口沿用前一节的核查结果。首页的能力描述不代表已完成全新 Windows 全流程或长期稳定性实测。

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

SPP 使用明确文件清单复制到 release-stage，未复制 tools/windows 下的 BAT。两个工作流都没有把玩家的已运行目录直接压缩。本次同时核对实际 ZIP 的哈希、CRC、文件清单及 BUILD_INFO，未发现个人运行配置、聊天记录或日志；这不是完整 DLL/EXE 安全审计。

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
| 已完成（当前两包） | 实际 Release ZIP 内容核查 | 原 ZIP 与源库 SHA256 一致；文件清单未含个人 CFG、运行 config.json、history、memory_profiles、日志或备份；凭据嵌入等二进制语义风险未作完整审计 |
| 必须 | 已验证的 Fun-ASR 全新环境 | 用干净 Windows 建环境、完整下载模型、成功加载、F8/持续通话测试；保存精确依赖版本，不只写 pip install 成功 |
| 来源与文件对应已完成；实测待补 | 后藤 v2ProPlus 权重、Mayuri 参考 WAV/TXT 与 26 项命名 | 原链接、文件名、上游许可标注已列明；仍需在干净环境下载并实际试听合成 |
| 操作说明已完成；实测待补 | 解决默认 MAY WAV 不存在的初次安装问题 | A4 提供 Neutral 原 WAV/TXT，A6 列出 26 项原路径和目标名称；上游音频不打包，使用条件按原发布者说明；仍需 Neutral 实测 |
| 必须 | 新手从零实测一次 | 只有 Steam 游戏、没有旧 CFG/缓存/模型的环境，按教程完成；将测试边界写实 |
| 建议 | 实际 GUI 截图 | Steam 定位目录、正确文件层级、F9 配置、服务就绪状态；截图前清除 Key 与私人聊天 |
| 建议 | 降低手工配置成本 | 之后另行实现干净配置向导/依赖安装器；本次提供原包与教程，未实现自动安装器 |
| 建议 | 统一源库 README 版本状态 | 避免正式 Release 与旧候选说明相互矛盾 |
| 建议 | 扩大备份范围并复测 | 明确包含 AIChat CFG/history 与 OriginalGameProgress 账本；不得把私人备份当安装包 |
| 建议 | 密钥与日志保护 | 另行设计 Windows 凭据保护、导出脱敏、日志开关和本地端点鉴权；现状在隐私页明示 |

本次交付包含两份正式原包、统一配对 Release、校验与来源记录，以及对应的玩家使用方法。声线来源与文件命名说明已补齐；干净 Windows 全流程实测与实际语音效果验证仍保留在待办中。
