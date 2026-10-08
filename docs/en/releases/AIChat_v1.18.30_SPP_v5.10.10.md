[简体中文](../../zh-CN/releases/AIChat_v1.18.30_SPP_v5.10.10.md) | [English](AIChat_v1.18.30_SPP_v5.10.10.md) | [日本語](../../ja/releases/AIChat_v1.18.30_SPP_v5.10.10.md)

# AIChat 1.18.30 + SPP 5.10.10

2026-10-08

This release combines nine fixes across memory import, voice echo filtering, exit cleanup and date-based recall. Update both AIChat and SPP. The three-language guides and package entry points are updated together.

1. Recognize modern `local_v1` saves first and import read-only. Pending WAL or writer locks block unsafe reads; profiles, summaries and communicated content are preserved.
2. Use only speech that has actually started playing as a TTS echo candidate. Future segments and subtitle-only content no longer suppress matching player input.
3. Use a monotonic capture clock for native-line echo evidence, including delayed ASR results. Restored history is not treated as freshly played speech.
4. Run exit cleanup in a separate hidden process so it survives game shutdown, with process identity checks before termination.
5. Apply date constraints before keyword/semantic ranking and TopK so out-of-range hits do not crowd out matching history.
6. Interpret “last weekend” as the weekend of the previous Monday-based calendar week, including the Sunday boundary.
7. Parse the full number in “last N days” before enforcing the 1–30 day limit; numbers such as 101 cannot match through a numeric suffix.
8. Give each legacy import retry its own staging snapshot and clean up that attempt. Repaired sources and deleted files are no longer mixed with stale data from a failed attempt.
9. Refresh echo timing when the same native line plays again, even if the history list deduplicates it, so freshly replayed speech is still filtered.

Prior repair validation: 666 top-level Go tests passed, 9 skipped; all five EXE pair tests passed; 1,548 C# assertions passed. Packaging checks cover source identity, binaries, per-file SHA-256, offline language links and extracted startup. This release has no new real-game, microphone or external-model acceptance result; historical N15 field tests do not certify this version. Large-history startup delays and reported frame-rate drops remain under investigation.

[Download / 下载 / ダウンロード](../DOWNLOADS.md) · [Upgrade / 升级 / 更新](../UPGRADE.md)
