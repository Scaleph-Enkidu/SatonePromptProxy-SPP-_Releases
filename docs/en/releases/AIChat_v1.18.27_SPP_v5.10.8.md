[简体中文](../../zh-CN/releases/AIChat_v1.18.27_SPP_v5.10.8.md) | [English](AIChat_v1.18.27_SPP_v5.10.8.md) | [日本語](../../ja/releases/AIChat_v1.18.27_SPP_v5.10.8.md)

# AIChat v1.18.27 SPP v5.10.8

[← Release archive](../RELEASE_ARCHIVE.md)

> Historical release record. Availability and test claims refer to the original date; use the current guides for installation.

N14 verified baseline, 2026-10-05. The development history cited `origin/develop` at `247ca30`, runtime `e7d21c31` and tested record `25becef5`. A 409 response refreshes SPP's reference policy and retries once with the new policy. Policy cache is invalidated across selection/session/restarts; the journal supports resend and expired-task cleanup.

Independent N14 review approved it. Six suites recorded 900/16/262/39/95/196. Two net472 rebuilds at the same HEAD matched byte-for-byte. Seal: attempt-18. Use [current installation](../INSTALL.md) and [memory import](../UPGRADE.md); original package identity is retained in the manifest.

## Original manifest and hash identifiers

[JSON](../../../releases/AIChat_v1.18.27_SPP_v5.10.8.json) · [原文 / Original](../../zh-CN/releases/AIChat_v1.18.27_SPP_v5.10.8.md)

- `c7c804b277d47d01f4064fced365e458d8c3ff5c4829580a1553603046fe35a6`
- `29841cfa2fac188c8b6da11d28a089776ca82c0a7a5f243a9e2153d54790abd0`
- `3248c2ce0c3fe7729e1d9b15f4d0442cfb96d9ddf9127ddcd05deb267f69bb33`
