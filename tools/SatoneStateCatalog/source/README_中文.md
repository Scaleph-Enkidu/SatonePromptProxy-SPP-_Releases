# 聪音当前外观采集器（独立 BepInEx 插件源码）

这个小插件帮助你边看游戏画面，边把内部 ID 对应到你自己描述的外观。它不依赖 AIChat 或 SPP，也不修改游戏存档。

## 功能

- 按 **F10** 打开窗口，读取当前生效的窗景 ID、聪音当前服装的型号与款式 ID、当前启用的眼镜及其他摆件的类别、型号和款式 ID。
- 点击一项，填写你实际看到的外观；点击 **Save this item and update the document**。
- 每次保存更新 `BepInEx/config/SatoneStateCatalog/catalog.json` 和 `appearance_catalog.md`。同一个类别与款式 ID 再次保存会修改该条，不会重复新增；已有文件的上一版本保留为 `.bak`。
- `待观察编号.md` 是从你提供的游戏程序集提取的编号清单，可以勾选观察进度。编号并不证明项目已经解锁，也不提供颜色推断。

例如看到 `decoration/Glasses | Glasses_2 / Glasses_2B`，可以输入“黑色细框圆眼镜”（这只是输入示例，**不是**对该编号真实外观的判断）。文档会把你的描述记在这个内部 ID 下。若同时启用多个窗景效果，列表会逐项显示；描述光照等组合效果时，请在文字里写明你当时的场景。

## 编译与安装

需要 Windows 上的 .NET SDK（能够编译 `net472`）以及**本机游戏目录**中已安装的 BepInEx 5。游戏目录应包含 `BepInEx/core/BepInEx.dll` 和 `Chill With You_Data/Managed/UnityEngine.CoreModule.dll`。本项目使用反射读取游戏对象，编译时不需要引用 `Assembly-CSharp.dll`。

在本项目文件夹里使用 PowerShell：

```powershell
dotnet build .\SatoneStateCatalog.csproj -c Release "-p:GameDir=C:\Games\Chill with You"
Copy-Item .\bin\Release\net472\SatoneStateCatalog.dll "C:\Games\Chill with You\BepInEx\plugins\"
```

把示例路径换成你的实际游戏目录。若 SDK 提示缺少 .NET Framework 4.7.2 的 reference assemblies，请在自己的开发环境安装 .NET Framework 4.7.2 Developer Pack。启动游戏，进入房间，按 F10 即可开始记录。窗口文本使用英文标签，输入框可填写中文描述。

## 关于未解锁项目

这个版本只读**当前确实处于活动状态**的对象。未解锁也没有实际显示的眼镜/窗景无法通过它自动对应真实外观。要补齐这些项目，可以在做好备份后使用单独的测试存档，逐一切换并描述；“100% 完成度”不保证覆盖限时或特殊活动内容。不要直接把来历不明的完成度存档覆盖唯一的游戏存档。

如果将来需要临时预览未解锁的物件，需要先确认游戏版本、解锁条件及切换接口，再单独开发只用于测试档的预览模式；本插件没有自动解锁、改成就或写存档的代码。

## 数据格式

JSON 顶层为 `schemaVersion`、`updatedUtc`、`entries`。每条含 `category`、`code`、`modelCode`、`description`、`observedUtc`、`updatedUtc`。推荐将 JSON 用于之后给 AIChat 做精确查表，Markdown 用于人工核对。

## 当前验证范围

根据所提供的 `Assembly-CSharp` DLL 核对了读取的类型、字段和方法名称。这里没有本机完整游戏目录、BepInEx 程序集或 .NET 编译器，因此**还没有编译 DLL，也没有进行游戏内运行测试**。游戏更新改变字段时需要重新核对。首次运行先用一项眼镜和一项窗景确认窗口与两份输出文件内容，再批量采集。
