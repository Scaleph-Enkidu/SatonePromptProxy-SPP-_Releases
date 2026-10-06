[简体中文](../../zh-CN/systems/RECALL.md) | [English](RECALL.md) | [日本語](../../ja/systems/RECALL.md)

# History retrieval

[Documentation](../README.md#systems) · AIChat 1.18.28 + SPP 5.10.8

Retrieval selects relevant exchanges from the active profile and provides them to the chat model when useful. It does not make the model read every past conversation on every turn.

| Method | Behavior | Installation |
| --- | --- | --- |
| Keyword recall | Searches text, keywords and Chinese/Japanese fragments | Built in; text chat needs no Python |
| Semantic recall | Compares meaning through a local vector model, helping with paraphrases | Optional approximately 94 MB ONNX component, explicitly enabled; runs on CPU |

For example, “How is the instrument you mentioned going?” may retrieve “I've been practicing piano” without sharing its exact words. A match still depends on records, wording, model and filters.

## History coverage

Keyword indexing covers all available history. The semantic projection retains at most the **latest 50,000 communicated records**. Older records remain in authoritative storage and are searchable by keyword. This is neither a memory-deletion limit nor the window's 50-utterance limit.

Each profile builds and queries its own index. The current presentation-tracking path confirms actually displayed text and completed speech segments; unpresented candidates cannot masquerade as communicated experiences.

## A match does not guarantee a mention

Scores, semantic lead and original-record verification determine whether a result enters this turn's context. Similarity is not the probability that a fact is correct. Conservative filtering helps avoid mixing similar but different experiences.

Long records can be truncated for the semantic model, while keyword search still uses full text. Even when relevant history reaches the model, it can overlook, misunderstand or omit it from its reply.

## Optional component states

ONNX is disabled by default. Missing/invalid files, load failures, busy states or timeouts can fall back to keyword recall, so text chat need not wait for semantics. First enablement or profile switching requires warm-up/building; `loading`, `building` and `ready` are different states.

`semantic_recall_v1` is a rebuildable cache under the maintenance procedure, but contains information derived from private exchanges and must be protected. It differs from authoritative `local_v1`, which must not be casually deleted. See [ONNX setup](../ONNX_SETUP.md) and [large-history resource measurements](../HARDWARE.md).
