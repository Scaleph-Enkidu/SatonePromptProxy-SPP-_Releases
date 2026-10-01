# ONNX 语义回忆：进阶说明与排错

**第一次安装请看[四阶段教程的阶段二](INSTALL.zh-CN.md#stage-2)。** 那里包含下载、放置、启用和验证的完整步骤。本页适用于 AIChat 1.17.1 + SPP 5.9.1，Windows x64，更新于 2026-10-01。

[返回安装教程](INSTALL.zh-CN.md#stage-2) · [下载与校验](DOWNLOADS.zh-CN.md) · [硬件开销](HARDWARE.zh-CN.md)

## 暂时停用，或以后重新启用

1. 等当前聊天结束，退出游戏。
2. 打开自己的 `SatonePromptProxy` 文件夹，双击 **Stop_SatonePromptProxy.bat**，等待窗口显示停止结果，再按任意键关闭窗口。它会强制停止所有名为 `SatonePromptProxy.exe` 的进程；同时运行多份 SPP 的玩家应分别管理各实例，不要在未完成的聊天中使用。
3. 双击 **Disable_Semantic_Recall.bat**，看到 **语义回忆已停用。** 后关闭窗口。
4. 双击 **Start_Text_Chat.bat**，然后启动游戏。文字聊天和关键词回忆仍能使用。

停用不会删除模型、缓存或聊天记录。以后想重新启用，停止 SPP，依次运行 **Verify_Semantic_Recall.bat** 和 **Enable_Semantic_Recall.bat**，然后重新启动 SPP，再按[阶段二](INSTALL.zh-CN.md#stage-2)检索已有聊天。

## 读懂“索引状态”

运行 SPP 后，双击 **Open_Dashboard.bat**，在“本地记忆管理”页面选择要查看的档案，然后在 **Recall 检索** 下点击 **索引状态**。每次点击会重新获取状态；等待后需要再次点击查看最新结果。

| semantic_state 显示的内容 | 含义与处理 |
|---|---|
| disabled | 模型没有启用。需要使用时，停止 SPP，运行 Enable 工具，然后重启。 |
| missing | 没有找到完整模型文件。检查 models\multilingual-e5-small 的位置，重新解压模型包，再运行 Verify 工具。 |
| waiting | 等待检索，或档案中没有可检索的交流。先在对应档案完成一轮聊天，再点击“检索”。空档案停在这里属于正常情况。 |
| loading | 正在加载模型。等一会儿再点“索引状态”。 |
| building | 正在准备当前档案的检索记录。旧聊天越多，需要的时间可能越长。 |
| ready | semantic_scope 对应档案的语义检索已经准备完成。确认它与当前查看档案一致，并检查 model_loaded 是否为 true，再进行实际检索。 |
| failed | 准备失败。查看同一段状态中的 last_error，按具体错误处理；必要时附脱敏后的错误求助。 |

其他有用的字段：

- engine: "native_keyword+onnx" 表示使用关键词与 ONNX 组合的回忆方式，不能单凭这个字段判断模型已经加载。
- worker.model_loaded: true 表示模型已加载。
- worker.embedded_exchanges 是已经准备好的交流数量。它不是游戏历史窗口的行数；有完整交流的档案应有对应记录。
- worker.semantic_scope 是模型最近准备的档案，例如 local:memory1。它应与“查看档案”选择一致；切换查看档案后若仍显示上一份档案，先对新选择点击“检索”，等待准备后再查状态。外层 profile_id 表示当前查看的档案，不能替代这个核对。
- 检索返回中的 semantic_ready: false 表示本次先使用关键词；首次准备或忙碌时可能出现。等准备完成后再查。

如果返回服务忙碌（HTTP 409），等当前聊天处理完成再试。“查看档案”只改变管理页查看的内容；要切换游戏聊天档案，请在 AIChat UI 的记忆档案设置中选择并保存。

### 找不到聊天，但模型已就绪

先用聊天中确实出现过的关键词检索，再换成相近的说法。检查返回内容里的 user_text、assistant_text 或 full_text 是否是那一段交流。

模型加载成功不保证所有换词都能找到。同一词语可能对应多段聊天；语义相似度不是正确率，也不是置信概率。semantic_qualified 是将结果用于聊天时的额外筛选，不能当成“模型能否运行”的唯一判断。

### 文件校验失败

模型目录应完整包含 model.onnx、tokenizer.json、onnxruntime.dll、onnxruntime_providers_shared.dll、COMPONENT.json 和 licenses。不要混用其他模型包里的单个文件。

重新下载[本版本模型包](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.17.1_SPP-v5.9.1/Satone_Semantic_E5_small_int8_ORT_1.30.0_Windows_x64.zip)，停止 SPP 后替换完整组件目录，再运行 Verify 工具。校验失败时工具不会改写启用配置；解决失败后再 Enable。

如果 Stop 工具提示“没有运行”，但管理页刷新后仍能访问，可能没有成功停止进程。先检查任务管理器中的 SPP 进程，再进行启停工具操作。

## 主程序升级与模型更新

只更新兼容的主程序时，保留已有的整个 models 文件夹和 semantic_recall_v1，不需要重新下载同一个约 94 MB 模型包。升级后再运行 Verify，并实际检索一次旧聊天。

需要更换模型组件时，先停机、备份，再替换完整的 models\multilingual-e5-small 目录。模型、tokenizer 与运行库必须来自同一兼容组件，不混用版本。精确文件身份见[原发布清单](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/AIChat-v1.17.0_SPP-v5.9.0/releases/AIChat_v1.17.0_SPP_v5.9.0.json)。

## 配置、缓存和来源

Enable 工具会先备份配置，再调整 embedding_enabled=true、embedding_auto_start=true 和 embedding_model_dir="models/multilingual-e5-small"。备份文件名是 config.json.before-semantic-时间编号。一般玩家使用 BAT 工具即可，无需手动修改这些键。

这套组件使用原生 CPU ONNX 路线。旧 Python Embedding worker 的模型目录不能直接替代它。缺文件、校验失败、加载失败或忙碌时，回忆可以先使用关键词。

semantic_recall_v1 是可重建的语义缓存，也应作为私人数据保护。**它与不能随意删除的聊天权威记录、记忆档案和旧数据库不同。** 语义检索覆盖最新 50,000 条已交流记录；更旧记录仍保存在存档中，并可由关键词检索。实际内存与首次准备耗时见[硬件说明](HARDWARE.zh-CN.md)，约 94 MB 只表示压缩下载大小。

模型来源：[intfloat/multilingual-e5-small 的固定 revision](https://huggingface.co/intfloat/multilingual-e5-small/tree/614241f622f53c4eeff9890bdc4f31cfecc418b3)。运行库来源：[ONNX Runtime 1.30.0](https://github.com/microsoft/onnxruntime/releases/tag/v1.30.0)。模型说明、E5 项目 MIT 许可、ORT 许可和第三方声明保留在组件的 licenses 目录中；固定 revision 和支持文件校验值记录在 COMPONENT.json。

**继续安装：** [③ 聪音发音](INSTALL.zh-CN.md#stage-3) · [④ 玩家语音识别](INSTALL.zh-CN.md#stage-4)。两者都不依赖这个模型。
