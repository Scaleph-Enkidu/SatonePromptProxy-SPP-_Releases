[简体中文](UPGRADE.md) | [English](../en/UPGRADE.md) | [日本語](../ja/UPGRADE.md)

# 升级、记忆继承与回退

[首页](README.md) · [安装](INSTALL.md) · [备份范围](DATA_AND_PRIVACY.md)

当前配对为 **AIChat 1.18.28 + SPP 5.10.8（N15）**。`docs_r1` 仅改文档，已安装 N15 的用户无需因此换运行程序或迁移存档。

## 1. 先完整备份

退出游戏、SPP 和语音服务，保存**整个旧 SPP 个人运行目录**，包括 `local_v1`、`memory_profiles`、配置、凭据、人格、旧格式文件；另外备份游戏 `BepInEx/config` 和现有 AIChat DLL/PDB。DLL 备份放在 `plugins` 外面。

## 2. 新目录安装并继承记忆

将新版 SPP 完整解压到新目录，替换游戏内唯一的 AIChat DLL/PDB。启动游戏与新 SPP，在 SPP／人格记忆设置中使用“继承旧版本记忆”，填写**旧 SPP 目录的绝对路径**。导入读取旧目录并备份目标；完成后确认档案与历史，保留原备份至新环境验证成功。

设置新 SPP EXE 路径，核对外部 TTS／ASR／模型路径。单纯换目录不会自动继承所有记忆，也不要用示例文件覆盖个人配置。见[迁移部署](PORTABLE_DEPLOYMENT.md)。

## 3. 必须刷新 N15 旧配置

Relaxed 移除端杯/喝茶动作 `256,751,753,755,52`，统一用 `752,50,51`。BepInEx 会保留旧 CFG，因此只换 DLL 不够。

推荐在 `BepInEx/config/com.username.chillaimod.cfg` 中，只把 `StablePoseOverrides` 的：

```text
Relaxed=256,751,753,755,52
```

改成：

```text
Relaxed=752,50,51
```

保留其他项目，保存并重启。也可备份后**只删除 `com.username.chillaimod.cfg`** 重新生成；这会重置按键、API、阈值、SPP 路径和情绪显示等选项，必须重新配置，但不会删除 SPP 记忆。

不要为刷新这项设置删除 `BepInEx.cfg`、`BepInEx/core`、`AIChatSatoneUX.history`、`SatoneInputHistory.v2.jsonl`、`AIChat.spp-*.json` 或旧记忆目录。

## 4. 核对与回滚

确认日志 `Loading [AIChat Remake 1.18.28]`、F9 的连接/路径以及 Dashboard 的继承记录。连续试几轮轻松对话，确认修复路径无端杯残留。[包内检查清单](PACKAGE_CHECKLIST.md)明确区分已有白名单实机证据和此前只做静态验证的标准池。

回滚前停机，恢复配对的旧程序**及更新前整套数据备份**。新记录不保证能被旧版完整理解。
