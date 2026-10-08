[简体中文](VOICE_SETUP.md) | [English](../en/VOICE_SETUP.md) | [日本語](../ja/VOICE_SETUP.md)

# 语音进阶与排错

[返回四阶段安装](INSTALL.md) · [下载清单](DOWNLOADS.md) · [硬件参考](HARDWARE.md)

**适用配对：AIChat 1.18.30 + SPP 5.10.10。** 第一次安装请按主教程逐步完成：

<a id="stage-3"></a>

[③ 让聪音读出回复：GPT-SoVITS 完整安装](INSTALL.md#stage-3)

<a id="stage-4"></a>

[④ 让聪音听懂你的话：Fun-ASR 完整安装](INSTALL.md#stage-4)

下面用于基本功能完成后的扩展和排错。GPT-SoVITS（文字变语音）与 Fun-ASR（语音变文字）分别安装，互不依赖；ONNX 也不是它们的前置条件。主程序包已有默认 Neutral 参考录音，GPT-SoVITS 环境、声线权重以及 ASR 环境／模型仍需外装。

**设备设置的位置：** TTS 在 GPT-SoVITS 的 tts_infer.yaml 里选择 device 与 is_half；Fun-ASR 的 CPU 路线使用带 device="cpu" 的脚本副本，并由 SPP 的 asr.server_script 指向它。CPU 的必需步骤已放在[主教程阶段四](INSTALL.md#asr-cpu)，无需在本页另找安装步骤，也不要向 SPP 添加不存在的 asr.device 字段。

2026-10-01 用户确认本机测试完成。这是已有测试的确认记录；本轮文档列出的完整新装依赖组合仍须以实际模型加载、朗读和 F8 识别确认，不扩展为全部硬件／声线／供应商组合已验收。

## 三个本地端口

| 端口 | 服务 | 用途 |
|---|---|---|
| 11435 | SPP | AIChat 共用语音地址；/tts、/asr 与状态页 |
| 9880 | GPT-SoVITS API | SPP 的 TTS 转发目标 |
| 9881 | Fun-ASR | SPP 的 ASR 转发目标；/health 健康页 |

游戏里的**语音服务地址（默认连接 SPP 的 TTS 与 ASR 代理）：**保持 http://127.0.0.1:11435。服务绑定本机地址，无需路由器端口转发。

<a id="voice-sources"></a>
> **关于聪音的其他语言发音**：由于聪音是日本人，所以其他语言说得不太好，尤其是英语，经常无法发音；推荐玩家尝试别的模型进行测试。

## 声线、参考音频与原作者来源

### 三种资源各负责什么

| 内容 | 作用 | 如何取得 |
|---|---|---|
| 基础预训练权重与文本模型 | 让 GPT-SoVITS 能运行 | 整合包自带或从[官方模型仓库](https://huggingface.co/lj1995/GPT-SoVITS/tree/main)补齐 |
| 特定声线的 GPT `.ckpt` / SoVITS `.pth` | 采用某个训练后的声音 | 从声线作者原发布页下载，并核对它针对 v2、v2Pro、v2ProPlus 等哪一版 |
| 参考 `.wav` 与准确台词 | 为一次合成提供发声参考 | 自己录制或取得有明确使用许可的音频 |

本项目现有示例组合是：**使用《孤独摇滚》的后藤一里（Hitori Gotoh）v2ProPlus 模型权重，并使用 Mayuri 的参考 WAV 与对应日语台词。** 这两个来源承担不同作用；不需要再把 Mayuri 的模型权重混入后藤权重中。

| 资源 | 原发布页与下载 | 本地放置位置示例 |
|---|---|---|
| 后藤一里声线，作者 lpkpaco | [模型主页](https://huggingface.co/lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models)；[原作者项目说明](https://github.com/lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models)；[gotoh-v1-3-1 的 v2ProPlus 文件夹](https://huggingface.co/lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models/tree/main/models/Hitori_Gotoh/v2ProPlus/gotoh-v1-3-1) | 下面两个文件分别放入对应权重目录 |
| GPT 权重 | [gotoh-v1-3-1-e16.ckpt](https://huggingface.co/lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models/resolve/main/models/Hitori_Gotoh/v2ProPlus/gotoh-v1-3-1/GPT/gotoh-v1-3-1-e16.ckpt?download=true)（约 155 MB） | `GPT-SoVITS/GPT_weights_v2ProPlus/gotoh-v1-3-1-e16.ckpt` |
| SoVITS 权重 | [gotoh-v1-3-1_e8_s368.pth](https://huggingface.co/lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models/resolve/main/models/Hitori_Gotoh/v2ProPlus/gotoh-v1-3-1/SoVITS/gotoh-v1-3-1_e8_s368.pth?download=true)（约 173 MB） | `GPT-SoVITS/SoVITS_weights_v2ProPlus/gotoh-v1-3-1_e8_s368.pth` |
| Mayuri 参考音频，发布者 SteinsGateSg | [项目主页](https://huggingface.co/SteinsGateSg/mayuri-voice)；[refs 文件夹](https://huggingface.co/SteinsGateSg/mayuri-voice/tree/main/refs)；[选段索引](https://huggingface.co/SteinsGateSg/mayuri-voice/blob/main/refs/index.csv) | 默认 Neutral 已随 SPP 包附带；仅在自行补齐其他情绪时下载相应 WAV／TXT |

只需下载表中的两个后藤权重，不能因为文件同名就改去 v4 目录取权重，也无需下载整个多 GB 声线仓库。Mayuri 这里只使用 `refs`，不需要该仓库的 `models/gpt` 与 `models/sovits`。

核查时，后藤模型页标注 `cc-by-nc-sa-4.0`，Mayuri 模型页标注 `License: other`。外部资源按各自发布者说明使用；本 Mod 包附带默认 Neutral 参考音频，不附带声线权重或其余情绪音频。

后藤模型页在 “Hitori Gotoh” 下明确列出 “v2ProPlus models” 与 “gotoh-v1-3-1”。Mayuri 原说明写明参考库有 “matching text files”。这里列出的是本项目采用的组合，不是两位发布者共同认证的配套方案；最终音色与情绪效果需要试听确认。

SPP 包含 `MAY_1158_Neutral.wav`；其他默认 `MAY_*.wav` 未包含。自行补齐其他情绪时可按下方 26 情绪表格命名，或在配置中填写真实相对路径。SPP 检查参考音频是否为可读取的标准 RIFF/WAVE、时长是否为 **3–10 秒**、台词是否非空。


<a id="tts-test"></a>
## 单独试听，区分 TTS 两层服务

完成[阶段三](INSTALL.md#stage-3)后，可以用下面方法定位“API 启动了但游戏没有声音”的原因。两项测试使用本地语音服务，不请求主聊天模型。

### 先测试 GPT-SoVITS 本身

1. 保持 run_api.bat 的窗口运行，用浏览器打开 [GPT-SoVITS API 文档](http://127.0.0.1:9880/docs)。
2. 展开 **POST /tts**，点 **Try it out**。将请求框原有内容全选，替换为：

~~~json
{
  "text": "こんにちは。",
  "text_lang": "ja",
  "ref_audio_path": "D:/LofiMOD/SatonePromptProxy/mayuri-voice/refs/MAY_1158_Neutral.wav",
  "prompt_text": "嫌がってるのに無理やり着せたりしてねトラウマになっちゃったら良くないもん。",
  "prompt_lang": "ja",
  "media_type": "wav",
  "streaming_mode": false
}
~~~

3. 点 **Execute**，等待完成。应返回 200 和音频响应；点响应中的 **Download file** 下载后，用播放器播放 WAV。若返回 JSON 错误，先看 message／Exception，修复其指出的模型、路径或语言问题。
4. 9880/docs 打不开时，先检查 API 窗口是否报错退出，以及是否显示监听 127.0.0.1:9880。go-webui.bat 打开的推理网页是另一进程，不能代替 API 就绪。

### 再测试 SPP 转发

1. 启动 SPP。在资源管理器中打开 D:\LofiMOD\SatonePromptProxy，在地址栏输入 powershell，按回车。本小节使用 **PowerShell**，与安装 ASR 时的 CMD 不同。
2. 逐行执行：

~~~powershell
$satoneBody = @{ text = '[Neutral] こんにちは。'; text_lang = 'ja'; media_type = 'wav'; streaming_mode = $false } | ConvertTo-Json
Invoke-WebRequest -Uri 'http://127.0.0.1:11435/tts' -Method Post -ContentType 'application/json; charset=utf-8' -Body ([System.Text.Encoding]::UTF8.GetBytes($satoneBody)) -OutFile 'D:\LofiMOD\SatonePromptProxy\spp-test.wav'
~~~

3. 双击生成的 spp-test.wav，确认能播放。之后把上面的 [Neutral] 换成已补齐的 [Happy]／[Sad] 等，可逐项试听。保留文字中的英文方括号和标签拼写。
4. 两层均成功后再回游戏：F9 → **展开设置 → TTS（文字转语音）**，核对朗读语言 ja、音量大于 0，点**保存并应用配置**，发一句文字并听朗读。默认共用语音地址保持 11435。

<a id="emotions-26"></a>
## 可选：补齐 26 种情绪参考音频
### 文件名和配置如何对应

**SPP 根据 `emotion_tts.mapping` 和 `emotion_tts.profiles` 找文件，不会扫描文件名猜测情绪。** 当前默认关系是一对一，例如 `Happy → profiles.Happy → path`。文件名本身可以自定义，但必须与该 `path` 一致。直接把某个文件改成 `开心.wav`，却保留旧 `path`，程序就找不到它。

下面列的是 **SPP 5.9.1 的 `config.example.json` 与 `profiles_26.csv` 中的默认名称**。Neutral 已随包提供；其余情绪音频是可选的自行补充。上游的 `worried`、`teasing` 等分类不等于 SPP 的 26 个标签；表格不保证每个片段都能完美表现对应情绪。

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

读取优先顺序是：**先读配置中非空的 `prompt`；只有 `prompt` 为空时，才读 WAV 旁边同名的 `.txt`。** 读取逻辑如下：

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

重新启动 SPP，检查 [TTS 状态](http://127.0.0.1:11435/tts/status)中的 `mapping`、`profiles` 与 `validation`，以及启动日志的 Voice Profile 自检。26 个默认项都配置正确时，应显示正常 26、异常 0。再用 上方“单独试听”中的 SPP 请求将 `[Neutral]` 改为 `[Happy]`、`[Sad]` 等分别试听；这些本地 TTS 测试不调用主聊天 API。

某个现有配置的 WAV 缺失、时长不符或台词为空时，SPP 会尝试回退到可用的 Neutral；因此“能发声”不证明那个情绪文件已被使用。Neutral 本身也坏了，就无法靠回退解决。文件自检通过也不保证 26 种听感都有明显区别。


<a id="tts-troubleshooting"></a>
## TTS 常见问题

| 现象 | 先做什么 |
|---|---|
| run_api.bat 双击后显示错误并停在“请按任意键继续” | 保留窗口，读最先出现的 Traceback；按阶段三核对 runtime\python.exe、两份后藤权重与基础模型的实际位置 |
| 显示 fall back to default t2s_weights_path／vits_weights_path | 配置路径没有找到文件；修正 tts_infer.yaml 和对应文件位置，重启 API，确认启动输出采用后藤权重 |
| GPU 配置出现 CUDA is not available | 更新对应 NVIDIA 驱动，检查是否选了正确整合包；需要 CPU 时用阶段三完整 CPU YAML |
| SPP 找不到 Neutral，或者没有可回退的录音 | 打开 /tts/status，核对 validation.Neutral.valid 为 true、resolved_path 指向包内 WAV；再按阶段三的旧配置纠正步骤处理 |
| 只听见一种情绪 | 主包只附带 Neutral；其他文件缺失时会回落到 Neutral。按本页表格补充后逐项试听 |
| WAV 能播放，游戏却无声 | 核对游戏 TTS 朗读音量、Windows 音量混合器中游戏音量，以及是否点了保存并应用配置 |
| API 显示地址已被占用 | 关闭自己先前启动的 9880 API 窗口，再运行一份；不要同时启动多套 API |
| WebUI 已换声线，游戏仍读旧声线 | 编辑真正由 run_api.bat 读取的 tts_infer.yaml，重启 API；WebUI 模型选择不会改另一个进程 |
| CPU 合成很慢 | 先用短句完成一次实际合成，再评估游戏等待时间；降低音量或修改 ONNX 设置不会加速 TTS |

SPP 日志在 D:\LofiMOD\SatonePromptProxy\SatonePromptProxy_v5.10.10.log。GPT-SoVITS 的模型和合成异常则先看 run_api.bat 窗口。排错时保留**第一条错误及完整文件路径**，比只截最后一行更有用。

### 可选：用包内脚本联动启动

D:\LofiMOD\SatonePromptProxy 中的 Set_GPTSoVITS_RunApi_Path.bat 可记录 TTS 启动位置：

1. 双击它，输入 D:\LofiMOD\GPT-SoVITS\run_api.bat 的完整路径，回车，确认出现 [OK] Saved。
2. 在游戏 F9 → **展开设置 → TTS（文字转语音） → TTS 启动脚本路径：**填 D:\LofiMOD\SatonePromptProxy\Start_AIChat_Services.bat。
3. 勾选**启动游戏时自动运行 TTS 服务**，点**保存并应用配置**，下次启动游戏验证。

它读取 service_paths.ini，启动 SPP 与已配置的 GPT-SoVITS API。脚本不会安装环境或权重；这些需先按主教程完成。直接使用阶段三的 run_api.bat 路径也可以。

<a id="asr-cpu"></a>
<a id="asr-troubleshooting"></a>
## ASR 常见问题与诊断

CPU 的首次安装步骤见[主教程 CPU 分支](INSTALL.md#asr-cpu)。这里只处理功能完成后的排错和调整。

| 现象 | 先做什么 |
|---|---|
| Python／py 找不到 | 按阶段四安装完整 Python 3.12 x64 与启动器；安装后关闭旧 CMD，重新在 FunASR-Runtime 地址栏打开 CMD |
| pip 或导入报错 | 使用独立环境的 .venv\Scripts\python.exe 执行阶段四原命令，先让 pip check 与 import 检查通过 |
| model.pt 存在但模型加载失败 | 核对完整模型目录，尤其 configuration.json、config.yaml、multilingual.tiktoken 与 Qwen3-0.6B 内实际文件；重新执行完整 snapshot_download |
| CPU 路线仍连着旧服务 | 停止自己先前手动启动的 9881 服务，再重启 SPP；检查 /asr/status 的 server_script 确实指向 CPU 副本 |
| /asr/status 的 ready 一直为 false | 查看 last_error 与 SPP 日志的第一条 Python 错误；目录存在或 pip 安装成功不能替代模型加载 |
| /health 返回 ok，但 F8 没文字 | 核对 Windows 麦克风权限，在游戏持续通话设置中选择实际麦克风并保存；先说一条短句 |
| F8 识别正常，持续通话容易漏头／截断 | 用下面的本地录音测试检查输入，再逐项调整 VAD；VAD 是“何时开始／结束录音”的判断 |
| 服务显示就绪，但识别延迟较长 | 先比较同一短句在当前 CPU／GPU 上的等待；记录设备、句长与耗时，再评估持续通话 |
| 没装 TTS，找不到 ASR 地址设置 | 共用地址在游戏 TTS（文字转语音）设置中，默认 11435；选麦克风在持续通话设置中 |

### 麦克风与说话检测

F9 → **展开设置 → 持续通话**中已有下列诊断功能：

- **选择麦克风（按住说话与持续通话共用）**：点击实际设备，再点保存并应用配置。
- **麦克风测试：安静录音 10 秒／说话录音 10 秒**：两次测试分别保留背景噪声和说话样本，仅保存本机，不送入 ASR；完成后停止监听。
- **保存下一次按住说话的原始录音（仍正常识别）**：用于区分原录音漏字和识别误差。
- **临时试用阈值 0.0005（保存后生效，停止通话后恢复）**：作为可回退的检测尝试；先保存再试听／观察，不要一次改动多个参数。

先让 F8 短句识别正常，再调整持续通话。起声阈值太高会漏掉轻声，太低会把背景噪声当说话；说完后的停顿决定何时送去识别。修改参数后点**保存并应用配置**，等当前发言结束后再测试。

### 热词、服务状态与升级

打开 [SPP ASR 状态](http://127.0.0.1:11435/asr/status)与[后端健康页](http://127.0.0.1:9881/health)，分别查看 ready、python、server_script、model_path，以及 hotwords_backend_supported／hotwords_supported。热词支持信息是接口能力，不保证每个词都识别正确；实际仍要用 F8 说出相关词核对。

健康页不报告模型设备。CPU 用户以明确的 device="cpu" 脚本副本、SPP 解析到的 server_script 和实际识别来核对自己的路线。更新 SPP 后，把新随包脚本的修复同步到 CPU 副本，再保留这一项设备参数；不要长期保留旧接口代码。

在 D:\LofiMOD\FunASR-Runtime 地址栏打开 CMD，下面命令可把实际环境版本保存为 asr-environment.txt，供自己回退或排错：

~~~bat
.venv\Scripts\python.exe -m pip freeze > asr-environment.txt
~~~

### 官方运行依据

- [Fun-ASR 运行依赖](https://github.com/QwenAudio/Fun-ASR/blob/main/requirements.txt)列出 torch／torchaudio ≥ 2.9.0、transformers ≥ 4.51.3 与 funasr ≥ 1.3.26。
- [PyTorch 历史版本页](https://pytorch.org/get-started/previous-versions/)提供 2.9.1 的 CPU／CUDA 12.8 对应安装命令。
- [官方 Fun-ASR-Nano-2512](https://huggingface.co/FunAudioLLM/Fun-ASR-Nano-2512)说明 AutoModel 的本地模型路径及 cuda:0／cpu 设备值。
- [FunASR 1.3.26 发行页](https://pypi.org/project/funasr/1.3.26/)提供本教程使用的工具包；模型实现与旧版本可能不同。

需要升级程序看[升级与回退](INSTALL.md#upgrade)，备份模型以外的个人数据看[数据与隐私](DATA_AND_PRIVACY.md)。
