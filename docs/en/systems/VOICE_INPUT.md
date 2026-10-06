[简体中文](../../zh-CN/systems/VOICE_INPUT.md) | [English](VOICE_INPUT.md) | [日本語](../../ja/systems/VOICE_INPUT.md)

# Voice input and continuous conversation

[Documentation](../README.md#systems) · AIChat 1.18.28 + SPP 5.10.8

The microphone records your voice, Fun-ASR converts it to text, then the chat model receives that text. ASR recognizes you; TTS speaks for Satone. They can be installed independently.

| Mode | Operation | Use |
| --- | --- | --- |
| Push to talk | Hold F8 to record, release to submit; UI button also available | Control each recording and test short recognition first |
| Continuous conversation | Enable listening on the selected microphone; VAD separates utterances | Speak without holding a key each time |

Both modes use the same selected microphone. Missing, disabled, loading and ready are different component states. Story/disconnection restrictions still apply.

## Detection and buffering

VAD decides when speech starts and stops. Too high a threshold misses quiet speech; too low can accept fans, keyboards or background sound. The pause setting affects when an utterance is submitted. A short pre-speech buffer preserves audio before detection, reducing clipped beginnings. It cannot fix model recognition errors or guarantee segmentation on every device.

## Queues and stopping

Recorded but incomplete inputs are managed by session, profile and processing state. A full queue, save failure or retained input awaiting confirmation may pause listening to preserve existing recordings. Stopping a call does not necessarily erase queued input or mean that no server received a request. Handle retained input individually through the [recovery instructions](../INSTALL.md#preserved-voice).

When interrupting playback, later memory/relationship processing uses confirmable actual communication, not the whole unheard response.

## Diagnosis

1. Use F8 for a short sentence; confirm microphone input and reasonable transcription.
2. For missing initial words, save raw audio or run the microphone test to see whether recording itself lost them.
3. If audio is intact but text is wrong, inspect model, noise and hotword support. Hotwords do not guarantee correct recognition.
4. Once F8 works, change continuous-conversation settings one at a time and save/apply.

The separate 10-second quiet/speaking tests save locally without ASR. Saving the next push-to-talk raw recording still performs normal recognition. See [voice diagnostics](../VOICE_SETUP.md#asr-troubleshooting).
