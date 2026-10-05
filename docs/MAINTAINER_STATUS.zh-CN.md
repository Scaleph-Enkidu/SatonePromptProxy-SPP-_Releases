# AIChat 1.17.1 + SPP 5.9.1 发布与验证记录

已正式发布至公开配对与两私库，三处均为 Latest，30 附件下载逐字节回查通过；[本次完整发布档案](OFFICIAL_1.17.1_5.9.1_20261001.md)与[回执](AIChat_1.17.1_SPP_5.9.1_PUBLICATION_20261001.json)记录真实范围及 SHA。运行源码与已发布 ZIP 不因本次收尾改变。

用户授权合并当前 UI/同步修改、其他对话完成的四个 BAT 和最新教程，正式发布到两个私库与公开发布库。

AIChat 包含好感度同步、中文模型切换、TTS 异常折叠、独立透明度/RGB/明度、分区恢复、最近 50 句提示及 AIChat Remake控制台标题。SPP 5.9.1 更新应用版本，合入 BAT 修复和教程；没有新增记忆迁移或性能优化。已知大 WAL 冷启动耗时与游戏掉帧限制继续保留。

本地构建/检查、候选 SHA、资产哈希、实际解压与发布下载回查分别记录在 [本次发布档案](OFFICIAL_1.17.1_5.9.1_20261001.md)。旧失败/授权续轮和原发布资产保留，不将本地 PASS 当成新增游戏场景实测。

以下为 1.17.0 / 5.9.0 的历史发布与文档修订记录：

---

# AIChat 1.17.0 + SPP 5.9.0 发布与验证记录

[返回首页](../README.md) · [玩家四阶段安装](INSTALL.zh-CN.md) · [下载清单](DOWNLOADS.zh-CN.md)

记录日期：**2026-10-01**。**用户已于当天确认本机测试完成，并批准文档、封包和正式发布。** 此确认按用户原意记录，不虚构逐项硬件型号、供应商、声线、ASR／TTS 环境或全新 Windows 测试清单。

## 文档修订 1

针对 AIChat 包内 README／版本改动原先主要是链接的问题，已发布[独立公开文档修订1](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/tag/AIChat-v1.17.0_SPP-v5.9.0-docs-r1)（Latest）；两私库当前推荐docs_r2组件包，保留原正式及R1资产。公开推荐首装包为 `SatoneMod_AIChat_1.17.0_SPP_5.9.0_Windows_x64_docs_r1.zip`；仅补齐包内可独立阅读的 README、安装与版本改动正文，程序仍为 AIChat 1.17.0 + SPP 5.9.0，程序及模型不变，已安装用户无需升级。

模型 ZIP 的文件名、URL、字节和 SHA-256 保持原样，无需重下。原发布附件 `INSTALL_zh-CN.md` 保持原字节，新指南以当前 main 安装文档与新 ZIP 正文为准。[修订 manifest](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/main/releases/AIChat_v1.17.0_SPP_v5.9.0_docs_r1.json)记录修订资产；包内说明用于离线阅读；公开8与私库各10附件下载回查通过，详细两轮与发布结果见[正文修订完成记录](CP23_DOCUMENTATION_REVISION_20261001.md)。下方正式发布记录与 hash 表是原正式资产的证据。

## 原2026-10-01正式发布完成（历史记录）

**原AIChat 1.17.0 + SPP 5.9.0 当时正式发布并设为Latest**：[公开配对 Release](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/tag/AIChat-v1.17.0_SPP-v5.9.0)。[安装入口](INSTALL.zh-CN.md)按文字、ONNX 选装、聪音发音、玩家语音识别四阶段排列；必需步骤在正文，进阶配置可跳过。两私库的自身程序 Release 同步发布，模型只在公开 Release 作为独立附件，不入源码 Git。

| 正式 ZIP | 字节数 | SHA-256 |
|---|---:|---|
| 主程序配对包（原正式资产） | 10,862,696 | `988026cff09c63727bec83bf6bc8769289bceda5a120282296df3c0c825dd22b` |
| 可选 ONNX 组件 | 93,821,443 | `88c77b40c89df19e316aebf497ff30fc4d5504138955ba92e0f2d4875b639d8d` |

第一轮本地发布检查通过：27 项校验器测试、清单与四份 ZIP 核验、11 个隔离实际解压分支。草稿上传发现 GitHub 将中文包外附件名归一为 `default.md`，造成名称碰撞；尚未正式发布时修订为 ASCII 附件名，并补防回归。第二轮 **30 项校验器测试、文档／工作流和全部资产校验通过**；四份 ZIP 字节未变，实际启动、追加模型、缓存重启、覆盖升级保留 17 个测试文件和坏／缺模型回退引用第一轮同一 ZIP 的验收。未重编受测 EXE／DLL，未触发第三轮或补跑远端 CI。

正式标签固定提交：SPP `60a316fd538304f014067a451b14d8620ba2de54`、AIChat `8474684ce6e614d4162dfed9528479246978f13f`、公开库 `08481af11c838f5d05067a64f2c580fc17d0c1cf`。本次新标签在草稿期以 `force=false` 快进到修订提交；历史正式标签与附件保留。发布前下载回查公开 8 件、两私库各 4 件附件，逐字节与清单一致；发布后确认三个 Release 均非草稿、非预发布且 Latest 正确。包外说明为 `INSTALL_zh-CN.md`／`RELEASE_NOTES_zh-CN.md`，公开页面以中文标签显示，包内中文文件名保留。

上述是本次发布工具与分发资产证据，运行代码仍绑定下文原受测源码；用户实机确认独立记录，不扩写成未提供的服务／硬件矩阵。大 WAL 约 495 秒／整管线约 944 MB 的限制没有在本次发布中消除。完整本地证据保存在 `D:/SatoneDev/deliverables/CP23-Official-20261001/Evidence`。

## 当前公开分发形态

公开主下载为两类 ZIP：

- `SatoneMod_AIChat_1.17.0_SPP_5.9.0_Windows_x64_docs_r1.zip`：约 11 MB 的 AIChat＋SPP 配对程序、说明与工具，带默认 Neutral 参考音频，不含 ONNX 模型。
- `Satone_Semantic_E5_small_int8_ORT_1.30.0_Windows_x64.zip`：约 94 MB 的可选 E5 int8／tokenizer／Windows x64 ORT CPU 1.30.0 与许可。

模型不默认启用，文字聊天与内置关键词回忆可单独使用，不需要 Python。模型不是 GPT-SoVITS／Fun-ASR 前置依赖。语音运行环境、声线权重及 ASR 模型外装；私库单组件包只用于来源与组件构建，不是玩家必需额外下载。

[文档修订 1 manifest](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/main/releases/AIChat_v1.17.0_SPP_v5.9.0_docs_r1.json)记录修订 ZIP 的字节数、SHA-256、成员及来源；[原配对 manifest](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/AIChat-v1.17.0_SPP-v5.9.0/releases/AIChat_v1.17.0_SPP_v5.9.0.json)保留原正式资产身份。包内 `BUILD_INFO.json`／`COMPONENT.json` 记录文件身份；文档修订不代表重新运行全部源码测试。

## 固定受测代码与自动化

CP23 D 的受测运行代码为：

| 组件 | 固定受测提交 |
|---|---|
| AIChat 1.17.0 | `ef2e302af1575a6fcbe50720f87f3b88b5d8e076` |
| SPP 5.9.0 | `f0f2257b72a1f388bd7bf0cc5aec148ef00805d1` |

来源为源库的 `docs/CP23_STAGE_D_VALIDATION_20261001.md`、`docs/CP23_SPLIT_DISTRIBUTION_20261001.md` 与交付的 `VALIDATION.json`／`PACKAGE_ACCEPTANCE.json`。运行受测 SHA、封包文档 HEAD 与最终文档 HEAD 分开记录；玩家不需要私库权限才能安装，公开下载和教程保持自足。

- D 第二轮：14 项后端检查、9 项客户端检查 PASS；Go 全量 520 顶层／1029 含子项 PASS，7 项 SKIP，适用的 EXE／资源／进程 owner 路径另行检查。两个真实厂商 API 没有在该自动化轮次调用。
- 真实 int8 ONNX worker：**12/12 合成正例 Top1、10/12 正例通过保守注入筛选、0/3 合成负例通过筛选**。真实模型不等于真实玩家语料；结果不保证每次换词检索正确。
- 分包实际解压与覆盖升级：**11 分支 PASS**。覆盖未装模型、纯关键词启停、追加组件、实际 worker 查询、缓存重启、配置／组件／旧 DB／玩家哨兵保留、覆盖后重启、缺／坏组件回退。隔离目录有中文和空格，子进程 PATH 为空，不依赖 Python 运行 Recall；开发检查脚本本身使用 Python。
- 包校验覆盖 CRC、安全路径、成员清单与逐文件 hash，程序／参考 WAV、组件固定支持文件与完整许可，以及个人运行数据排除。发布包的最终名称与身份以本次 manifest 为准，不沿用旧候选 ZIP 的 hash。

首轮失败与诊断产物按历史保留，没有覆盖失败记录。文档与分包整理没有重新运行大 WAL 测量；资源数值继续绑定原 D 受测代码与输入。

## 资源边界

原 **350 MB 门禁只包含真实 worker＋5 万向量**，第二轮最大 **332,283,904 B**，不含存档、关键词、WAL 或启动。

全新进程整管线采用 20 ms working-set 采样；5 万条合成真实格式 WAL 的启动重放与档案投影 **495.12 秒**，观察峰值 **943,693,824 B**。大 WAL 冷启动仍慢，整套 SPP 不能称为“350 MB”。较短输入、已加载缓存与冷启动不是同一个指标；详细表格见[硬件页](HARDWARE.zh-CN.md)。

合成 WAL 按真实格式／hash 链生成并经过生产恢复，不冒称每轮都执行真实云端生成或 live commit／fsync；生命周期向量缓存为合成向量，不冒称所有记录都由 E5 推理。真实玩家文本、设备与存档规模会改变结果。

## 安装说明与来源保留

- 首页功能介绍后立即提供大标题安装入口；Release 顶部提供同一入口。
- 四阶段为文字 → ONNX 选装 → GPT-SoVITS → Fun-ASR，每阶段先写文件位置、设置、启动和验收，再折叠进阶配置。关键配置不藏进折叠。
- Recall 同时支持本地管理页 UI 与 `/recall/test?q=...`／`/recall/status`。旧 Dashboard／截图没有查询区时直接用端点；首次查询触发后台暖机，不能只看“文件存在”。
- 语义验收检查 `engine=native_keyword+onnx`、`worker.model_loaded`、`worker.semantic_state`、`worker.embedded_exchanges` 和当前档案作用域。
- E5 revision 固定为 `614241f622f53c4eeff9890bdc4f31cfecc418b3`，组件保留模型说明、E5 项目 MIT 许可、ORT 许可与第三方声明。声线作者、Mayuri 参考音频与其原始许可标注继续见[语音页](VOICE_SETUP.zh-CN.md)。
- AIChat 基于 [qzrs777/AIChat](https://github.com/qzrs777/AIChat)，原作者 Elysia777 与许可证保留。项目特色与 Meta 叙述保留在首页；旧发布文档继续作为历史记录。

## 后续仍需按事实扩充的证据

用户本机测试确认已完成；本次没有新增全部显卡／驱动／供应商／声线的逐项矩阵，也没有虚构干净 Windows 全流程、真实玩家召回质量或独立第三方审查。之后遇到问题，应记录实际环境、组合、档案、时间、复现与脱敏日志，再补对应证据。

主程序更新默认复用兼容的同一模型组件；仅当模型／tokenizer／ORT 或兼容条件改变时，才更新组件身份与下载。保护 `local_v1`、全部档案、连接凭据、模型、缓存与声线资源；任何冷启动优化仍需保持权威恢复校验。

## 不可变发布的追加方式

公开原Release启用不可变发布，GitHub拒绝追加资产（HTTP 422）。公开修订使用独立 `AIChat-v1.17.0_SPP-v5.9.0-docs-r1` 发布，原正式Tag与资产保留。模型在新发布中复用同一原ZIP字节，版本和原下载地址不变。私库最初追加的docs_r1保留，当前docs_r2仅更正公开修订下载链接；运行文件相同。当前28附件上传及下载逐字节回查完成；公开修订已正式发布并确认Latest，原公开8资产另外回查恒等。
