# 下载清单：AIChat 1.16.65 + SPP 5.8.42

[返回首页](../README.md) · [按步骤安装](INSTALL.zh-CN.md) · [语音配置](VOICE_SETUP.zh-CN.md)

版本和链接核对日期：**2026-09-30**。[配对发布页](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/tag/AIChat-v1.16.65_SPP-v5.8.42)的 Assets 提供两份安装包；不要把 GitHub 自动生成的 Source code ZIP 当作插件。需要回退时用仍保留的[上一稳定配对 AIChat 1.16.23 + SPP 5.8.26](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/tag/AIChat-v1.16.23_SPP-v5.8.26)。

| 文件 | 放置位置 | SHA-256 |
|---|---|---|
| [AIChat_v1.16.65.zip](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.16.65_SPP-v5.8.42/AIChat_v1.16.65.zip) | 取出 `AIChat.dll` 和配套 PDB，放入游戏 `BepInEx/plugins` | `270923a5ba46796f0f119e82f94fc23d9959bbb65e89fd81b0e0447249819d42` |
| [SatonePromptProxy_v5.8.42.zip](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.16.65_SPP-v5.8.42/SatonePromptProxy_v5.8.42.zip) | 完整解压到固定 SPP 目录，保留 `mayuri-voice/refs/` | `e18dabb5253a332d18124f80aa43bae39a467394da415fb67e01b6dfbef61e85` |
| [tools/SatoneStateCatalog](../tools/SatoneStateCatalog/README_中文.md)（可选） | 把 `prebuilt/SatoneStateCatalog.dll` 放进 `BepInEx/plugins`，游戏内按 F10 | `e3d1802848997c9a91efd94fe23e2ba5ebe4a4d0d2f4e3684836201834b12c06`（DLL） |

两包包含版本说明和文件校验清单，不含玩家 API Key、配置或记忆。已有安装升级时保留个人数据。下载后可在文件夹地址栏输入 `powershell`，分别执行 `Get-FileHash .\AIChat_v1.16.65.zip -Algorithm SHA256` 与 `Get-FileHash .\SatonePromptProxy_v5.8.42.zip -Algorithm SHA256`，和上表比较。

## 游戏与基础加载器

- 在 Steam 安装 **Chill with You : Lo-Fi Story**。
- 安装 [BepInEx 5.4.23.5 Windows x64](https://github.com/BepInEx/BepInEx/releases/tag/v5.4.23.5) 到游戏 EXE 同层。已有 BepInEx 时先核对版本和现有插件，勿清空其他 Mod。

## 想听到语音时

- 安装 [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS)及与你设备相容的运行环境。Windows 整合包与版本选择见[上游列表](https://huggingface.co/lj1995/GPT-SoVITS-windows-package/tree/main)。
- 另下载[“孤独摇滚”后藤一里 v2ProPlus 声线](https://huggingface.co/lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models/tree/main/models/Hitori_Gotoh/v2ProPlus/gotoh-v1-3-1)的 **GPT `.ckpt` 与 SoVITS `.pth` 两份权重**，按[语音教程](VOICE_SETUP.zh-CN.md)加载。不要混用 v4 权重。
- **Neutral 参考音频已经在 SPP ZIP 内**，路径为 `mayuri-voice/refs/MAY_1158_Neutral.wav`；不需要为基本发声再单独下载这段。其他情绪音频未随包提供。旧 `emotion_tts.ref_root` 如指向外部目录，需核对指向。
- 声线模型的[原作者许可](https://huggingface.co/lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models)为 CC BY-NC-SA 4.0；Neutral 音频的[原项目](https://huggingface.co/SteinsGateSg/mayuri-voice)标注 `License: other`。按各来源条件使用，听感需自行试听。

## 想用麦克风或检索时

- 麦克风另需 [Fun-ASR 项目](https://github.com/QwenAudio/Fun-ASR)、[Fun-ASR-Nano-2512 模型](https://huggingface.co/FunAudioLLM/Fun-ASR-Nano-2512)、匹配的 Python/Torch 环境。SPP 包内服务脚本不等于已经安装模型。
- 按意思查找旧对话可选 [multilingual-e5-small](https://huggingface.co/intfloat/multilingual-e5-small) 等本地 Embedding 模型；只打字聊天无需先装它。

OpenAI 和 DeepSeek 需要各自账户与 API Key。首次模型默认值分别为 `gpt-6-luna`、`deepseek-flash`（截至 2026-09-28）；请以各家官网当前模型列表和账户权限为准。插件和模型文件不会附送 API 额度。
