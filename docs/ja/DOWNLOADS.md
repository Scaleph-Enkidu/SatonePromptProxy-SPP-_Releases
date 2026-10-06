[简体中文](../zh-CN/DOWNLOADS.md) | [English](../en/DOWNLOADS.md) | [日本語](DOWNLOADS.md)

# ダウンロードと SHA-256 検証

[← ホーム](README.md)

現在の組み合わせは **AIChat 1.18.28 + SPP 5.10.8** です。下の三言語文書改訂版を推奨します。変更は説明のみで、全実行ファイルは元 N15 と同じです。N15 導入済みなら文書の閲覧だけで構いません。旧 Relaxed 設定は[更新手順](UPGRADE.md)に従ってください。

- [三言語プログラムパッケージ（約 43 MB）](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.18.28_SPP-v5.10.8-docs-r1/SatoneMod_AIChat_1.18.28_SPP_5.10.8_Windows_x64_docs_r1.zip)
- [元 N15 ZIP（約 39 MB、元ハッシュを保持）](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.18.28_SPP-v5.10.8/SatoneMod_AIChat_1.18.28_SPP_5.10.8_Windows_x64.zip)
- [任意 ONNX（約 94 MB）](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.17.1_SPP-v5.9.1-license-r1/Satone_Semantic_E5_small_int8_ORT_1.30.0_Windows_x64.zip)
- [文書改訂 manifest](../../releases/AIChat_v1.18.28_SPP_v5.10.8_docs_r1.json)

更新前にゲーム・サービスを終了します。GitHub 自動生成の Source code ZIP をインストーラーの代わりにしないでください。TTS 環境・重み、ASR 環境・モデルは別で、Neutral 参考音声は付属します。[導入](INSTALL.md)と[音声](VOICE_SETUP.md)を参照してください。

## 検証手順

```powershell
Get-FileHash .\SatoneMod_AIChat_1.18.28_SPP_5.10.8_Windows_x64_docs_r1.zip -Algorithm SHA256
```

PowerShell の結果を隣接 `.sha256` と manifest の `package_sha256` に照合します。文書改訂で ZIP ハッシュは変わりますが、DLL／PDB／EXE などの実行バイトは同一です。

[SHA-256](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.18.28_SPP-v5.10.8-docs-r1/SatoneMod_AIChat_1.18.28_SPP_5.10.8_Windows_x64_docs_r1.zip.sha256)

旧版、撤去済み添付、当時の検証範囲は[履歴](RELEASE_ARCHIVE.md)にあります。
