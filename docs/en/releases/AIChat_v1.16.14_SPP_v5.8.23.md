[简体中文](../../zh-CN/releases/AIChat_v1.16.14_SPP_v5.8.23.md) | [English](AIChat_v1.16.14_SPP_v5.8.23.md) | [日本語](../../ja/releases/AIChat_v1.16.14_SPP_v5.8.23.md)

# AIChat v1.16.14 SPP v5.8.23

[← Release archive](../RELEASE_ARCHIVE.md)

> Historical release record. Availability and test claims refer to the original date; use the current guides for installation.

This combined distribution reused the two official component ZIPs unchanged, without recompilation; hashes matched their source releases. At that time the release repository was private and downloads needed access. Public release-repository access would not require access to either private source repository. No clean-Windows end-to-end installation test was claimed.

AIChat's source was `0e3aadeec171fa07b798baf517650f42ff441c95`; SPP's was `bc6e22e184ad98fde472374abcae65ca72364831`. AIChat's original BUILD_INFO still named SPP 5.8.22 from its build; this distribution paired that same AIChat with 5.8.23 without rewriting its archive.

SPP 5.8.23 scheduled memory organization at 32,000 total API input tokens with an approximate recent-text retention target of 12,000. In-game long-conversation acceptance remained pending.

The original installation used `AIChat_v1.16.14.zip` (DLL into BepInEx/plugins) and the complete `SatonePromptProxy_v5.8.23.zip` in its own directory. `_SHA256.txt`, the original AIChat MIT/attribution file and the JSON manifest were verification/legal material, not plugins. BepInEx and your own API Key were required; voice/microphone needed external environments/models/references. GitHub's automatic Source code ZIP was not the installer and Git was unnecessary.

Upgrade advice at the time was to exit services, back up personal data, replace the single DLL and preserve SPP configuration, persona, memories, relationships and audio. Use today's [upgrade guide](../UPGRADE.md) for current versions. Old keys/history remaining after DLL replacement came from separately saved local files.

The ZIP inventory contained no personal CFG, live config.json, runtime_paths.json, chat history, memory_profiles or logs; official templates/docs remained. Hash/inventory checking was not a full binary audit.

## Original manifest and hash identifiers

[JSON](../../../releases/AIChat_v1.16.14_SPP_v5.8.23.json) · [原文 / Original](../../zh-CN/releases/AIChat_v1.16.14_SPP_v5.8.23.md)

- `65684dac51fdae292d0e4676dc1a458396c5bb01a63e15472537f5c5b8143cf1`
- `bcad7805fa8193b8efd9a14e82ef8be16b65d9d9f6c86fad674719cc17150c6e`
