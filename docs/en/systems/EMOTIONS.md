[简体中文](../../zh-CN/systems/EMOTIONS.md) | [English](EMOTIONS.md) | [日本語](../../ja/systems/EMOTIONS.md)

# Emotions

[Documentation](../README.md#systems) · AIChat 1.18.30 + SPP 5.10.10

Emotions describe the tone of a current segment, not a permanent relationship score. The program supports 26 fixed tags. Their spelling is part of the protocol and must not be translated in configuration.

| UI color group | Tags |
| --- | --- |
| Positive / red | `Happy`, `Excited`, `Relaxed`, `Affectionate`, `Playful`, `Teasing`, `Smug` |
| Negative / blue | `Sad`, `Crying`, `Pouting`, `Angry`, `Chiding`, `Nervous`, `Afraid`, `Shocked`, `Mocking`, `Sarcastic`, `Disagree` |
| Neutral or mixed / yellow | `Neutral`, `Tired`, `Sleepy`, `Confused`, `Curious`, `Think`, `Surprised`, `Shy` |

Colors are display groupings, not affection rewards or penalties. Disconnection and unknown states do not add new emotion tags.

`Happy`, `Relaxed` and `Excited` differ in intensity and situation. `Surprised` is not the same as a stronger `Shocked`. Friendly `Teasing` differs from `Mocking` or `Sarcastic`; `Chiding` can be a reprimand without the full anger of `Angry`. `Curious` denotes real curiosity and `Think` deliberation, not generic engagement. `Tired` and `Sleepy` distinguish fatigue from drowsiness.

High affection does not impose a quota of positive responses. Mood, context and unresolved conflicts still matter. Emotion alone does not prove a relationship change.

Speech uses per-segment tags to select references through `emotion_tts.mapping` and `profiles`. Missing optional references fall back to `Neutral`; the main package supplies the Neutral WAV so all 26 recordings are not required to begin. Labels do not guarantee that different weights, references or environments will express them equally well. See [voice setup](../VOICE_SETUP.md#emotions-26) and [speech/subtitles](SPEECH.md).
