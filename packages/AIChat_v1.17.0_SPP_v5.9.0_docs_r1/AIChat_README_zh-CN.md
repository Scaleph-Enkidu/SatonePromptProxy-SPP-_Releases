# AIChat 1.17.0：包内使用说明

配对程序为 **AIChat 1.17.0 + SatonePromptProxy 5.9.0**，适用于 Steam Windows 版《放松时光：与你共享 Lo-Fi 故事》。这是**文档修订 1**：补齐包内说明，不改 AIChat DLL 或 SPP EXE，运行版本保持不变。

AIChat 是游戏里的聊天界面；SPP 是在本机组织人设、记忆和模型请求的服务。先完成文字聊天，再按需加装语义回忆、聪音朗读或麦克风输入。

## 能做什么

- 与聪音文字聊天，使用游戏原生字幕、动画和聊天历史；回复在整轮播放或字幕展示完成后写入历史。
- 使用三个独立记忆档案，查看关系和情绪；人设、长期记忆、关键词回忆由配对 SPP 管理。
- 按当前存档同步已经历的剧情知识与原版台词，配合原版剧情门禁和特殊演出。
- 选装后使用 GPT-SoVITS 朗读回复，或用 Fun-ASR 把玩家语音转成文字；两种能力可分别安装。

## 文件放在哪里

推荐使用公开配对包，它已包含 AIChat 和 SPP；若取得仅 AIChat 的单组件包，还需配对的 SPP 5.9.0。本文位于安装包的 AIChat 组件根目录，详细教程在同层 `docs`文件夹。解压后保留目录结构：

| 文件 | 安装位置 |
| --- | --- |
| 本组件的 `AIChat.dll`、`AIChat.pdb`（配对包中位于 `AIChat/`） | 游戏 EXE 所在目录下的 `BepInEx/plugins` |
| 整个 `SatonePromptProxy` 文件夹 | 固定的个人目录，例如 `D:\LofiMOD\SatonePromptProxy`，不要只复制 EXE |
| 可选模型包里的 `models` | SPP EXE 同层；不要放到游戏插件目录或形成 `models/models` |
| 本组件同层 `docs` | 完整安装、语音、数据与排错说明，保留以便离线阅读 |

## 首次安装：先让文字聊天成功

1. 从 Steam 打开游戏目录，运行游戏一次并退出。将 **BepInEx 5.4.23.5 Windows x64** 解压到游戏 EXE 同层；那里应有 `BepInEx` 和 `winhttp.dll`。再运行游戏一次，确认生成 `BepInEx/plugins` 和 `BepInEx/LogOutput.log`，然后退出。
2. 将本包的 AIChat DLL/PDB 放入 `BepInEx/plugins`，只保留一份可加载的 AIChat DLL；旧 `AIChatSatoneUXPatch.dll` 移出插件目录。把完整 SPP 文件夹放到固定目录。
3. 运行 SPP 目录里的 `Start_Text_Chat.bat` 或 `SatonePromptProxy.exe`。首次启动会从示例生成 `config.json`；用浏览器打开 `http://127.0.0.1:11435/`，核对 SPP **5.9.0**。
4. 启动游戏、进入场景，按 **F9** 打开窗口，核对 AIChat **1.17.0**。点击 **“展开设置”**，展开 **“SPP 与记忆（人格代理）”**，将 **“SPP 启动文件路径：”**设为实际的 `SatonePromptProxy.exe` 路径。
5. 展开 **“LLM（聊天模型与连接）”**，选择要用的 OpenAI、DeepSeek 或中转站等服务。在 **“API Key（接口密钥）”**和 **“模型名称（可修改）”**填写自己的有效信息；中转站还要填写其要求的 API 地址。预填模型只是示例，以服务商当前权限和说明为准。
6. 点击常驻操作栏的 **“保存并应用配置”**。选择与编辑只是草稿，显示“（待应用）”时尚未切换。云端服务需要自己的 Key 和额度。
7. 如果首次接入时出现旧记忆选择，先备份，再按需要选择 **“带入旧版记忆并继续”**或 **“跳过旧版记忆，继续使用”**；跳过不会删除原文件。新玩家按界面完成当前档案准备。**先完成弹出的档案／旧记忆选择，再等所选服务显示“（正在使用）”后发消息**；连接激活可能正在等待这一步，不能只停在等待状态。
8. 保持 SPP 运行，输入一句普通问候并发送。看到回复、字幕/历史和恢复后的可输入状态，即完成文字阶段。未安装语音或 ONNX 不应妨碍打字；首次安装保留 `embedding_enabled=false`、`embedding_auto_start=false`。

这一阶段不用填写 TTS 启动脚本，不勾选“启动游戏时自动运行 TTS 服务”，不开持续通话。AIChat 使用 SPP 时，本地聊天入口为 `http://127.0.0.1:11435/v1/chat/completions`；不要把云端 Key 或云端 URL 填到语音服务地址。

## 日常操作

| 操作 | 默认快捷键或按钮 |
| --- | --- |
| 打开/关闭 AIChat 窗口 | **F9** |
| 发送文字 / 输入换行 | **Enter** / **Shift+Enter**；设置中“反转回车键行为”会交换二者 |
| 按住录音、松开提交 | **F8**，需先完成 ASR 安装 |
| 连续语音交谈 | 完成 ASR 短句测试后，再使用“开始持续通话” |

窗口里的“记忆档案：”选择对应独立记录；改变需要保存的设置后仍要点击“保存并应用配置”。原版剧情、失联或聪音不在座位等状态可能暂时限制聊天，请先处理游戏提示。回复中或待结算时不要反复重发同一条。

## 四阶段依赖：按需加装

1. **文字聊天**：游戏、BepInEx、配对主程序与聊天连接即可；关键词回忆已内置，不需要 Python、ONNX、TTS 或 ASR。
2. **ONNX 语义回忆（选装）**：另下载约 94 MB 的 E5 int8/ORT 组件包，停掉 SPP，把 `models` 放到 EXE 同层，运行 `Verify_Semantic_Recall.bat`、`Enable_Semantic_Recall.bat`后重启。首次 Recall 查询会触发暖机和后台准备；期间关键词回忆可用。
3. **聪音 TTS（选装）**：另装 GPT-SoVITS 环境和 GPT/SoVITS 声线权重，启动监听 9880 的 API，先生成并试听实际 WAV。在 **“TTS（文字转语音）”**中将 **“语音服务地址（默认连接 SPP 的 TTS 与 ASR 代理）：”**设为 `http://127.0.0.1:11435`，朗读语言设为 `ja`、音量大于 0，保存应用。包内 Neutral 参考录音不等于完整语音环境。
4. **玩家 ASR（选装）**：另建 Fun-ASR Python 环境和模型，按指南配置 SPP 的 `asr`，确认 9881 服务与麦克风权限。AIChat 共用上述语音服务地址，保存应用后先用 F8 测试短句，再开持续通话。

各阶段不依赖后续阶段，**ONNX 不是 TTS/ASR 的前置条件**；ASR 不要求先装 TTS，TTS 也不要求 ASR。只想打字并听聪音回复，可停在第三阶段。

## 升级与保留资料

退出游戏、SPP 和语音服务，备份 AIChat CFG/history 与整个 SPP 个人目录，再覆盖新版 DLL/PDB、程序及配套工具。保留 `config.json`、连接凭据、`local_v1`、整个 `memory_profiles`、人格修改、`models`、`semantic_recall_v1`、原版进度账本和声线资源。

不要删除整个 SPP 目录，也不要用 `config.example.json` 覆盖个人配置。已装且校验通过的同一模型组件可复用；组件变更时停机替换完整目录，禁止混装。整版本回退应恢复升级前成对程序和整套资料备份。

## 常见排查

| 问题 | 先做什么 |
| --- | --- |
| F9 没反应 | 查 `BepInEx/LogOutput.log`、插件层级、重复 DLL和旧 UXPatch；确认 BepInEx 正常加载 |
| 文字无法发送或连接失败 | 确认 SPP 管理页可打开、服务确实显示“（正在使用）”；核对 Key、模型和供应商返回的 401/404/429 |
| 提示语音模块未安装 | 可以继续打字；需要麦克风时再装 Fun-ASR，不用为此安装 ONNX |
| 有文字没有声音 | 查 9880 API、实际 WAV、权重/参考录音路径、TTS设置和音量；仅“就绪”不证明音频可播放 |
| F8 没有识别结果 | 查 Windows 麦克风权限、9881和 `/asr/status` 的实际环境、脚本、模型路径 |
| 大存档启动久、一直等待 | 查 SPP 日志，不重复启动或删存档；5万条合成WAL曾测得约495秒启动、整管线峰约944MB |

求助时说明版本、使用组合、时间和复现步骤；分享日志前隐藏 Key、私人聊天和本机路径。

完整步骤见 [本包安装指南](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/main/docs/INSTALL.zh-CN.md)、[语音设置](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/main/docs/VOICE_SETUP.zh-CN.md)和[备份与隐私](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/main/docs/DATA_AND_PRIVACY.zh-CN.md)。在线入口：[统一安装指南](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/main/docs/INSTALL.zh-CN.md) / [本配对 Release](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/tag/AIChat-v1.17.0_SPP-v5.9.0)。
