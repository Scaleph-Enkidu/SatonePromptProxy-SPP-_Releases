[简体中文](../../zh-CN/systems/SERVICES.md) | [English](SERVICES.md) | [日本語](../../ja/systems/SERVICES.md)

# Starting and managing services

[Documentation](../README.md#systems) · AIChat 1.18.28 + SPP 5.10.8

Text chat, semantic recall, speech synthesis and recognition are installed in stages. Missing later services should not block configured text chat. An open console does not mean every model is ready.

| Service | Default local port | Responsibility |
| --- | ---: | --- |
| SPP | 11435 | Chat proxy, persona, memory, relationships, status and TTS/ASR forwarding |
| GPT-SoVITS API | 9880 | Speech synthesis |
| Fun-ASR | 9881 | Microphone recognition |
| ONNX worker | No separate player-managed network service | CPU semantic retrieval managed by SPP |

Keep the game's shared voice URL at `http://127.0.0.1:11435`. Local use needs no router port forwarding.

| Tool | Purpose |
| --- | --- |
| `SatonePromptProxy.exe` | Direct launch used by the installation guide |
| `Start_Text_Chat.bat` | Convenient launch of the same SPP |
| `Set_GPTSoVITS_RunApi_Path.bat` | Save the prepared TTS launch-script path |
| `Start_AIChat_Services.bat` | Start SPP and configured GPT-SoVITS; does not install dependencies/weights |
| `Stop_SatonePromptProxy.bat` | Stop SPP, not uninstall models or delete memory |
| In-game automatic start/stop options | Manage the configured service lifecycle; save and verify actual behavior |

GPT-SoVITS can also use its own `run_api.bat`. Manually launched and plugin-launched processes have different ownership; check each after exiting the game. An auto-stop option does not mean “terminate every Python process.”

## Installed, starting and ready

Missing files, loading and passing a current health check are distinct states. Confirm TTS with actual playable synthesis and ASR with an actual recognized utterance. Repeated launches can occupy ports and duplicate model memory. Check existing processes and preserve the first error/full path rather than repeatedly double-clicking scripts.

Fun-ASR restart state is tracked separately. If its result is unknown, inspect the current service rather than assuming a network interruption means a successful restart. TTS reference details appear under the failure-reason section.

For upgrades, exit game/services and back up personal data. Follow the current [new-directory/import procedure](../UPGRADE.md); preserve configuration, credentials, memories, relationships, persona, model and voice folders. Reuse compatible model components. Stop SPP before ONNX configuration tools. See [resource usage](../HARDWARE.md) and [backup scope](../DATA_AND_PRIVACY.md).
