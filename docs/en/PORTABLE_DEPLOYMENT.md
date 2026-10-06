[简体中文](../zh-CN/PORTABLE_DEPLOYMENT.md) | [English](PORTABLE_DEPLOYMENT.md) | [日本語](../ja/PORTABLE_DEPLOYMENT.md)

# Moving a portable SPP installation

[Install](INSTALL.md) · [Upgrade](UPGRADE.md) · [Backup scope](DATA_AND_PRIVACY.md)

This current 5.10.8 guide replaces the package's mixed CP14/CP23-era deployment advice. Use a short path such as `D:\LofiMOD\SatonePromptProxy`, with external `FunASR-Runtime`, `Fun-ASR-Nano-2512` and `GPT-SoVITS` folders nearby. Keep the bundled `SatonePersona_v4.6.txt`: an omitted persona previously caused first-start `/persona` failure. Copying the EXE alone is insufficient for a new installation.

## First startup and path resolution

SPP uses existing `config.json`, otherwise creates it from `config.example.json`. Missing both files or malformed JSON produces an explicit error. Historically, 5.8.23 backed up and migrated the old default consolidation threshold from 24000 to 32000; that is not an instruction to replace all custom fields during updates.

Valid explicit ASR paths take precedence. For the service script, the bundled `satone_funasr_server_v1.py` is next; valid `runtime_paths.json` and standard-directory discovery provide fallbacks. Standard layouts include `AI/FunASR-Runtime` and `AI/Fun-ASR-Nano-2512`, or the same nearby names without `AI`. Stale machine paths are rediscovered; path cache is not memory. For predictable first installation, enter the Python/script/model paths explicitly as in the tutorial.

`http://127.0.0.1:11435/asr/status` shows resolved paths and `path_source` (`manual/cached/discovered/mixed`). CPU needs a current script copy with `device="cpu"`. An already running 9881 backend may be reused; identify and stop an old instance before expecting changed configuration to take effect.

## References and moving computers

Keep `mayuri-voice/refs/MAY_1158_Neutral.wav` in its relative layout. SPP can search its own and parent directory; for custom storage set the actual `emotion_tts.ref_root`. Clear/fix old paths to nonexistent external folders and inspect `/tts/status`. Other emotion references remain optional downloads.

Preserve the entire personal SPP runtime: authoritative `local_v1`, every profile, legacy JSON/databases, relationships, memories, credentials, persona and usage. Do not rely on an old short file list. Retain original-game progress and `.prev` recovery files, but verify Steam identity again on the new machine. Back up game-side configuration/history separately. `runtime_paths.json` can be rebuilt; `local_v1` cannot be treated as cache.

Copy or reinstall external voice environments, weights, references and optional ONNX. A Python virtual environment may need recreation on another PC. Old Python embedding models are only for rollback; current keyword/ONNX paths do not use them. Install a new version separately and import old memory before changing your long-term runtime location or overwriting old data.

## Failures and hotwords

Unavailable optional TTS/ASR/ONNX components report their own errors without making configured text chat depend on them. Invalid core configuration, non-loopback listening addresses, unsafe core-state initialization or an occupied port can still prevent SPP startup.

Check `hotwords_version=1`, `hotwords_count>0`, `hotwords_backend_supported=true` and the actual script path. A word-list file alone does not prove the model received hotwords. `asr.language=auto` can send Chinese/Japanese words; a forced language follows its selection. Hotwords do not guarantee accuracy: use F8 and inspect game ASR/SPP logs. See [voice diagnosis](VOICE_SETUP.md#asr-troubleshooting).
