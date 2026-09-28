# 语音与麦克风设置

[返回安装步骤](INSTALL.zh-CN.md) · [下载清单](DOWNLOADS.zh-CN.md)

本文将“聪音发声”和“听懂玩家说话”分开设置。前者使用 GPT-SoVITS，后者使用 Fun-ASR；装好一个不会自动装好另一个。

**适用配对：AIChat 1.16.23 + SPP 5.8.26（2026-09-28）。** SPP ZIP 已有默认 `mayuri-voice/refs/MAY_1158_Neutral.wav`，基本朗读不必再下载或改名这段参考音频。已具备 GPT-SoVITS 程序与运行环境的玩家，只需另准备“孤独摇滚”声线的 GPT／SoVITS 权重并在服务中加载；麦克风仍需另装 Fun-ASR。以下 A6 表格用于**可选**的多情绪参考音频。

**先选择硬件路线：** 完整 GPU 语音暂建议 8 GB 显存起步、12 GB 或以上更有余量；这不是最低配置测试结果，依据和限制见[运行开销与显卡兼容说明](HARDWARE.zh-CN.md)。CUDA 路线面向兼容 NVIDIA 显卡。非 NVIDIA 玩家可以先用文字聊天；完整语音需要对应的 CPU 环境或另行验证的 GPU 后端，不能照抄 CUDA 安装步骤。CPU 语音的整套 Windows 实时体验尚未验收。

**Fun-ASR 当前不会被 SPP 强制设为 CPU。** 随包脚本没有传入 `device`，不能把 `embedding_device: "cpu"` 当成语音识别设置。需要明确选择 CPU 时，见 [B5](#b5-需要让-fun-asr-使用-cpu-时)。

**验证边界：** 下面根据当前 SPP/AIChat 源码与上游文档编写，尚未在没有开发环境的新 Windows 电脑上走完全部步骤。后藤一里模型链接与 Mayuri 的 26 项文件对应关系已经核实；GPU/驱动/Python 依赖组合和整套安装后的实际声音效果，仍需在干净环境验证。无法验证的部分不会写成“一键安装成功”。

## A. 让聪音发声

### A1. 安装 GPT-SoVITS

1. 打开[官方项目](https://github.com/RVC-Boss/GPT-SoVITS)和[官方整合包列表](https://huggingface.co/lj1995/GPT-SoVITS-windows-package/tree/main)。根据显卡与上游说明选择 Windows 包；非 NVIDIA 玩家需要上游支持的 CPU 环境，不能默认选择 CUDA 包。上游源码安装也提供 CPU 选项，但 Python 路径不一定是下文的 `runtime\python.exe`。本教程推荐后藤一里的 **v2ProPlus** 权重，所选整合包必须支持 v2ProPlus，并提供 `api_v2.py`。
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

本教程推荐的组合是：**使用《孤独摇滚》的后藤一里（Hitori Gotoh）v2ProPlus 模型权重，并使用 Mayuri 的参考 WAV 与对应日语台词。** 这两个来源承担不同作用；不需要再把 Mayuri 的模型权重混入后藤权重中。

| 资源 | 原发布页与下载 | 本地放置位置示例 |
|---|---|---|
| 后藤一里声线，作者 lpkpaco | [模型主页](https://huggingface.co/lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models)；[原作者项目说明](https://github.com/lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models)；[gotoh-v1-3-1 的 v2ProPlus 文件夹](https://huggingface.co/lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models/tree/main/models/Hitori_Gotoh/v2ProPlus/gotoh-v1-3-1) | 下面两个文件分别放入对应权重目录 |
| GPT 权重 | [gotoh-v1-3-1-e16.ckpt](https://huggingface.co/lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models/resolve/main/models/Hitori_Gotoh/v2ProPlus/gotoh-v1-3-1/GPT/gotoh-v1-3-1-e16.ckpt?download=true)（约 155 MB） | `GPT-SoVITS/GPT_weights_v2ProPlus/gotoh-v1-3-1-e16.ckpt` |
| SoVITS 权重 | [gotoh-v1-3-1_e8_s368.pth](https://huggingface.co/lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models/resolve/main/models/Hitori_Gotoh/v2ProPlus/gotoh-v1-3-1/SoVITS/gotoh-v1-3-1_e8_s368.pth?download=true)（约 173 MB） | `GPT-SoVITS/SoVITS_weights_v2ProPlus/gotoh-v1-3-1_e8_s368.pth` |
| Mayuri 参考音频，发布者 SteinsGateSg | [项目主页](https://huggingface.co/SteinsGateSg/mayuri-voice)；[refs 文件夹](https://huggingface.co/SteinsGateSg/mayuri-voice/tree/main/refs)；[选段索引](https://huggingface.co/SteinsGateSg/mayuri-voice/blob/main/refs/index.csv) | 默认 Neutral 已随 SPP 包附带；仅在自行补齐其他情绪时下载相应 WAV／TXT |

只需下载表中的两个后藤权重，不能因为文件同名就改去 v4 目录取权重，也无需下载整个多 GB 声线仓库。Mayuri 这里只使用 `refs`，不需要该仓库的 `models/gpt` 与 `models/sovits`。

核查时，后藤模型页标注 `cc-by-nc-sa-4.0`，Mayuri 模型页标注 `License: other`。外部资源按各自发布者说明使用；本 Mod 包附带默认 Neutral 参考音频，不附带声线权重或其余情绪音频。

后藤模型页在 “Hitori Gotoh” 下明确列出 “v2ProPlus models” 与 “gotoh-v1-3-1”。Mayuri 原说明写明参考库有 “matching text files”。这里推荐的是本项目采用的组合，不是两位发布者共同认证的配套方案；最终音色与情绪效果需要试听确认。

SPP 包含 `MAY_1158_Neutral.wav`；其他默认 `MAY_*.wav` 未包含。自行补齐其他情绪时可按 A6 表格命名，或在配置中填写真实相对路径。SPP 检查参考音频是否为可读取的标准 RIFF/WAVE、时长是否为 **3–10 秒**、台词是否非空。

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

使用上面推荐的两个后藤文件时，在已有 `custom:` 节内将这三项改为：

```yaml
version: v2ProPlus
t2s_weights_path: GPT_weights_v2ProPlus/gotoh-v1-3-1-e16.ckpt
vits_weights_path: SoVITS_weights_v2ProPlus/gotoh-v1-3-1_e8_s368.pth
```

这只是三个键的示例；请保持它们在 `custom:` 下原有的缩进，并保留基础模型等其他键。此处连接的是 GPT-SoVITS 自带 `api_v2.py`，无需运行声线作者仓库里的另一套 WebUI 或 API。

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

先使用包内的正常说话参考，其他情绪缺失时由它兜底。不要为第一轮安装准备几十个未经核对的情绪文件。

1. 在 SPP 完整包内确认 `mayuri-voice/refs/MAY_1158_Neutral.wav`。整包解压时不要打散目录。
2. 新安装请保留 `config.example.json` 中 `emotion_tts.ref_root` 的空值、`fallback_profile: "Neutral"` 和 `profiles.Neutral.path: "MAY_1158_Neutral.wav"`；SPP 会查找包内相对目录。不要将示例配置覆盖到已有个人 `config.json`。
3. 若旧 `config.json` 把 `emotion_tts.ref_root` 指向外部目录，退出 SPP 后将其清空，或改为包内 `mayuri-voice/refs` 的**实际绝对路径**。同时核对 Neutral 的 `path` 和 `prompt` 与包内音频匹配；默认模板已有对应日语台词。

```json
{
  "ref_root": "",
  "fallback_profile": "Neutral",
  "profiles": {
    "Neutral": {
      "path": "MAY_1158_Neutral.wav",
      "prompt": "嫌がってるのに無理やり着せたりしてねトラウマになっちゃったら良くないもん。",
      "lang": "ja"
    }
  }
}
```

这只是 `emotion_tts` 内相关字段的结构示例，不要覆盖整份配置。自己更换录音时，`prompt` 必须同步改为那段音频实际说出的原文；若使用同名 TXT，也可把 `prompt` 设为 `""`。保留 `emotion_tts.enabled=true` 与 `upstream_url=http://127.0.0.1:9880`，模型输出仍用 `text_lang=ja`。

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

### A6. 完整配置 26 种情绪：文件究竟应该叫什么

**SPP 根据 `emotion_tts.mapping` 和 `emotion_tts.profiles` 找文件，不会扫描文件名猜测情绪。** 当前默认关系是一对一，例如 `Happy → profiles.Happy → path`。文件名本身可以自定义，但必须与该 `path` 一致。直接把某个文件改成 `开心.wav`，却保留旧 `path`，程序就找不到它。

下面列的是 **SPP 5.8.26 的 `config.example.json` 与 `profiles_26.csv` 中的默认名称**。Neutral 已随包提供；其余情绪音频是可选的自行补充。上游的 `worried`、`teasing` 等分类不等于 SPP 的 26 个标签；表格不保证每个片段都能完美表现对应情绪。

#### 按默认命名准备文件

1. Neutral 已经在包内；需要更多情绪时，再打开对应 WAV／TXT 链接，保存真正的音频与文本，不要将网页另存后伪装成 WAV。
2. 把新增文件放进 SPP 包内 `mayuri-voice/refs`，按最后一列命名。若使用 TXT，名称与 WAV 相同，仅扩展名改为 `.txt`。
3. 同一个上游片段被用于两个标签时，需要复制两份再分别命名；不要反复改名导致前一个文件消失。本表使用 24 段不同录音形成 26 个配置项，配置项数量不代表拥有 26 段不同录音。
4. 保留默认的 `mapping`、26 个 `profiles`、`fallback_profile: "Neutral"` 和空 `ref_root`；如果旧配置已指向外部目录，请改向实际放置音频的目录。不要用完整默认配置覆盖自己的其他设置。

| 标签，按此拼写 | 中文含义 | Mayuri 原文件与下载 | 复制到 refs 后的默认文件名 |
|---|---|---|---|
| `Neutral` | 平静/无明显情绪 | [worried/MAY_1158.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/worried/MAY_1158.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/worried/MAY_1158.txt?download=true) | `MAY_1158_Neutral.wav` |
| `Happy` | 开心/愉快 | [teasing/MAY_0336.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/teasing/MAY_0336.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/teasing/MAY_0336.txt?download=true) | `MAY_0336_Happy.wav` |
| `Excited` | 兴奋/激动 | [excited/MAY_0279.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/excited/MAY_0279.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/excited/MAY_0279.txt?download=true) | `MAY_0279_Excited.wav` |
| `Relaxed` | 放松/安心 | [serious/MAY_0046.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/serious/MAY_0046.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/serious/MAY_0046.txt?download=true) | `MAY_0046_Relaxed.wav` |
| `Sad` | 悲伤/低落 | [sad/MAY_0160.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/sad/MAY_0160.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/sad/MAY_0160.txt?download=true) | `MAY_0160_Sad.wav` |
| `Crying` | 哭泣/哽咽 | [serious/MAY_1382.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/serious/MAY_1382.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/serious/MAY_1382.txt?download=true) | `MAY_1382_Crying.wav` |
| `Pouting` | 委屈/赌气 | [embarrassed/MAY_0030.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/embarrassed/MAY_0030.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/embarrassed/MAY_0030.txt?download=true) | `MAY_0030_Pouting.wav` |
| `Tired` | 疲惫/没精神 | [gentle/MAY_1311.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/gentle/MAY_1311.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/gentle/MAY_1311.txt?download=true) | `MAY_1311_Tired.wav` |
| `Sleepy` | 困倦/半梦半醒 | [other/MAY_0529.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/other/MAY_0529.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/other/MAY_0529.txt?download=true) | `MAY_0529_Sleepy.wav` |
| `Angry` | 生气/愤怒 | [teasing/MAY_0355.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/teasing/MAY_0355.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/teasing/MAY_0355.txt?download=true) | `MAY_0355_Angry.wav` |
| `Chiding` | 责怪/轻斥/数落 | [serious/MAY_0575.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/serious/MAY_0575.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/serious/MAY_0575.txt?download=true) | `MAY_0575_Chiding.wav` |
| `Nervous` | 紧张/不安 | [worried/MAY_0035.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/worried/MAY_0035.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/worried/MAY_0035.txt?download=true) | `MAY_0035_Nervous.wav` |
| `Afraid` | 害怕/恐惧 | [worried/MAY_0512.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/worried/MAY_0512.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/worried/MAY_0512.txt?download=true) | `MAY_0512_Afraid.wav` |
| `Confused` | 困惑/不解 | [embarrassed/MAY_0170.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/embarrassed/MAY_0170.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/embarrassed/MAY_0170.txt?download=true) | `MAY_0170_Confused.wav` |
| `Curious` | 好奇/感兴趣 | [embarrassed/MAY_0170.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/embarrassed/MAY_0170.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/embarrassed/MAY_0170.txt?download=true) | `MAY_0170_Curious.wav` |
| `Think` | 思考/斟酌 | [serious/MAY_0328.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/serious/MAY_0328.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/serious/MAY_0328.txt?download=true) | `MAY_0328_Think.wav` |
| `Surprised` | 惊讶/意外 | [serious/MAY_1464.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/serious/MAY_1464.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/serious/MAY_1464.txt?download=true) | `MAY_1464_Surprised.wav` |
| `Shocked` | 震惊/强烈惊愕 | [teasing/MAY_0201.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/teasing/MAY_0201.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/teasing/MAY_0201.txt?download=true) | `MAY_0201_Shocked.wav` |
| `Shy` | 害羞/不好意思 | [gentle/MAY_0838.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/gentle/MAY_0838.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/gentle/MAY_0838.txt?download=true) | `MAY_0838_Shy.wav` |
| `Affectionate` | 亲昵/撒娇 | [gentle/MAY_1410.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/gentle/MAY_1410.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/gentle/MAY_1410.txt?download=true) | `MAY_1410_Affectionate.wav` |
| `Playful` | 调皮/玩闹 | [teasing/MAY_0336.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/teasing/MAY_0336.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/teasing/MAY_0336.txt?download=true) | `MAY_0336_Playful.wav` |
| `Teasing` | 调侃/逗弄 | [happy/MAY_1063.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/happy/MAY_1063.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/happy/MAY_1063.txt?download=true) | `MAY_1063_Teasing.wav` |
| `Mocking` | 嘲笑/挖苦 | [neutral/MAY_0939.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/neutral/MAY_0939.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/neutral/MAY_0939.txt?download=true) | `MAY_0939_Mocking.wav` |
| `Sarcastic` | 反讽/冷嘲 | [excited/MAY_1428.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/excited/MAY_1428.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/excited/MAY_1428.txt?download=true) | `MAY_1428_Sarcastic.wav` |
| `Smug` | 得意/自满/故意自傲 | [neutral/MAY_0485.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/neutral/MAY_0485.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/neutral/MAY_0485.txt?download=true) | `MAY_0485_Smug.wav` |
| `Disagree` | 反对/不赞同 | [neutral/MAY_0053.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/neutral/MAY_0053.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/neutral/MAY_0053.txt?download=true) | `MAY_0053_Disagree.wav` |

标签使用上表英文原样拼写，特别注意 **`Think`、`Surprised`、`Disagree`**，不要换成 `Thinking`、`Surprise` 或中文。保持 Windows 文件扩展名可见，避免出现 `.wav.wav` 或 `.txt.txt`。

#### 台词如何填写，以及为什么放了 TXT 仍可能不对

当前原包内的 26 条默认 `prompt` 与本次核对的 Mayuri 索引台词相同。使用表中同一段音频时可以保留这些默认台词；如果换了录音，必须同步修改，不能只改文件名。

读取优先顺序是：**先读配置中非空的 `prompt`；只有 `prompt` 为空时，才读 WAV 旁边同名的 `.txt`。** [SPP 5.8.23 源码](https://github.com/Scaleph-Enkidu/SatonePromptProxy/blob/916c61a71973f825266be7140d84c45afbd6bcaa/main.go)原文如下（源码仓库需要访问权限）：

```go
if strings.TrimSpace(profile.Prompt) != "" {
    return strings.TrimSpace(profile.Prompt)
}
txt := strings.TrimSuffix(absWav, filepath.Ext(absWav)) + ".txt"
```

这是函数中的两段原文，中间省略了空路径判断。如果希望按同名 TXT 读取，将对应情绪的 `prompt` 设为 `""`；TXT 保存为 UTF-8，内容应是该 WAV 实际说出的日语原文，仍需试听核对。`lang` 使用 `ja`。例如，仅修改 `profiles` 下已有的 Neutral 项：

```json
"Neutral": {
  "path": "MAY_1158_Neutral.wav",
  "prompt": "",
  "lang": "ja"
}
```

另一种方法是保留上游目录和原名：例如完整下载 `refs` 后，把 `ref_root` 指向它，令 `profiles.Neutral.path` 为 `worried/MAY_1158.wav`，并将 `prompt` 留空以读取旁边的 `MAY_1158.txt`。两种方法都可以，但不能混用文件名却忘了修改路径。SPP 不会读取 `profiles_26.csv` 自动改写配置，修改 CSV 本身不会生效。

#### 如何确认已被调用

重新启动 SPP，检查 [TTS 状态](http://127.0.0.1:11435/tts/status)中的 `mapping`、`profiles` 与 `validation`，以及启动日志的 Voice Profile 自检。26 个默认项都配置正确时，应显示正常 26、异常 0。再用 A5 的 SPP 请求将 `[Neutral]` 改为 `[Happy]`、`[Sad]` 等分别试听；这些本地 TTS 测试不调用主聊天 API。

某个现有配置的 WAV 缺失、时长不符或台词为空时，SPP 会尝试回退到可用的 Neutral；因此“能发声”不证明那个情绪文件已被使用。Neutral 本身也坏了，就无法靠回退解决。文件自检通过也不保证 26 种听感都有明显区别。

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
2. 在 [PyTorch 官方选择器](https://pytorch.org/get-started/locally/)选择 Windows、Pip、Python。NVIDIA GPU 路线选择兼容驱动的 CUDA 平台；非 NVIDIA 玩家或希望识别使用 CPU 的玩家选择 CPU，不能照抄 CUDA 的安装命令。按照页面提供的命令安装 **torch 和 torchaudio**，将其开头 `pip`/`pip3` 改成 `.venv\Scripts\python.exe -m pip`，保证装进刚建的环境。
3. 与[上游 requirements.txt](https://github.com/QwenAudio/Fun-ASR/blob/main/requirements.txt)核对：本次读取要求 `torch>=2.9.0`、`torchaudio>=2.9.0`、`transformers>=4.51.3`、`funasr>=1.3.26` 等。若选择器显示更旧的缓存版本，不能把它当成满足要求。torch 与 torchaudio 也应互相匹配。
4. 在刚才的 CMD 中继续：

```bat
.venv\Scripts\python.exe -m pip install -r "D:\LofiMOD\AI\Fun-ASR-source\requirements.txt"
.venv\Scripts\python.exe -m pip install huggingface_hub
.venv\Scripts\python.exe -c "import torch,torchaudio,funasr; print(torch.__version__,torchaudio.__version__); print('CUDA available:',torch.cuda.is_available())"
```

**依赖检查：** 导入无错误；计划使用 NVIDIA GPU 时 `CUDA available` 应为 `True`。明确安装 CPU 环境时返回 `False` 是正常的，不能因此判为安装失败。这个值只说明 CUDA 是否可用，不证明模型已经运行在 GPU／CPU；仍须完成模型加载、实际识别和设备核对。AMD／Intel GPU 路线不在本教程已验证范围内。

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

### B5. 需要让 Fun-ASR 使用 CPU 时

**这是需要实测的手动适配方法，不是已发布的 CPU 模式开关。** 当前 SPP 5.8.26 没有 `asr.device` 配置字段；向 JSON 中添加这个字段不会改变设备。已有可用环境请先保留原脚本与 `asr.server_script` 值，不要在 GPT-SoVITS 环境中直接改装 ASR 依赖。

1. 按 B1／B2 建立独立环境；如果目标就是 CPU，选择 CPU 版 PyTorch。保留与当前 `Fun-ASR-Nano-2512`、`funasr.AutoModel` 路线相符的依赖，不能直接替换为 HF／GGUF 模型。
2. 关闭 SPP 与已确认的旧 ASR 服务，将包内 `satone_funasr_server_v1.py` 复制到自己的 ASR 目录，命名为 `satone_funasr_server_cpu_v1.py`，只将模型初始化这一行改为：

   ```python
   model = AutoModel(model=model_dir, trust_remote_code=True, device="cpu")
   ```

   原行没有 `device` 参数。保留其余代码和缩进，尤其是热词、UTF-8 和 HTTP 接口逻辑。

3. 将 SPP `config.json` 内的 `asr.server_script` 改为这份副本的完整路径，例如 `D:/LofiMOD/AI/FunASR-Runtime/satone_funasr_server_cpu_v1.py`；`asr.python` 指向对应独立环境。此处是既有字段，不能改错为根级字段。
4. 重新启动。检查 `/asr/status` 的解析脚本路径确实是副本，确认 9881 没有复用原 GPU 服务；再检查 `/health` 并用 F8 实际识别中日文短句。健康页返回成功不代表设备和性能已验证，当前健康页也没有报告模型设备。
5. 对比该 ASR 进程及整卡显存的启动前后读数，再测试较长音频和持续通话。记录 CPU、内存、识别延迟与失败情况。CPU 模式可能增加延迟；若依赖报错或超过超时，需要修复后才能列为兼容。

回退时先停服务，再恢复原 `asr.server_script` 和环境路径。后续升级随包脚本时，需将修复同步到自己的副本，不能一直保留旧接口实现。

若 TTS 也要使用 CPU，需在 GPT-SoVITS 的实际 `custom:` 节另设 `device: cpu`、`is_half: false`，保持声线版本和权重正确，并重启它的 API；改变 ASR 不会改变 TTS。先完成 A 部分单独合成，再验证游戏内延迟。上游支持 CPU 配置不等于当前整合包和声线组合已经通过本项目测试。

## 三个本地端口

| 端口 | 服务 | 玩家要用的地址 |
|---|---|---|
| 11435 | SPP | 聊天 `/v1/chat/completions`；TTS 根地址；Dashboard/状态页 |
| 9880 | GPT-SoVITS | SPP 转发目标；API `/tts` |
| 9881 | Fun-ASR | SPP 转发目标；`/asr` 与 `/health` |

本教程都绑定本机地址，不需要设置路由器端口转发或把服务暴露到互联网。
