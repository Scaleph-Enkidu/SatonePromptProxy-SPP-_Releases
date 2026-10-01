# ONNX 语义回忆选装：E5 small int8 + ORT 1.30.0

[返回四阶段安装](INSTALL.zh-CN.md#stage-2) · [下载清单](DOWNLOADS.zh-CN.md) · [资源边界](HARDWARE.zh-CN.md)

适用 **AIChat 1.17.0 + SPP 5.9.0**，Windows x64，2026-10-01。**这是阶段二选装项，不默认启用。** 文字聊天与关键词回忆无需它；GPT-SoVITS 发音和 Fun-ASR 麦克风也不依赖它。

## 必需步骤：放置、设置、启动、验收

1. 先完成[文字聊天](INSTALL.zh-CN.md#stage-1)，正常退出 SPP。下载 [Satone_Semantic_E5_small_int8_ORT_1.30.0_Windows_x64.zip](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.17.0_SPP-v5.9.0/Satone_Semantic_E5_small_int8_ORT_1.30.0_Windows_x64.zip)（约 94 MB），把其中的 `models` 文件夹复制到 **SPP EXE 旁**。
2. 确认 `models/multilingual-e5-small` 内有 `model.onnx`、`tokenizer.json`、`onnxruntime.dll`、`onnxruntime_providers_shared.dll`、`COMPONENT.json` 和 `licenses`。不要解压到游戏插件目录，也不要形成 `models/models`。
3. 双击主程序目录中的 `Verify_Semantic_Recall.bat`，看到“组件文件校验通过”后，再运行 `Enable_Semantic_Recall.bat`。**解压不等于启用。** 工具先备份配置，运行中的 SPP 会拒绝改写；成功后重新启动 SPP。
4. 打开 [Recall 测试](http://127.0.0.1:11435/recall/test?q=%E8%AE%B0%E5%BE%97%E6%88%91%E4%BB%AC%E8%81%8A%E8%BF%87%E4%BB%80%E4%B9%88%E5%90%97)，或 `http://127.0.0.1:11435/recall/test?q=你的查询`，**触发首次后台暖机与向量准备**。本地管理页若提供 Recall 查询区，也可在其中输入；旧 Dashboard／截图没有此区时直接用端点。仅打开状态页不等于触发了暖机。
5. 查看 [Recall 状态](http://127.0.0.1:11435/recall/status)，等待当前档案 `worker.semantic_state="ready"`，确认 `engine="native_keyword+onnx"`、`worker.model_loaded=true`、`worker.semantic_scope` 是当前档案，并检查 `worker.embedded_exchanges`。有可索引交流时应大于 0，空档案可为 0；大量记录准备需要时间，期间仍可用关键词回忆。
6. 对当前档案确实聊过的话题做换词查询，检查结果内容；加载 ready 不保证每次换词都命中。语义相似度不是置信概率，`semantic_qualified` 是额外的保守筛选。

<details>
<summary>进阶配置（可跳过）</summary>

- 启用工具调整 `embedding_enabled=true`、`embedding_auto_start=true` 与 `embedding_model_dir="models/multilingual-e5-small"`。这是原生 CPU ONNX 路线，不需旧 Python Embedding worker；旧 Python／SQLite 模型目录不能直接作为新组件。
- `disabled` 表示未启用，`missing` 表示缺文件，`waiting/loading/building` 表示等待首次查询或后台准备；`failed` 结合 `worker.last_error` 排查。缺组件、校验失败、加载失败或忙碌时回退关键词。
- 停用：退出 SPP → `Disable_Semantic_Recall.bat` → 重启。模型、缓存和存档保留。配置备份名为 `config.json.before-semantic-时间编号`。
- 组件身份由固定 revision、四个支持文件的 hash 和 `COMPONENT.json` 记录。支持同一组件的程序升级保留整个 `models` 与 `semantic_recall_v1`，重新校验即可；组件升级才需停机替换完整目录，不能混用版本。
- `semantic_recall_v1` 是可重建的私人缓存，权威 WAL 与档案不是缓存。语义最多覆盖最新 50,000 条已交流记录，关键词仍覆盖完整历史，旧 DB 与权威存档不删减。
- 精确包身份见[公开发布清单](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/AIChat-v1.17.0_SPP-v5.9.0/releases/AIChat_v1.17.0_SPP_v5.9.0.json)；模型说明、E5 项目 MIT 许可、ORT 许可和第三方声明在组件的 `licenses` 中。约 94 MB 是压缩下载大小，内存范围见[硬件页](HARDWARE.zh-CN.md)。

</details>

**下一阶段：** [③ 让聪音发音](INSTALL.zh-CN.md#stage-3)。不需要声音可继续只用文字与回忆。2026-10-01 用户确认本机测试完成；自动化合成语料和资源测量与这条确认分开记录，见[维护记录](MAINTAINER_STATUS.zh-CN.md)。
