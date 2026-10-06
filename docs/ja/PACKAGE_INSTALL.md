[简体中文](../zh-CN/PACKAGE_INSTALL.md) | [English](../en/PACKAGE_INSTALL.md) | [日本語](PACKAGE_INSTALL.md)

# N15 文書改訂パッケージ：導入と復元

**AIChat 1.18.28 + SPP 5.10.8**、文書改訂 **docs_r1、2026-10-06**。公開済み N15 の文書を三言語化したもので、新しい未公開実行候補ではありません。元 ZIP は残し、文書以外の実行ファイルはすべて同一です。

ルート `README.md` が三言語入口、`AIChat/README.md` と `SatonePromptProxy/README.md` が各部の入口です。全文は `docs/zh-CN`、`docs/en`、`docs/ja` にあり、オフラインで読めます。外部ダウンロード、Web 状態、ソースのリンクには対応サービス・通信が必要です。

1. ゲーム・SPP を終了し、旧バイナリ、SPP 個人フォルダー全体、ゲームの `BepInEx/config` を保存します。
2. AIChat DLL／PDB を `BepInEx/plugins` へ入れます。新規 SPP は全フォルダーが必要です。N9～N14 から同じ 5.10.8 を使っている場合、EXE 自体は同一です。
3. 新しい SPP フォルダーに移す場合は[取り込み](UPGRADE.md)で旧絶対パスを指定し、先に旧データを消しません。
4. Relaxed を `752,50,51` に更新するか、保存してプラグイン CFG だけを再生成します。再生成ではパス、API、しきい値、キー、感情表示などが初期化されます。
5. ログの 1.18.28 と[確認項目](PACKAGE_CHECKLIST.md)を検証します。依存環境・音声は[完全手順](INSTALL.md)を参照してください。

復元時は停止し、対応する旧 DLL／PDB、SPP、更新前の設定・データ全体を戻します。文書の閲覧・交換だけならセーブ移行は不要です。`BUILD_INFO.json` は元の N15 封存記録を保持し、`DOCUMENTATION_REVISION.json` に今回の文書変更、元 ZIP ハッシュ、未変更ファイルの証明を記録します。
