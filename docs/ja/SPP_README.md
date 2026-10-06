[简体中文](../zh-CN/SPP_README.md) | [English](../en/SPP_README.md) | [日本語](SPP_README.md)

# SatonePromptProxy 5.10.8：パッケージ README

[文書ホーム](README.md) · [導入](INSTALL.md) · [移設](PORTABLE_DEPLOYMENT.md)

AIChat 1.18.28 と組み合わせ、モデル代理、人格、3 記憶、関係、キーワード・任意意味検索、TTS／ASR 転送を担当します。`D:\LofiMOD\SatonePromptProxy` などに完全な構成で置きます。

`SatonePromptProxy.exe` を実行し、`127.0.0.1:11435` の待ち受けを確認して開いたままにします。F9 で SPP パス、サービスのキー、モデルを設定して保存・適用します。初回は `config.example.json` から `config.json` を作るため、個人設定を例で上書きしないでください。`Start_Text_Chat.bat` も同じサービスを起動します。他のツールは[サービス管理](systems/SERVICES.md)を参照してください。

文字とキーワード検索に Python は不要です。任意の CPU ONNX E5 int8／ORT は別途約 94 MB で、停止後に Verify／Enable を実行します。TTS・ASR はこれに依存しません。付属するのは `mayuri-voice/refs/MAY_1158_Neutral.wav` で、GPT-SoVITS 全体、声の重み、Fun-ASR モデルではありません。[音声設定](VOICE_SETUP.md)に環境と試験手順があります。

ゲームの共通 URL は `http://127.0.0.1:11435` で、TTS 9880、ASR 9881 に転送します。パス・状態・CPU 手順は[導入説明](INSTALL.md)に従ってください。ログ画面はコマンド入力欄ではありません。

更新時は停止して旧実行フォルダー全体を残し、新しいフォルダーへ記憶を取り込みます。`local_v1` は消せるキャッシュではありません。`SatonePersona_v4.6.txt` は共有、長期関係は各プロファイルで独立します。大規模履歴の起動は遅いままです。[負荷](HARDWARE.md)と、キー・会話・ベクトルを守る[データ説明](DATA_AND_PRIVACY.md)を確認してください。

`docs_r1` は EXE、BAT、標準設定、人格、ASR スクリプト、モデル、参考録音を変えません。[クレジットと許諾](LICENSE_SCOPE.md)、第三者の元ライセンスも保持します。
