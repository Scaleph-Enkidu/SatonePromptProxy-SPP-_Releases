# 从零安装：AIChat 1.17.0 + SPP 5.9.0

[返回首页](../README.md) · [下载与校验](DOWNLOADS.zh-CN.md) · [语音详细设置](VOICE_SETUP.zh-CN.md)

适用于 Steam Windows 版《放松时光：与你共享 Lo-Fi 故事》，更新于 **2026-10-01**。

当前新玩家推荐 **文档修订 1（`docs_r1`）** 主程序包：补齐包内可独立阅读的 README、安装与版本改动正文，程序与模型保持不变，版本仍为 AIChat 1.17.0 + SPP 5.9.0。首次安装步骤与原包相同；原正式包保留，已安装用户无需为文档修订更新程序。原发布附件 `INSTALL_zh-CN.md` 保持原字节，新指南以本页和新 ZIP 内正文为准。

**先完成阶段一，文字聊天就能独立使用。** 后续按需增加：② ONNX 模型选装 → ③ 聪音发音 → ④ 玩家语音识别。各阶段不依赖后续阶段；② 可跳过，GPT-SoVITS 和 Fun-ASR 都不依赖 ONNX。云端聊天需要自己的 API Key 与额度；[费用说明](API_COST.zh-CN.md)以供应商实时价格和账单为准。

| 阶段 | 必需的下载 | 成功标志 |
|---|---|---|
| [① 文字聊天](#stage-1) | 配对主程序 ZIP、游戏与 BepInEx | F9 中发文字得到回复；没有语音模型也能继续打字 |
| [② ONNX 选装](#stage-2) | 可选 E5 int8 + ORT 模型 ZIP | Recall 的 engine、model_loaded、semantic_state 与索引数量符合当前档案 |
| [③ 聪音发音](#stage-3) | GPT-SoVITS 环境及声线 GPT／SoVITS 权重 | 测试 WAV 可播放，游戏能朗读回复 |
| [④ 玩家语音识别](#stage-4) | Fun-ASR 环境与模型 | F8 短句能识别并进入聊天 |

<a id="stage-1"></a>
## 阶段一：文字聊天（先完成）

### 文件放在哪里

1. 在 Steam 中运行游戏一次并退出。右击游戏 →“管理”→“浏览本地文件”，找到游戏 EXE 所在目录。
2. 将 [BepInEx 5.4.23.5 Windows x64](https://github.com/BepInEx/BepInEx/releases/tag/v5.4.23.5) 解压到游戏 EXE 同层，那里应有 `BepInEx` 和 `winhttp.dll`。启动游戏一次，确认生成 `BepInEx/LogOutput.log` 与 `BepInEx/plugins`，再退出。
3. 下载 [SatoneMod_AIChat_1.17.0_SPP_5.9.0_Windows_x64_docs_r1.zip](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.17.0_SPP-v5.9.0/SatoneMod_AIChat_1.17.0_SPP_5.9.0_Windows_x64_docs_r1.zip)（约 11 MB）。它已配对包含 AIChat 与 SPP，**无需再下载私库的单组件包**；不要选 Source code ZIP。
4. 把包内 `AIChat/AIChat.dll` 与配套 `AIChat.pdb` 放入 `游戏目录/BepInEx/plugins`。只保留一份可加载的 AIChat DLL；旧 `AIChatSatoneUXPatch.dll` 也移出插件目录。
5. 把包内整个 `SatonePromptProxy` 文件夹放到固定位置，例如 `D:\LofiMOD\SatonePromptProxy`。EXE 旁应有 `config.example.json`、`SatonePersona_v4.6.txt`、BAT 工具、ASR 脚本和 `mayuri-voice/refs/MAY_1158_Neutral.wav`。不要只复制 EXE。

### 设置什么

1. 运行 `Start_Text_Chat.bat` 或 `SatonePromptProxy.exe`。新目录首次启动会创建 `config.json`；打开本机 [SPP 管理页](http://127.0.0.1:11435/)，核对 **5.9.0**。默认端口是 **11435**。
2. 启动游戏，进入场景按 **F9**，核对 **AIChat 1.17.0**。在设置中让 **SPP 程序路径**指向刚才的 EXE，本地聊天地址使用 `http://127.0.0.1:11435/v1/chat/completions`。
3. 在 **LLM（聊天模型与连接）** 中选择所用服务，例如 OpenAI、DeepSeek 或中转站，填写该服务的 Key、可用模型名称和要求的 API 地址。输入框预填名称只是可修改的示例；以服务商当前列表和自己的权限为准。
4. 点击 **“保存并应用配置”**；若弹出档案准备或旧记忆选择，先备份并完成选择，再等待界面显示当前使用的连接后发新消息。连接激活可能正在等待该选择。勾选或编辑尚未保存的草稿不会立即切换正在使用的服务。
5. 这一阶段不使用语音时，暂不设置 TTS 启动脚本、不勾选“启动游戏时自动运行 TTS 服务”、不开持续通话；尚未安装 Fun-ASR 的提示不妨碍文字聊天。**保留 `embedding_enabled=false`、`embedding_auto_start=false`，模型默认不启用。**

### 启动与验收

保持 SPP 运行，在 F9 窗口输入一句普通问候并发送，应看到回复、字幕／历史和恢复后的可输入状态。Enter 发送，Shift+Enter 换行。未安装语音或 ONNX 时仍应能继续打字；关键词回忆已经内置，无需 Python。

<details>
<summary>进阶配置（可跳过）</summary>

- 新版首次接入旧档案时可以选择导入或跳过；跳过不等于删除旧文件。三个档案独立，同一档案切换服务无需删记忆。
- 默认人格文件为 `SatonePersona_v4.6.txt`，全局共用；修改会影响三个档案。原版经历同步需要游戏运行时可验证的 Steam 身份。
- Meta 恐怖演出与 F10 外观采集器的特色说明保留在[首页](../README.md)；采集器是独立可选工具，不是文字聊天前置依赖。
- 主聊天通过云端 API 运行；本教程未提供已验证的纯离线主聊天安装路线。主程序与本地回忆不需要 Python，后续语音环境另计。

</details>

**下一阶段：** [② 安装可选 ONNX 模型](#stage-2)。不需要语义回忆时，直接进入 [③ 聪音发音](#stage-3)，或停在这里使用文字聊天。

<a id="stage-2"></a>
## 阶段二：ONNX 语义回忆（可选）

这一步让旧对话支持换词查询，不负责生成聊天、发音或识别麦克风。**可跳过，TTS／ASR 不依赖它。**

### 文件放在哪里

1. 正常退出 SPP，下载 [Satone_Semantic_E5_small_int8_ORT_1.30.0_Windows_x64.zip](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.17.0_SPP-v5.9.0/Satone_Semantic_E5_small_int8_ORT_1.30.0_Windows_x64.zip)（约 94 MB）。
2. 把模型包中的 `models` 文件夹复制到 **SPP EXE 所在目录**。不要放进游戏插件目录，也不要形成 `models/models`。结果应为：

```text
D:\LofiMOD\SatonePromptProxy\
  SatonePromptProxy.exe
  Verify_Semantic_Recall.bat
  Enable_Semantic_Recall.bat
  models\multilingual-e5-small\
    model.onnx
    tokenizer.json
    onnxruntime.dll
    onnxruntime_providers_shared.dll
    COMPONENT.json
    licenses\
```

### 设置、启动与验收

1. 双击 `Verify_Semantic_Recall.bat`，确认“组件文件校验通过”。再双击 `Enable_Semantic_Recall.bat`，成功后重新启动 SPP。**不要省略校验或启用步骤；只解压模型不会启用语义回忆。** 工具会先备份配置；SPP 运行中会拒绝改写。
2. 打开 [Recall 测试](http://127.0.0.1:11435/recall/test?q=%E8%AE%B0%E5%BE%97%E6%88%91%E4%BB%AC%E8%81%8A%E8%BF%87%E4%BB%80%E4%B9%88%E5%90%97)，或使用 `http://127.0.0.1:11435/recall/test?q=你的查询`。**第一次查询会触发后台暖机与向量准备**；仅打开状态页不等于已经触发。也可在本地管理页支持的 Recall 查询界面操作；旧 Dashboard 或旧截图可能没有这个输入区，直接用端点即可。
3. 打开 [Recall 状态](http://127.0.0.1:11435/recall/status)。等待当前档案的 `worker.semantic_state` 从 `waiting/loading/building` 变为 **`ready`**，确认 **`engine: "native_keyword+onnx"`**、**`worker.model_loaded: true`**，并查看 **`worker.embedded_exchanges`** 与 `worker.semantic_scope`。已有可索引交流时数量应大于 0；全新空档案可以为 0。
4. 用当前档案里确实聊过的话题换词再查一次，观察结果是否符合那段交流。模型加载成功不保证每个换词都命中；`semantic_qualified` 是保守注入筛选，原始相似度不是置信概率。大量旧记录的后台准备需要时间，期间仍可使用关键词回忆。

<details>
<summary>进阶配置（可跳过）</summary>

- 工具使用现有键 `embedding_enabled=true`、`embedding_auto_start=true`、`embedding_model_dir="models/multilingual-e5-small"`。名称含 embedding 不代表仍要安装旧 Python worker；本版本使用原生 ONNX CPU 路线，旧 Python／SQLite 模型目录不能直接替代组件。
- 停用时退出 SPP，运行 `Disable_Semantic_Recall.bat`，再启动。模型、存档与缓存保留。配置备份名为 `config.json.before-semantic-时间编号`。
- `disabled` 表示未启用，`missing` 表示缺文件，`failed` 应结合 `worker.last_error` 排查。文件损坏、不支持的 hash、加载失败或忙碌会回退关键词；不要用来源不明的单个 DLL 拼装。
- 模型由固定 revision、四个支持文件的 hash 和 `COMPONENT.json` 识别。以后更新兼容的主程序，保留整个 `models` 与 `semantic_recall_v1`，校验同一组件即可，不必重新下载约 94 MB。组件升级时停机替换完整目录，不混用版本。
- 语义缓存位于 SPP 根目录 `semantic_recall_v1`，可以重建，不是权威存档。语义只覆盖最新 50,000 条已交流记录；关键词仍覆盖完整历史，旧数据库和核心存档原样保留。

</details>

**下一阶段：** [③ 让聪音发音](#stage-3)。不需要声音可继续只用文字与本地回忆。

<a id="stage-3"></a>
## 阶段三：让聪音发音（GPT-SoVITS）

**本阶段不依赖 ONNX 或 Fun-ASR。** 程序包已带 Neutral 参考音频，仍需外装 GPT-SoVITS 运行环境和 GPT／SoVITS 声线权重。

### 必需步骤：放置、设置、启动、验收

1. 按[语音页阶段三](VOICE_SETUP.zh-CN.md#stage-3)下载并完整解压支持所用声线版本的 GPT-SoVITS，例如放到 `D:\LofiMOD\GPT-SoVITS`；根目录应有 `api_v2.py`、`GPT_SoVITS` 和实际 Python 环境。
2. 将声线的 GPT `.ckpt` 与 SoVITS `.pth` 放到其对应权重目录。按语音页核对 `tts_infer.yaml` 的版本、权重、基础模型路径以及设备／精度；创建并启动监听 **127.0.0.1:9880** 的 `run_api.bat`。WebUI 打开不等于 API 已启动。
3. SPP `config.json` 中保留 `emotion_tts.enabled=true`、`upstream_url="http://127.0.0.1:9880"`、`fallback_profile="Neutral"`。新装使用空 `ref_root` 与包内 `MAY_1158_Neutral.wav`；旧配置若指向外部目录，清空或改为包内 `mayuri-voice/refs` 的实际绝对路径。参考台词必须匹配录音，默认模板已有台词。
4. 重启 SPP，打开 [TTS 状态](http://127.0.0.1:11435/tts/status)。先按语音页生成并播放实际测试 WAV，再在 AIChat 的 TTS 设置中将“语音服务地址”设为 **`http://127.0.0.1:11435`**、朗读语言设为 `ja`、音量大于 0，点击“保存并应用配置”，发送一句文字确认游戏能发声。**服务状态就绪不能替代听到可播放的声音。**

<details>
<summary>进阶配置（可跳过）</summary>

- 已完成手动启动与试听后，可运行 `Set_GPTSoVITS_RunApi_Path.bat` 保存自己的 `run_api.bat` 路径，再用 `Start_AIChat_Services.bat` 启动服务。
- 其余情绪参考录音是可选资源，缺失时使用 Neutral。26 项配置与声线作者／参考录音许可见[语音页](VOICE_SETUP.zh-CN.md#stage-3)。
- CPU 路线与减少重复进程的说明见[硬件页](HARDWARE.zh-CN.md)；语音速度取决于实际模型、设备和环境。

</details>

**下一阶段：** [④ 安装玩家语音识别](#stage-4)。只想打字并听回复，可以停在这里。

<a id="stage-4"></a>
## 阶段四：玩家语音识别（Fun-ASR）

**Fun-ASR 不依赖 ONNX，也不要求先装 GPT-SoVITS。** 想同时听到回复时才需要阶段三。

### 必需步骤：放置、设置、启动、验收

1. 按[语音页阶段四](VOICE_SETUP.zh-CN.md#stage-4)建立独立 Python 环境（例如 `D:\LofiMOD\AI\FunASR-Runtime\.venv`），安装匹配的 Torch／torchaudio／FunASR 依赖。不要改装 GPT-SoVITS 的自带环境来安装 ASR。
2. 完整下载 `FunAudioLLM/Fun-ASR-Nano-2512` 到 `D:\LofiMOD\AI\Fun-ASR-Nano-2512`。模型根目录应有 `config.yaml`、`configuration.json`、`model.pt`、`Qwen3-0.6B` 等；只下载单个权重不足以启动。
3. 退出 SPP，在自己的 `config.json` 的 `asr` 节填实际 `python` 和 `model_path`，保留 `enabled=true`、`auto_start=true`、`upstream_url="http://127.0.0.1:9881"`、`language="auto"`；`server_script` 可留空使用包内 `satone_funasr_server_v1.py`。这些是 `asr` 内的字段，不能写到 JSON 根级。
4. 重启 SPP，等待加载。查看 [ASR 状态](http://127.0.0.1:11435/asr/status) 与 [后端健康页](http://127.0.0.1:9881/health)，核对环境、脚本和模型路径，后端应返回 `ok: true`。
5. 在 AIChat 的 TTS 设置中核对共用的“语音服务地址”为 **`http://127.0.0.1:11435`**，点击“保存并应用配置”；不使用 TTS 时也通过此地址代理 ASR。在 Windows 选择可用麦克风并允许游戏录音。先按住 **F8** 说一句短话、松开，确认识别文字进入聊天并收到回复；成功后再自行开启持续通话（默认关闭）。健康页成功不等于麦克风和真实识别已验收。

<details>
<summary>进阶配置（可跳过）</summary>

- 当前随包脚本未强制 `device="cpu"`，ONNX 的 CPU 设置不影响 ASR。希望 ASR 使用 CPU 时按[语音页的进阶配置](VOICE_SETUP.zh-CN.md#asr-cpu)测试独立脚本副本。
- 若 9881 已有旧 ASR 服务，SPP 可能复用它；按命令行确认身份后停掉旧服务，再核对新模型。不要按占用大小猜服务身份。
- 分别测试较长录音、持续通话与中／日文短句，记录延迟与错误；硬件／依赖不同会改变结果。

</details>

**下一步：** 按需使用已完成的组合；[升级与排错](#upgrade)和[数据备份](DATA_AND_PRIVACY.zh-CN.md)在下方。2026-10-01 用户已确认本机测试完成；这不代表所有硬件、供应商和语音组合都已测试。

<a id="upgrade"></a>
## 升级、回退与排错

升级前退出游戏、SPP 与相关语音服务，备份 AIChat CFG/history 和整个 SPP 个人运行目录。覆盖新版 DLL／PDB、SPP 程序与配套工具，**保留 `config.json`、连接凭据、`local_v1`、整个 `memory_profiles`、人格修改、`models`、`semantic_recall_v1`、原版进度账本和声线资源**。不要先删除整个 SPP 目录，也不要用 `config.example.json` 覆盖个人配置。

回退时成对恢复升级前的 AIChat／SPP 程序，以及整套配置与存档备份；新版本产生的数据不保证旧版本完整理解。[上一配对 Release](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/tag/AIChat-v1.16.65_SPP-v5.8.42)保留。仅停用语义模型可用 Disable 工具，不需要删存档。

| 症状 | 先检查 |
|---|---|
| F9 无反应 | 游戏 `BepInEx/LogOutput.log`、插件层级、重复 DLL |
| SPP 打不开 | SPP 日志、`config.json` 格式、本机 11435 端口；大存档启动可能较慢 |
| 云端聊天失败 | 当前已应用的连接、Key、模型和 URL；401／404／429 以服务商返回为准 |
| ONNX 不 ready | `/recall/status`、模型层级、Verify 结果、是否 Enable、是否已发首次查询 |
| 有文字无声音 | 9880 API、权重版本、Neutral 实际路径、TTS 开关和实际 WAV 测试 |
| F8 不识别 | Windows 麦克风权限、9881、ASR 状态中的实际环境和首次 Python 错误 |

求助时附版本、组合、档案、时间和复现步骤；分享状态或日志前隐藏 Key、私人聊天与本机路径。[资源测量与限制](HARDWARE.zh-CN.md)和[维护记录](MAINTAINER_STATUS.zh-CN.md)说明自动化覆盖范围。
