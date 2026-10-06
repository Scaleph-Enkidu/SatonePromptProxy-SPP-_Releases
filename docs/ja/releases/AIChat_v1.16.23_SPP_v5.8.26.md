[简体中文](../../zh-CN/releases/AIChat_v1.16.23_SPP_v5.8.26.md) | [English](../../en/releases/AIChat_v1.16.23_SPP_v5.8.26.md) | [日本語](AIChat_v1.16.23_SPP_v5.8.26.md)

# AIChat v1.16.23 SPP v5.8.26

[← 履歴一覧](../RELEASE_ARCHIVE.md)

> 過去の公開記録です。配布状況・試験範囲は当時のもので、現行の導入には現在の手順を使ってください。

2026-09-28 の CP14-9 配布です。新規 OpenAI 設定の例は `gpt-6-luna`、DeepSeek は `deepseek-flash` で、案内日を 2026-09-28 としました。既存の独自モデルを保ち、名前も編集可能です。利用可否は提供元資料に従います。会社・キー・モデルの選択は下書きとなり、保存・適用で切り替えます。中継設定は提供元 API に合わせます。

以前の返答状態・音声・エラー・記憶の修正を維持しました。1.16.22＋5.8.26 の主要機能は保守者が実機確認し、標準モデルの変更はローカル CI 13 項目を通過しました。Windows 組み込み管理者が `LA` と表示される際に、正しい認証ファイル権限を不正と扱う問題も修正しました。

`mayuri-voice/refs/MAY_1158_Neutral.wav` が付属します。GPT-SoVITS 環境、Bocchi の GPT／SoVITS 重み、他の感情 WAV、Fun-ASR モデルは別途必要です。

当時は両コンポーネント ZIP を取得し、停止後に DLL／PDB を交換、SPP 全体を別配置して、設定・キー・人格・記憶を保つ手順でした。外部 `emotion_tts.ref_root` は修正または空にします。復元は対応するプログラムとバックアップを戻し、モデル変更だけなら記憶移行は不要です。現行版には[現在の導入](../INSTALL.md)と[更新](../UPGRADE.md)を使ってください。

ローカル CI は核心・UI・組み合わせ動作と DLL／EXE 構築を確認しました。実 OpenAI／DeepSeek と 1.16.23 の音声は各機器での確認が必要でした。個人データやキーは含みません。

## 元 manifest とハッシュ識別子

[JSON](../../../releases/AIChat_v1.16.23_SPP_v5.8.26.json) · [原文 / Original](../../zh-CN/releases/AIChat_v1.16.23_SPP_v5.8.26.md)

- `570db4e02b6fdb216923cc8585fd3c590607061211bfed8da77af652c9684a8f`
- `b9c7ed3eba98d428d740cb2f46d2aeb2cb571e3d3274679ca37f876c6716e6da`
- `ad79cf940b28545f2034c841755fb6c5a9479b250e45763d7fecf629bf0a9970`
