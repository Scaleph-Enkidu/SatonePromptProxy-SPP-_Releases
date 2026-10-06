[简体中文](../../zh-CN/tools/BUILD_STATE_CATALOG.md) | [English](BUILD_STATE_CATALOG.md) | [日本語](../../ja/tools/BUILD_STATE_CATALOG.md)

# Build SatoneStateCatalog from source

[Tool guide](STATE_CATALOG.md) · [Source folder](../../../tools/SatoneStateCatalog/source)

The project targets `net472`. Use a .NET SDK capable of building it; install the .NET Framework 4.7.2 Developer Pack if reference assemblies are missing. Set `GameDir` to your own game directory, not the example location.

The build references `BepInEx/core/BepInEx.dll` and `Chill With You_Data/Managed/UnityEngine.CoreModule.dll`. It uses reflection for game types and does not add an `Assembly-CSharp` build reference. Original research checked type/field/method names from the supplied assembly; that alone is not runtime validation.

Open PowerShell in the source folder, with the game closed:

```powershell
dotnet build .\SatoneStateCatalog.csproj -c Release "-p:GameDir=C:\Games\Chill with You"
Copy-Item .\bin\Release\net472\SatoneStateCatalog.dll "C:\Games\Chill with You\BepInEx\plugins\"
```

Back up any existing plugin outside `plugins`. In game, test at least one glasses style and one window view before broader collection. F10's UI is English; descriptions can use your language. Only active items can be described. Unlock/preview support would require separate implementation; do not assume it exists.

The earliest source-only note said no complete game/BepInEx compiler environment was available. A later prebuilt artifact has its own [build record](../../../tools/SatoneStateCatalog/prebuilt/BUILD_INFO.json). Keep that chronology distinct: a successful compile is not a completed game test. Remove the plugin if it does not work with your installed game version.
