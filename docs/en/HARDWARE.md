[简体中文](../zh-CN/HARDWARE.md) | [English](HARDWARE.md) | [日本語](../ja/HARDWARE.md)

# Resource usage and hardware limits

[Home](README.md) · [Installation](INSTALL.md) · [Voice](VOICE_SETUP.md)

The current pair is AIChat 1.18.30 + SPP 5.10.10. Measurements below retain their original dates and test scope; documentation updates are not new hardware validation.

## VRAM observations

**Local GPT-SoVITS and Fun-ASR need several additional GB of VRAM when run on GPU, alongside the game and desktop.** A 2026-09-27 screenshot recorded:

| Process | Dedicated GPU memory | Scope |
| --- | ---: | --- |
| Python process 1 | Approximately 2.17 GiB | Command line not recorded; cannot identify TTS/ASR/another instance |
| Python process 2 | Approximately 1.92 GiB | Same limitation |
| Game | Approximately 0.63 GiB | One scene, not every scene's peak |

These are observations, not fixed per-component requirements. Model, precision, device and phase were not fully recorded. GiB uses 1024³ bytes; GB uses 1000³. The RAM measurements below are a different resource. Shared GPU resources can be counted in several processes: **do not add those three readings and call the result total card usage**. Check Task Manager → Performance → GPU → Dedicated GPU memory; see [Microsoft's accounting explanation](https://devblogs.microsoft.com/directx/gpus-in-the-task-manager/) and the [historical record](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/63925a2ede595ac852b8d69a8572dcd64cfa6372/README.md).

Use **8 GB as an evaluation starting point for full GPU voice; 12 GB or more gives greater headroom**. This is not a tested minimum across GPU/voice combinations and excludes a separately hosted local chat LLM.

| VRAM/use | Possible approach |
| --- | --- |
| 12 GB+ | More headroom for game, TTS, ASR and peaks; still measure selected models/resolution |
| 8 GB | Starting point to evaluate full GPU voice; remove duplicate services and measure whole-card peaks |
| 6 GB | Try GPU TTS + CPU ASR; verify F8, continuous conversation and latency |
| 4 GB or less / integrated graphics | Start with text; validate a suitable CPU voice environment separately |
| Text + cloud API | Cloud chat weights are not loaded into local VRAM; TTS/ASR can be omitted |

Capacity does not prove backend compatibility. AMD/Intel Windows GPU voice backends have not been comprehensively validated and cannot use NVIDIA CUDA instructions unchanged. **There is no fully validated universal low-VRAM mode, and the reported game frame-rate drop remains unresolved.**

## Components and storage

The game uses GPU resources; AIChat handles UI, subtitles, recording and playback. SPP/keyword recall uses local CPU, RAM and files without Python. Optional E5 int8 runs on CPU through its bundled ORT. GPT-SoVITS and Fun-ASR use the device selected in their own environments/scripts. ONNX's CPU setting does not select ASR's device. Browsers/desktop applications also consume resources.

The current documentation ZIP is approximately 43 MB (original N15: approximately 39 MB); the earlier 1.17.x ZIP was approximately 11 MB. The optional model ZIP is approximately 94 MB. **Download sizes are not RAM limits.** Extraction, tokenizers, libraries, vectors, keyword indices, WAL replay and external voice environments add disk/memory usage. Later stages are optional; ONNX is not required for speech.

## RAM and startup: historical CP23 D measurements

These synthetic lifecycle measurements used **20 ms working-set sampling of the SPP parent plus real ONNX worker**. They are system RAM, not VRAM; they exclude the game and external TTS/ASR and are not universal maxima. Decimal MB are used.

| Metric | 10,000 synthetic records | 50,000 synthetic records |
| --- | ---: | ---: |
| Real-format WAL size / frames | 81.62 MB / 100,314 | 409.89 MB / 501,564 |
| Startup replay and archive projection | 11.65 s | **495.12 s (about 8 min 15 s)** |
| First keyword build | 73.58 ms | 439.82 ms |
| Mean warm keyword query | 10.94 ms | 87.62 ms |
| Mean authority check + keyword + real semantic query | 23.37 ms | 140.22 ms |
| Observed whole-pipeline peak | 440,557,568 B (about 441 MB) | **943,693,824 B (about 944 MB)** |
| Observed warm hybrid-query peak | 343,506,944 B | 735,981,568 B |

A separate **350 MB gate covered only the real int8 worker plus 50,000 vectors under sustained queries**, with a second-round maximum of **332,283,904 B**. It excluded records, keywords, WAL and startup. It is not a claim that all of SPP uses ≤350 MB.

Large-WAL cold start remains slow; no cold-start speed gate was set and passed. The synthetic WAL used the real format/hash chain, not 50,000 real cloud/live-commit turns. Lifecycle cache vectors were synthetic, not all inferred through E5. Real model load/query was separately checked. Player text, hardware and history change results. [Original maintenance evidence (Chinese)](../MAINTAINER_STATUS.zh-CN.md) preserves the scope.

## Device choices and measurement

On NVIDIA with matching CUDA, establish text first and test TTS/ASR separately. On AMD/Intel/integrated graphics, begin with text and CPU ONNX; voice needs a suitable CPU environment or supported backend. GPU TTS + CPU ASR reduces ASR GPU load but adds CPU/RAM demand and latency. Fully CPU voice may not feel real-time.

For GPT-SoVITS CPU use both `device: cpu` and `is_half: false`. The bundled Fun-ASR `AutoModel` has no explicit CPU argument; use the [CPU script copy](INSTALL.md#asr-cpu), not an unsupported device string. Consult the [PyTorch selector](https://pytorch.org/get-started/locally/) for the environment actually supported.

1. Add Command line to Task Manager's Details view. TTS commonly runs `api_v2.py`, ASR `satone_funasr_server_v1.py`; this semantic worker is a native SPP child, not `embedding_worker.py`.
2. Keep only needed instances. Close an unnecessary WebUI inference process when using the API. Closing a browser tab or continuous conversation does not unload a model process.
3. Measure desktop, game only, then TTS, ASR and semantic queries separately. Record whole-card/RAM peaks, model, device, precision, resolution and latency.
4. Try lighter weights/precision only when supported, then confirm playable synthesis and recognition of short and longer recordings.

Distinguish dedicated VRAM, shared GPU memory and system RAM. Retain whole-card screenshots and process command lines. Do not terminate Windows desktop processes to save mod memory.
