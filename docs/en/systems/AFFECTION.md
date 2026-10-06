[简体中文](../../zh-CN/systems/AFFECTION.md) | [English](AFFECTION.md) | [日本語](../../ja/systems/AFFECTION.md)

# Affection and relationship scores

[Documentation](../README.md#systems) · AIChat 1.18.28 + SPP 5.10.8

The displayed affection combines an **AI relationship score** with a **familiarity bonus from the original game**. They are stored separately; the game bonus does not rewrite the four AI relationship dimensions.

## AI relationship score

| Dimension | Meaning | Weight |
| --- | --- | ---: |
| Affection (A) | Personal affection and meaningful shared experiences | 50% |
| Trust (T) | Honesty, reliability and respect for refusal/boundaries | 20% |
| Comfort (C) | Natural, safe, low-pressure interaction | 20% |
| Openness (O) | Willingness to share personal thoughts and having them respected | 10% |

Each dimension is bounded from 0 to 100, with fractional progress retained.

```text
F = 0.50 × A + 0.20 × T + 0.20 × C + 0.10 × O
```

New Memory 1 and Memory 2 profiles default to 10 in all four dimensions, giving F=10. Memory 3 defaults to a maximum-affection test preset with all four at 100. Existing profiles or a disabled preset use their actual saved state. Upgrading does not require resetting a relationship.

Changes accumulate in steps of **0.05**. For example, A=10 with 0.90 fractional progress becomes A=11 with 0.05 remaining after +0.15. Weighting and rounding mean small changes may not immediately alter the displayed value.

For ordinary updates, each dimension changes by **−0.50 to +0.30**; no more than two dimensions may increase, and total positive growth is at most **+0.30**. Important events default to an absolute per-dimension limit of 2 and total positive growth of **+2.00**. These are dimension limits, not fixed changes to the displayed score. Repeated pressure follows [separate rules](BOUNDARIES.md).

Ordinary factual questions often do not change the long-term relationship. Agreeing to flirt, act cute or grant a request does not automatically earn affection. Respect, reliability, responses to voluntary sharing and meaningful experiences matter more.

After a genuine question expressed with `Curious`, a relevant, substantive answer on the player's next turn may qualify for A +0.05 and C +0.05. It still needs validation and remains subject to total limits. The same question cannot earn twice; the same topic cannot repeatedly earn this reward within the latest 20 observed exchanges. A tag, question mark or long answer alone is insufficient evidence.

## Original-game bonus

The ledger records confirmed completed work time and distinct main-story chapters. H is completed work hours after the ledger baseline; N is the number of distinct chapters credited:

```text
W = 40 × ln(1 + H / 18) / ln(4)
S = N × 5/9
L = W + S
B = L                                  when L ≤ 60
B = 60 + 10 × (1 − exp(−(L − 60) / 40)) when L > 60
Displayed affection = round(min(100, max(0, F + B)))
```

H is completed work reported by the game, not total application uptime. Chapters are deduplicated; replaying one does not earn again, and previously excluded baseline contributions are not restored. Each credited chapter contributes 5/9 under the current rule.

For H=54 and N=36, W=40, S=20 and B=60. With F=10, the display is 70. This is a calculation example, not a value promised for every completed save. Growth slows above L=60; B approaches 70 and the final display remains capped at 100.

The bonus requires a valid game identity, synchronization in this session and the profile's original-game bonus setting. If any is missing, only F may appear. A higher display does not mean the AI relationship file received the same increase.

## Relationship stages

Stages use the unrounded score. After applying the game bonus, everyday familiarity can use the resulting stage.

| Score | Identifier | Meaning |
| --- | --- | --- |
| 0 ≤ score < 20 | distant | Distant |
| 20 ≤ score < 40 | acquaintance | Newly acquainted |
| 40 ≤ score < 60 | familiar | Familiar |
| 60 ≤ score < 80 | close | Close |
| 80 ≤ score < 95 | very_close | Very close |
| 95 ≤ score ≤ 100 | intimate | Highly intimate |

**High affection still permits refusal.** Mood, unresolved conflicts and explicit boundaries affect responses. Personal or intimate requests also depend on the underlying AI trust/openness and other conditions; the game bonus alone cannot unlock them. A stage is not a fixed acceptance probability.

Background relationship updates and the display may finish after the main reply. Periodic reconciliation organizes short-term state, conflicts and records without adding dimension scores. Each [memory profile](MEMORY.md) has its own AI relationship.
