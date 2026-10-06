[简体中文](../../zh-CN/releases/AIChat_v1.17.0_SPP_v5.9.0.md) | [English](AIChat_v1.17.0_SPP_v5.9.0.md) | [日本語](../../ja/releases/AIChat_v1.17.0_SPP_v5.9.0.md)

# AIChat v1.17.0 SPP v5.9.0

[← Release archive](../RELEASE_ARCHIVE.md)

> Historical release record. Availability and test claims refer to the original date; use the current guides for installation.

Official pair dated 2026-10-01. The user confirmed local testing; this did not cover every hardware/provider/voice combination.

Documentation revision 1 supplied standalone package README, installation and changelog text without changing programs/models. Existing users did not need runtime updates for that revision. The original INSTALL attachment retained its released bytes; revised guides lived in the docs_r1 archive. Model URLs/hashes stayed unchanged.

Text and keyword recall became independent of the old Python embedding environment; text input worked without microphone components. Optional E5 small int8 and Windows x64 ORT CPU 1.30.0 were distributed separately and disabled by default. Missing/bad/busy/failed semantic components fell back to keywords and did not become a mandatory turn-settlement dependency.

The paired program was about 11 MB and optional model about 94 MB. Compatible program updates could reuse the checked component. Complete `models` went beside the EXE; Verify/Enable/Disable ran while stopped. The first query triggered warm-up/vector preparation with per-profile status; old Dashboards without a Recall area could use local endpoints.

Recall indexed accepted, actually presented communication. Old databases remained; semantics covered the latest 50,000 records, keywords the full history, and authority records were not deleted. Recall recovery did not regenerate confirmed replies or repeat confirmed relationship/memory effects. Installation was rewritten into text, ONNX, TTS and ASR stages. Default Neutral was bundled; environments/weights were external. The private repositories' separate component ZIPs were not extra requirements, and Source code ZIP was not an installer.

Historical update advice was to stop all services, back up, replace programs/tools and retain credentials, `local_v1`, all `memory_profiles`, custom persona, models, `semantic_recall_v1` and voice assets. Do not delete the runtime or replace personal config with an example. Whole-version rollback needed matching old programs and pre-upgrade data; disabling ONNX alone used its tool. For today's procedure use [UPGRADE](../UPGRADE.md).

Verification: D round 2 passed 14 backend + 9 client checks; extraction/overlay covered 11 passing branches. Real ONNX synthetic retrieval achieved 12/12 positive Top1, 10/12 qualified and 0/3 negative qualified, not a guarantee for player queries. With 20 ms working-set sampling, a 50,000-record real-format synthetic WAL took about 495 s to cold-start; pipeline peak was 943,693,824 B. The worker/vector-only 350 MB gate observed 332,283,904 B and was not a whole-SPP memory cap. Large WAL startup remained slow; no universal clean-machine/provider/voice claim was made. Cloud API charges followed live provider billing; no credits were included.

## Original manifest and hash identifiers

[JSON](../../../releases/AIChat_v1.17.0_SPP_v5.9.0.json) · [原文 / Original](../../zh-CN/releases/AIChat_v1.17.0_SPP_v5.9.0.md)
