[简体中文](../zh-CN/PORTABLE_DEPLOYMENT.md) | [English](../en/PORTABLE_DEPLOYMENT.md) | [日本語](PORTABLE_DEPLOYMENT.md)

# SPP の移設ガイド

[導入](INSTALL.md) · [更新](UPGRADE.md) · [バックアップ](DATA_AND_PRIVACY.md)

5.10.10 向けの説明で、旧パッケージの CP14／CP23 が混在した案内を置き換えます。`D:\LofiMOD\SatonePromptProxy` のような短いパスと、隣接する `FunASR-Runtime`、`Fun-ASR-Nano-2512`、`GPT-SoVITS` を推奨します。付属の `SatonePersona_v4.6.txt` を保持してください。人格の欠落で初回 `/persona` が失敗した経緯があり、新規導入で EXE だけのコピーは不十分です。

## 初回起動とパス

既存の `config.json` を使い、なければ `config.example.json` から生成します。両方ない場合や JSON 不正では明確に失敗します。過去の 5.8.23 は旧標準の整理しきい値 24000 を保存して 32000 に移しましたが、全独自項目を上書きする指示ではありません。

ASR は有効な明示パスを優先します。サービススクリプトは次に付属の `satone_funasr_server_v1.py` を使え、その後は有効な `runtime_paths.json` と標準配置を参照します。`AI/FunASR-Runtime`、`AI/Fun-ASR-Nano-2512`、または `AI` なしの同名隣接配置を探します。無効な機器パスは再探索され、パスキャッシュは記憶ではありません。初回は手順どおり Python・スクリプト・モデルを明示すると確実です。

`http://127.0.0.1:11435/asr/status` で実際のパスと `path_source`（manual/cached/discovered/mixed）を確認できます。CPU は `device="cpu"` を加えた現行スクリプトのコピーが必要です。9881 の既存サービスが再利用される場合があるので、変更前に旧インスタンスを確認・停止します。

## 参考音声と PC 移行

`mayuri-voice/refs/MAY_1158_Neutral.wav` の相対配置を維持します。SPP は自身と親フォルダーを探せます。別置きなら実際の `emotion_tts.ref_root` を指定します。古い外部パスは空にするか直し、`/tts/status` で確認してください。他の感情音声は任意の追加です。

個人用 SPP 全体を残します。正本 `local_v1`、全プロファイル、旧 JSON・DB、関係、記憶、認証、人格、使用量を含み、古い短い一覧だけに頼りません。原作進行と `.prev` も保持しますが、新 PC で Steam 識別を再確認します。ゲーム側の設定・履歴も別に保存します。`runtime_paths.json` は再構築できても、`local_v1` はキャッシュ扱いできません。

外部音声環境・重み・参考音声・任意 ONNX はコピーまたは再導入します。Python 仮想環境は別 PC で再作成が必要な場合があります。旧 Python embedding モデルは復元用だけで、現行のキーワード／ONNX は使いません。新しい版は別フォルダーへ入れ、旧記憶を取り込んで確認してから常用パスを整理します。

## 障害とホットワード

任意 TTS／ASR／ONNX が使えなくても、それぞれの状態にエラーを出し、設定済み文字チャットを依存させません。ただし核心設定の不正、loopback 以外の待ち受け、安全に初期化できない状態、ポート競合は SPP 起動を妨げ得ます。

`hotwords_version=1`、`hotwords_count>0`、`hotwords_backend_supported=true` と実際のスクリプトを確認します。辞書ファイルだけではモデルに届いた証拠になりません。`asr.language=auto` は中日語を送れ、固定言語は選択に従います。精度保証ではないので F8 とゲーム・SPP の ASR ログで確認します。[音声診断](VOICE_SETUP.md#asr-troubleshooting)も参照してください。
