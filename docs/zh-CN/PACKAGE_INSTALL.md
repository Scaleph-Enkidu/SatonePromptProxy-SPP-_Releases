[简体中文](PACKAGE_INSTALL.md) | [English](../en/PACKAGE_INSTALL.md) | [日本語](../ja/PACKAGE_INSTALL.md)

# N15 文档修订包：安装与回滚

版本 **AIChat 1.18.28 + SPP 5.10.8**，文档修订 **docs_r1，2026-10-06**。这是已发布 N15 程序的三语文档修订，不是新的未发布运行候选。原包保留，本包所有非文档运行文件与原包一致。

包根目录 `README.md` 提供三语入口；`AIChat/README.md`、`SatonePromptProxy/README.md` 提供组件入口。三语全文位于 `docs/zh-CN`、`docs/en`、`docs/ja`，可离线阅读。外部下载、网页状态和源代码链接仍需对应服务或网络。

1. 退出游戏及 SPP，备份旧程序、整个 SPP 数据目录和游戏 `BepInEx/config`。
2. AIChat DLL/PDB 放入 `BepInEx/plugins`。没有 SPP 时安装完整 SPP 目录；从 N9～N14 升级且已有同一 SPP 5.10.8 时，EXE 本身没有变化。
3. 需要移至新 SPP 目录时，按[升级页](UPGRADE.md)用旧目录的绝对路径导入，不先删除旧数据。
4. 刷新 `StablePoseOverrides` 的 Relaxed 项为 `752,50,51`，或备份后仅重建插件 CFG。重建 CFG 会重置路径/API/阈值/按键和情绪显示等选项。
5. 确认日志版本 1.18.28，并执行[检查清单](PACKAGE_CHECKLIST.md)。新装的详细依赖与语音步骤见[完整安装](INSTALL.md)。

回滚时停机并恢复对应旧 DLL/PDB、SPP 程序及升级前的完整配置/数据备份。只阅读或替换本次文档不需要迁移存档。`BUILD_INFO.json` 保留原 N15 的封存记录；`DOCUMENTATION_REVISION.json` 记录本次文档成员变化、原包哈希及未变文件证明。
