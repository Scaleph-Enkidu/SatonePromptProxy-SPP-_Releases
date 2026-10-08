[简体中文](../zh-CN/DOWNLOADS.md) | [English](../en/DOWNLOADS.md) | [日本語](DOWNLOADS.md)

# ダウンロードと SHA-256 検証

**AIChat 1.18.30 + SPP 5.10.10**

今回のリリースは、記憶取り込み、音声エコー除去、終了時の後処理、日付による検索の計 9 件の修正をまとめています。AIChat と SPP の両方を更新してください。三言語の説明とパッケージ内の入口も更新しました。

- [ZIP](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.18.30_SPP-v5.10.10/SatoneMod_AIChat_1.18.30_SPP_5.10.10_Windows_x64.zip)
- [SHA-256](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.18.30_SPP-v5.10.10/SatoneMod_AIChat_1.18.30_SPP_5.10.10_Windows_x64.zip.sha256)
- [Manifest](../../releases/AIChat_v1.18.30_SPP_v5.10.10.json)
- [ONNX (optional)](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.17.1_SPP-v5.9.1-license-r1/Satone_Semantic_E5_small_int8_ORT_1.30.0_Windows_x64.zip)

ゲームと SPP を終了し、旧 SPP フォルダー全体とプラグイン設定を保存してから AIChat DLL／PDB と SPP を更新します。SPP を移す場合は[更新手順](UPGRADE.md)に従って記憶を取り込んでください。修正済みの Relaxed 設定を再度初期化する必要はありません。GitHub 自動生成の Source code ZIP は導入用ではありません。TTS、ASR、意味検索モデルは任意の外部コンポーネントです。

```powershell
Get-FileHash .\SatoneMod_AIChat_1.18.30_SPP_5.10.10_Windows_x64.zip -Algorithm SHA256
```

SHA-256 = `.sha256` = manifest `package_sha256`.

[Release notes](releases/AIChat_v1.18.30_SPP_v5.10.10.md) · [Archive](RELEASE_ARCHIVE.md)
