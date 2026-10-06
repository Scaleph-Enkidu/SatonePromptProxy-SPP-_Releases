[简体中文](../../zh-CN/tools/STATE_CATALOG.md) | [English](../../en/tools/STATE_CATALOG.md) | [日本語](STATE_CATALOG.md)

# SatoneStateCatalog：F10 外観カタログ

[ホーム](../README.md) · [構築手順](BUILD_STATE_CATALOG.md) · [観察待ち ID](OBSERVED_IDS.md)

AIChat・SPP に依存しない BepInEx プラグインです。F10 で現在の窓景色、服、眼鏡、飾りの ID を読み、実際の見た目を記述できます。今後の外観認識・会話操作用の資料であり、その機能自体を実装するツールではありません。

## 導入と記録

BepInEx 5 を導入し、[構築済み SatoneStateCatalog.dll](../../../tools/SatoneStateCatalog/prebuilt/SatoneStateCatalog.dll) をゲームの `BepInEx/plugins` にコピーします。起動して F10 を押します。ツール UI は英語ですが、説明には中国語・英語・日本語を使えます。現在の項目を選び、外観を入力して **Save this item and update the document** を押します。

`BepInEx/config/SatoneStateCatalog/catalog.json` と `appearance_catalog.md` に書き込み、直前の `.bak` を保持します。同じカテゴリ・スタイル ID は重複追加せず更新します。窓効果が複数有効なら、すべてを挙げて組み合わせの見た目を説明してください。

`Glasses_2 / Glasses_2B` に「黒い細い丸フレーム」と書く例は、確認済みの対応表ではありません。内部名だけで色や外観を判断せず、実際に観察します。

## 範囲とセーブ

DLL はローカルの BepInEx／Unity 参照で構築され、[BUILD_INFO](../../../tools/SatoneStateCatalog/prebuilt/BUILD_INFO.json) に出典があります。ゲーム内の完全な試験は未実施です。有効状態を読むだけで、解放、実績変更、ゲームセーブ書き込みはしません。互換性の問題があれば DLL を外してください。

ロック中で表示できない項目は、この読み取りツールでは外観を確認できません。必要なら自分のバックアップや別テストセーブを使い、唯一のセーブを不明な「100% セーブ」で置き換えないでください。自動解放・プレビューモードはありません。

## 出力と共有

`catalog.json` は `schemaVersion`、`updatedUtc`、`entries` を持ち、各項目は `category`、`code`、`modelCode`、`description`、`observedUtc`、`updatedUtc` を含みます。内容を確認して JSON／Markdown を Issue で共有できます。この説明が自動送信することはありません。
