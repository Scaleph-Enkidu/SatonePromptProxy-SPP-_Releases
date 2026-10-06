[简体中文](../../zh-CN/releases/AIChat_v1.18.28_SPP_v5.10.8.md) | [English](AIChat_v1.18.28_SPP_v5.10.8.md) | [日本語](../../ja/releases/AIChat_v1.18.28_SPP_v5.10.8.md)

# AIChat v1.18.28 SPP v5.10.8

[← Release archive](../RELEASE_ARCHIVE.md)

> Historical release record. Availability and test claims refer to the original date; use the current guides for installation.

N15, 2026-10-05, fixes the cup remaining in Satone's hand. Both the Relaxed animation pool and default StablePoseOverrides remove cup/tea actions 256/751/753/755/52 and use prop-free 752,50,51. Source history: `origin/develop` at `66cb827`, runtime `530d06a`, tested record `c31dcc1`. Existing installations must [refresh the old configuration](../UPGRADE.md).

Independent first-round review approved the fix. Six suites recorded 900/16/262/39/95/196; two net472 rebuilds matched byte-for-byte. Seal: attempt-19. In-game evidence covers two whitelist-path Relaxed turns, id:50/id:752, without residual cup props. The standard pool was not additionally tested in game and was covered by static review only.

The original runtime archive is retained with its original hash. The later docs_r1 revision only adds trilingual documentation; see [documentation revision](DOCS_TRILINGUAL_20261006.md). Installation and migration follow [INSTALL](../INSTALL.md) and [UPGRADE](../UPGRADE.md).

## Original manifest and hash identifiers

[JSON](../../../releases/AIChat_v1.18.28_SPP_v5.10.8.json) · [原文 / Original](../../zh-CN/releases/AIChat_v1.18.28_SPP_v5.10.8.md)

- `5c13266e6ec9d1f7e775bb305d1734099b845acc91ecb27902c5290b9bb2f45e`
- `78c418ce77e13edec1826452b1649ebe4caf1cb941fd4277a4ffc16d6c8c0f44`
- `9ed7977780dbfb3f70fd8055fa86741a1fb8777e78d1bd1342814786c50203b4`
