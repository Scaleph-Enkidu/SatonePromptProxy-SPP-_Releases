[简体中文](../../zh-CN/releases/AIChat_v1.16.23_SPP_v5.8.26.md) | [English](AIChat_v1.16.23_SPP_v5.8.26.md) | [日本語](../../ja/releases/AIChat_v1.16.23_SPP_v5.8.26.md)

# AIChat v1.16.23 SPP v5.8.26

[← Release archive](../RELEASE_ARCHIVE.md)

> Historical release record. Availability and test claims refer to the original date; use the current guides for installation.

CP14-9 paired release, 2026-09-28. New OpenAI configurations suggested `gpt-6-luna`, DeepSeek `deepseek-flash`, dated 2026-09-28. Existing custom models were retained and names remained editable; availability followed the provider's documentation. Choosing a company/key/model first created a draft; Save and apply performed the switch. Relay settings followed the relay's API.

Earlier response-state, voice, error and memory fixes continued. The maintainer confirmed the main features of 1.16.22 + 5.8.26 in game; the new default-model change passed 13 local CI checks. SPP fixed Windows' built-in administrator being displayed as `LA` and valid private credential permissions incorrectly being rejected.

The package added `mayuri-voice/refs/MAY_1158_Neutral.wav`. GPT-SoVITS/runtime and Bocchi GPT/SoVITS weights remained external. Other emotion WAVs and Fun-ASR models were not bundled.

The original instructions downloaded both component ZIPs, stopped game/SPP, replaced DLL/PDB and extracted the full SPP separately while preserving config, keys, persona and memory. An external `emotion_tts.ref_root` needed correction or clearing. Rollback restored the paired programs and backups; switching models required no save migration. Use the current [installation](../INSTALL.md) and [upgrade](../UPGRADE.md) for current releases.

Local CI covered core/UI/paired flows and DLL/EXE builds. Real OpenAI/DeepSeek calls and 1.16.23 voice results still needed checks on the user's hardware. No player data or personal keys were bundled.

## Original manifest and hash identifiers

[JSON](../../../releases/AIChat_v1.16.23_SPP_v5.8.26.json) · [原文 / Original](../../zh-CN/releases/AIChat_v1.16.23_SPP_v5.8.26.md)

- `570db4e02b6fdb216923cc8585fd3c590607061211bfed8da77af652c9684a8f`
- `b9c7ed3eba98d428d740cb2f46d2aeb2cb571e3d3274679ca37f876c6716e6da`
- `ad79cf940b28545f2034c841755fb6c5a9479b250e45763d7fecf629bf0a9970`
