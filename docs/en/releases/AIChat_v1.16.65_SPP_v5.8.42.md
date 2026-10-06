[简体中文](../../zh-CN/releases/AIChat_v1.16.65_SPP_v5.8.42.md) | [English](AIChat_v1.16.65_SPP_v5.8.42.md) | [日本語](../../ja/releases/AIChat_v1.16.65_SPP_v5.8.42.md)

# AIChat v1.16.65 SPP v5.8.42

[← Release archive](../RELEASE_ARCHIVE.md)

> Historical release record. Availability and test claims refer to the original date; use the current guides for installation.

CP21 paired release, 2026-09-30, following 1.16.23 + 5.8.26. It included CP19-1 reasoning effort/fallback, CP20 progress-gated story knowledge, CP21 original-line timeline and a chat-window iteration (bubbles, fonts, single-line input and resize handles).

Meta stages became replayable per game session, starting at stage 1 on launch. A same-session reset used a new idempotent endpoint and atomic write. The historical notes described a first ending retaining glitches and subsequent completion exiting normally, with persistent ending detection; consult [current Meta behavior](../systems/META.md) for the present session rules. Scene records remained for the current session and were removed on next login, preserving ordinary dialogue. Records from 5.8.41 and earlier remained replayable without new `recovery_required` errors.

Original upgrade instructions replaced the paired programs after backup and kept configuration, persona and memories; current users should follow [UPGRADE](../UPGRADE.md). The preceding stable release was available then but was later withdrawn; see the [archive](../RELEASE_ARCHIVE.md).

The independent F10 SatoneStateCatalog tool was included in the repository to record active appearance IDs/descriptions under `BepInEx/config/SatoneStateCatalog`, without save changes or unlocking.

This was a local real-machine build without a matching CI workflow run. AIChat built with zero errors and six passing test projects. SPP go vet was clean; tests passed apart from five known environment failures (one ASR and four Recall/Python). Its window arc/reset endpoint was checked against a copy of a player's real 470-commit save. Real APIs, Unity and voice on different devices remained outside that universal acceptance claim. No personal keys/player data were included.

## Original manifest and hash identifiers

[JSON](../../../releases/AIChat_v1.16.65_SPP_v5.8.42.json) · [原文 / Original](../../zh-CN/releases/AIChat_v1.16.65_SPP_v5.8.42.md)

- `270923a5ba46796f0f119e82f94fc23d9959bbb65e89fd81b0e0447249819d42`
- `e18dabb5253a332d18124f80aa43bae39a467394da415fb67e01b6dfbef61e85`
- `ad79cf940b28545f2034c841755fb6c5a9479b250e45763d7fecf629bf0a9970`
