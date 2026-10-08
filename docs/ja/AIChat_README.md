[简体中文](../zh-CN/AIChat_README.md) | [English](../en/AIChat_README.md) | [日本語](AIChat_README.md)

# AIChat 1.18.30：パッケージ README

[文書ホーム](README.md) · [導入](INSTALL.md) · [更新](UPGRADE.md)

Windows／Steam 版 Chill with You: Lo-Fi Story のゲーム側プラグインで、SPP 5.10.10 と組み合わせます。UI／字幕は中国語・英語・日本語に対応し、発音は外部の声・モデルに依存します。

ゲームを終了して BepInEx 5.4.23.5 x64 を導入し、一度起動します。`AIChat/AIChat.dll` と `AIChat.pdb` をゲームの `BepInEx/plugins` へ入れます。DLL は 1 つだけにし、バックアップは外へ置いてください。F9 で画面を開き、SPP EXE パスと LLM 接続を保存・適用します。Enter は送信、Shift+Enter は改行です。F8 の音声入力には任意 ASR が必要です。連続会話は無効から始まり、自分で有効にします。

N15 は Relaxed のコップ残留を修正します。旧 `StablePoseOverrides` の Relaxed を `Relaxed=752,50,51` にするか、保存後に `com.username.chillaimod.cfg` だけを再生成します。BepInEx 設定全体や記憶を消さないでください。N14 の 409 参考ポリシー更新修正も保たれています。[更新内容](releases/AIChat_v1.18.28_SPP_v5.10.8.md)を参照してください。

最近 50 発言の表示は保存上限ではありません。3 プロファイル、人格、好感度、感情、原作同期、Meta は[システム説明](README.md#systems)にあります。API 枠は自分で用意し、TTS・ASR・ONNX は個別に選べます。[負荷](HARDWARE.md)、[データ保護](DATA_AND_PRIVACY.md)、[許諾範囲](LICENSE_SCOPE.md)を確認してください。

今回のリリースは、記憶取り込み、音声エコー除去、終了時の後処理、日付による検索の計 9 件の修正をまとめています。AIChat と SPP の両方を更新してください。三言語の説明とパッケージ内の入口も更新しました。
