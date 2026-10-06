[简体中文](../../zh-CN/systems/RECOVERY.md) | [English](RECOVERY.md) | [日本語](../../ja/systems/RECOVERY.md)

# Reply validation and recovery

[Documentation](../README.md#systems) · AIChat 1.18.28 + SPP 5.10.8

The system distinguishes a model's generated answer, the program's accepted answer and what the player actually saw or heard. This reduces the effect of malformed output, disconnection and interrupted playback on memory, relationships and repeated-question judgments.

## Validation

Replies require valid emotion tags, speech/subtitle fields and segment limits. Missing fields, invalid tags, excess length or incomplete provider output cannot simply pass straight into subtitles and speech. The program may attempt format repair and bounded regeneration within retry/time budgets; persistent failures end with the appropriate failure state. This is not unlimited retry, fact checking or a translation guarantee.

| Presentation | What later processing may use |
| --- | --- |
| Text and speech completed | Confirmed content for context, memory and relationships |
| Only subtitles completed | Confirmed visible text; not an invented completed audio track |
| Only speech completed | Confirmed playback; not an assumption that all subtitles appeared |
| Partly shown/played | Only confirmed portions, retaining incomplete status |
| Unpresented, late or unconfirmable receipts | Not the entire candidate as a received answer |

Candidates may remain in local diagnostics/recovery records without being treated as full shared experiences. Legacy imports and compatibility paths without new presentation tracking follow their historical handling; these rules do not retroactively reclassify every old record.

## Disconnection and duplicate requests

Local records retain request/background-task progress so reconnects and restarts can resume from known state and avoid applying the same reward, penalty or memory write twice. Unknown outcomes are not treated as success.

If a remote model completed work but its result was not reliably recorded locally before interruption, recovery may call it again. **Preventing duplicate local effects does not guarantee one remote call.** Failures, cancellations and recovery may incur API usage.

For pending-confirmation or retained-input messages, inspect the state and use the UI's recovery actions. Do not delete `local_v1`, whole profiles or credentials merely to clear a warning. Record versions, time, input method, visible/audible output, UI state and redacted logs. Distinguish recognition, model, synthesis and playback failures. See [services](SERVICES.md) and [privacy](../DATA_AND_PRIVACY.md).
