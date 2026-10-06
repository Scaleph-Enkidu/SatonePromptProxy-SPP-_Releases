[简体中文](../zh-CN/VOICE_SETUP.md) | [English](VOICE_SETUP.md) | [日本語](../ja/VOICE_SETUP.md)

# Advanced voice setup and troubleshooting

[Installation](INSTALL.md) · [Downloads](DOWNLOADS.md) · [Hardware](HARDWARE.md)

<a id="stage-3"></a>
[First-time TTS installation: stage 3](INSTALL.md#stage-3)

<a id="stage-4"></a>
[First-time ASR installation: stage 4](INSTALL.md#stage-4)

For AIChat 1.18.28 + SPP 5.10.8. TTS and ASR are independent; neither requires ONNX. The main package supplies a Neutral reference WAV, while GPT-SoVITS, voice weights and the ASR environment/model are external. Configure TTS devices in `tts_infer.yaml` with `device`/`is_half`; select the Fun-ASR CPU script through `asr.server_script`. There is no SPP `asr.device` field.

The maintainer's local test confirmation dated 2026-10-01 is historical evidence, not acceptance of every newly installed dependency/hardware/voice/provider combination. Actual loading, speech and F8 recognition remain the checks on your machine.

| Port | Service | Use |
| --- | --- | --- |
| 11435 | SPP | Shared game voice address; `/tts`, `/asr` and status pages |
| 9880 | GPT-SoVITS API | SPP's synthesis backend |
| 9881 | Fun-ASR | Recognition backend; `/health` |

Keep the game's shared voice address at `http://127.0.0.1:11435`. Bind locally; no router forwarding is needed.

<a id="voice-sources"></a>
## Voice weights, reference recordings and sources

The documented voice is designed around Japanese. Chinese/English UI and subtitles do not guarantee this voice's pronunciation in those languages, particularly English; test a model suited to your desired speech language.

| Resource | Purpose | Source |
| --- | --- | --- |
| Base pretrained/text models | Run GPT-SoVITS | Bundle or [official model repository](https://huggingface.co/lj1995/GPT-SoVITS/tree/main) |
| Voice GPT `.ckpt` / SoVITS `.pth` | A trained voice for a specific v2/v2Pro/v2ProPlus version | Voice author's original release |
| Reference WAV and exact transcript | A vocal example for an individual synthesis | Your recording or audio with appropriate permission |

This example combines **Hitori Gotoh v2ProPlus weights with a Mayuri reference WAV and Japanese transcript**. These serve different roles. Do not mix Mayuri model weights into the Gotoh pair.

- Gotoh by lpkpaco: [model page](https://huggingface.co/lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models), [author's project](https://github.com/lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models), [v2ProPlus gotoh-v1-3-1 folder](https://huggingface.co/lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models/tree/main/models/Hitori_Gotoh/v2ProPlus/gotoh-v1-3-1).
- [GPT weight](https://huggingface.co/lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models/resolve/main/models/Hitori_Gotoh/v2ProPlus/gotoh-v1-3-1/GPT/gotoh-v1-3-1-e16.ckpt?download=true), about 155 MB → `GPT-SoVITS/GPT_weights_v2ProPlus/gotoh-v1-3-1-e16.ckpt`.
- [SoVITS weight](https://huggingface.co/lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models/resolve/main/models/Hitori_Gotoh/v2ProPlus/gotoh-v1-3-1/SoVITS/gotoh-v1-3-1_e8_s368.pth?download=true), about 173 MB → `GPT-SoVITS/SoVITS_weights_v2ProPlus/gotoh-v1-3-1_e8_s368.pth`.
- Mayuri references by SteinsGateSg: [project](https://huggingface.co/SteinsGateSg/mayuri-voice), [refs](https://huggingface.co/SteinsGateSg/mayuri-voice/tree/main/refs), [transcript index](https://huggingface.co/SteinsGateSg/mayuri-voice/blob/main/refs/index.csv). Only Neutral is bundled; other WAV/TXT files are optional.

Download the two Gotoh weights, not the entire multi-GB voice repository or similarly named v4 files. Mayuri's `models/gpt` and `models/sovits` are not needed here. The recorded source labels were `cc-by-nc-sa-4.0` for Gotoh and `License: other` for Mayuri; follow each publisher's conditions. This combination is the project's example, not a jointly certified package from both authors. Listen to verify the result.

SPP checks that a reference is readable standard RIFF/WAVE, **3–10 seconds** long, with a nonempty transcript. The main package includes `MAY_1158_Neutral.wav`, not every `MAY_*.wav`.

<a id="tts-test"></a>
## Test the two TTS layers separately

These local synthesis tests do not call the main chat model.

### GPT-SoVITS directly

Keep `run_api.bat` running, open [9880/docs](http://127.0.0.1:9880/docs), expand **POST /tts**, choose **Try it out**, and replace the request body with:

```json
{
  "text": "こんにちは。",
  "text_lang": "ja",
  "ref_audio_path": "D:/LofiMOD/SatonePromptProxy/mayuri-voice/refs/MAY_1158_Neutral.wav",
  "prompt_text": "嫌がってるのに無理やり着せたりしてねトラウマになっちゃったら良くないもん。",
  "prompt_lang": "ja",
  "media_type": "wav",
  "streaming_mode": false
}
```

Adapt the file path, not the reference transcript. Click **Execute**. Expect HTTP 200 and audio; use **Download file** and play the WAV. A JSON error requires reading its message/exception and fixing model/path/language. If the page is unavailable, inspect the API window and its listening address. A separate WebUI is not proof the API is ready.

### Through SPP

Start SPP. Open `D:\LofiMOD\SatonePromptProxy` in Explorer, type `powershell` in the address bar and run these lines in **PowerShell**, not the CMD used for ASR installation:

```powershell
$satoneBody = @{ text = '[Neutral] こんにちは。'; text_lang = 'ja'; media_type = 'wav'; streaming_mode = $false } | ConvertTo-Json
Invoke-WebRequest -Uri 'http://127.0.0.1:11435/tts' -Method Post -ContentType 'application/json; charset=utf-8' -Body ([System.Text.Encoding]::UTF8.GetBytes($satoneBody)) -OutFile 'D:\LofiMOD\SatonePromptProxy\spp-test.wav'
```

Play `spp-test.wav`. Replace `[Neutral]` with a reference you have installed, such as `[Happy]` or `[Sad]`, to test it. Keep the exact English bracketed tag. If both layers work, return to F9 → TTS, check `ja`, volume above zero, shared URL 11435, save/apply and send a message.

<a id="emotions-26"></a>
## Optional references for all 26 emotions

SPP uses `emotion_tts.mapping` → `profiles` → `path`; it does not infer emotion by scanning filenames. Custom filenames work only if configuration points to them. The table preserves the defaults from the documented 5.9.1 configuration/`profiles_26.csv`; later personal configuration may differ. Upstream folders such as `worried` are not the same as SPP's tag taxonomy and do not guarantee perfect emotional performance.

Download real WAV/TXT content, place optional recordings in `mayuri-voice/refs`, and use the final-column names (TXT uses the same stem). Two tags sharing a source need two named copies rather than renaming one back and forth: **24 distinct recordings form 26 configuration entries**. Keep the existing mapping/profiles, `fallback_profile: "Neutral"` and empty `ref_root` unless your actual reference location requires another root. Do not overwrite unrelated settings with a whole default configuration.

| Tag (exact spelling) | Meaning | Original WAV / TXT | Filename in refs |
| --- | --- | --- | --- |
| `Neutral` | Calm / neutral | [worried/MAY_1158.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/worried/MAY_1158.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/worried/MAY_1158.txt?download=true) | `MAY_1158_Neutral.wav` |
| `Happy` | Happy | [teasing/MAY_0336.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/teasing/MAY_0336.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/teasing/MAY_0336.txt?download=true) | `MAY_0336_Happy.wav` |
| `Excited` | Excited | [excited/MAY_0279.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/excited/MAY_0279.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/excited/MAY_0279.txt?download=true) | `MAY_0279_Excited.wav` |
| `Relaxed` | Relaxed | [serious/MAY_0046.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/serious/MAY_0046.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/serious/MAY_0046.txt?download=true) | `MAY_0046_Relaxed.wav` |
| `Sad` | Sad | [sad/MAY_0160.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/sad/MAY_0160.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/sad/MAY_0160.txt?download=true) | `MAY_0160_Sad.wav` |
| `Crying` | Crying | [serious/MAY_1382.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/serious/MAY_1382.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/serious/MAY_1382.txt?download=true) | `MAY_1382_Crying.wav` |
| `Pouting` | Pouting | [embarrassed/MAY_0030.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/embarrassed/MAY_0030.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/embarrassed/MAY_0030.txt?download=true) | `MAY_0030_Pouting.wav` |
| `Tired` | Tired | [gentle/MAY_1311.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/gentle/MAY_1311.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/gentle/MAY_1311.txt?download=true) | `MAY_1311_Tired.wav` |
| `Sleepy` | Sleepy | [other/MAY_0529.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/other/MAY_0529.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/other/MAY_0529.txt?download=true) | `MAY_0529_Sleepy.wav` |
| `Angry` | Angry | [teasing/MAY_0355.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/teasing/MAY_0355.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/teasing/MAY_0355.txt?download=true) | `MAY_0355_Angry.wav` |
| `Chiding` | Chiding | [serious/MAY_0575.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/serious/MAY_0575.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/serious/MAY_0575.txt?download=true) | `MAY_0575_Chiding.wav` |
| `Nervous` | Nervous | [worried/MAY_0035.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/worried/MAY_0035.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/worried/MAY_0035.txt?download=true) | `MAY_0035_Nervous.wav` |
| `Afraid` | Afraid | [worried/MAY_0512.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/worried/MAY_0512.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/worried/MAY_0512.txt?download=true) | `MAY_0512_Afraid.wav` |
| `Confused` | Confused | [embarrassed/MAY_0170.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/embarrassed/MAY_0170.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/embarrassed/MAY_0170.txt?download=true) | `MAY_0170_Confused.wav` |
| `Curious` | Curious | [embarrassed/MAY_0170.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/embarrassed/MAY_0170.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/embarrassed/MAY_0170.txt?download=true) | `MAY_0170_Curious.wav` |
| `Think` | Thinking | [serious/MAY_0328.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/serious/MAY_0328.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/serious/MAY_0328.txt?download=true) | `MAY_0328_Think.wav` |
| `Surprised` | Surprised | [serious/MAY_1464.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/serious/MAY_1464.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/serious/MAY_1464.txt?download=true) | `MAY_1464_Surprised.wav` |
| `Shocked` | Shocked | [teasing/MAY_0201.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/teasing/MAY_0201.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/teasing/MAY_0201.txt?download=true) | `MAY_0201_Shocked.wav` |
| `Shy` | Shy | [gentle/MAY_0838.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/gentle/MAY_0838.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/gentle/MAY_0838.txt?download=true) | `MAY_0838_Shy.wav` |
| `Affectionate` | Affectionate | [gentle/MAY_1410.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/gentle/MAY_1410.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/gentle/MAY_1410.txt?download=true) | `MAY_1410_Affectionate.wav` |
| `Playful` | Playful | [teasing/MAY_0336.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/teasing/MAY_0336.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/teasing/MAY_0336.txt?download=true) | `MAY_0336_Playful.wav` |
| `Teasing` | Teasing | [happy/MAY_1063.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/happy/MAY_1063.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/happy/MAY_1063.txt?download=true) | `MAY_1063_Teasing.wav` |
| `Mocking` | Mocking | [neutral/MAY_0939.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/neutral/MAY_0939.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/neutral/MAY_0939.txt?download=true) | `MAY_0939_Mocking.wav` |
| `Sarcastic` | Sarcastic | [excited/MAY_1428.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/excited/MAY_1428.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/excited/MAY_1428.txt?download=true) | `MAY_1428_Sarcastic.wav` |
| `Smug` | Smug | [neutral/MAY_0485.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/neutral/MAY_0485.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/neutral/MAY_0485.txt?download=true) | `MAY_0485_Smug.wav` |
| `Disagree` | Disagreeing | [neutral/MAY_0053.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/neutral/MAY_0053.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/neutral/MAY_0053.txt?download=true) | `MAY_0053_Disagree.wav` |

Use exact tag spelling, especially `Think`, `Surprised`, `Disagree`, not `Thinking`, `Surprise` or translations. Show extensions to avoid `.wav.wav`/`.txt.txt`.

### Transcript precedence

The documented default prompts match the checked Mayuri index for those recordings. Keep them only when using the same audio. If you replace the recording, update its transcript too.

**A nonempty configured `prompt` wins. Only an empty prompt loads the adjacent same-stem `.txt`.** To use UTF-8 TXT, edit the existing profile, for example:

```json
"Neutral": {
  "path": "MAY_1158_Neutral.wav",
  "prompt": "",
  "lang": "ja"
}
```

TXT must contain the Japanese words actually spoken in the WAV; listen to check. Alternatively, retain the upstream folder names, set `ref_root` to the original `refs`, use `worried/MAY_1158.wav` as the Neutral path, and leave `prompt` empty for `MAY_1158.txt`. Do not mix layouts without updating paths. Editing `profiles_26.csv` alone does not rewrite the live configuration.

Restart SPP and inspect [TTS status](http://127.0.0.1:11435/tts/status): `mapping`, `profiles`, `validation` and startup Voice Profile checks. A fully supplied default set should report 26 valid/0 invalid. Test each tag through SPP. Missing WAVs, invalid durations or empty prompts may fall back to Neutral, so hearing sound does not prove the requested reference was used. If Neutral is invalid too, fallback cannot help. Valid files do not guarantee 26 audibly distinct emotions.

<a id="tts-troubleshooting"></a>
## TTS troubleshooting

| Symptom | Action |
| --- | --- |
| Launcher errors then waits for a key | Keep the window; read the first traceback and verify bundled Python, both Gotoh weights and base models |
| `fall back to default t2s_weights_path` / `vits_weights_path` | Fix actual YAML/file locations, restart and confirm Gotoh weights load |
| `CUDA is not available` | Match NVIDIA driver/bundle, or use the complete CPU settings |
| No valid Neutral | Check `validation.Neutral.valid` and `resolved_path`; repair old configuration as in stage 3 |
| Only one emotion is audible | Only Neutral is bundled; add optional references and test individually |
| WAV plays but game is silent | Game TTS volume, Windows mixer and saved/applied settings |
| Address already in use | Stop your old API instance on 9880; run one instance |
| WebUI voice changed but game did not | Edit the YAML actually read by `run_api.bat`; restart the API |
| CPU synthesis slow | Test a short sentence, then assess latency; volume and ONNX settings do not speed up TTS |

SPP log: `D:\LofiMOD\SatonePromptProxy\SatonePromptProxy_v5.10.8.log`. GPT-SoVITS errors are in its API window. Preserve the first error and full path.

For linked startup, run `Set_GPTSoVITS_RunApi_Path.bat`, enter `D:\LofiMOD\GPT-SoVITS\run_api.bat` and confirm `[OK] Saved`. Set the game's TTS launch script to `D:\LofiMOD\SatonePromptProxy\Start_AIChat_Services.bat`, enable auto-start, save and verify next launch. It reads `service_paths.ini` and starts prepared services; it does not install environments/weights. Direct `run_api.bat` use is also valid.

<a id="asr-cpu"></a>
<a id="asr-troubleshooting"></a>
## ASR and microphone troubleshooting

First-time CPU setup is in [installation stage 4](INSTALL.md#asr-cpu).

| Symptom | Action |
| --- | --- |
| Python/py missing | Install full Python 3.12 x64 and launcher; reopen CMD |
| pip/import error | Use `.venv\Scripts\python.exe`; make the documented pip/import checks pass |
| `model.pt` exists but loading fails | Confirm the complete configuration/tokenizer/Qwen3 folder; repeat full `snapshot_download` |
| CPU route uses an old backend | Stop your old 9881 service; verify the CPU `server_script` in SPP status |
| `ready` stays false | Read `last_error` and the first Python error; existing folders/install success do not prove loading |
| Health is OK but F8 yields no text | Windows microphone permissions, actual device selection and save/apply |
| F8 works, continuous mode clips speech | Test raw recording before changing VAD one setting at a time |
| Ready but slow | Compare the same short utterance on the chosen device; record duration/latency |
| ASR address hard to find without TTS | Shared URL is in TTS settings, default 11435; microphone selection is in continuous-conversation settings |

F9 continuous-conversation diagnostics provide a shared microphone selector, separate **10-second quiet/speaking recordings** (local only, no ASR; listening stops afterward), and **save the next push-to-talk raw recording** (normal recognition still runs). The temporary threshold trial **0.0005** takes effect after saving and returns on stopping the call. Treat it as a reversible trial, not a universal value. Establish F8 first; adjust onset/pause settings one at a time, save/apply and wait for the current utterance to finish before retesting.

Inspect [SPP ASR status](http://127.0.0.1:11435/asr/status) and [backend health](http://127.0.0.1:9881/health) for `ready`, paths, `hotwords_backend_supported` and `hotwords_supported`. Capability flags do not guarantee word accuracy; speak the term with F8. Health does not report model device. CPU verification uses the explicit `device="cpu"` script, resolved path and real recognition. Refresh custom CPU scripts from each new bundled implementation.

In CMD inside `FunASR-Runtime`, save installed versions for diagnosis/rollback:

```bat
.venv\Scripts\python.exe -m pip freeze > asr-environment.txt
```

Runtime references: [Fun-ASR dependencies](https://github.com/QwenAudio/Fun-ASR/blob/main/requirements.txt), [PyTorch 2.9.1 CPU/CUDA instructions](https://pytorch.org/get-started/previous-versions/), [Fun-ASR-Nano-2512](https://huggingface.co/FunAudioLLM/Fun-ASR-Nano-2512), [FunASR 1.3.26](https://pypi.org/project/funasr/1.3.26/). Follow [upgrade](UPGRADE.md) and [backup/privacy](DATA_AND_PRIVACY.md) before changing an existing setup.
