[简体中文](../zh-CN/PACKAGE_CHECKLIST.md) | [English](PACKAGE_CHECKLIST.md) | [日本語](../ja/PACKAGE_CHECKLIST.md)

# Post-upgrade checklist

Prior repair validation: 666 top-level Go tests passed, 9 skipped; all five EXE pair tests passed; 1,548 C# assertions passed. Packaging checks cover source identity, binaries, per-file SHA-256, offline language links and extracted startup. This release has no new real-game, microphone or external-model acceptance result; historical N15 field tests do not certify this version. Large-history startup delays and reported frame-rate drops remain under investigation.

## N15 fix

- Refresh the old CFG so Relaxed uses `752,50,51`.
- Try at least three relaxed conversations that elicit `[Relaxed]`. The `[Satone14/动画] 整轮回复动作` log should use id:752/id:50/id:51, not 256/751/753/755/52. No cup/prop should remain.
- Optionally back up configuration, set `PreferStableConversationPoses=false`, test the standard pool, then restore the setting. Historical in-game evidence covers two whitelist turns (id:50/id:752); the standard pool had static review only.
- Confirm `Loading [AIChat Remake 1.18.30]` in the log.

## Regression samples

- Continue after moving/restarting SPP; check that all requests no longer fail with 409 while only subtitles remain.
- Check collapse arrows, submenus, old-memory import, profile headings and long-path fields.
- Toggle emotion display and check the history label before timestamps.
- Check self-echo filtering, opening greetings and original snack lines entering history.
- Select Chinese, English and Japanese and check UI/subtitle choices. Inspect actual text and speech separately; translated UI is not all-language voice acceptance.

Useful logs include actions, original-animation suppression, `[VoiceCall/Echo] suppressed` and `[TTS]`. Remove keys/private dialogue before reporting.

This release combines nine fixes across memory import, voice echo filtering, exit cleanup and date-based recall. Update both AIChat and SPP. The three-language guides and package entry points are updated together.

Recheck failed-import retries, all three profiles and summaries, echo filtering for repeated native lines, delayed ASR, date-constrained recall, and managed-process cleanup after game exit.
