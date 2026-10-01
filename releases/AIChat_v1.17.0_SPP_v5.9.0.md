# AIChat 1.17.0 + SatonePromptProxy 5.9.0

# 🚀 从这里开始安装：四阶段教程

**[打开安装教程](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/main/docs/INSTALL.zh-CN.md)** · **[下载主程序配对包（文档修订 1，约 11 MB）](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.17.0_SPP-v5.9.0/SatoneMod_AIChat_1.17.0_SPP_5.9.0_Windows_x64_docs_r1.zip)** · [全部下载与校验清单](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/main/docs/DOWNLOADS.zh-CN.md)

**① 文字聊天 → ② ONNX 模型选装 → ③ 聪音发音（GPT-SoVITS） → ④ 玩家语音识别（Fun-ASR）。** 文字聊天完成后即可独立运行；各阶段不依赖后续阶段。② 可跳过，③／④ 都不依赖 ONNX。每阶段必需步骤在教程正文，进阶配置可折叠跳过。

正式配对，2026-10-01。**用户已确认本机测试完成**；记录不扩展成全部硬件、厂商和语音组合的测试结论。

## 文档修订 1

本修订仅补齐包内可独立阅读的 README、安装与版本改动正文，程序仍为 **AIChat 1.17.0 + SPP 5.9.0**，程序及模型不变。新玩家推荐 `docs_r1` 主程序包，首次安装步骤相同；原正式包保留，已安装用户无需为文档修订升级。模型继续使用原文件、原 URL 和原 SHA-256，无需重下。

原发布附件 `INSTALL_zh-CN.md` 保持原发布字节；新指南以顶部当前安装页与新 ZIP 内正文为准。文档修订资产身份见[修订清单](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/main/releases/AIChat_v1.17.0_SPP_v5.9.0_docs_r1.json)，原正式资产仍按原清单保留。

已安装用户可单独阅读或保存这两份正文：[AIChat 包内 README 完整正文](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.17.0_SPP-v5.9.0/AIChat_README_zh-CN.md) / [AIChat 版本与改动完整正文](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.17.0_SPP-v5.9.0/AIChat_CHANGELOG_zh-CN.md)，无需替换程序。

## 本次更新

- **文字与回忆可以独立使用。** 关键词回忆改为程序内置，不需要旧 Python Embedding 环境；没有麦克风模块也能继续文字输入。
- **ONNX 语义回忆成为选装组件。** E5 small int8 与 Windows x64 ORT CPU 1.30.0 另包分发，不默认启用。模型缺失、坏文件、失败或忙碌时回退关键词，不参与必须完成的回合结算。
- **程序和模型分开更新。** 主程序配对包约 11 MB，可选模型包约 94 MB；兼容的主程序更新可复用同一校验通过的组件，不必每次重下模型。
- **模型有校验与启停工具。** 在 SPP EXE 旁放入完整 `models`，停机运行 Verify／Enable／Disable 工具。首次查询触发后台暖机与向量准备，状态显示当前档案进度；旧管理页没有 Recall 查询区时可使用本机端点。
- **旧数据与结算边界保留。** 回忆只索引已接受且实际呈现的有效交流；旧数据库原样保留。语义覆盖最新 50,000 条，关键词继续覆盖完整历史，权威存档不删减。旧 Recall 的恢复不重新生成已确认回复或重做已确认关系／记忆效果。
- 安装说明按文字、ONNX、TTS、ASR 四阶段重写，保留项目人格、记忆、剧情同步、Meta 演出与 F10 外观采集器介绍。默认 Neutral 已在程序包，语音环境和权重另装。

## 两类公开 ZIP

| 文件 | 用途 |
|---|---|
| `SatoneMod_AIChat_1.17.0_SPP_5.9.0_Windows_x64_docs_r1.zip` | 必需配对主程序：AIChat＋SPP、工具、说明、Neutral 参考音频 |
| `Satone_Semantic_E5_small_int8_ORT_1.30.0_Windows_x64.zip` | 可选模型：E5 int8、tokenizer、ORT 与完整许可 |

私有源码库的单组件包不是玩家必需额外下载。GitHub 自动生成的 Source code ZIP 不是安装包。修订 ZIP 的精确字节数、SHA-256、成员和来源见[文档修订 1 manifest](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/main/releases/AIChat_v1.17.0_SPP_v5.9.0_docs_r1.json)及[下载清单](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/main/docs/DOWNLOADS.zh-CN.md)；原 ZIP 与模型身份保留在[原配对 manifest](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/AIChat-v1.17.0_SPP-v5.9.0/releases/AIChat_v1.17.0_SPP_v5.9.0.json)。

GPT-SoVITS 环境、声线 GPT／SoVITS 权重、Fun-ASR 环境和模型不在上述两包内；Neutral 路径为 `SatonePromptProxy/mayuri-voice/refs/MAY_1158_Neutral.wav`。其余情绪音频可选，来源与许可见[语音页](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/main/docs/VOICE_SETUP.zh-CN.md)。

## 升级与回退

退出游戏、SPP 和语音服务，备份后覆盖 DLL／PDB、SPP 程序与配套工具。**保留个人配置、连接凭据、`local_v1`、整个 `memory_profiles`、人格修改、`models`、`semantic_recall_v1` 与声线资源**，不要先删整个运行目录，也不要用示例覆盖个人 `config.json`。

[上一配对 AIChat 1.16.65 + SPP 5.8.42](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/tag/AIChat-v1.16.65_SPP-v5.8.42)保留。整版本回退应成对恢复原程序和升级前整套配置／存档，新写数据不保证旧版完整理解；只停用 ONNX 可用 Disable 工具。

## 验证与限制

- D 第二轮 14 项后端＋9 项客户端检查通过；分包实际解压与覆盖升级 **11 分支 PASS**。
- 真实 ONNX worker 的合成语料测试：**12/12 正例 Top1、10/12 qualified、0/3 负例 qualified**。不代表真实玩家检索每次成功。
- 20 ms working-set 采样下，5 万条合成真实格式 WAL 冷启动约 **495 秒**，整管线观察峰值 **943,693,824 B**。350 MB 门禁只包含 worker＋向量，观察最大 **332,283,904 B**；不能宣传整套 SPP ≤350 MB。
- 大 WAL 启动仍慢。自动化与用户本机确认分开记录，不虚构全硬件、真实供应商／语音矩阵或干净机验证；来源和完整范围见[维护记录](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/main/docs/MAINTAINER_STATUS.zh-CN.md)与[硬件页](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/main/docs/HARDWARE.zh-CN.md)。

云端 API 用量按供应商实时价格和账单计费；安装包不附送额度。分享问题日志前移除 API Key 与私人聊天。
