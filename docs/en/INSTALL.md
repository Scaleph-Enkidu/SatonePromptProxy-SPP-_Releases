[简体中文](../zh-CN/INSTALL.md) | [English](INSTALL.md) | [日本語](../ja/INSTALL.md)

# Four-stage installation

[Home](README.md) · [Downloads and checksums](DOWNLOADS.md) · [License scope](LICENSE_SCOPE.md)

For **AIChat 1.18.30 + SPP 5.10.10**, release 2026-10-08. Existing users should read [upgrade and backup](UPGRADE.md) first. This update replaces both AIChat and SPP; optional models are unchanged.

Examples use `D:\LofiMOD`. If you use `C:\LofiMOD` or another location, change every corresponding path consistently. The F9 interface supports Chinese, English and Japanese. Control names below describe their function; older screenshots may show Chinese labels. Prefer short paths without non-ASCII characters when troubleshooting external tools.

Read [hardware and startup limits](HARDWARE.md) before adding voice. Text chat works alone; ONNX, TTS and ASR are optional independent additions after text chat.

<a id="stage-1"></a>
## 1. Text chat

### Install the plugin

1. Exit the game. In Steam, use Manage → Browse local files to open the game directory.
2. Download [BepInEx 5.4.23.5 for Windows x64](https://github.com/BepInEx/BepInEx/releases/download/v5.4.23.5/BepInEx_win_x64_5.4.23.5.zip). Extract `BepInEx` and `winhttp.dll` alongside the game executable. Launch the game once, then exit so configuration folders are created.
3. Download the [paired program package](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.18.30_SPP-v5.10.10/SatoneMod_AIChat_1.18.30_SPP_5.10.10_Windows_x64.zip). Copy `AIChat/AIChat.dll` and `AIChat.pdb` to the game's `BepInEx\plugins`, replacing the old plugin without leaving duplicate DLLs. Existing users must refresh the old Relaxed animation whitelist as described in [UPGRADE](UPGRADE.md).
4. Extract the entire `SatonePromptProxy` folder to `D:\LofiMOD\SatonePromptProxy`. Keep its data files and relative directories together. It does not belong inside the game's plugin folder.

### Start and connect SPP

Run `SatonePromptProxy.exe`. Its window is a log, not a command prompt. Keep it open and look for the listening address `http://127.0.0.1:11435/v1/chat/completions`. Do not paste installation commands into it.

Open the game, press F9 and expand settings. In the SPP/memory (persona proxy) section, set the executable path to `D:\LofiMOD\SatonePromptProxy\SatonePromptProxy.exe`. Copy the folder path from Explorer and append the executable name if needed. Enable automatic SPP startup if desired, save/apply, and check that SPP is running.

### Apply an LLM connection

In LLM settings, choose a supported service such as OpenAI or DeepSeek, enter that service's API Key and model name, or configure a relay's base URL and credentials according to its instructions. Model names supplied by the UI are examples, not a guarantee that your account supports them. A ChatGPT subscription is not an API balance. See [costs](API_COST.md) and [connections](systems/CONNECTIONS.md).

Save and apply. Wait for the applied/success state rather than assuming an edited draft is already active. On a new installation, initialize the new profile. If offered old-memory import, either import using the old directory or explicitly skip; skipping does not delete old files.

Type a greeting and press Enter. Shift+Enter inserts a newline. A reply confirms text chat. Original-game idle speech can interrupt conversation; the base game's self-talk filter near the penguin avatar can reduce interruptions. N15 fixes the Relaxed cup animation but existing configurations still need the whitelist update.

### Useful settings

SPP auto-stop is separate from auto-start. Verify actual service state after closing the game. Three memory profiles have separate histories/relationships; the persona file `SatonePersona_v4.6.txt` is shared. Back up custom persona changes. Providers/models can be switched without deleting memory. Protect keys and local conversations as explained in [privacy](DATA_AND_PRIVACY.md).

<a id="stage-2"></a>
## 2. Optional ONNX semantic recall

First complete a conversation, such as mentioning piano practice, so the profile has something to retrieve. An empty profile cannot prove recall works.

1. Wait for the reply to finish, exit the game, and run `Stop_SatonePromptProxy.bat`.
2. Download the [E5 small int8 + ORT 1.30.0 component](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.17.1_SPP-v5.9.1-license-r1/Satone_Semantic_E5_small_int8_ORT_1.30.0_Windows_x64.zip), approximately 94 MB. Put its `models` folder next to `SatonePromptProxy.exe`, not in `BepInEx\plugins` and not inside another `models` folder.
3. Run `Verify_Semantic_Recall.bat`, then `Enable_Semantic_Recall.bat`. Require explicit successful verification/enabling messages. A window that flashes closed is not proof; use the [script troubleshooting](#semantic-script) below.
4. Start SPP again. Open `Open_Dashboard.bat`, select the profile to inspect, and search its Recall page for a topic from a completed conversation. Selecting a Dashboard view does not switch the game's active profile.

The index-status button refreshes on each click. A query triggers warm-up; merely opening the page does not. Confirm `model_loaded: true`, `semantic_state: ready`, and the correct `semantic_scope` such as `local:memory1`. `loading`, `building` or `waiting` require interpretation, not a claim of readiness. An empty profile can legitimately be waiting.

Inspect `user_text` and `assistant_text`, then try a paraphrase. A paraphrase is not guaranteed to match. `semantic_ready: false` permits keyword fallback; if busy, wait until chat finishes and retry. ONNX is not needed for TTS or ASR.

To disable, stop SPP, run `Disable_Semantic_Recall.bat`, then restart. This does not delete chat records. See [ONNX details](ONNX_SETUP.md) and [resource measurements](HARDWARE.md).

<a id="stage-3"></a>
## 3. Speech synthesis with GPT-SoVITS

This example uses the Hitori Gotoh v2ProPlus weights with a Japanese Mayuri Neutral reference. Their roles and licenses differ; see [voice sources](VOICE_SETUP.md#voice-sources). The main mod includes the Neutral WAV, but not the GPT-SoVITS runtime or voice weights. UI/subtitle language support does not guarantee multilingual pronunciation from this voice.

### 3.1 Runtime and weights

Use [7-Zip](https://www.7-zip.org/) to extract the appropriate official Windows bundle:

| Environment | Download |
| --- | --- |
| CPU or supported NVIDIA GPUs other than RTX 50 | [GPT-SoVITS-v2pro-20250604.7z](https://huggingface.co/lj1995/GPT-SoVITS-windows-package/resolve/main/GPT-SoVITS-v2pro-20250604.7z?download=true), about 8.19 GB |
| NVIDIA RTX 50 series | [GPT-SoVITS-v2pro-20250604-nvidia50.7z](https://huggingface.co/lj1995/GPT-SoVITS-windows-package/resolve/main/GPT-SoVITS-v2pro-20250604-nvidia50.7z?download=true), about 8.84 GB |

These are NVIDIA CUDA instructions; AMD/Intel users should use the CPU route or a separately supported backend. Update the matching [NVIDIA driver](https://www.nvidia.com/Download/index.aspx). The bundle has its own Python; do not install Fun-ASR into that environment.

Extract to `D:\LofiMOD\GPT-SoVITS` so it directly contains `api_v2.py`, `runtime\python.exe` and `GPT_SoVITS\configs\tts_infer.yaml`. Avoid an extra nested runtime folder.

Download only these two [lpkpaco Hitori Gotoh v2ProPlus weights](https://huggingface.co/lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models), published under CC BY-NC-SA 4.0:

| File | Destination under GPT-SoVITS |
| --- | --- |
| [gotoh-v1-3-1-e16.ckpt](https://huggingface.co/lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models/resolve/main/models/Hitori_Gotoh/v2ProPlus/gotoh-v1-3-1/GPT/gotoh-v1-3-1-e16.ckpt?download=true) | `GPT_weights_v2ProPlus/gotoh-v1-3-1-e16.ckpt` |
| [gotoh-v1-3-1_e8_s368.pth](https://huggingface.co/lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models/resolve/main/models/Hitori_Gotoh/v2ProPlus/gotoh-v1-3-1/SoVITS/gotoh-v1-3-1_e8_s368.pth?download=true) | `SoVITS_weights_v2ProPlus/gotoh-v1-3-1_e8_s368.pth` |

Keep the bundle's actual pretrained files under `GPT_SoVITS/pretrained_models/chinese-roberta-wwm-ext-large`, `chinese-hubert-base`, and `sv/pretrained_eres2netv2w24s4ep4.ckpt`. If missing, the [SV weight](https://huggingface.co/lj1995/GPT-SoVITS/resolve/main/sv/pretrained_eres2netv2w24s4ep4.ckpt?download=true) comes from the official repository. Empty folders or tiny Git LFS pointer files are not models. Do not substitute v4 weights because their names look similar.

### 3.2 Configure the inference file

Back up `GPT_SoVITS\configs\tts_infer.yaml` as `tts_infer.yaml.bak`. Replace its contents with:

```yaml
custom:
  bert_base_path: GPT_SoVITS/pretrained_models/chinese-roberta-wwm-ext-large
  cnhuhbert_base_path: GPT_SoVITS/pretrained_models/chinese-hubert-base
  device: cuda
  is_half: true
  t2s_weights_path: GPT_weights_v2ProPlus/gotoh-v1-3-1-e16.ckpt
  version: v2ProPlus
  vits_weights_path: SoVITS_weights_v2ProPlus/gotoh-v1-3-1_e8_s368.pth
```

For CPU, change **both** `device: cuda` to `device: cpu` and `is_half: true` to `is_half: false`; leave the remaining paths/version unchanged. Use two-space indentation below `custom:`, which must remain at the top level. Reference: [official configuration](https://github.com/RVC-Boss/GPT-SoVITS/blob/main/GPT_SoVITS/configs/tts_infer.yaml) and [inference implementation](https://github.com/RVC-Boss/GPT-SoVITS/blob/main/GPT_SoVITS/TTS_infer_pack/TTS.py).

### 3.3 Create and test the API launcher

Create `D:\LofiMOD\GPT-SoVITS\run_api.bat` with:

```bat
@echo off
cd /d "%~dp0"
"runtime\python.exe" -s api_v2.py -a 127.0.0.1 -p 9880 -c "GPT_SoVITS/configs/tts_infer.yaml"
pause
```

Save as UTF-8 with file type “All files”. Enable Explorer's filename extensions (Windows 11: View → Show → File name extensions) and ensure the file is not `run_api.bat.txt`.

Run it and keep the window open. Confirm application startup completes and Uvicorn listens at `http://127.0.0.1:9880`; inspect output to ensure the v2ProPlus Gotoh weights were loaded. `CUDA is not available` is a failure, not readiness: fix driver/runtime selection or use the CPU configuration.

Open [the local API documentation](http://127.0.0.1:9880/docs) and find `/tts`. `go-webui.bat` is not required; a WebUI in another process does not replace the API.

### 3.4 Check the Neutral reference

Play `D:\LofiMOD\SatonePromptProxy\mayuri-voice\refs\MAY_1158_Neutral.wav`. In [SPP TTS status](http://127.0.0.1:11435/tts/status), confirm `validation.Neutral.valid` is `true` and `resolved_path` points to this actual WAV. Leave a working fresh default alone.

For an old misconfigured profile, stop SPP and back up `config.json`, then edit the existing `emotion_tts` fields (do not replace unrelated configuration): `enabled: true`, `upstream_url: "http://127.0.0.1:9880"`, empty `ref_root`, `fallback_profile: "Neutral"`. Under `profiles.Neutral`, use `path: "MAY_1158_Neutral.wav"`, `lang: "ja"` and this exact recording transcript:

> 嫌がってるのに無理やり着せたりしてねトラウマになっちゃったら良くないもん。

The reference transcript must match the WAV; do not translate it to the documentation language. JSON strings need double quotes and booleans are unquoted. Save, restart SPP and recheck validation. Further reference choices are [documented separately](VOICE_SETUP.md#emotions-26).

### 3.5 Connect the game

F9 → settings → TTS: set the launch script to `D:\LofiMOD\GPT-SoVITS\run_api.bat`, enable automatic TTS startup if desired, and keep the **shared voice service URL at `http://127.0.0.1:11435`**, not 9880 or 9881. Set speech language `ja` for this reference setup and volume above zero (for example 1.00). Save/apply.

Send a short greeting. Confirm both visible text and audible speech; CPU synthesis may take longer. After closing the game, close any API window started manually, then relaunch to verify auto-start separately. See [isolated synthesis tests](VOICE_SETUP.md#tts-test) if there is no sound.

<a id="stage-4"></a>
## 4. Microphone input with Fun-ASR

ASR needs working text chat, not TTS or ONNX. This guide uses Fun-ASR-Nano-2512. Headphones reduce feedback; self-echo suppression is not perfect. Adjust VAD against your microphone's measured quiet/speaking levels rather than assuming one universal threshold.

### 4.1 Separate Python environment

Install [Python 3.12.10 Windows x64](https://www.python.org/ftp/python/3.12.10/python-3.12.10-amd64.exe), the full installer rather than the embeddable package. Include the `py` launcher and pip, and enable “Add Python to PATH”. Create `D:\LofiMOD\FunASR-Runtime`, open it in Explorer, type `cmd` in the address bar and press Enter. These commands belong in **CMD**, not SPP's log window:

```bat
py -3.12 --version
py -3.12 -m venv .venv
.venv\Scripts\python.exe -m pip install --upgrade pip
```

The first line should show Python 3.12.x. If `py` is missing, modify the Python installation to include the launcher, close the old CMD and open a new one.

### 4.2 Choose GPU or CPU, then install dependencies

For supported NVIDIA RTX 20/30/40/50 hardware with a suitable CUDA 12.8 driver:

```bat
.venv\Scripts\python.exe -m pip install torch==2.9.1 torchaudio==2.9.1 --index-url https://download.pytorch.org/whl/cu128
```

For CPU, including the CPU route on AMD/Intel machines, use this **instead**:

```bat
.venv\Scripts\python.exe -m pip install torch==2.9.1 torchaudio==2.9.1 --index-url https://download.pytorch.org/whl/cpu
```

Then run these shared commands:

```bat
.venv\Scripts\python.exe -m pip install funasr==1.3.26 transformers==4.51.3 huggingface_hub==0.36.0 zhconv whisper_normalizer pyopenjtalk-plus==0.4.1.post8 compute-wer openai-whisper
.venv\Scripts\python.exe -m pip check
.venv\Scripts\python.exe -c "import torch, torchaudio, funasr, transformers; print('torch', torch.__version__); print('torchaudio', torchaudio.__version__); print('transformers', transformers.__version__); print('cuda', torch.cuda.is_available())"
```

Require `No broken requirements found`, successful imports without a traceback, matching Torch/torchaudio 2.9.1 variants (`+cu128` or `+cpu`) and transformers 4.51.3. CUDA should be available for the GPU route; `False` is expected for CPU. Do not infer GPU readiness solely from a successful pip install. These wheel instructions do not require installing a separate CUDA Toolkit. See [PyTorch versions](https://pytorch.org/get-started/previous-versions/) and [Fun-ASR dependencies](https://github.com/QwenAudio/Fun-ASR/blob/main/requirements.txt).

### 4.3 Download the complete model

In the same environment:

```bat
.venv\Scripts\python.exe -c "from huggingface_hub import snapshot_download; snapshot_download(repo_id='FunAudioLLM/Fun-ASR-Nano-2512', local_dir='D:/LofiMOD/Fun-ASR-Nano-2512')"
```

No Git setup is needed. Rerun the same command after an interrupted download. The model folder must contain real `config.yaml`, `configuration.json`, `model.pt`, `multilingual.tiktoken` and the full `Qwen3-0.6B` directory. A single `model.pt`, empty folders or LFS pointer text is insufficient. Do not rename an `-hf`, GGUF or faster-whisper model to this directory and expect compatibility.

<a id="asr-cpu"></a>
### 4.4 Select the service script

Stop SPP. GPU users use the bundled `D:\LofiMOD\SatonePromptProxy\satone_funasr_server_v1.py`.

For CPU, copy that current bundled file to `D:\LofiMOD\FunASR-Runtime\satone_funasr_server_cpu_v1.py`. In the copy, replace:

```python
model = AutoModel(model=model_dir, trust_remote_code=True)
```

with:

```python
model = AutoModel(model=model_dir, trust_remote_code=True, device="cpu")
```

Preserve indentation and everything else. Make sure the extension is `.py`, not `.py.txt`. The supported configuration field is `asr.server_script`; do not add a nonexistent `asr.device` setting.

### 4.5 Configure SPP and verify readiness

Back up `config.json`. Edit these fields within its existing `asr` object, preserving any other settings. This is a fragment of the full configuration, not a replacement for the entire file:

```json
"asr": {
  "enabled": true,
  "auto_start": true,
  "auto_restart": true,
  "stop_with_proxy": true,
  "python": "D:/LofiMOD/FunASR-Runtime/.venv/Scripts/python.exe",
  "server_script": "D:/LofiMOD/SatonePromptProxy/satone_funasr_server_v1.py",
  "model_path": "D:/LofiMOD/Fun-ASR-Nano-2512",
  "upstream_url": "http://127.0.0.1:9881",
  "language": "auto"
}
```

CPU users replace only `server_script` above with `D:/LofiMOD/FunASR-Runtime/satone_funasr_server_cpu_v1.py`. Adapt every path to your installation. Save valid JSON and start SPP; do not double-click the Python script separately.

Check [SPP ASR status](http://127.0.0.1:11435/asr/status): `ready: true`, correct `python`, `server_script` and `model_path`. Check [backend health](http://127.0.0.1:9881/health): `ok: true`. Loading may take time. On failure, read the first Python error and `last_error` in `SatonePromptProxy_v5.10.10.log`. An existing manually launched service on 9881 may still be a GPU instance; stop that old service before restarting SPP on the CPU route.

### 4.6 Choose a microphone and speak

Allow microphone access for desktop apps in Windows privacy settings. In F9 settings → continuous conversation, select your actual microphone and save/apply. This microphone is shared by push-to-talk and continuous modes; you can choose it without enabling continuous listening. The shared voice URL is in TTS settings and remains `http://127.0.0.1:11435` even if TTS is not installed.

Hold F8, say a short sentence and release, or use the voice button. Require a reasonable transcript and a reply. Only then enable continuous conversation, save/apply, speak and pause to confirm detection. Disable/save or use the stop control to stop listening. Continuous conversation starts disabled each game session.

After updating SPP, recreate/update a custom CPU script from the new bundled version, retaining `device="cpu"`. Do not keep an obsolete service implementation indefinitely. See [microphone/VAD diagnostics](VOICE_SETUP.md#asr-troubleshooting).

<a id="upgrade"></a>
## Upgrading and rollback

Use the current [upgrade guide](UPGRADE.md): back up the entire old SPP runtime and game configuration/history, extract to a **new SPP directory**, then use the memory-import action with the old directory's absolute path. Reapply service paths and the N15 whitelist change. Keep DLL/PDB backups outside `BepInEx\plugins` to avoid loading duplicates. A reliable rollback restores the matching old program **and data**, not only one executable.

## Troubleshooting

| Symptom | First check |
| --- | --- |
| F9 does not open | BepInEx installed beside the game EXE, plugin DLL in `plugins`, no duplicates |
| SPP not detected | Executable path, running status and listening log |
| API reply fails | Applied connection, key, model permissions and API balance |
| ONNX has no result | Completed history in selected profile; query to trigger warm-up |
| TTS silent | API on 9880, reference validation, speech language and game/system volume |
| ASR has no text | Health on 9881, SPP ready state, Windows permissions and selected microphone |
| Game frame rate drops after SPP starts | Record conditions/processes; see the startup section below and hardware notes |

<a id="semantic-script"></a>
### Semantic BAT window closes immediately

After exiting game/SPP, open CMD in the SPP folder and run the desired operation directly:

```bat
SatonePromptProxy.exe --semantic-component verify
SatonePromptProxy.exe --semantic-component enable
```

To disable instead:

```bat
SatonePromptProxy.exe --semantic-component disable
```

Require explicit success. If already running/locked, stop the service and retry. Component file verification does not prove the runtime worker has warmed up; restart and query to check `ready`.

<a id="spp-start-window"></a>
### SPP startup window and frame rate

`SatonePromptProxy.exe` directly shows the service log. `Start_Text_Chat.bat` is another entry to the same service and some older tool revisions minimize its window. A hidden/minimized window does not mean it stopped. Confirm the listening line and F9 status. Large history can cause slow cold starts. The reported game frame-rate problem's root cause remains unconfirmed; stopping/restarting may help temporarily but is not a proven fix. See [hardware measurements](HARDWARE.md).

<a id="preserved-voice"></a>
### Retained voice inputs

Old retained inputs are not automatically sent into a new session, and their warning is not an ONNX failure. Start SPP with a confirmed active connection. In F9 continuous-conversation settings (listening need not be enabled), inspect each retained item's count, profile and text.

Copying text to the input box only creates a draft. Check the destination profile, send it deliberately if appropriate, then remove its queued copy. Removing a queue entry does not delete conversation history. Audio export saves only the recording under `BepInEx\config\AIChat.preserved-inputs`; it does not run ASR or automatically send it.

Process entries individually. These actions apply immediately without Save/apply; allow a few seconds for status to refresh and the warning to clear. Redact API Keys and private conversations before sharing diagnostic logs.
