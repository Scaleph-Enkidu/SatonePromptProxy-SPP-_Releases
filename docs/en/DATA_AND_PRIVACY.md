[简体中文](../zh-CN/DATA_AND_PRIVACY.md) | [English](DATA_AND_PRIVACY.md) | [日本語](../ja/DATA_AND_PRIVACY.md)

# Data, backups and privacy

[Home](README.md) · [Upgrade](UPGRADE.md) · [API costs](API_COST.md)

Local storage and provider-side processing are separate. Cloud chat sends the chosen context to the selected endpoint. Do not publish your runtime folder as if it were a clean release package.

## Local files

| Location | Contents and handling |
| --- | --- |
| `BepInEx/config/com.username.chillaimod.cfg` | Plugin settings and possibly key drafts; sensitive |
| `BepInEx/config/AIChatSatoneUX.history` | Window history; Base64 is not encryption and this is not all memory |
| `BepInEx/LogOutput.log` | May include ASR text, replies, TTS information and paths |
| SPP `config.json` | Addresses and paths; the standard credential store is separate |
| `connections.v1.json`, `connection_credentials.v1.json` | Saved connections and credentials/API Keys |
| `SatonePersona_v4.6.txt` | Shared persona; custom text may be private |
| `local_v1/commits.jsonl`, `active_selection.v1.json` and associated locks/recovery files | Authoritative records/state, not disposable cache |
| `memory_profiles/memory1/local_v1` and other profiles | Profile records/projections; retain all profiles |
| Legacy `记忆1`, `记忆2`, `记忆3`, `SatoneMemory.json`, `SatoneRelationship.json`, `SatoneArchive.jsonl`, `SatoneChat.txt`, `SatoneRecall.db` | Older installation data may coexist with current records |
| `semantic_recall_v1` | Private text fingerprints/vectors; rebuildable does not mean public |
| `models/multilingual-e5-small` | Generic model component, not personal conversation memory |
| `OriginalGameProgress.json` and recovery copies | Derived game identity/progress ledger |
| `runtime_paths.json`, `service_paths.ini` | Machine-local paths, potentially including usernames |
| `usage_stats.json`, logs and configuration backups | Usage, diagnostics and possibly sensitive settings |

The original game's saves are separate again. Keep both current English profile IDs and legacy Chinese-named folders when backing up. The 50,000-record semantic limit does not delete authoritative history.

Credential file permissions restrict access but are not encryption. Showing/hiding a key changes visibility, not storage protection. Key drafts can also remain in plugin configuration.

## What leaves the computer

Your chosen cloud/relay endpoint receives the request context and authentication needed for that service. A relay is an additional recipient. Switching service or deleting local history does not delete the old provider's retained data; consult the provider's policy, for example [OpenAI API data controls](https://platform.openai.com/docs/guides/your-data).

Local ASR normally deletes temporary WAVs after processing, but interrupted runs, exports or backups can leave copies. Changing a local endpoint to a remote service changes who receives the data. The three loopback ports 11435/9880/9881 are for local use; they are not an isolation boundary against software using the same account. Do not expose them through public port forwarding.

## Back up and move

Exit the game and services. Back up the game's configuration/history and relevant logs plus the entire SPP runtime: authoritative WAL/state, all profiles/legacy files, credentials, persona, semantic cache, model and reference audio. Separately retain or reinstall external GPT-SoVITS/Fun-ASR environments and weights. A Dashboard backup is not necessarily a full filesystem backup.

Use the [new-directory/import upgrade procedure](UPGRADE.md). For rollback, restore the matching program and full pre-upgrade data. On another PC, correct paths, reinstall Python virtual environments where needed, and verify game/Steam identity again; an old ledger does not establish the new session's identity.

## Sharing and removal

Before reporting a problem, remove API Keys, bearer tokens, personal identifiers, private dialogue and sensitive paths. Revoke a leaked key rather than relying on deleting a public post.

To disable the mod, stop its services and remove its DLL while retaining data. Full local removal additionally requires deleting your own runtime/configuration/history and any backup/export copies you intend to remove; uninstalling the plugin alone does not erase them or provider data.

Release manifests check recorded package contents/hashes and absence of known player files. They are not a full binary security audit. Historical test claims apply only to their stated date and scope.
