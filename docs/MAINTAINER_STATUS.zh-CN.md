# AIChat 1.17.0 + SPP 5.9.0 发布与验证记录

[返回首页](../README.md) · [玩家四阶段安装](INSTALL.zh-CN.md) · [下载清单](DOWNLOADS.zh-CN.md)

记录日期：**2026-10-01**。**用户已于当天确认本机测试完成，并批准文档、封包和正式发布。** 此确认按用户原意记录，不虚构逐项硬件型号、供应商、声线、ASR／TTS 环境或全新 Windows 测试清单。

## 当前公开分发形态

公开主下载为两类 ZIP：

- `SatoneMod_AIChat_1.17.0_SPP_5.9.0_Windows_x64.zip`：约 11 MB 的 AIChat＋SPP 配对程序、说明与工具，带默认 Neutral 参考音频，不含 ONNX 模型。
- `Satone_Semantic_E5_small_int8_ORT_1.30.0_Windows_x64.zip`：约 94 MB 的可选 E5 int8／tokenizer／Windows x64 ORT CPU 1.30.0 与许可。

模型不默认启用，文字聊天与内置关键词回忆可单独使用，不需要 Python。模型不是 GPT-SoVITS／Fun-ASR 前置依赖。语音运行环境、声线权重及 ASR 模型外装；私库单组件包只用于来源与组件构建，不是玩家必需额外下载。

[配对 manifest](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/AIChat-v1.17.0_SPP-v5.9.0/releases/AIChat_v1.17.0_SPP_v5.9.0.json)记录最终字节数、SHA-256、ZIP 成员、源提交及封包来源；包内 `BUILD_INFO.json`／`COMPONENT.json` 记录文件身份。这里不猜测发布 ZIP 的 hash，也不把文档提交当作重新运行全部源码测试的证据。

## 固定受测代码与自动化

CP23 D 的受测运行代码为：

| 组件 | 固定受测提交 |
|---|---|
| AIChat 1.17.0 | `c5da60b686766189c30ed7d69b71dab41098f6d2` |
| SPP 5.9.0 | `5232d58882668fc1cf446db923fc8822fec2a810` |

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
