[简体中文](../zh-CN/ONNX_SETUP.md) | [English](../en/ONNX_SETUP.md) | [日本語](ONNX_SETUP.md)

# 任意の ONNX 意味検索

[導入の第 2 段階](INSTALL.md#stage-2) · [ダウンロード](DOWNLOADS.md) · [ハードウェア](HARDWARE.md)

Windows x64 用 E5 int8／ORT 一式を使います。文字チャットとキーワード検索は内蔵で Python 不要、TTS／ASR とも独立しています。意味検索 worker はネイティブの CPU 処理で、旧 Python embedding worker ではありません。

## 検証・有効化・無効化

会話完了を待ってゲームを終了し、SPP を止めてから `Verify_Semantic_Recall.bat`、`Enable_Semantic_Recall.bat`、`Disable_Semantic_Recall.bat` を使い、EXE または `Start_Text_Chat.bat` で再起動します。停止ツールは同名 `SatonePromptProxy.exe` をまとめて止める場合があるため、複数起動時は注意してください。「未起動」なのに Dashboard が開く場合はプロセスを調べます。

ツールの明確な成功表示を確認します。有効化では `config.json.before-semantic-<timestamp>` に設定を保存し、`embedding_enabled=true`、`embedding_auto_start=true`、`embedding_model_dir="models/multilingual-e5-small"` を設定します。無効化しても会話は消えません。ファイル検証は準備完了の証明ではなく、Recall 検索で実行時の準備を始めます。

## 状態の読み方

| 状態 | 意味・操作 |
| --- | --- |
| `disabled` | 無効 |
| `missing` | 必須ファイル不足 |
| `waiting` | 利用できる記録・処理待ち。空プロファイルでは正常な場合がある |
| `loading` | モデル読み込み中。待って更新 |
| `building` | ベクトル・索引の準備中 |
| `ready` | 現在の意味検索が準備完了。実際の検索で確認 |
| `failed` | `last_error`、モデル、ログを確認 |

`engine: native_keyword+onnx` だけでは読み込み成功を証明しません。`worker.model_loaded`、`semantic_state`、対象プロファイルの `worker.semantic_scope` を見ます。`worker.embedded_exchanges` は画面履歴の件数ではなく、外側の `profile_id` は worker の対象確認の代わりになりません。`semantic_ready: false` ではキーワード検索へ戻れます。busy／409 なら会話完了後に再試行し、起動を繰り返さないでください。

Dashboard のプロファイル選択は閲覧対象だけを変えます。完了した交流の語句で検索し、`user_text`、`assistant_text`、原文全文を確認してから言い換えを試します。`qualified` は追加の採用条件で、読み込み完了や事実の正確さの確率ではありません。1 件ヒットしないだけで故障とは判断できません。

## ファイルと更新

`model.onnx`、`tokenizer.json`、`onnxruntime.dll`、`onnxruntime_providers_shared.dll`、`COMPONENT.json`、ライセンスを検証済みの一式として保ちます。異なるモデル・実行環境を混ぜないでください。互換性のあるプログラム更新では同じ約 94 MB のコンポーネントとキャッシュを再利用し、再検証と実検索を行います。モデル更新ではバックアップ・停止後、専用 manifest に従って対応するフォルダー全体を置き換えます。

`semantic_recall_v1` は私的情報から生成したデータです。手順に従って再構築できますが正本 WAL ではありません。`local_v1` を消さないでください。意味検索は最新 50,000 件、キーワード検索は全履歴を対象とします。

記載の [multilingual E5 small](https://huggingface.co/intfloat/multilingual-e5-small) はリビジョン `614241f622f53c4eeff9890bdc4f31cfecc418b3` に固定され、[ONNX Runtime 1.30.0](https://github.com/microsoft/onnxruntime/releases/tag/v1.30.0) を使います。`COMPONENT.json` と各ライセンスを保持してください。Mod 独自のライセンスへ変更するものではありません。
