[简体中文](../zh-CN/README.md) | [English](README.md) | [日本語](../ja/README.md)

# Satone Mod: conversations that continue, relationships that grow

An unofficial mod for **Chill with You: Lo-Fi Story on Windows/Steam**. AIChat provides in-game chat, subtitles, playback and controls. SatonePromptProxy (SPP) handles model connections, persona, memory, relationships and voice forwarding. The program supports **Chinese, English and Japanese UI/subtitles**. Speech quality in each language still depends on the chosen voice/model; the documented setup uses Japanese speech.

**AIChat 1.18.30 + SPP 5.10.10**. This release combines nine fixes across memory import, voice echo filtering, exit cleanup and date-based recall. Update both AIChat and SPP. The three-language guides and package entry points are updated together.

![Installed chat interface](../images/install-success.png)

## Before installation: resource limits

**Running the game, GPT-SoVITS and Fun-ASR together adds CPU/RAM demand and several GB of VRAM.** Treat **8 GB VRAM as an evaluation starting point for full GPU voice, with 12 GB+ offering more headroom**, not a verified minimum. At 6 GB, consider GPU TTS + CPU ASR; at 4 GB or integrated graphics, start with text. Cloud chat does not load its LLM locally; hosting your own local LLM adds separate requirements.

A 2026-09-27 screenshot showed two unidentified Python processes at approximately 2.17/1.92 GiB and the game at 0.63 GiB. Do not sum process readings into a whole-card peak. Historical synthetic tests of SPP+ONNX observed approximately **441/944 MB RAM** and **11.65/495.12 seconds startup** for 10,000/50,000 records, excluding game/TTS/ASR. The 350 MB gate covered only the worker.

**Large-history cold starts remain slow, the reported game frame-rate drop is unresolved, and no universal low-VRAM mode has been fully validated.** AMD/Intel GPUs cannot use NVIDIA CUDA instructions unchanged; start with text and CPU ONNX. Approximately 43 MB trilingual program and 94 MB model download sizes are not memory limits. Read the [hardware evidence and scope](HARDWARE.md).

## Install, upgrade and troubleshoot

| Task | Guide |
| --- | --- |
| First installation | [Complete four-stage tutorial](INSTALL.md) |
| Program and checksums | [Downloads and SHA-256](DOWNLOADS.md) |
| Existing installation | [Upgrade, memory import and rollback](UPGRADE.md) |
| Optional semantic recall | [ONNX setup](ONNX_SETUP.md) |
| Speech, microphone and diagnosis | [Advanced voice setup](VOICE_SETUP.md) |
| API spending | [Costs and billing](API_COST.md) |
| Back up or move | [Data and privacy](DATA_AND_PRIVACY.md) · [Portable deployment](PORTABLE_DEPLOYMENT.md) |
| Package documentation | [AIChat README](AIChat_README.md) · [SPP README](SPP_README.md) · [Install/rollback](PACKAGE_INSTALL.md) |

Stages are **1 text → 2 optional ONNX → 3 optional TTS → 4 optional ASR**. Text works by itself; the other components are individually optional, and TTS/ASR do not require ONNX. F9 opens chat, Enter sends, Shift+Enter adds a newline, F8 is push-to-talk. Continuous conversation must be explicitly enabled.

N15 removes cup actions from Relaxed. Existing users must refresh `StablePoseOverrides` to `Relaxed=752,50,51`; see the upgrade guide. N14's reference-policy refresh fix remains included. When changing SPP directories, use the new installation's old-memory import action and retain the old directory.

## Memory, personality and shared experiences

The persona draws on more than 1,700 original lines and retains Satone's autonomy, voice and boundaries. She can be affectionate, joke or share voluntarily, and she can refuse. High affection is not unconditional obedience. The 26 emotions describe individual speech segments rather than fixed relationship rewards.

Three profiles store separate conversations, long-term memory and AI relationships, continuing across model/provider changes. Each turn uses selected recent text, summaries and relevant history. Keywords cover all available history; optional ONNX semantics covers the latest 50,000 eligible exchanges without deleting older authoritative records. `SatonePersona_v4.6.txt` is shared across profiles.

Original story knowledge follows confirmed identity/progress; chapter 31 and other disconnection states respect the game. Failed identity synchronization does not itself mean all AI chat is unavailable, but it cannot establish fictional progress. The original-game familiarity bonus is separate from AI affection, trust, comfort and openness.

Full window/outfit/glasses/decoration awareness is not yet integrated. Persistent questions about why she will not look outside can trigger a Meta sequence of avoidance, disconnection and glitches. The author found even the text-only performance scarier than expected. It can be disabled/reset, and new sessions start at stage 1. Read the [Meta controls and spoiler section](systems/META.md).

<a id="systems"></a>
## System guides

- [Persona](systems/PERSONA.md)
- [Affection calculation](systems/AFFECTION.md)
- [Boundaries and repair](systems/BOUNDARIES.md)
- [26 emotions](systems/EMOTIONS.md)
- [Memory and profiles](systems/MEMORY.md)
- [History retrieval](systems/RECALL.md)
- [Story knowledge](systems/STORY_KNOWLEDGE.md)
- [Original-story coordination](systems/STORY_COORDINATION.md)
- [Meta performance](systems/META.md)
- [Chat UI and history](systems/CHAT_UI.md)
- [Validation and recovery](systems/RECOVERY.md)
- [Model connections](systems/CONNECTIONS.md)
- [Service management](systems/SERVICES.md)
- [Speech and subtitles](systems/SPEECH.md)
- [Voice input and continuous conversation](systems/VOICE_INPUT.md)

## Optional F10 appearance catalog

[SatoneStateCatalog](tools/STATE_CATALOG.md) reads active appearance IDs and lets you describe them. It does not unlock content or modify saves, and does not give Satone scene controls. See [building from source](tools/BUILD_STATE_CATALOG.md) and [IDs awaiting observation](tools/OBSERVED_IDS.md). Build evidence is distinguished from in-game testing.

<a id="roadmap"></a>
## Future work

Improve speech and language-appropriate voices, build the appearance-description catalog and explore conversational control of environments/items. Chinese/English/Japanese UI and subtitles are now current features, not pending roadmap work. Chinese speech and other voice outcomes still depend on suitable models and further testing.

## Releases, credits and licensing

[Trilingual documentation revision](releases/DOCS_TRILINGUAL_20261006.md) · [N15 notes](releases/AIChat_v1.18.28_SPP_v5.10.8.md) · [History and verification archive](RELEASE_ARCHIVE.md)

AIChat is based on [qzrs777/AIChat](https://github.com/qzrs777/AIChat) by Elysia777. Scaleph maintains this project with AI-assisted development. Licensable original content uses PolyForm Noncommercial 1.0.0; upstream, third-party and previously granted MIT rights remain. See [scope](LICENSE_SCOPE.md), [LICENSE](../../LICENSE) and [NOTICE](../../NOTICE). GPT-SoVITS, Fun-ASR, E5, ORT, voice models and recordings retain their own source conditions.


[Nine fixes in this release](releases/AIChat_v1.18.30_SPP_v5.10.10.md)
