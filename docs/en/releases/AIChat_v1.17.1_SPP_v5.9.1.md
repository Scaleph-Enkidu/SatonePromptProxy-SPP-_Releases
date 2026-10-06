[简体中文](../../zh-CN/releases/AIChat_v1.17.1_SPP_v5.9.1.md) | [English](AIChat_v1.17.1_SPP_v5.9.1.md) | [日本語](../../ja/releases/AIChat_v1.17.1_SPP_v5.9.1.md)

# AIChat v1.17.1 SPP v5.9.1

[← Release archive](../RELEASE_ARCHIVE.md)

> Historical release record. Availability and test claims refer to the original date; use the current guides for installation.

Official pair dated 2026-10-01. AIChat resynchronized original-game progress after connection/configuration changes and service recovery, showed synchronization before first binding and refreshed affection after success. Model switching showed a Chinese success message; TTS reference names/reasons were grouped under failure reasons.

Window and history-box backgrounds gained independent opacity (0.00 transparent, 1.00 opaque). Custom history color added RGB/lightness without merging settings, title, input and history layout areas. The history notice specified the latest 50 utterances, and the title was AIChat Remake console. Existing chat, native subtitles/animations, three profiles, relationships/emotions, Meta, F8 and continuous conversation remained.

SPP 5.9.1 rebuilt with the new application version; other core service logic retained the tested implementation. Start_Text_Chat.bat ran the same-directory SPP in the current console and retained launch errors/exit code with a key wait. Verify/Enable/Disable semantic scripts used stable ASCII commands and CRLF to fix Windows CMD parsing. The paired guide added direct EXE launch, BAT fallback, semantic troubleshooting and real retained-input copy/export/remove controls.

No new memory migration, model version, FPS fix or large-WAL acceleration was claimed. ONNX stayed optional/reusable. Historical upgrades stopped services, backed up and replaced DLL/PDB/EXE/tools while retaining configuration, credentials, all memory/history, models/cache and voice environments. Current upgrades use [UPGRADE](../UPGRADE.md). Local build/UI/synchronization regression and packaging were not proof of every game scene being tested; frame-rate root cause and large-save cold start remained unresolved.

## Original manifest and hash identifiers

[JSON](../../../releases/AIChat_v1.17.1_SPP_v5.9.1.json) · [原文 / Original](../../zh-CN/releases/AIChat_v1.17.1_SPP_v5.9.1.md)
