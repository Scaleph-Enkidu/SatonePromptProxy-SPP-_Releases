[简体中文](../zh-CN/PACKAGE_CHECKLIST.md) | [English](PACKAGE_CHECKLIST.md) | [日本語](../ja/PACKAGE_CHECKLIST.md)

# N15 local verification checklist

Record pass, fail or not reproducible for each item with redacted evidence. These are recheck instructions, not a claim that this documentation revision ran the game again.

## N15 fix

- Refresh the old CFG so Relaxed uses `752,50,51`.
- Try at least three relaxed conversations that elicit `[Relaxed]`. The `[Satone14/动画] 整轮回复动作` log should use id:752/id:50/id:51, not 256/751/753/755/52. No cup/prop should remain.
- Optionally back up configuration, set `PreferStableConversationPoses=false`, test the standard pool, then restore the setting. Historical in-game evidence covers two whitelist turns (id:50/id:752); the standard pool had static review only.
- Confirm `Loading [AIChat Remake 1.18.28]` in the log.

## Regression samples

- Continue after moving/restarting SPP; check that all requests no longer fail with 409 while only subtitles remain.
- Check collapse arrows, submenus, old-memory import, profile headings and long-path fields.
- Toggle emotion display and check the history label before timestamps.
- Check self-echo filtering, opening greetings and original snack lines entering history.
- Select Chinese, English and Japanese and check UI/subtitle choices. Inspect actual text and speech separately; translated UI is not all-language voice acceptance.

Useful logs include actions, original-animation suppression, `[VoiceCall/Echo] suppressed` and `[TTS]`. Remove keys/private dialogue before reporting.
