[简体中文](AIChat_v1.18.28_SPP_v5.10.8.md) | [English](../../en/releases/AIChat_v1.18.28_SPP_v5.10.8.md) | [日本語](../../ja/releases/AIChat_v1.18.28_SPP_v5.10.8.md)

> 历史版本记录：下载可用性、授权与测试范围按原日期理解；旧公开附件可能已下架。当前安装请从[文档首页](../README.md)进入。

# AIChat 1.18.28 / SPP 5.10.8 — N15

2026-10-05：N15。修复「水杯卡手」：Relaxed 动画池与 `StablePoseOverrides` 默认白名单移除端杯/喝茶动作（256/751/753/755/52），统一为无道具动作 `752,50,51`（开发库 `origin/develop` @ `66cb827`；运行代码提交 `530d06a`；受测记录 `c31dcc1`）。更新玩家需要刷新旧配置，见[《升级与更新指南》](../UPGRADE.md)。

主程序包：[SatoneMod_AIChat_1.18.28_SPP_5.10.8_Windows_x64.zip](../../../packages/AIChat_v1.18.28_SPP_v5.10.8/SatoneMod_AIChat_1.18.28_SPP_5.10.8_Windows_x64.zip)（SHA-256 `5c13266e6ec9d1f7e775bb305d1734099b845acc91ecb27902c5290b9bb2f45e`）。独立审查（第一轮）通过；六套件 900/16/262/39/95/196；net472 两次重建逐字节一致（DLL `78c418ce77e13edec1826452b1649ebe4caf1cb941fd4277a4ffc16d6c8c0f44`、PDB `9ed7977780dbfb3f70fd8055fa86741a1fb8777e78d1bd1342814786c50203b4`）；封存 attempt-19；实机（白名单路径）2 轮 Relaxed 播放 id:50 / id:752，无端杯残留；标准池路径未实机补测，由静态审查覆盖。

安装与迁移教程见[完整安装教程](../INSTALL.md)与 README「更新版本后的记忆继承问题」。
