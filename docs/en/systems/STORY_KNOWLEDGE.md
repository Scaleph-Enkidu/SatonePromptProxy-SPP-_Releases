[简体中文](../../zh-CN/systems/STORY_KNOWLEDGE.md) | [English](STORY_KNOWLEDGE.md) | [日本語](../../ja/systems/STORY_KNOWLEDGE.md)

# Story knowledge and shared experiences

[Documentation](../README.md#systems) · AIChat 1.18.30 + SPP 5.10.10

Besides AI conversations, Satone can use confirmed game progress to understand important events that have already happened. Captured story lines, idle speech and click reactions retain their source and can connect later conversations with your experiences in the game.

| Source | Information |
| --- | --- |
| Game-progress synchronization | Completed chapters, important events and relevant current state |
| Organized story knowledge | Facts and character experiences appropriate to confirmed progress |
| Captured original lines | Story dialogue, idle speech and click reactions actually captured |
| AI exchanges in this profile | Memory and relationships formed through the mod |

Sources are handled separately. Original lines are not new player messages, and original-game experiences must not be counted again as ordinary AI relationship rewards.

## Spoiler boundaries

Knowledge sent to the model follows confirmable progress. A future event is not sent as a shared experience just because it exists in the knowledge collection. A player's claim that an event happened differs from confirmed game progress. Unknown identity, progress or state must not be filled in with invented later events. The model can still guess or answer incorrectly; this is not an absolute spoiler guarantee for every wording.

Story knowledge explains what happened; the original-game contribution ledger calculates familiarity. The latter does not change the four AI relationship dimensions or unlock story restrictions, disconnection scenes or persona boundaries. See [affection](AFFECTION.md) and [story coordination](STORY_COORDINATION.md).

## Environmental information

Date/time may be provided when needed. Complete descriptions of the current window view, outfit, glasses and decorations are not yet integrated. Capturing a line does not mean Satone can read the entire screen. The [F10 catalog tool](../tools/STATE_CATALOG.md) helps map internal IDs to descriptions. Changing the environment or items through conversation remains on the [roadmap](../README.md#roadmap).
