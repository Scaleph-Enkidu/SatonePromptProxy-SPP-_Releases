# SatoneStateCatalog：聪音当前外观采集器（F10）

这是给**愿意一起统计道具／服饰外观**的志愿者准备的小插件。它不依赖 AIChat 或 SPP，也不修改游戏存档：按 **F10** 打开窗口，读取当前生效的窗景、服装、眼镜与其他摆件的内部编号，让你把"编号"和"你实际看到的样子"一条条对上。

## 为什么需要它

模组里的聪音现在还不知道自己房间窗外是什么景色、身上穿着哪件衣服。要让聪音"真的看见"，就得先把每个内部编号对应的外观写成文字——数据齐了以后，才能继续做用语音让聪音换背景、换衣服这类功能。手工统计工作量很大，所以做成这个采集器，谁都能帮忙记一点。

## 安装（推荐：预编译 DLL）

1. 确认游戏已装 BepInEx 5（游戏目录里有 `BepInEx/core/BepInEx.dll`）。
2. 把 `prebuilt/SatoneStateCatalog.dll` 复制到 `游戏目录/BepInEx/plugins/`。
3. 启动游戏、进入房间，按 **F10** 打开窗口；窗口文本是英文标签，输入框可以填中文描述。
4. 点击一项，填写你实际看到的外观，再点 **Save this item and update the document**。

保存后会写入（并在同一目录保留上一版 `.bak`）：

- `BepInEx/config/SatoneStateCatalog/catalog.json`（给以后做精确查表用）
- `BepInEx/config/SatoneStateCatalog/appearance_catalog.md`（给人核对用）

同一类别与款式 ID 再次保存会修改该条，不会重复新增。若同时启用多个窗景效果，列表会逐项显示；描述光照等组合效果时，请在文字里写明当时的场景。

> 例如看到 `decoration/Glasses | Glasses_2 / Glasses_2B`，可以输入"黑色细框圆眼镜"——这只是输入示例，**不是**对该编号真实外观的判断。

## 关于预编译 DLL 与源码

- `prebuilt/SatoneStateCatalog.dll` 由 `source/` 里的源码在本机当前游戏版本（BepInEx 5 + 当前 Unity 模块）编译，**尚未在游戏内验证**。首次使用请先确认窗口能打开、保存后上述两个文件真的出现。
- 它只读取当前生效的对象，**不会**解锁内容、改成就或写存档；如果游戏更新后插件失效或日志报错，从 `plugins` 目录删掉这个 DLL 即可，游戏不受影响。
- 想自己编译或修 bug：源码在 `source/`。需要 Windows 上的 .NET SDK（net472 目标）和本机游戏目录：

```powershell
dotnet build .\SatoneStateCatalog.csproj -c Release "-p:GameDir=C:\Games\Chill with You"
Copy-Item .\bin\Release\net472\SatoneStateCatalog.dll "C:\Games\Chill with You\BepInEx\plugins\"
```

`source/待观察编号.md` 是从游戏程序集提取的编号清单，用来勾选观察进度；编号本身不代表已经解锁，也不提供颜色推断。

## 关于未解锁项目

这个插件只读**当前确实处于活动状态**的对象。未解锁、也没有实际显示的眼镜／窗景无法自动对应真实外观。要补齐可以在做好备份后用单独的测试存档逐一切换并描述；"100% 完成度"不保证覆盖限时或特殊活动内容。**不要**用来历不明的完成度存档覆盖你的唯一存档。本插件没有自动解锁、改成就或写存档的代码。

## 数据格式

`catalog.json` 顶层为 `schemaVersion`、`updatedUtc`、`entries`；每条含 `category`、`code`、`modelCode`、`description`、`observedUtc`、`updatedUtc`。JSON 供之后给 AIChat 做精确查表，Markdown 供人工核对。

如果你愿意把整理好的 `appearance_catalog.md`（或 `catalog.json`）发到[发布库 Issues](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/issues)，我会非常感激——哪怕只统计一部分。
