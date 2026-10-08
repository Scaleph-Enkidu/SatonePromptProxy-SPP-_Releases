[简体中文](../../zh-CN/systems/STORY_COORDINATION.md) | [English](STORY_COORDINATION.md) | [日本語](../../ja/systems/STORY_COORDINATION.md)

# Coordinating AI chat with the original story

[Documentation](../README.md#systems) · AIChat 1.18.30 + SPP 5.10.10

AI and original dialogue share the same character, subtitle and audio environment. The plugin reads game state to coordinate speaking and input, reducing overlapping subtitles, voices and actions.

| State | Input behavior |
| --- | --- |
| Original story playing | Story takes priority; new AI input is temporarily blocked |
| Original disconnection or Meta glitch lock | New AI input is blocked; the corresponding state is displayed |
| Unstable synchronization | Status is shown; actual input eligibility still follows story/conversation state |
| Normal | AI chat is available unless another input restriction applies |
| Original state cannot be read | Existing story protection is retained; normality is not invented |

Priority is **story playback → disconnection/Meta lock → unstable → normal**. Keyboard send, F8, buttons, continuous conversation and retries all go through input checks.

## Special chapters

Disconnection stages such as chapter 31 follow actual game state. Changing models, profiles, persona or the game-bonus setting cannot force a return to normal. Recovery requires the original state to recover under the appropriate conditions. The plugin reads progress rather than completing the game through fictional level or waiting-time rules. The familiarity bonus only affects relationship projection.

## Lines and playback

Story dialogue, click reactions, random idle speech and system events have distinct sources. Original subtitles, audio and actions are protected according to their source and playback state. Controls for random speech and random actions are separate.

AI responses play in segments; interruptions record only confirmed presentation/playback. Original audio is not all treated as ordinary AI replies, and a reply still being generated must not overwrite story subtitles.

These rules do not prove that every scene, provider or voice combination is conflict-free. Story freezes, frame-rate drops or device problems still need reproduction. If ordinary scenes remain blocked, record chapter, synchronization message, versions and time, then inspect [service state](SERVICES.md). Do not delete saves or disable all story protection to diagnose it.
