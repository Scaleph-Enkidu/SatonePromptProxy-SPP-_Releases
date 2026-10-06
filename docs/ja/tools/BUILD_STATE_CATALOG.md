[简体中文](../../zh-CN/tools/BUILD_STATE_CATALOG.md) | [English](../../en/tools/BUILD_STATE_CATALOG.md) | [日本語](BUILD_STATE_CATALOG.md)

# SatoneStateCatalog のソース構築

[ツール説明](STATE_CATALOG.md) · [ソース](../../../tools/SatoneStateCatalog/source)

対象は `net472` です。対応する .NET SDK を使い、参照アセンブリが不足する場合は .NET Framework 4.7.2 Developer Pack を導入します。`GameDir` は例のままではなく、自分のゲームフォルダーにします。

参照するのは `BepInEx/core/BepInEx.dll` と `Chill With You_Data/Managed/UnityEngine.CoreModule.dll` です。ゲーム型にはリフレクションを使い、`Assembly-CSharp` をビルド参照に追加しません。元の調査で型・フィールド・メソッド名を確認しましたが、それだけで実行時の動作確認にはなりません。

ゲームを閉じ、ソースフォルダーで PowerShell を開きます。

```powershell
dotnet build .\SatoneStateCatalog.csproj -c Release "-p:GameDir=C:\Games\Chill with You"
Copy-Item .\bin\Release\net472\SatoneStateCatalog.dll "C:\Games\Chill with You\BepInEx\plugins\"
```

既存プラグインのバックアップは `plugins` の外へ置きます。ゲームで少なくとも眼鏡 1 種と窓景色 1 種を試してから収集を広げます。F10 UI は英語で、説明は自分の言語で入力できます。有効な項目だけが対象です。解放・プレビューは別実装が必要で、存在すると仮定しないでください。

初期のソース説明には完全なゲーム・BepInEx の構築環境がない旨があり、後の構築済み成果物には別の[構築記録](../../../tools/SatoneStateCatalog/prebuilt/BUILD_INFO.json)があります。この時系列を区別してください。コンパイル成功はゲーム内試験の完了ではありません。導入済みゲームで動かない場合は外してください。
