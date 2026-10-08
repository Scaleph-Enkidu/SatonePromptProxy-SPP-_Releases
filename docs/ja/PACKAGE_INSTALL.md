[简体中文](../zh-CN/PACKAGE_INSTALL.md) | [English](../en/PACKAGE_INSTALL.md) | [日本語](PACKAGE_INSTALL.md)

# 導入とロールバック

**AIChat 1.18.30 + SPP 5.10.10 · 2026-10-08**

今回のリリースは、記憶取り込み、音声エコー除去、終了時の後処理、日付による検索の計 9 件の修正をまとめています。AIChat と SPP の両方を更新してください。三言語の説明とパッケージ内の入口も更新しました。

ゲームと SPP を終了し、旧 SPP フォルダー全体とプラグイン設定を保存してから AIChat DLL／PDB と SPP を更新します。SPP を移す場合は[更新手順](UPGRADE.md)に従って記憶を取り込んでください。修正済みの Relaxed 設定を再度初期化する必要はありません。GitHub 自動生成の Source code ZIP は導入用ではありません。TTS、ASR、意味検索モデルは任意の外部コンポーネントです。

ルートと両コンポーネントの README に中国語・英語・日本語の入口があり、全文はそれぞれの `docs/zh-CN`、`docs/en`、`docs/ja` にあります。新規導入では SPP のフォルダー構成を保ってください。AIChat DLL／PDB をゲームの `BepInEx/plugins` へ置き、AIChat DLL は 1 つだけにしてバックアップを外に保存します。戻すときはサービスを止め、旧プログラムと更新前のデータ一式を復元します。`BUILD_INFO.json` に本版のソース、バイナリ、各ファイルのハッシュを記録しています。

[Install](INSTALL.md) · [Upgrade](UPGRADE.md) · [Checks](PACKAGE_CHECKLIST.md)
