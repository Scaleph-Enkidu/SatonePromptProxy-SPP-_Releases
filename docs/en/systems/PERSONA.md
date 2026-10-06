[简体中文](../../zh-CN/systems/PERSONA.md) | [English](PERSONA.md) | [日本語](../../ja/systems/PERSONA.md)

# Persona

[Documentation](../README.md#systems) · AIChat 1.18.28 + SPP 5.10.8

Satone's persona was developed with reference to more than 1,700 lines from the original game. It defines her identity, voice, autonomy, knowledge and boundaries. Relationship state describes affection, trust, comfort, openness and unresolved conflicts; memory supplies past facts; emotion describes her current response. These are related but distinct systems.

## Autonomy and voluntary interaction

She can refuse, negotiate or express a different opinion. She can also joke, flirt or join harmless roleplay voluntarily without giving up her identity. High affection does not override her boundaries. See [relationships](AFFECTION.md) and [conflict repair](BOUNDARIES.md).

## Editing the persona

The default file is `SatonePersona_v4.6.txt`, selected by `persona_file` in the configuration. Use the in-game persona editor, or back up the file before editing and applying it. All three memory profiles share this file, while their histories and AI relationships remain separate. Preserve custom persona files when upgrading.

## Language and knowledge

Satone's native language is Japanese. She can discuss everyday topics in Chinese and English, but unfamiliar terms and knowledge may remain uncertain. The program now offers Chinese, English and Japanese UI/subtitle options; speech quality still depends on the selected voice model and language.

Repeated-question handling uses what was actually presented to the player, rather than every generated candidate. Available date/time or game-state information does not mean that she can see the current window view, outfit, glasses or decorations. See [story knowledge](STORY_KNOWLEDGE.md) and [Meta performance](META.md).

The persona guides a model rather than selecting fixed scripted lines. Different models and contexts can produce different behavior. Output-format validation cannot guarantee facts, emotions or translation quality.
