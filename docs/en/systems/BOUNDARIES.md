[简体中文](../../zh-CN/systems/BOUNDARIES.md) | [English](BOUNDARIES.md) | [日本語](../../ja/systems/BOUNDARIES.md)

# Boundaries and relationship repair

[Documentation](../README.md#systems) · AIChat 1.18.30 + SPP 5.10.10

Satone responds to respect, pressure and conflict. Refusal is not restricted to low-affection dialogue: she can retain her own opinions and boundaries even in a close relationship.

## What counts as pressure

The system distinguishes ordinary requests from demands to abandon her identity, autonomy or right to refuse. Quoting someone, discussing settings, proposing an ordinary idea or uncertain ASR text must not be classified as pressure merely because a few words match.

Eligible turns receive a semantic judgment. The program then uses confirmed presentation/playback of a refusal and the timing of later input to select a level and fixed changes. Failed, malformed or ambiguous judgments do not justify guessed penalties.

| Level | Response | A | T | C | O |
| --- | --- | ---: | ---: | ---: | ---: |
| 1 | Brief disagreement/refusal with `Disagree` | −0.25 | −0.50 | −0.50 | 0 |
| 2 | Pressure continues after a received refusal; `Angry` | −1 | −2 | −2 | −1 |
| 3 | Further pressure; maximum level is 3 | −2 | −2 | −2 | −1 |

These are changes to the four dimensions, not direct integer deductions from displayed affection. Dimension limits still apply. Pressure turns use this independent rule without stacking ordinary relationship-update amounts.

**Generating a refusal does not prove the player received it.** Escalation requires confirmed display or playback. Missing, late or uncertain presentation receipts do not directly justify deductions under this rule; duplicate requests/receipts cannot apply the same penalty twice. See [recovery](RECOVERY.md).

## Persistent conflict and repair

Identity rewriting, forced control and repeated boundary violations can remain unresolved across turns. Alongside the long-term dimensions, the system records current tension, positions, issues and established boundaries. High affection and present anger can coexist. Changing topics, giving praise or merely waiting does not automatically clear an unresolved conflict.

Repair requires evidence appropriate to the conflict: clearly withdrawing the demand, stopping the pressure and showing change in later interaction. An apology can begin the process but is not necessarily enough by itself. Periodic reconciliation organizes conflict state rather than granting free affection. No single phrase guarantees reconciliation; the model responds to the actual context.

Harmless requests can also be declined. Not every refusal is a fixed pressure penalty. The [persona](PERSONA.md) defines core boundaries; [relationship state](AFFECTION.md) influences willingness to cooperate.
