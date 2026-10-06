[简体中文](../../zh-CN/releases/AIChat_v1.16.14_SPP_v5.8.23.md) | [English](../../en/releases/AIChat_v1.16.14_SPP_v5.8.23.md) | [日本語](AIChat_v1.16.14_SPP_v5.8.23.md)

# AIChat v1.16.14 SPP v5.8.23

[← 履歴一覧](../RELEASE_ARCHIVE.md)

> 過去の公開記録です。配布状況・試験範囲は当時のもので、現行の導入には現在の手順を使ってください。

公式コンポーネント 2 ZIP を変更・再ビルドせずまとめ、元の Release とハッシュが一致した配布です。当時の公開用リポジトリは Private で、取得には権限が必要でした。Public 化後は開発私有リポジトリの権限に依存しません。クリーンな Windows での全導入試験を行ったとはしていません。

AIChat の元コミットは `0e3aadeec171fa07b798baf517650f42ff441c95`、SPP は `bc6e22e184ad98fde472374abcae65ca72364831` です。AIChat の BUILD_INFO には構築時の SPP 5.8.22 が残りますが、そのままの AIChat を 5.8.23 と組み合わせ、ZIP を書き換えていません。

SPP 5.8.23 は API 総入力 32,000 token で記憶整理を予約し、最近の原文を概算 12,000 token 残す設定です。ゲーム内の長時間会話の受け入れ確認は未完了でした。

当時は `AIChat_v1.16.14.zip` の DLL を BepInEx/plugins へ、`SatonePromptProxy_v5.8.23.zip` 全体を専用フォルダーへ置きました。`_SHA256.txt`、元 AIChat MIT とクレジット、JSON manifest は検証・許諾資料で、プラグインではありません。BepInEx と自分の API Key が必要で、音声・マイクには外部環境・モデル・参考音声も必要でした。Source code ZIP はインストーラーではなく、Git も不要です。

当時の更新案内は停止・バックアップ後に唯一の DLL を交換し、SPP の設定・人格・記憶・関係・音声を残すものでした。現行版は[現在の更新手順](../UPGRADE.md)に従います。DLL 交換後も残るキーや履歴は別保存ファイル由来です。

ZIP 一覧に個人 CFG、実 config.json、runtime_paths.json、会話履歴、memory_profiles、ログはなく、公式例・文書を保持していました。ハッシュ・一覧検証は完全なバイナリ監査ではありません。

## 元 manifest とハッシュ識別子

[JSON](../../../releases/AIChat_v1.16.14_SPP_v5.8.23.json) · [原文 / Original](../../zh-CN/releases/AIChat_v1.16.14_SPP_v5.8.23.md)

- `65684dac51fdae292d0e4676dc1a458396c5bb01a63e15472537f5c5b8143cf1`
- `bcad7805fa8193b8efd9a14e82ef8be16b65d9d9f6c86fad674719cc17150c6e`
