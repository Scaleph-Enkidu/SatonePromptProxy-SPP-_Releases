[简体中文](../zh-CN/SPP_README.md) | [English](SPP_README.md) | [日本語](../ja/SPP_README.md)

# SatonePromptProxy 5.10.10: package README

[Documentation](README.md) · [Full installation](INSTALL.md) · [Portable deployment](PORTABLE_DEPLOYMENT.md)

Paired with AIChat 1.18.30, SPP manages model proxying, persona, three memory profiles, relationships, keyword/optional semantic recall and TTS/ASR forwarding. Keep the complete directory layout, for example at `D:\LofiMOD\SatonePromptProxy`.

Run `SatonePromptProxy.exe`, confirm listening on `127.0.0.1:11435`, and keep the window open. Configure the SPP path, provider key and model in F9, then save/apply. First startup creates `config.json` from `config.example.json`; do not overwrite your personal file with the example. `Start_Text_Chat.bat` starts the same service. See [service management](systems/SERVICES.md) for other tools and auto-start.

Text and keyword recall need no Python. Optional CPU ONNX E5 int8/ORT is a separate approximately 94 MB component; stop SPP before Verify/Enable. TTS and ASR do not depend on it. The package supplies `mayuri-voice/refs/MAY_1158_Neutral.wav`, not GPT-SoVITS, voice weights or the Fun-ASR model. [Voice setup](VOICE_SETUP.md) explains environments and tests.

The game's shared voice URL is `http://127.0.0.1:11435`; SPP forwards to TTS 9880 and ASR 9881. Follow [installation](INSTALL.md) for paths, state checks and CPU steps. The SPP log window is not a shell.

For upgrades, stop services and preserve the whole old runtime, then import into a new directory. Never treat `local_v1` as disposable cache. `SatonePersona_v4.6.txt` is shared; long-term relationships are separate per profile. Large-history cold starts remain slow; see [hardware](HARDWARE.md). Protect keys, conversations and vector caches as described in [data/privacy](DATA_AND_PRIVACY.md).

This release combines nine fixes across memory import, voice echo filtering, exit cleanup and date-based recall. Update both AIChat and SPP. The three-language guides and package entry points are updated together.
