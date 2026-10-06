[简体中文](../../zh-CN/systems/MEMORY.md) | [English](MEMORY.md) | [日本語](../../ja/systems/MEMORY.md)

# Memory and profiles

[Documentation](../README.md#systems) · AIChat 1.18.28 + SPP 5.10.8

Satone does not send every past conversation in every model request. Local records are retained; each turn combines recent exchanges, organized memory and relevant retrieved history.

## Three independent profiles

Memory 1, Memory 2 and Memory 3 have separate conversations, long-term memory and AI relationships. Switching selects that profile's experiences. The persona file is shared, and providers/models can change while retaining the same profile's local memory and relationship. A different model can still change tone or understanding. Memory 3's default maximum-affection test preset differs from an ordinary new profile; see [affection](AFFECTION.md).

| Content | Role |
| --- | --- |
| Recent original text | Continuity for the current topic |
| Long-term summary | Important information organized from older exchanges |
| Full local records and history index | Stored experiences retrieved when relevant, not all sent every turn |

The window's latest 50 utterances are not a storage limit. Summaries may omit details and retrieval may miss them. Being saved locally does not mean the model saw the information in this request.

## Automatic organization

The default threshold is **32,000 tokens**, with a recent-text retention target of about **12,000 tokens**. Tokens are model text units, not a character count. Local chat also considers the estimated request budget and recent message count and can organize earlier near a limit.

These figures are neither a universal context limit nor a promise that every request uses exactly that many tokens. Persona, input, summaries and other context also consume space; connection-specific budgets affect timing.

Older exchanges are summarized while original records remain. Generated but unpresented/unplayed content must not be remembered as already communicated. If summarization fails, history is retained and success is not assumed. A request may be unable to continue if its context still exceeds the budget.

## Storage and upgrades

Authoritative local-chat records reside in `local_v1`; profile data also appears in `memory_profiles`. Older installations may retain legacy JSON, text and database files. A legacy file not changing does not prove that new conversations were lost.

Exit the game and services, then back up the entire personal SPP runtime folder plus game-side configuration and history. Authoritative records are not disposable cache. Follow [data, backup and privacy](../DATA_AND_PRIVACY.md) and the [upgrade guide](../UPGRADE.md).
