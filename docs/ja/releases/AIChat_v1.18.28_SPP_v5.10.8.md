[简体中文](../../zh-CN/releases/AIChat_v1.18.28_SPP_v5.10.8.md) | [English](../../en/releases/AIChat_v1.18.28_SPP_v5.10.8.md) | [日本語](AIChat_v1.18.28_SPP_v5.10.8.md)

# AIChat v1.18.28 SPP v5.10.8

[← 履歴一覧](../RELEASE_ARCHIVE.md)

> 過去の公開記録です。配布状況・試験範囲は当時のもので、現行の導入には現在の手順を使ってください。

2026-10-05 の N15 は手にコップが残る問題を修正します。Relaxed 動作プールと標準 StablePoseOverrides から 256/751/753/755/52 を除き、道具なしの 752,50,51 に統一しました。履歴は `origin/develop` の `66cb827`、実行 `530d06a`、試験 `c31dcc1` です。既存ユーザーは[旧設定の更新](../UPGRADE.md)が必要です。

独立審査の第 1 回で承認され、6 スイートは 900/16/262/39/95/196、net472 の 2 回構築がバイト一致しました。封存は attempt-19。実機証拠はホワイトリスト経路の Relaxed 2 回、id:50／id:752 でコップ残留なしです。標準プールは追加実機試験なし、静的確認のみです。

元の実行 ZIP とハッシュは保持します。後の docs_r1 は三言語文書だけを追加します。[文書改訂](DOCS_TRILINGUAL_20261006.md)を参照してください。導入・移行は [INSTALL](../INSTALL.md) と [UPGRADE](../UPGRADE.md) に従います。

## 元 manifest とハッシュ識別子

[JSON](../../../releases/AIChat_v1.18.28_SPP_v5.10.8.json) · [原文 / Original](../../zh-CN/releases/AIChat_v1.18.28_SPP_v5.10.8.md)

- `5c13266e6ec9d1f7e775bb305d1734099b845acc91ecb27902c5290b9bb2f45e`
- `78c418ce77e13edec1826452b1649ebe4caf1cb941fd4277a4ffc16d6c8c0f44`
- `9ed7977780dbfb3f70fd8055fa86741a1fb8777e78d1bd1342814786c50203b4`
