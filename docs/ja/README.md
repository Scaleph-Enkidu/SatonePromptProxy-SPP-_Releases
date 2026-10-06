[简体中文](../zh-CN/README.md) | [English](../en/README.md) | [日本語](README.md)

# 聡音 Mod：続く会話、少しずつ育つ関係

Windows／Steam 版 **Chill with You: Lo-Fi Story** 向けの非公式 Mod です。AIChat がゲーム内チャット、字幕、再生、操作を担当し、SatonePromptProxy（SPP）がモデル接続、人格、記憶、関係、音声転送を扱います。**中国語・英語・日本語の UI／字幕**に対応しています。各言語の発音品質は声・モデルに依存し、導入例は日本語音声です。

現在の組み合わせ：**AIChat 1.18.28 + SPP 5.10.8（N15）**。今回の `docs_r1` は三言語の文書とパッケージ説明の整理で、実行バイナリは変わりません。

![導入後のチャット画面](../images/install-success.png)

## 導入前に：負荷と既知の制約

**ゲーム、GPT-SoVITS、Fun-ASR の同時実行には追加の CPU・RAM と数 GB の VRAM が必要です。** GPU 音声一式は **8 GB を検討開始点、12 GB 以上を余裕のある構成**としますが、検証済み最低要件ではありません。6 GB なら GPU TTS＋CPU ASR、4 GB 以下や内蔵 GPU では文字から始めます。クラウド LLM の重みは PC に載りませんが、自前のローカル LLM は別途資源が必要です。

2026-09-27 の画像では、用途未確認の Python 2 プロセスが約 2.17／1.92 GiB、ゲームが約 0.63 GiB でした。これを足してカード全体のピークにはできません。過去の合成記録 1 万／5 万件では、SPP＋ONNX が約 **441／944 MB RAM**、起動 **11.65／495.12 秒**で、ゲーム・TTS・ASR を含みません。350 MB の基準は worker のみです。

**大規模履歴の起動遅延と、報告されたゲームのフレーム低下は未解決で、統一の低 VRAM モードも検証完了していません。** AMD／Intel GPU に NVIDIA CUDA 手順をそのまま使わず、文字と CPU ONNX から始めてください。三言語プログラム約 43 MB、モデル約 94 MB はダウンロード容量であり、メモリ上限ではありません。[測定と範囲](HARDWARE.md)を確認してください。

## 導入・更新・トラブル対処

| 目的 | 説明 |
| --- | --- |
| 初めて導入 | [4 段階の完全手順](INSTALL.md) |
| プログラムと検証ファイル | [ダウンロードと SHA-256](DOWNLOADS.md) |
| 旧版から更新 | [更新・記憶取り込み・復元](UPGRADE.md) |
| 意味検索を追加 | [ONNX 設定](ONNX_SETUP.md) |
| 発声・マイク・診断 | [音声の詳細](VOICE_SETUP.md) |
| API 支出 | [費用と請求](API_COST.md) |
| 保存・移設 | [データとプライバシー](DATA_AND_PRIVACY.md) · [移設ガイド](PORTABLE_DEPLOYMENT.md) |
| パッケージ内説明 | [AIChat README](AIChat_README.md) · [SPP README](SPP_README.md) · [導入と復元](PACKAGE_INSTALL.md) |

順序は **① 文字 → ② 任意 ONNX → ③ 任意 TTS → ④ 任意 ASR** です。文字だけでも利用でき、後の各機能は個別に選べます。TTS／ASR に ONNX は不要です。F9 でチャット、Enter で送信、Shift+Enter で改行、F8 を押して話します。連続会話は自分で有効にします。

N15 で Relaxed のコップ動作を外しました。既存設定の `StablePoseOverrides` を `Relaxed=752,50,51` に更新してください。N14 の参考ポリシー更新修正も含みます。SPP のフォルダー変更時は新環境の旧記憶取り込みを使い、旧フォルダーを保持してください。

## 人格、記憶、共有体験

人格は原作 1,700 行以上の台詞を参考に、聡音の自主性、話し方、境界を保ちます。親しく話し、冗談を言い、自発的に打ち明ける一方で、断ることもできます。高好感度は無条件の服従ではありません。26 感情は発話区間の表現で、固定の好感度加点ではありません。

3 つのプロファイルで会話・長期記憶・AI 関係を別々に保存し、サービスやモデルを変えても継続できます。毎回使うのは選択した最近の原文、要約、関連履歴です。キーワード検索は全履歴、任意 ONNX は最新 50,000 件が対象で、古い正本を削除しません。人格ファイル `SatonePersona_v4.6.txt` は共通です。

原作の知識は確認済みの識別・進行に従い、第 31 章などの通信断は原作状態を尊重します。識別同期の失敗だけで全 AI 会話が使えなくなるわけではありませんが、進行を想像で確定しません。原作の親しさ加算と AI の好感・信頼・安心・自己開示は別々です。

窓景色、服、眼鏡、飾りの完全な認識はまだありません。「なぜ外を見ないのか」と問い続けると、回避、通信断、画面乱れの Meta 演出になる場合があります。作者は文字だけでも予想以上に怖かったと述べています。設定で無効化・リセットでき、起動ごとに第 1 段階から始まります。[演出の操作とネタバレ](systems/META.md)を参照してください。

<a id="systems"></a>
## システムの説明

- [人格](systems/PERSONA.md)
- [好感度の計算](systems/AFFECTION.md)
- [境界と関係修復](systems/BOUNDARIES.md)
- [26 種の感情](systems/EMOTIONS.md)
- [記憶とプロファイル](systems/MEMORY.md)
- [過去の会話の検索](systems/RECALL.md)
- [物語の知識](systems/STORY_KNOWLEDGE.md)
- [原作との調整](systems/STORY_COORDINATION.md)
- [Meta 演出](systems/META.md)
- [チャット画面と履歴](systems/CHAT_UI.md)
- [検証と復旧](systems/RECOVERY.md)
- [モデル接続](systems/CONNECTIONS.md)
- [サービス管理](systems/SERVICES.md)
- [音声と字幕](systems/SPEECH.md)
- [音声入力と連続会話](systems/VOICE_INPUT.md)

## 任意の F10 外観カタログ

[SatoneStateCatalog](tools/STATE_CATALOG.md) は現在の外観 ID を読み、説明を書き込める独立ツールです。解放やセーブ変更、聡音からの場面操作は行いません。[ソースからの構築](tools/BUILD_STATE_CATALOG.md)と[観察待ち ID](tools/OBSERVED_IDS.md)もあります。構築確認と実機試験の範囲を区別しています。

<a id="roadmap"></a>
## 今後の予定

音声体験と言語に合う声の改善、外観説明カタログの整備、会話による環境・道具操作を検討します。中英日 UI／字幕は現在の機能となり、未開発項目から外しました。中国語音声などの品質は対応モデルと今後の確認に依存します。

## 版、クレジット、ライセンス

[三言語文書改訂](releases/DOCS_TRILINGUAL_20261006.md) · [N15 更新内容](releases/AIChat_v1.18.28_SPP_v5.10.8.md) · [履歴と検証資料](RELEASE_ARCHIVE.md)

AIChat は Elysia777 による [qzrs777/AIChat](https://github.com/qzrs777/AIChat) に基づきます。Scaleph が AI の支援を使って開発・保守しています。許諾可能な独自内容は PolyForm Noncommercial 1.0.0 で、元作者、第三者、以前の MIT 許諾の権利は保持されます。[範囲](LICENSE_SCOPE.md)、[LICENSE](../../LICENSE)、[NOTICE](../../NOTICE)を参照してください。GPT-SoVITS、Fun-ASR、E5、ORT、声のモデル、録音は各出典の条件に従います。
