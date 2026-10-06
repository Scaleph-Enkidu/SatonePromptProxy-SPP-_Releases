[简体中文](../zh-CN/VOICE_SETUP.md) | [English](../en/VOICE_SETUP.md) | [日本語](VOICE_SETUP.md)

# 音声の詳細設定とトラブル対処

[導入](INSTALL.md) · [ダウンロード](DOWNLOADS.md) · [ハードウェア](HARDWARE.md)

<a id="stage-3"></a>
[初回 TTS 導入：第 3 段階](INSTALL.md#stage-3)

<a id="stage-4"></a>
[初回 ASR 導入：第 4 段階](INSTALL.md#stage-4)

AIChat 1.18.28 + SPP 5.10.8 向けです。TTS と ASR は独立し、ONNX も不要です。主パッケージには Neutral WAV があり、GPT-SoVITS、声の重み、ASR 環境・モデルは別途導入します。TTS の機器は `tts_infer.yaml` の `device`／`is_half`、Fun-ASR の CPU は `asr.server_script` で専用コピーを指定します。SPP に `asr.device` はありません。

2026-10-01 の保守者のローカル確認は過去の記録であり、新規環境・機器・声・サービスの全組み合わせの合格ではありません。自分の PC で読み込み、発声、F8 認識を確認してください。

| ポート | サービス | 用途 |
| --- | --- | --- |
| 11435 | SPP | ゲームの共通音声 URL、`/tts`・`/asr`・状態表示 |
| 9880 | GPT-SoVITS API | 合成バックエンド |
| 9881 | Fun-ASR | 認識バックエンド、`/health` |

ゲームの共通音声 URL は `http://127.0.0.1:11435` にします。ローカルで待ち受け、ルーターのポート開放は不要です。

<a id="voice-sources"></a>
## 声の重み・参考音声・出典

この構成の声は日本語を中心にしています。中国語・英語の UI と字幕に対応していても、その声の各言語、特に英語の発音を保証しません。希望する発話言語に合うモデルを試してください。

| 素材 | 役割 | 入手先 |
| --- | --- | --- |
| 基礎・テキストモデル | GPT-SoVITS を動かす | 統合パッケージまたは[公式モデル](https://huggingface.co/lj1995/GPT-SoVITS/tree/main) |
| 声の GPT `.ckpt`／SoVITS `.pth` | v2／v2Pro／v2ProPlus 等に対応する学習済みの声 | 作者の元の公開ページ |
| 参考 WAV と正確な台詞 | 個々の合成の発声例 | 自分の録音、または利用許諾のある音声 |

例では**後藤ひとりの v2ProPlus 重みと、Mayuri の WAV・日本語台詞**を使います。役割は別で、Mayuri のモデル重みを後藤の組に混ぜる必要はありません。

- lpkpaco 氏の後藤モデル：[モデルページ](https://huggingface.co/lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models)、[作者プロジェクト](https://github.com/lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models)、[v2ProPlus gotoh-v1-3-1](https://huggingface.co/lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models/tree/main/models/Hitori_Gotoh/v2ProPlus/gotoh-v1-3-1)。
- [GPT 重み](https://huggingface.co/lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models/resolve/main/models/Hitori_Gotoh/v2ProPlus/gotoh-v1-3-1/GPT/gotoh-v1-3-1-e16.ckpt?download=true)、約 155 MB → `GPT-SoVITS/GPT_weights_v2ProPlus/gotoh-v1-3-1-e16.ckpt`。
- [SoVITS 重み](https://huggingface.co/lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models/resolve/main/models/Hitori_Gotoh/v2ProPlus/gotoh-v1-3-1/SoVITS/gotoh-v1-3-1_e8_s368.pth?download=true)、約 173 MB → `GPT-SoVITS/SoVITS_weights_v2ProPlus/gotoh-v1-3-1_e8_s368.pth`。
- SteinsGateSg の Mayuri 参考音声：[プロジェクト](https://huggingface.co/SteinsGateSg/mayuri-voice)、[refs](https://huggingface.co/SteinsGateSg/mayuri-voice/tree/main/refs)、[台詞索引](https://huggingface.co/SteinsGateSg/mayuri-voice/blob/main/refs/index.csv)。付属は Neutral のみで、他の WAV／TXT は任意です。

必要なのは後藤の 2 重みで、数 GB の全リポジトリや同名に見える v4 ファイルではありません。Mayuri の `models/gpt`・`models/sovits` も不要です。記録時の表記は後藤が `cc-by-nc-sa-4.0`、Mayuri が `License: other` です。各公開元の条件に従ってください。この組み合わせは本プロジェクトの例で、両作者が共同認証した構成ではありません。最終的には試聴して確認します。

SPP は標準 RIFF/WAVE として読めること、長さ **3～10 秒**、台詞が空でないことを確認します。主パッケージに含むのは `MAY_1158_Neutral.wav` で、全 `MAY_*.wav` ではありません。

<a id="tts-test"></a>
## 2 層の TTS を別々に試す

次のローカル合成テストは主会話モデルを呼びません。

### GPT-SoVITS 単体

`run_api.bat` を起動したまま [9880/docs](http://127.0.0.1:9880/docs) の **POST /tts** → **Try it out** を開き、要求本文を置き換えます。

```json
{
  "text": "こんにちは。",
  "text_lang": "ja",
  "ref_audio_path": "D:/LofiMOD/SatonePromptProxy/mayuri-voice/refs/MAY_1158_Neutral.wav",
  "prompt_text": "嫌がってるのに無理やり着せたりしてねトラウマになっちゃったら良くないもん。",
  "prompt_lang": "ja",
  "media_type": "wav",
  "streaming_mode": false
}
```

パスは実環境に合わせ、参考台詞は変えません。**Execute** を押し、HTTP 200 と音声応答を確認します。**Download file** で WAV を保存して再生してください。JSON エラーなら message／Exception を読み、モデル・パス・言語を直します。ページが開かなければ API ウィンドウと待ち受けを確認します。別の WebUI の起動だけでは API の準備完了になりません。

### SPP 経由

SPP を起動し、エクスプローラーで `D:\LofiMOD\SatonePromptProxy` を開いてアドレス欄へ `powershell` と入力します。ASR 導入で使った CMD ではなく、**PowerShell** で次を実行します。

```powershell
$satoneBody = @{ text = '[Neutral] こんにちは。'; text_lang = 'ja'; media_type = 'wav'; streaming_mode = $false } | ConvertTo-Json
Invoke-WebRequest -Uri 'http://127.0.0.1:11435/tts' -Method Post -ContentType 'application/json; charset=utf-8' -Body ([System.Text.Encoding]::UTF8.GetBytes($satoneBody)) -OutFile 'D:\LofiMOD\SatonePromptProxy\spp-test.wav'
```

`spp-test.wav` を再生します。導入済みの `[Happy]`・`[Sad]` などに変えて個別に試せます。角括弧と英語タグの綴りは保ちます。両方成功したら F9 → TTS で `ja`、0 より大きい音量、共通 URL 11435 を確認し、保存・適用してメッセージを送ります。

<a id="emotions-26"></a>
## 任意：26 感情の参考音声

SPP は `emotion_tts.mapping` → `profiles` → `path` を参照し、ファイル名から感情を推測しません。独自名でも設定と一致すれば使えます。表は記録済みの 5.9.1 設定／`profiles_26.csv` の標準名で、後の個人設定とは異なる場合があります。出典側の `worried` などの分類は SPP のタグと同じではなく、感情表現の一致を保証しません。

実体の WAV／TXT を取得して `mayuri-voice/refs` に置き、右列の名前にします。TXT は同じ名前で拡張子だけ変えます。同じ元音声を 2 タグで使う場合は 2 コピーを作り、名前の付け替えで片方を失わないようにします。**24 種の録音を 26 設定項目に対応させた表**です。既存の mapping・profiles、`fallback_profile: "Neutral"`、空の `ref_root` を基本に、実際の配置が異なる場合だけ直します。全設定を標準ファイルで上書きしないでください。

| タグ（原綴り） | 意味 | 元 WAV／TXT | refs 内の名前 |
| --- | --- | --- | --- |
| `Neutral` | 平静・中立 | [worried/MAY_1158.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/worried/MAY_1158.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/worried/MAY_1158.txt?download=true) | `MAY_1158_Neutral.wav` |
| `Happy` | 嬉しい | [teasing/MAY_0336.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/teasing/MAY_0336.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/teasing/MAY_0336.txt?download=true) | `MAY_0336_Happy.wav` |
| `Excited` | 興奮 | [excited/MAY_0279.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/excited/MAY_0279.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/excited/MAY_0279.txt?download=true) | `MAY_0279_Excited.wav` |
| `Relaxed` | リラックス | [serious/MAY_0046.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/serious/MAY_0046.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/serious/MAY_0046.txt?download=true) | `MAY_0046_Relaxed.wav` |
| `Sad` | 悲しい | [sad/MAY_0160.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/sad/MAY_0160.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/sad/MAY_0160.txt?download=true) | `MAY_0160_Sad.wav` |
| `Crying` | 泣く | [serious/MAY_1382.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/serious/MAY_1382.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/serious/MAY_1382.txt?download=true) | `MAY_1382_Crying.wav` |
| `Pouting` | すねる | [embarrassed/MAY_0030.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/embarrassed/MAY_0030.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/embarrassed/MAY_0030.txt?download=true) | `MAY_0030_Pouting.wav` |
| `Tired` | 疲れ | [gentle/MAY_1311.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/gentle/MAY_1311.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/gentle/MAY_1311.txt?download=true) | `MAY_1311_Tired.wav` |
| `Sleepy` | 眠い | [other/MAY_0529.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/other/MAY_0529.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/other/MAY_0529.txt?download=true) | `MAY_0529_Sleepy.wav` |
| `Angry` | 怒り | [teasing/MAY_0355.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/teasing/MAY_0355.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/teasing/MAY_0355.txt?download=true) | `MAY_0355_Angry.wav` |
| `Chiding` | たしなめる | [serious/MAY_0575.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/serious/MAY_0575.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/serious/MAY_0575.txt?download=true) | `MAY_0575_Chiding.wav` |
| `Nervous` | 緊張 | [worried/MAY_0035.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/worried/MAY_0035.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/worried/MAY_0035.txt?download=true) | `MAY_0035_Nervous.wav` |
| `Afraid` | 恐れ | [worried/MAY_0512.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/worried/MAY_0512.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/worried/MAY_0512.txt?download=true) | `MAY_0512_Afraid.wav` |
| `Confused` | 困惑 | [embarrassed/MAY_0170.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/embarrassed/MAY_0170.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/embarrassed/MAY_0170.txt?download=true) | `MAY_0170_Confused.wav` |
| `Curious` | 好奇心 | [embarrassed/MAY_0170.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/embarrassed/MAY_0170.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/embarrassed/MAY_0170.txt?download=true) | `MAY_0170_Curious.wav` |
| `Think` | 思案 | [serious/MAY_0328.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/serious/MAY_0328.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/serious/MAY_0328.txt?download=true) | `MAY_0328_Think.wav` |
| `Surprised` | 驚き | [serious/MAY_1464.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/serious/MAY_1464.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/serious/MAY_1464.txt?download=true) | `MAY_1464_Surprised.wav` |
| `Shocked` | 強い衝撃 | [teasing/MAY_0201.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/teasing/MAY_0201.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/teasing/MAY_0201.txt?download=true) | `MAY_0201_Shocked.wav` |
| `Shy` | 照れ | [gentle/MAY_0838.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/gentle/MAY_0838.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/gentle/MAY_0838.txt?download=true) | `MAY_0838_Shy.wav` |
| `Affectionate` | 親愛 | [gentle/MAY_1410.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/gentle/MAY_1410.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/gentle/MAY_1410.txt?download=true) | `MAY_1410_Affectionate.wav` |
| `Playful` | おどける | [teasing/MAY_0336.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/teasing/MAY_0336.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/teasing/MAY_0336.txt?download=true) | `MAY_0336_Playful.wav` |
| `Teasing` | からかう | [happy/MAY_1063.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/happy/MAY_1063.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/happy/MAY_1063.txt?download=true) | `MAY_1063_Teasing.wav` |
| `Mocking` | 嘲る | [neutral/MAY_0939.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/neutral/MAY_0939.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/neutral/MAY_0939.txt?download=true) | `MAY_0939_Mocking.wav` |
| `Sarcastic` | 皮肉 | [excited/MAY_1428.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/excited/MAY_1428.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/excited/MAY_1428.txt?download=true) | `MAY_1428_Sarcastic.wav` |
| `Smug` | 得意げ | [neutral/MAY_0485.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/neutral/MAY_0485.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/neutral/MAY_0485.txt?download=true) | `MAY_0485_Smug.wav` |
| `Disagree` | 反対 | [neutral/MAY_0053.wav](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/neutral/MAY_0053.wav?download=true) · [TXT](https://huggingface.co/SteinsGateSg/mayuri-voice/resolve/main/refs/neutral/MAY_0053.txt?download=true) | `MAY_0053_Disagree.wav` |

`Think`、`Surprised`、`Disagree` などは原綴りのまま使い、`Thinking`、`Surprise`、翻訳名に変えません。拡張子を表示し、`.wav.wav`／`.txt.txt` を避けます。

### 台詞の優先順

記録済みの標準 prompt は確認した Mayuri 索引と一致します。同じ音声なら残せますが、録音を替えたら台詞も更新してください。

**空でない設定 `prompt` が優先され、空の場合だけ WAV と同名の隣接 `.txt` を読みます。** UTF-8 TXT を使う例として、既存項目だけを次のように編集します。

```json
"Neutral": {
  "path": "MAY_1158_Neutral.wav",
  "prompt": "",
  "lang": "ja"
}
```

TXT は WAV 内で実際に話している日本語原文にし、試聴で確認します。出典のフォルダー名を保つ方法もあります。`ref_root` を元の `refs` にし、Neutral を `worried/MAY_1158.wav`、prompt を空にすれば隣の `MAY_1158.txt` を読めます。配置を混ぜてパス更新を忘れないでください。`profiles_26.csv` だけを編集しても実設定は変わりません。

SPP を再起動し、[TTS 状態](http://127.0.0.1:11435/tts/status)の `mapping`、`profiles`、`validation` と起動時の Voice Profile チェックを確認します。標準全項目が正しければ正常 26・異常 0 になります。各タグを SPP 経由で試してください。ファイル不足、長さ不正、空台詞は Neutral に戻る場合があるため、音が出ても指定音声を使った証拠にはなりません。Neutral も壊れていれば代替できません。正常なファイルでも 26 感情が明確に聞き分けられる保証はありません。

<a id="tts-troubleshooting"></a>
## TTS の問題

| 症状 | 対処 |
| --- | --- |
| 起動でエラー後、キー待ちになる | 画面を保持し、最初の traceback、付属 Python、後藤 2 重み、基礎モデルを確認 |
| `fall back to default t2s_weights_path`／`vits_weights_path` | YAML と実ファイルの位置を直し、再起動して使用重みを確認 |
| `CUDA is not available` | NVIDIA ドライバー・パッケージを合わせるか、完全な CPU 設定へ |
| 有効な Neutral がない | `validation.Neutral.valid` と `resolved_path` を確認し、第 3 段階で旧設定を修正 |
| 1 感情しか聞こえない | 付属は Neutral のみ。任意参考音声を追加して個別試聴 |
| WAV は再生できるがゲームが無音 | ゲーム TTS 音量、Windows ミキサー、保存・適用を確認 |
| アドレス使用中 | 自分の旧 9880 API を終了し、1 つだけ起動 |
| WebUI の声変更がゲームに反映されない | `run_api.bat` が実際に読む YAML を編集して API 再起動 |
| CPU 合成が遅い | 短文で合成確認後に待ち時間を評価。音量や ONNX 設定では高速化しない |

SPP ログは `D:\LofiMOD\SatonePromptProxy\SatonePromptProxy_v5.10.8.log`、GPT-SoVITS のエラーは API ウィンドウで確認します。最初のエラーと完全なパスを残してください。

連動起動では `Set_GPTSoVITS_RunApi_Path.bat` に `D:\LofiMOD\GPT-SoVITS\run_api.bat` を入力し、`[OK] Saved` を確認します。ゲームの TTS 起動先を `D:\LofiMOD\SatonePromptProxy\Start_AIChat_Services.bat` にして自動起動を有効化・保存し、次回確認します。`service_paths.ini` を読んで準備済みサービスを起動するだけで、環境や重みは導入しません。直接 `run_api.bat` を使っても構いません。

<a id="asr-cpu"></a>
<a id="asr-troubleshooting"></a>
## ASR とマイクの問題

CPU の初回設定は[導入第 4 段階](INSTALL.md#asr-cpu)です。

| 症状 | 対処 |
| --- | --- |
| Python／py がない | 完全版 Python 3.12 x64 とランチャーを入れ、CMD を開き直す |
| pip／import エラー | `.venv\Scripts\python.exe` で手順のチェックを通す |
| `model.pt` があるのに失敗 | 設定・tokenizer・Qwen3 全体を確認し、完全な `snapshot_download` を再実行 |
| CPU 設定なのに旧サービスを使用 | 旧 9881 を終了し、SPP の CPU `server_script` を確認 |
| `ready` が false のまま | `last_error` と最初の Python エラー。フォルダーの存在や pip 成功だけでは不足 |
| health は正常、F8 が無反応 | Windows 権限、実際のマイク、保存・適用を確認 |
| F8 は正常、連続会話で欠ける | 原音を調べてから VAD を 1 項目ずつ調整 |
| 準備完了でも遅い | 同じ短文を選択機器で比較し、発話長と遅延を記録 |
| TTS 未導入で ASR URL が見つからない | TTS 設定内の共通 URL 11435 を使用。マイクは連続会話設定で選択 |

F9 の連続会話診断には共通マイク選択、**無音・発話の各 10 秒録音**（ローカルのみ、ASR へ送らず終了後に待ち受け停止）、**次の押して話す原音を保存**（通常の認識も実行）があります。しきい値 **0.0005** の一時試行は保存後に有効となり、通話停止後に戻ります。万能値ではなく戻せる試行として使ってください。まず F8 を確認し、開始・停止条件を 1 つずつ変更して保存・適用し、現在の発言が終わってから再試験します。

[SPP ASR 状態](http://127.0.0.1:11435/asr/status)と[backend health](http://127.0.0.1:9881/health)で `ready`、各パス、`hotwords_backend_supported`、`hotwords_supported` を確認します。対応フラグは認識精度の保証ではないので F8 で実際に発音します。health はモデル機器を報告しません。CPU は明示的な `device="cpu"`、解決済みパス、実認識で確認します。更新ごとに CPU コピーへ新実装を反映してください。

`FunASR-Runtime` の CMD で、診断・復元用に版を保存できます。

```bat
.venv\Scripts\python.exe -m pip freeze > asr-environment.txt
```

根拠：[Fun-ASR 依存関係](https://github.com/QwenAudio/Fun-ASR/blob/main/requirements.txt)、[PyTorch 2.9.1 CPU／CUDA](https://pytorch.org/get-started/previous-versions/)、[Fun-ASR-Nano-2512](https://huggingface.co/FunAudioLLM/Fun-ASR-Nano-2512)、[FunASR 1.3.26](https://pypi.org/project/funasr/1.3.26/)。既存環境を変える前に[更新](UPGRADE.md)と[バックアップ](DATA_AND_PRIVACY.md)を確認してください。
