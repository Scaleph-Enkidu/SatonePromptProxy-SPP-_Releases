[简体中文](../zh-CN/INSTALL.md) | [English](../en/INSTALL.md) | [日本語](INSTALL.md)

# 4 段階の導入手順

[ホーム](README.md) · [ダウンロードとハッシュ](DOWNLOADS.md) · [ライセンスの範囲](LICENSE_SCOPE.md)

対象は **AIChat 1.18.30 + SPP 5.10.10**、更新日は 2026-10-08 です。既存ユーザーは先に[更新とバックアップ](UPGRADE.md)を読んでください。AIChat と SPP の両方を更新してください。任意モデルの変更はありません。

例では `D:\LofiMOD` を使います。`C:\LofiMOD` などに置く場合は、対応するすべてのパスを統一して変更してください。F9 の UI は中国語・英語・日本語に対応しています。以下の操作名は機能を示し、古い画像では中国語表示の場合があります。外部ツールの問題を調べる際は、短い英数字のパスを推奨します。

音声導入前に[ハードウェアと起動時間](HARDWARE.md)を確認してください。文字チャットだけでも使えます。ONNX・TTS・ASR は、その後に個別に追加できる任意機能です。

<a id="stage-1"></a>
## 1. 文字チャット

### プラグインの導入

1. ゲームを終了します。Steam の管理 → ローカルファイルを閲覧でゲームフォルダーを開きます。
2. [BepInEx 5.4.23.5 Windows x64](https://github.com/BepInEx/BepInEx/releases/download/v5.4.23.5/BepInEx_win_x64_5.4.23.5.zip) をダウンロードし、`BepInEx` と `winhttp.dll` をゲーム EXE と同じ場所に展開します。一度起動して終了し、設定フォルダーを生成します。
3. [対応するプログラムセット](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.18.30_SPP-v5.10.10/SatoneMod_AIChat_1.18.30_SPP_5.10.10_Windows_x64.zip)を取得します。`AIChat/AIChat.dll` と `AIChat.pdb` をゲームの `BepInEx\plugins` にコピーし、旧プラグインを置き換えます。重複 DLL を残さないでください。既存ユーザーは [UPGRADE](UPGRADE.md) の Relaxed アニメーション設定の更新も必要です。
4. `SatonePromptProxy` フォルダー全体を `D:\LofiMOD\SatonePromptProxy` に展開します。付属データと相対配置を保ち、ゲームのプラグインフォルダーには入れません。

### SPP の起動と接続

`SatonePromptProxy.exe` を実行します。開く画面はコマンド入力欄ではなくログです。閉じずに、`http://127.0.0.1:11435/v1/chat/completions` の待ち受け表示を確認します。導入用コマンドをここへ貼り付けないでください。

ゲームで F9 を押して設定を開き、SPP・記憶（人格プロキシ）の EXE パスに `D:\LofiMOD\SatonePromptProxy\SatonePromptProxy.exe` を指定します。必要ならエクスプローラーからフォルダーパスをコピーして EXE 名を追加します。自動起動を使う場合は有効にし、保存・適用後に実行状態を確認します。

### LLM 接続の適用

LLM 設定で OpenAI・DeepSeek などのサービスを選び、その API Key とモデル名を入力します。中継サービスなら、案内に従ってベース URL と認証を設定します。画面の標準モデル名は例であり、全アカウントで使える保証はありません。ChatGPT の定額契約は API 残高とは別です。[費用](API_COST.md)と[接続](systems/CONNECTIONS.md)を参照してください。

保存・適用して、適用済み・成功の表示を待ちます。編集欄の内容だけで切り替え完了と判断しないでください。新規導入では新しいプロファイルを準備します。旧記憶の取り込みが提示された場合は旧フォルダーを指定するか、明示的にスキップします。スキップしても旧ファイルは消えません。

短い挨拶を入力し Enter で送信します。Shift+Enter は改行です。返答が来れば文字チャットの確認になります。原作の独り言が会話を遮る場合は、ペンギンのアバター付近にある原作の独り言フィルターで減らせます。N15 のコップ修正を使うには、旧設定のホワイトリスト更新も必要です。

### よく使う設定

SPP の自動終了は自動起動とは別です。ゲーム終了後の実際の状態を確認してください。3 つの記憶プロファイルは履歴・関係が別で、人格ファイル `SatonePersona_v4.6.txt` は共有します。独自編集はバックアップしてください。記憶を削除せずにサービス・モデルを切り替えられます。キーと会話データの扱いは[プライバシー](DATA_AND_PRIVACY.md)を参照してください。

<a id="stage-2"></a>
## 2. 任意の ONNX 意味検索

先に「ピアノを練習している」などの会話を完了させます。空のプロファイルでは過去検索の動作を確認できません。

1. 返答の完了を待ってゲームを終了し、`Stop_SatonePromptProxy.bat` を実行します。
2. 約 94 MB の [E5 small int8 + ORT 1.30.0](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.17.1_SPP-v5.9.1-license-r1/Satone_Semantic_E5_small_int8_ORT_1.30.0_Windows_x64.zip) を取得します。中の `models` を `SatonePromptProxy.exe` の隣に置きます。`BepInEx\plugins` や二重の `models` フォルダーには入れません。
3. `Verify_Semantic_Recall.bat`、続いて `Enable_Semantic_Recall.bat` を実行し、明確な成功表示を確認します。一瞬で閉じた場合は成功とせず、下の[スクリプト診断](#semantic-script)へ進みます。
4. SPP を再起動し、`Open_Dashboard.bat` から対象プロファイルの Recall を開き、完了済みの会話を検索します。Dashboard の閲覧対象を変えても、ゲームの有効プロファイルは変わりません。

索引状態はボタンを押すたびに更新されます。ページを開くだけではなく、検索で準備が始まります。`model_loaded: true`、`semantic_state: ready` と、`local:memory1` など正しい `semantic_scope` を確認してください。`loading`、`building`、`waiting` を準備完了と取り違えないでください。空のプロファイルで waiting は正常な場合があります。

`user_text` と `assistant_text` を確認してから、言い換えでも試します。必ず一致するわけではありません。`semantic_ready: false` ではキーワード検索へ戻れます。処理中なら会話終了後に再試行します。TTS・ASR のために ONNX を入れる必要はありません。

無効化は SPP 停止 → `Disable_Semantic_Recall.bat` → 再起動です。会話は削除されません。[ONNX の詳細](ONNX_SETUP.md)と[負荷の測定](HARDWARE.md)も参照してください。

<a id="stage-3"></a>
## 3. GPT-SoVITS による発声

例では後藤ひとりの v2ProPlus 重みと、Mayuri の日本語 Neutral 参考音声を組み合わせます。役割とライセンスは異なるため、[音声素材の出典](VOICE_SETUP.md#voice-sources)を確認してください。主パッケージには Neutral WAV がありますが、GPT-SoVITS 環境・声の重みは別途必要です。UI／字幕の多言語対応は、この声の全言語での発音を保証しません。

### 3.1 環境と重み

[7-Zip](https://www.7-zip.org/) で、適切な公式 Windows 統合パッケージを展開します。

| 環境 | ダウンロード |
| --- | --- |
| CPU、または RTX 50 以外の対応 NVIDIA GPU | [GPT-SoVITS-v2pro-20250604.7z](https://huggingface.co/lj1995/GPT-SoVITS-windows-package/resolve/main/GPT-SoVITS-v2pro-20250604.7z?download=true)、約 8.19 GB |
| NVIDIA RTX 50 | [GPT-SoVITS-v2pro-20250604-nvidia50.7z](https://huggingface.co/lj1995/GPT-SoVITS-windows-package/resolve/main/GPT-SoVITS-v2pro-20250604-nvidia50.7z?download=true)、約 8.84 GB |

CUDA 手順は NVIDIA 用です。AMD・Intel では CPU 経路か、別途対応が確認されたバックエンドを使います。[NVIDIA ドライバー](https://www.nvidia.com/Download/index.aspx)も適切なものに更新してください。統合パッケージの Python に Fun-ASR を混ぜないでください。

`D:\LofiMOD\GPT-SoVITS` の直下に `api_v2.py`、`runtime\python.exe`、`GPT_SoVITS\configs\tts_infer.yaml` が来るよう展開します。余分な入れ子フォルダーに注意してください。

[lpkpaco 氏の後藤ひとり v2ProPlus](https://huggingface.co/lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models) から、CC BY-NC-SA 4.0 で公開されている次の 2 ファイルを取得します。

| ファイル | GPT-SoVITS 内の配置 |
| --- | --- |
| [gotoh-v1-3-1-e16.ckpt](https://huggingface.co/lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models/resolve/main/models/Hitori_Gotoh/v2ProPlus/gotoh-v1-3-1/GPT/gotoh-v1-3-1-e16.ckpt?download=true) | `GPT_weights_v2ProPlus/gotoh-v1-3-1-e16.ckpt` |
| [gotoh-v1-3-1_e8_s368.pth](https://huggingface.co/lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models/resolve/main/models/Hitori_Gotoh/v2ProPlus/gotoh-v1-3-1/SoVITS/gotoh-v1-3-1_e8_s368.pth?download=true) | `SoVITS_weights_v2ProPlus/gotoh-v1-3-1_e8_s368.pth` |

`GPT_SoVITS/pretrained_models` 内の `chinese-roberta-wwm-ext-large`、`chinese-hubert-base`、`sv/pretrained_eres2netv2w24s4ep4.ckpt` の実ファイルも必要です。不足時は[公式 SV 重み](https://huggingface.co/lj1995/GPT-SoVITS/resolve/main/sv/pretrained_eres2netv2w24s4ep4.ckpt?download=true)を取得します。空フォルダーや小さな Git LFS ポインターはモデルではありません。同名に見えても v4 用重みで代用しないでください。

### 3.2 推論設定

`GPT_SoVITS\configs\tts_infer.yaml` を `tts_infer.yaml.bak` にバックアップし、内容を次に置き換えます。

```yaml
custom:
  bert_base_path: GPT_SoVITS/pretrained_models/chinese-roberta-wwm-ext-large
  cnhuhbert_base_path: GPT_SoVITS/pretrained_models/chinese-hubert-base
  device: cuda
  is_half: true
  t2s_weights_path: GPT_weights_v2ProPlus/gotoh-v1-3-1-e16.ckpt
  version: v2ProPlus
  vits_weights_path: SoVITS_weights_v2ProPlus/gotoh-v1-3-1_e8_s368.pth
```

CPU では **2 箇所とも**変更します。`device: cuda` を `device: cpu`、`is_half: true` を `is_half: false` にし、他のパス・版はそのままにします。`custom:` は最上位、下は半角スペース 2 個で字下げします。[公式設定](https://github.com/RVC-Boss/GPT-SoVITS/blob/main/GPT_SoVITS/configs/tts_infer.yaml)と[推論実装](https://github.com/RVC-Boss/GPT-SoVITS/blob/main/GPT_SoVITS/TTS_infer_pack/TTS.py)も参照できます。

### 3.3 API 起動ファイル

`D:\LofiMOD\GPT-SoVITS\run_api.bat` を作り、次を保存します。

```bat
@echo off
cd /d "%~dp0"
"runtime\python.exe" -s api_v2.py -a 127.0.0.1 -p 9880 -c "GPT_SoVITS/configs/tts_infer.yaml"
pause
```

文字コードは UTF-8、種類は「すべてのファイル」にします。エクスプローラーで拡張子を表示し（Windows 11：表示 → 表示 → ファイル名拡張子）、`run_api.bat.txt` になっていないことを確認します。

実行してウィンドウを開いたままにします。起動完了、Uvicorn の `http://127.0.0.1:9880` 待ち受け、v2ProPlus の後藤重みが読み込まれたことを確認します。`CUDA is not available` は準備完了ではありません。ドライバー・パッケージを直すか CPU 設定に変更してください。

[ローカル API 説明](http://127.0.0.1:9880/docs)を開き、`/tts` を確認します。`go-webui.bat` は不要で、別プロセスの WebUI は API の代わりにはなりません。

### 3.4 Neutral 参考音声

`D:\LofiMOD\SatonePromptProxy\mayuri-voice\refs\MAY_1158_Neutral.wav` を再生します。[SPP TTS 状態](http://127.0.0.1:11435/tts/status)で `validation.Neutral.valid` が `true`、`resolved_path` がこの WAV を指すことを確認します。新規の標準設定が動いていれば変更不要です。

旧設定が壊れている場合は SPP を止めて `config.json` をバックアップし、既存の `emotion_tts` 内だけを修正します。`enabled: true`、`upstream_url: "http://127.0.0.1:9880"`、空の `ref_root`、`fallback_profile: "Neutral"` を使います。`profiles.Neutral` は `path: "MAY_1158_Neutral.wav"`、`lang: "ja"`、台詞は次の原文です。

> 嫌がってるのに無理やり着せたりしてねトラウマになっちゃったら良くないもん。

台詞は WAV と一致させ、文書の言語に翻訳しないでください。JSON の文字列は二重引用符、真偽値には引用符を付けません。保存して SPP を再起動し、再検証します。追加の参考音声は[詳細設定](VOICE_SETUP.md#emotions-26)で説明しています。

### 3.5 ゲームと接続

F9 → 設定 → TTS で起動スクリプトを `D:\LofiMOD\GPT-SoVITS\run_api.bat` に設定します。必要なら自動起動を有効にします。**共通音声 URL は `http://127.0.0.1:11435`** のままで、9880・9881 にはしません。この参考構成では朗読言語を `ja`、音量を 0 より大きく（例：1.00）して保存・適用します。

短い挨拶を送り、文字と実際の音声を両方確認します。CPU 合成は待ち時間が長くなることがあります。ゲーム終了後に手動起動した API を閉じ、次の起動で自動起動も確認します。無音なら[単独合成テスト](VOICE_SETUP.md#tts-test)へ進みます。

<a id="stage-4"></a>
## 4. Fun-ASR によるマイク入力

必要なのは動作する文字チャットで、TTS・ONNX は必須ではありません。Fun-ASR-Nano-2512 を使います。ヘッドホンで回り込みを減らしてください。自己音声のエコー抑制は完全ではありません。VAD は一律の数値ではなく、実際の無音時・発話時の入力に合わせて調整します。

### 4.1 専用 Python 環境

[Python 3.12.10 Windows x64](https://www.python.org/ftp/python/3.12.10/python-3.12.10-amd64.exe) の通常インストーラーを使います。埋め込み版ではありません。`py` ランチャーと pip を含め、「Add Python to PATH」を有効にします。`D:\LofiMOD\FunASR-Runtime` を作成して開き、アドレス欄に `cmd` と入力します。以下は **CMD** 用で、SPP のログ画面に入力しません。

```bat
py -3.12 --version
py -3.12 -m venv .venv
.venv\Scripts\python.exe -m pip install --upgrade pip
```

最初の行で Python 3.12.x を確認します。`py` がなければインストーラーの変更からランチャーを追加し、古い CMD を閉じて開き直します。

### 4.2 GPU または CPU を選択

対応する NVIDIA RTX 20/30/40/50 と CUDA 12.8 に対応するドライバーでは次を使います。

```bat
.venv\Scripts\python.exe -m pip install torch==2.9.1 torchaudio==2.9.1 --index-url https://download.pytorch.org/whl/cu128
```

CPU（AMD・Intel 機の CPU 経路を含む）では、上の代わりにこちらを使います。

```bat
.venv\Scripts\python.exe -m pip install torch==2.9.1 torchaudio==2.9.1 --index-url https://download.pytorch.org/whl/cpu
```

続いて共通の依存関係と確認を実行します。

```bat
.venv\Scripts\python.exe -m pip install funasr==1.3.26 transformers==4.51.3 huggingface_hub==0.36.0 zhconv whisper_normalizer pyopenjtalk-plus==0.4.1.post8 compute-wer openai-whisper
.venv\Scripts\python.exe -m pip check
.venv\Scripts\python.exe -c "import torch, torchaudio, funasr, transformers; print('torch', torch.__version__); print('torchaudio', torchaudio.__version__); print('transformers', transformers.__version__); print('cuda', torch.cuda.is_available())"
```

`No broken requirements found`、例外なしの import、Torch／torchaudio の一致する 2.9.1（`+cu128` または `+cpu`）、transformers 4.51.3 を確認します。GPU 経路では CUDA が利用可能、CPU では `False` が正常です。pip の成功だけでは GPU の準備完了を証明しません。この wheel 手順で別の CUDA Toolkit 導入は不要です。[PyTorch の版](https://pytorch.org/get-started/previous-versions/)と [Fun-ASR 依存関係](https://github.com/QwenAudio/Fun-ASR/blob/main/requirements.txt)も参照してください。

### 4.3 モデル全体を取得

同じ環境で実行します。

```bat
.venv\Scripts\python.exe -c "from huggingface_hub import snapshot_download; snapshot_download(repo_id='FunAudioLLM/Fun-ASR-Nano-2512', local_dir='D:/LofiMOD/Fun-ASR-Nano-2512')"
```

Git は不要です。中断したら同じコマンドを再実行します。モデルフォルダーには実体のある `config.yaml`、`configuration.json`、`model.pt`、`multilingual.tiktoken`、完全な `Qwen3-0.6B` が必要です。`model.pt` だけ、空フォルダー、LFS ポインターでは足りません。`-hf`、GGUF、faster-whisper のモデルを名前変更しても互換にはなりません。

<a id="asr-cpu"></a>
### 4.4 サービススクリプト

SPP を停止します。GPU では付属の `D:\LofiMOD\SatonePromptProxy\satone_funasr_server_v1.py` を使います。

CPU では現在の付属ファイルを `D:\LofiMOD\FunASR-Runtime\satone_funasr_server_cpu_v1.py` にコピーし、コピー内の次の行を変更します。

```python
model = AutoModel(model=model_dir, trust_remote_code=True)
```

変更後：

```python
model = AutoModel(model=model_dir, trust_remote_code=True, device="cpu")
```

字下げと他の部分は保ちます。拡張子は `.py` で、`.py.txt` にしません。使用する設定は `asr.server_script` です。存在しない `asr.device` を追加しないでください。

### 4.5 SPP の設定と準備確認

`config.json` をバックアップし、既存の `asr` オブジェクト内の該当項目を編集します。他の設定を保持してください。次は設定の一部分であり、ファイル全体を置き換える内容ではありません。

```json
"asr": {
  "enabled": true,
  "auto_start": true,
  "auto_restart": true,
  "stop_with_proxy": true,
  "python": "D:/LofiMOD/FunASR-Runtime/.venv/Scripts/python.exe",
  "server_script": "D:/LofiMOD/SatonePromptProxy/satone_funasr_server_v1.py",
  "model_path": "D:/LofiMOD/Fun-ASR-Nano-2512",
  "upstream_url": "http://127.0.0.1:9881",
  "language": "auto"
}
```

CPU では `server_script` だけを `D:/LofiMOD/FunASR-Runtime/satone_funasr_server_cpu_v1.py` にします。すべてのパスを実際の配置に合わせ、有効な JSON として保存して SPP を起動します。Python ファイルを別途ダブルクリックしません。

[SPP ASR 状態](http://127.0.0.1:11435/asr/status)で `ready: true` と正しい `python`、`server_script`、`model_path` を確認し、[バックエンド](http://127.0.0.1:9881/health)で `ok: true` を確認します。読み込みには時間がかかる場合があります。失敗時は `SatonePromptProxy_v5.10.10.log` の最初の Python エラーと `last_error` を読みます。9881 に手動起動した旧 GPU サービスが残っている場合は、それを止めてから CPU 構成の SPP を再起動してください。

### 4.6 マイクを選んで話す

Windows のプライバシー設定でデスクトップアプリのマイク利用を許可します。F9 → 設定 → 連続会話で実際のマイクを選び、保存・適用します。押して話す操作と共通で、連続待ち受けを有効にせず選択できます。共通 URL は TTS 設定内にあり、TTS 未導入でも `http://127.0.0.1:11435` を使います。

F8 を押して短く話し、離すか音声ボタンを使います。妥当な認識文と返答を確認してから連続会話を有効にし、保存・適用して、発話と停止で検出を確認します。無効化して保存するか停止ボタンで待ち受けを止めます。ゲーム起動ごとに連続会話は無効から始まります。

SPP 更新後は、新しい付属版から CPU 用コピーを更新し、`device="cpu"` を残します。古い実装を使い続けないでください。[マイク・VAD の診断](VOICE_SETUP.md#asr-troubleshooting)も参照してください。

<a id="upgrade"></a>
## 更新とロールバック

[現在の更新手順](UPGRADE.md)に従い、旧 SPP フォルダー全体とゲーム設定・履歴を保存し、**新しい SPP フォルダー**へ展開して、旧フォルダーの絶対パスから記憶を取り込みます。サービスパスと N15 のホワイトリストを再設定します。DLL／PDB のバックアップは重複読み込みを防ぐため `BepInEx\plugins` の外へ置きます。確実なロールバックには、対応する旧プログラム**とデータ**を戻します。

## よくある問題

| 症状 | 最初に確認すること |
| --- | --- |
| F9 が開かない | ゲーム EXE の隣の BepInEx、plugins 内の DLL、重複がないか |
| SPP が見つからない | EXE パス、実行状態、待ち受けログ |
| API 返答が失敗 | 適用済み接続、キー、モデル権限、API 残高 |
| ONNX の結果がない | 対象プロファイルの完了済み履歴、準備を始める検索 |
| TTS が無音 | 9880 API、参考音声、言語、ゲーム・システム音量 |
| ASR が文字を返さない | 9881 health、SPP ready、Windows 権限、選択マイク |
| SPP 起動後にフレーム低下 | 条件とプロセスを記録し、下記とハードウェア説明を確認 |

<a id="semantic-script"></a>
### 意味検索の BAT がすぐ閉じる

ゲーム・SPP を終了して SPP フォルダーで CMD を開き、必要な操作を直接実行します。

```bat
SatonePromptProxy.exe --semantic-component verify
SatonePromptProxy.exe --semantic-component enable
```

無効化する場合はこちらです。

```bat
SatonePromptProxy.exe --semantic-component disable
```

明確な成功を確認します。起動中・ロック中なら停止して再試行してください。ファイル検証は worker の準備完了を意味しないため、再起動して検索し `ready` を確認します。

<a id="spp-start-window"></a>
### SPP 起動画面とフレーム低下

`SatonePromptProxy.exe` はサービスログを表示します。`Start_Text_Chat.bat` も同じサービスの入口で、旧ツールではウィンドウが最小化される場合があります。非表示・最小化は停止ではありません。待ち受けログと F9 状態を確認します。大きな履歴ではコールドスタートが遅くなることがあります。報告されたゲームのフレーム低下は原因未確定で、再起動が一時的に効いても修正済みとは言えません。[測定結果](HARDWARE.md)を参照してください。

<a id="preserved-voice"></a>
### 保留された音声入力

旧入力は新しいセッションへ自動送信されません。この警告は ONNX の故障でもありません。接続が適用済みの SPP を起動し、F9 の連続会話設定で件数、プロファイル、文字内容を確認します。待ち受けの有効化は不要です。

入力欄へコピーしても下書きになるだけです。送信先プロファイルを確認し、必要なら自分で送信してから待機側のコピーを削除します。待機項目の削除は会話履歴の削除ではありません。音声書き出しは `BepInEx\config\AIChat.preserved-inputs` に録音を保存するだけで、ASR や自動送信は行いません。

1 件ずつ処理します。これらの操作は保存・適用を待たず即時反映され、数秒後に状態と警告が更新されます。ログを共有する前に API Key と私的な会話を伏せてください。
