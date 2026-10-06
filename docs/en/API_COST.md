[简体中文](../zh-CN/API_COST.md) | [English](API_COST.md) | [日本語](../ja/API_COST.md)

# API costs

[Home](README.md) · [Connections](systems/CONNECTIONS.md) · [Privacy](DATA_AND_PRIVACY.md)

The package includes no API credits. Bring your own provider account, API permission and balance. A ChatGPT subscription does not include the same thing as API credit. Default model names are editable examples; confirm availability with the provider.

## What is billed

Requests include the current message plus persona, recent conversation, memory and rules. Relationship/memory updates, format repair and retries may make additional requests. Reasoning tokens and cache categories can affect costs. A visible chat turn is not necessarily one API call; failure or cancellation may still consume usage.

Use live provider prices and billing records: [OpenAI pricing](https://openai.com/api/pricing/), [models](https://developers.openai.com/api/docs/models), [usage](https://platform.openai.com/usage), [billing](https://platform.openai.com/settings/organization/billing/overview), and [DeepSeek pricing](https://api-docs.deepseek.com/quick_start/pricing). Relays may set different prices. This guide does not promise a fixed per-turn price.

```text
Cost = sum(usage in each billed category × that category's current unit price)
Observed cost per completed turn = total measured cost / completed turns
Estimated days = balance / (observed cost per turn × expected daily turns)
```

Do not count cached input twice. Include background calls, and use the actual invoice for taxes, fees and billing rules. Estimates are not spending caps. Test a small number of turns first and inspect provider usage. An alert threshold is not necessarily a hard cutoff.

SPP's local pricing table may lag the provider. A zero/unknown local estimate does not mean free usage. Pricing is matched to returned model identifiers and cannot guarantee retrospective invoice accuracy. Historical local confirmation on 2026-10-01 was not a complete billing matrix across all services.

Local ONNX, GPT-SoVITS and Fun-ASR do not use the OpenAI voice API merely by running locally, but consume hardware resources/electricity. If configured to use a remote voice service, that service's rates and terms apply.
