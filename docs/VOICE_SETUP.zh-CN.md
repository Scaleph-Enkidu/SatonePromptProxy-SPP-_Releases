# 语音与麦克风设置

[返回安装步骤](INSTALL.zh-CN.md) · [下载清单](DOWNLOADS.zh-CN.md)

本文将“聪音发声”和“听懂玩家说话”分开设置。前者使用 GPT-SoVITS，后者使用 Fun-ASR；装好一个不会自动装好另一个。

**验证边界：** 下面根据当前 SPP/AIChat 源码与上游文档编写，尚未在没有开发环境的新 Windows 电脑上走完全部步骤。尤其是 GPU/驱动/Python 依赖组合与开发者实际使用的声线来源，仍需发布前验证。无法验证的部分不会写成“一键安装成功”。

## A. 让聪音发声

### A1. 安装 GPT-SoVITS

1. 打开[官方项目](https://github.com/RVC-Boss/GPT-SoVITS)和[官方整合包列表](https://huggingface.co/lj1995/GPT-SoVITS-windows-package/tree/main)。根据显卡与上游说明选择 Windows 包；本教程以 v2Pro 系列提供的 `api_v2.py` 为连接方式。
2. 用 7-Zip 解压到 `D:\LofiMOD\GPT-SoVITS`。这里应当能直接看到 `api_v2.py`、`runtime` 和 `GPT_SoVITS` 子文件夹。若多套了一层文件夹，以实际包含这些文件的一层作为根目录。
3. 双击包内 `go-webui.bat`，按终端提示打开本地网页，在 TTS 推理页进行单独测试。
4. 选择匹配的 GPT 权重和 SoVITS 权重，上传有效参考录音，填写录音原文与语言，再输入要合成的日语，先确认网页能生成可播放声音。

上游 README 对整合包的原文说明是：

> “download the integrated package” / “double-click on go-webui.bat”

网页能打开只说明 WebUI 已启动；游戏需要的是接下来设置的 **API 服务**。

### A2. 分清三个文件来源

| 内容 | 作用 | 如何取得 |
|---|---|---|
| 基础预训练权重与文本模型 | 让 GPT-SoVITS 能运行 | 整合包自带或从[官方模型仓库](https://huggingface.co/lj1995/GPT-SoVITS/tree/main)补齐 |
| 特定声线的 GPT `.ckpt` / SoVITS `.pth` | 采用某个训练后的声音 | 从声线作者原发布页下载，并核对它针对 v2、v2Pro、v2ProPlus 等哪一版 |
| 参考 `.wav` 与准确台词 | 为一次合成提供发声参考 | 自己录制或取得有明确使用许可的音频 |

可以先用基础模型与自己的录音检查流程；这不会保证得到与开发者相同的声线。本项目当前还缺少“开发者所用声线的准确原发布链接与文件清单”，因此严格复现该声音的步骤暂不能闭合。不能靠一个相似角色名称推断正确模型。

SPP 默认模板引用的 `MAY_*.wav` **没有随包提供**。如果这些文件不存在，必须配置自己实际拥有的参考录音。SPP 对有效参考音频的检查包括：标准 RIFF/WAVE、能读取、时长 **3–10 秒**，并有非空台词。实际选择时用一段清晰的单人讲话，避免音乐、多人重叠或长静音。

### A3. 让 API 使用正确的模型

WebUI 中切换了模型，不代表另一个 API 进程也自动切换了模型。

1. 用记事本打开 `GPT_SoVITS\configs\tts_infer.yaml`，先保留一份自己的备份。
2. 在实际启用的 `custom:` 配置中核对下面的键，不要破坏其他节、缩进或文本模型路径：

| 键 | 填写规则 |
|---|---|
| `version` | 与所选 SoVITS 权重一致，例如 `v2`、`v2Pro` 或 `v2ProPlus`，区分大小写 |
| `t2s_weights_path` | 实际的 GPT `.ckpt` 路径 |
| `vits_weights_path` | 实际的 SoVITS `.pth` 路径 |
| `bert_base_path` / `cnhuhbert_base_path` | 必须指向已存在的基础模型目录 |
| `device` / `is_half` | 兼容 NVIDIA GPU 的常见组合是 `cuda` / `true`；CPU 尝试使用 `cpu` / `false`，本项目不保证其实时性能 |

YAML 使用空格缩进，不用 Tab。Windows 路径可写成 `D:/LofiMOD/...`，避免反斜杠转义问题。v2Pro 系列还依赖对应的基础权重和说话人编码模型，缺文件时按[上游 v2Pro 说明](https://github.com/RVC-Boss/GPT-SoVITS#v2pro-release-notes)补齐。

3. 在 GPT-SoVITS 根目录创建 `run_api.bat`；记事本保存类型选“所有文件”，内容为：

```bat
@echo off
cd /d "%~dp0"
"runtime\python.exe" -s api_v2.py -a 127.0.0.1 -p 9880 -c "GPT_SoVITS/configs/tts_infer.yaml"
pause
```

这是本文给出的启动脚本示例，不是两个 Mod ZIP 内自带的文件。若所选整合包没有 `runtime\python.exe`，不能照抄这个路径，需使用该整合包的实际 Python 路径。

4. 关闭先前不需要的 WebUI 推理进程，避免重复占用显存，再运行 `run_api.bat`。终端应该监听 `127.0.0.1:9880`，不是报错后退出。

### A4. 先配置一个 Neutral 参考音频

暂时只做一个正常说话参考，其他情绪缺失时由它兜底。不要为第一轮安装准备几十个未经核对的情绪文件。

1. 新建 `D:\LofiMOD\voice\refs`，放入自己的 `neutral.wav`。
2. 退出 SPP，用记事本打开 SPP 的 `config.json`。
3. 找到已有的 `emotion_tts`，修改其中 `ref_root`、`fallback_profile` 和 `profiles.Neutral`。下面是结构示例，**不是整个 config.json**；不要把它覆盖到整份配置上：

```json
{
  "ref_root": "D:/LofiMOD/voice/refs",
  "fallback_profile": "Neutral",
  "profiles": {
    "Neutral": {
      "path": "neutral.wav",
      "prompt": "在这里填写这段录音实际说出的全部原文",
      "lang": "ja"
    }
  }
}
```

如果参考录音是日语，`lang` 用 `ja`；`prompt` 必须换成那段日语原文，不是要让模型朗读的新句子。保留 `emotion_tts.enabled=true` 与 `upstream_url=http://127.0.0.1:9880`，其他配置不变。模型输出仍用 `text_lang=ja`。

4. 重新运行 SPP，打开 [TTS 状态](http://127.0.0.1:11435/tts/status)，检查 Neutral 与实际路径。其他默认情绪的 WAV 缺失可以回落到 Neutral，但这不代表已具备完整情绪声线。

SPP 源码会合并默认 profiles，因此删掉其他情绪的 JSON 项不等于关闭所有默认检查。安装排查时，以自己的 Neutral 是否有效、实际合成是否成功为准。

### A5. 实际合成测试

浏览器打开 [GPT-SoVITS API 文档](http://127.0.0.1:9880/docs)。若该整合包提供此页，在 `POST /tts` 中点“Try it out”，填：

```json
{
  "text": "こんにちは。",
  "text_lang": "ja",
  "ref_audio_path": "D:/LofiMOD/voice/refs/neutral.wav",
  "prompt_text": "替换为录音中的日语原文",
  "prompt_lang": "ja",
  "media_type": "wav",
  "streaming_mode": false
}
```

执行后应得到能播放的 WAV。若返回 JSON 错误，先修复其指出的模型、音频或语言问题。

再检查 SPP 转发。在任意文件夹的地址栏输入 `powershell`，回车，执行下面的本地请求（会在当前文件夹创建 `spp-test.wav`）：

```powershell
$satoneBody = @{ text = '[Neutral] こんにちは。'; text_lang = 'ja'; media_type = 'wav'; streaming_mode = $false } | ConvertTo-Json
Invoke-WebRequest -Uri 'http://127.0.0.1:11435/tts' -Method Post -ContentType 'application/json; charset=utf-8' -Body ([System.Text.Encoding]::UTF8.GetBytes($satoneBody)) -OutFile '.\spp-test.wav'
```

播放这个 WAV。两层均成功后，再回到游戏发一句文字。游戏 TTS URL 应为 `http://127.0.0.1:11435`。

这些 TTS 测试使用本地语音服务，不请求主聊天模型。首次加载较慢；仍要以实际成功或错误为准，不把一直等待描述为已安装成功。

## B. 让聪音听懂麦克风

### B1. 准备独立 Python 环境

下面是需新 Windows 实测的手动安装路线。不会使用 Git 命令，也不建议为了安装 ASR 去升级 GPT-SoVITS 自带的 Python 依赖。

1. 从 [Python 官网](https://www.python.org/downloads/windows/)安装 **Python 3.12 的 64 位运行环境**，包含 Python 启动器。本文用 `py -3.12` 指定它；若提示找不到该版本，先完成 Python 安装，不要继续。
2. 新建 `D:\LofiMOD\AI\FunASR-Runtime`。在此文件夹地址栏输入 `cmd`，回车。以下命令使用 **命令提示符 CMD**，一行一行执行：

```bat
py -3.12 -m venv .venv
.venv\Scripts\python.exe -m pip install --upgrade pip
```

应出现 `.venv\Scripts\python.exe`。

### B2. 安装后端依赖

1. 打开 [Fun-ASR 官方仓库](https://github.com/QwenAudio/Fun-ASR)，点击 Code → Download ZIP，解压到 `D:\LofiMOD\AI\Fun-ASR-source`，确保其内部直接有 `requirements.txt`。此处下载源码是为了取上游运行依赖，和不能把 Mod 源码当成 DLL 安装包并不矛盾。
2. 在 [PyTorch 官方选择器](https://pytorch.org/get-started/locally/)选择 Windows、Pip、Python，以及与你显卡驱动兼容的计算平台。按照页面提供的命令安装 **torch 和 torchaudio**，将其开头 `pip`/`pip3` 改成 `.venv\Scripts\python.exe -m pip`，保证装进刚建的环境。
3. 与[上游 requirements.txt](https://github.com/QwenAudio/Fun-ASR/blob/main/requirements.txt)核对：本次读取要求 `torch>=2.9.0`、`torchaudio>=2.9.0`、`transformers>=4.51.3`、`funasr>=1.3.26` 等。若选择器显示更旧的缓存版本，不能把它当成满足要求。torch 与 torchaudio 也应互相匹配。
4. 在刚才的 CMD 中继续：

```bat
.venv\Scripts\python.exe -m pip install -r "D:\LofiMOD\AI\Fun-ASR-source\requirements.txt"
.venv\Scripts\python.exe -m pip install huggingface_hub
.venv\Scripts\python.exe -c "import torch,torchaudio,funasr; print(torch.__version__,torchaudio.__version__); print('CUDA available:',torch.cuda.is_available())"
```

**成功标志：** 导入无错误；计划用 NVIDIA GPU 时 CUDA available 应为 True。出现 False 不能算 GPU 环境已安装成功。CPU、AMD 等路线需另外验证性能与兼容性。

上游依赖清单使用范围版本，不是本项目验证过的锁定环境。正式面向零基础玩家发布前，维护者应补上自己实测成功的完整版本清单/安装器；本草稿保留这一缺项，不虚构成功记录。

### B3. 下载完整模型

在同一个 CMD 窗口执行：

```bat
.venv\Scripts\python.exe -c "from huggingface_hub import snapshot_download; snapshot_download(repo_id='FunAudioLLM/Fun-ASR-Nano-2512', local_dir='D:/LofiMOD/AI/Fun-ASR-Nano-2512')"
```

这是把官方模型仓库完整下载到指定目录，使用 Hugging Face 官方 `snapshot_download` 方法。等下载完成，不要只手动保存一个 `model.pt`。模型根目录中应有 `config.yaml`、`configuration.json`、`model.pt`、`Qwen3-0.6B` 等内容。

当前 SPP 脚本使用 `from funasr import AutoModel`。`Fun-ASR-Nano-2512-hf`、GGUF、Faster Whisper 都不能只改文件夹名称就作为此脚本的替代品。

### B4. 交给 SPP 启动

1. 关闭 SPP，在 config.json 的 `asr` 中填写实际路径。标准布局也可留空让 SPP 自动发现，但第一次安装显式填写更便于核对：

```json
{
  "python": "D:/LofiMOD/AI/FunASR-Runtime/.venv/Scripts/python.exe",
  "model_path": "D:/LofiMOD/AI/Fun-ASR-Nano-2512",
  "server_script": "",
  "enabled": true,
  "auto_start": true,
  "upstream_url": "http://127.0.0.1:9881",
  "language": "auto"
}
```

此处仍是 **asr 内部字段示例**，不是整个配置。保留已有其他字段。`server_script` 留空时，当前 SPP 优先使用包内 `satone_funasr_server_v1.py`，不需要从旧教程另外找同名旧脚本。

2. 启动 SPP，等待模型加载，打开 [ASR 状态](http://127.0.0.1:11435/asr/status) 和 [后端健康页](http://127.0.0.1:9881/health)。
3. 核对 Python、model_path、server_script 都指向刚才配置的位置；后端应返回 `ok: true`。若看到热词信息，继续核对 `hotwords_supported` 或 SPP 状态中的 `hotwords_backend_supported`。
4. 如果 9881 已有旧服务，SPP 可能复用它；先关闭明确属于旧 ASR 的进程，再重试。不要为了腾端口结束不认识的系统进程。
5. 回到游戏，选好 Windows 麦克风，先 F8、后持续通话，详见[安装页](INSTALL.zh-CN.md)。

加载失败时查看 SPP 日志中的首次 Python 异常。不要把“装好了 pip 包”“创建了模型文件夹”当作模型已经成功加载。上游注册/远程模型代码与本地依赖是否匹配，也属于全新安装必须检查的环节。

## 三个本地端口

| 端口 | 服务 | 玩家要用的地址 |
|---|---|---|
| 11435 | SPP | 聊天 `/v1/chat/completions`；TTS 根地址；Dashboard/状态页 |
| 9880 | GPT-SoVITS | SPP 转发目标；API `/tts` |
| 9881 | Fun-ASR | SPP 转发目标；`/asr` 与 `/health` |

本教程都绑定本机地址，不需要设置路由器端口转发或把服务暴露到互联网。
