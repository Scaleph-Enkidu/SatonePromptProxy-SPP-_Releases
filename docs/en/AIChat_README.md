[简体中文](../zh-CN/AIChat_README.md) | [English](AIChat_README.md) | [日本語](../ja/AIChat_README.md)

# AIChat 1.18.30: package README

[Documentation](README.md) · [Full installation](INSTALL.md) · [Upgrade](UPGRADE.md)

This is the game-side plugin for Chill with You: Lo-Fi Story on Windows/Steam, paired with SPP 5.10.10. UI/subtitles support Chinese, English and Japanese. Pronunciation depends on external voice models.

Exit the game, install BepInEx 5.4.23.5 x64 and launch once. Put `AIChat/AIChat.dll` and `AIChat.pdb` in the game's `BepInEx/plugins`. Keep one AIChat DLL and place backups outside that directory. F9 opens the console; configure/apply the SPP EXE path and LLM connection. Enter sends, Shift+Enter adds a newline. F8 push-to-talk needs optional ASR. Continuous conversation starts off and must be enabled deliberately.

N15 fixes the Relaxed cup prop. Existing configuration must change its Relaxed `StablePoseOverrides` entry to `Relaxed=752,50,51`, or back up and regenerate only `com.username.chillaimod.cfg`. Do not delete all BepInEx configuration or memories. N14's 409 reference-policy refresh fix remains. See [release notes](releases/AIChat_v1.18.28_SPP_v5.10.8.md).

Displaying 50 recent utterances does not mean only 50 are stored. [System guides](README.md#systems) cover three profiles, persona, affection, emotions, story coordination and Meta scenes. Cloud APIs need your own quota; TTS, ASR and ONNX are individually optional. Read [hardware](HARDWARE.md), [backup/privacy](DATA_AND_PRIVACY.md) and [license scope](LICENSE_SCOPE.md).

This release combines nine fixes across memory import, voice echo filtering, exit cleanup and date-based recall. Update both AIChat and SPP. The three-language guides and package entry points are updated together.
