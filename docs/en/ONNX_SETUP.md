[简体中文](../zh-CN/ONNX_SETUP.md) | [English](ONNX_SETUP.md) | [日本語](../ja/ONNX_SETUP.md)

# Optional ONNX semantic recall

[Installation stage 2](INSTALL.md#stage-2) · [Downloads](DOWNLOADS.md) · [Hardware](HARDWARE.md)

Use the complete Windows x64 E5 int8/ORT component. Text/keyword recall is built in and needs no Python; TTS/ASR are independent. The semantic worker is native CPU code, not the old Python embedding worker.

## Verify, enable, disable

Wait for chat to finish and exit the game. Stop SPP before running `Verify_Semantic_Recall.bat`, `Enable_Semantic_Recall.bat` or `Disable_Semantic_Recall.bat`, then restart `SatonePromptProxy.exe` or `Start_Text_Chat.bat`. The stop tool can stop all processes named `SatonePromptProxy.exe`; take care with multiple instances. A still-accessible Dashboard after “not running” needs process investigation.

Require explicit success from the tools. Enable backs up configuration as `config.json.before-semantic-<timestamp>` and sets `embedding_enabled=true`, `embedding_auto_start=true`, `embedding_model_dir="models/multilingual-e5-small"`. Disable does not delete conversations. File verification is not a readiness test: submit a Recall query to warm up the runtime.

## Read the status correctly

| State | Meaning/action |
| --- | --- |
| `disabled` | Not enabled |
| `missing` | Required component files are absent |
| `waiting` | Waiting for usable records/work; normal for an empty profile |
| `loading` | Model loading; wait and refresh |
| `building` | Preparing vectors/index |
| `ready` | Current semantic state is ready; verify a real query |
| `failed` | Inspect `last_error`, model files and logs |

`engine: native_keyword+onnx` alone does not prove the model loaded. Inspect `worker.model_loaded`, `semantic_state`, and `worker.semantic_scope` for the intended profile. `worker.embedded_exchanges` is not the UI history count; an outer `profile_id` is not a substitute for the worker's scope. `semantic_ready: false` permits keyword fallback. A busy/409 result calls for retrying after the active chat rather than restarting repeatedly.

Selecting a profile in Dashboard only changes the view. Search exact words from a completed exchange, inspect `user_text`, `assistant_text` and full original text, then try a paraphrase. A `qualified` semantic match is a further retrieval filter, not a model-loaded signal or fact-correctness probability. Failure to match one query does not by itself prove component failure.

## Files and updates

Keep `model.onnx`, `tokenizer.json`, `onnxruntime.dll`, `onnxruntime_providers_shared.dll`, `COMPONENT.json` and licenses as one verified set. Do not mix unrelated model/runtime files. Compatible program updates can reuse the same approximately 94 MB component and cache; verify again and run an actual query. For component updates, back up, stop SPP and replace the complete matching folder according to its own manifest.

`semantic_recall_v1` contains private derived data. It can be rebuilt by the maintenance procedure but is not the authoritative WAL. Do not delete `local_v1`. Semantics covers the latest 50,000 eligible records; keyword recall retains full history coverage.

The documented [multilingual E5 small model](https://huggingface.co/intfloat/multilingual-e5-small) is pinned to revision `614241f622f53c4eeff9890bdc4f31cfecc418b3`; the component uses [ONNX Runtime 1.30.0](https://github.com/microsoft/onnxruntime/releases/tag/v1.30.0). Preserve `COMPONENT.json` and their licenses. The component is not relicensed as the mod's own content.
