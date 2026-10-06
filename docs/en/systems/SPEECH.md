[简体中文](../../zh-CN/systems/SPEECH.md) | [English](SPEECH.md) | [日本語](../../ja/systems/SPEECH.md)

# Speech and subtitles

[Documentation](../README.md#systems) · AIChat 1.18.28 + SPP 5.10.8

AIChat presents subtitles and plays audio, SPP segments replies and forwards synthesis requests, and GPT-SoVITS generates speech from text, voice weights and reference audio. The program now has Chinese, English and Japanese UI/subtitle support. That does not imply every installed voice can pronounce all three languages well. The documented reference setup uses Japanese speech.

## Segment correspondence

Replies contain emotion and language fields validated before presentation. In the original Japanese-speech/Chinese-subtitle path, each Chinese field is limited to **41 characters including punctuation**. This is the documented Chinese-path rule, not an asserted universal limit for every localized display. Segmented playback can prefetch later audio. Corresponding language segments should convey the same meaning, but need not match character for character. Format checks cannot guarantee correct translation.

| Resource | Role |
| --- | --- |
| Voice weights | Trained voice and supported model version |
| Reference WAV | Vocal/tone example for synthesis |
| Reference transcript | What the WAV actually says |
| Emotion configuration | Select an available reference; use Neutral when an optional one is missing |

The package includes `mayuri-voice/refs/MAY_1158_Neutral.wav`, not the complete GPT-SoVITS runtime or voice weights. The WAV alone does not install speech, and 26 references are not required to start.

Use the reference status check and expanded failure reasons in TTS settings to inspect paths/files/content/service state. Optional missing emotions may use Neutral. An invalid default reference or failed backend cannot produce reliable speech merely because a setting exists. File validation is distinct from model load and successful playback.

Text chat works without TTS. After installing it, synthesize a short sentence and confirm in-game playback. For interruption, memory/relationship processing uses confirmed visible text and completed audio segments; unplayed candidate text is not all treated as heard. See [recovery](RECOVERY.md), [installation](../INSTALL.md#stage-3) and [advanced voice setup](../VOICE_SETUP.md).
