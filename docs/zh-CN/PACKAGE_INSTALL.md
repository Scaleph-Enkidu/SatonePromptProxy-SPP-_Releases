[简体中文](PACKAGE_INSTALL.md) | [English](../en/PACKAGE_INSTALL.md) | [日本語](../ja/PACKAGE_INSTALL.md)

# 安装与回滚

**AIChat 1.18.30 + SPP 5.10.10 · 2026-10-08**

本次合并两批共 9 项修复，更新记忆导入、语音回声过滤、退出清理与日期召回。需要更新 AIChat 和 SPP 两端程序；三语说明与包内入口同步更新。

退出游戏与 SPP，完整备份旧 SPP 目录和游戏插件配置后，再替换 AIChat DLL/PDB 及 SPP。若使用新 SPP 目录，按[升级指南](UPGRADE.md)继承记忆。已刷新过的 Relaxed 白名单无需再次重置。不要使用 GitHub 自动生成的 Source code ZIP 代替安装包。TTS、ASR 与语义模型仍为可选外部组件。

包根目录及两个组件目录的 README 均提供中英日入口，全文位于各自的 `docs/zh-CN`、`docs/en`、`docs/ja`。新安装保留 SPP 的完整目录结构。将 AIChat DLL/PDB 放入游戏 `BepInEx/plugins`，仅保留一个 AIChat DLL，备份放在插件目录外。回退前停机，恢复旧程序及升级前的整套数据备份。`BUILD_INFO.json` 记录本版源码、二进制与每个文件的散列。

[Install](INSTALL.md) · [Upgrade](UPGRADE.md) · [Checks](PACKAGE_CHECKLIST.md)
