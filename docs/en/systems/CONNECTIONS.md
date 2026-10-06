[简体中文](../../zh-CN/systems/CONNECTIONS.md) | [English](CONNECTIONS.md) | [日本語](../../ja/systems/CONNECTIONS.md)

# Model connections and switching

[Documentation](../README.md#systems) · AIChat 1.18.28 + SPP 5.10.8

A connection includes provider type, endpoint, model and credentials. Chat uses one applied connection at a time; an edited draft is not automatically active.

## Supported connection paths

The UI provides OpenAI, DeepSeek, Claude, Gemini, configurable relays and local Ollama. Model availability depends on the provider/account. Default names are editable examples, not a promise of access. Cloud APIs need API credentials and quota; relay endpoint/authentication/model names must follow that relay's API. Local Ollama needs your own running service and model, with additional RAM/VRAM requirements beyond cloud text chat.

## Save and switch

In F9 settings → LLM, edit the connection and select service/model, then save and apply. Check the successful switch status and currently applied service; the selection box alone is not proof. Active or uncertain turns must follow coordination/recovery rules. A request already started retains its original connection parameters.

Connection tests actually contact the service and may incur usage. A successful probe proves reachability at that moment, not every subsequent format, model, request or account balance.

Switching providers within a profile retains local history, memory and relationships. Tone and interpretation may change without any lost save. It does not delete data the old provider may retain. Keys are stored per connection; protect configuration and credential files. See [privacy](../DATA_AND_PRIVACY.md) and [costs](../API_COST.md).

## Reasoning effort

Options are Auto, None, Low, Medium, High and Max, corresponding to `auto / none / low / medium / high / max`. Manual effort applies to supported OpenAI/DeepSeek connections; other services use Auto. These map to provider/model capabilities rather than universal identical parameters. Higher effort may increase latency and usage without guaranteeing better persona fidelity or format. Handle unsupported settings through explicit status/errors; a fallback does not prove the requested level took effect.
