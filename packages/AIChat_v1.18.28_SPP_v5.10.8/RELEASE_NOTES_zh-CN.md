# N15 / AIChat 1.18.28 + SPP 5.10.8（开发库已验证基线）

- 包文件：`SatoneMod_AIChat_1.18.28_SPP_5.10.8_Windows_x64.zip`；SHA-256 `5c13266e6ec9d1f7e775bb305d1734099b845acc91ecb27902c5290b9bb2f45e`。
- 开发库基线：`origin/develop` 提交 `e0241db3924a81b866759b774eb65b7757837db2`（含 N15 运行代码提交 `9f2aef88f993c18fef3258495128f7cc4f8cb309`、受测记录 `45b4ef6fafb558148466a2b31dd0a60a12414563`）。
- 独立审查（第一轮）通过并处理 P1/P2；六套件 900/16/262/39/95/196；net472 两次重建逐字节一致（DLL `78c418ce…`、PDB `9ed79777…`）；封存 attempt-19。
- 实机验证（白名单路径）：2 轮 Relaxed 回复播放 id:50 / id:752，全日志无端杯动作 256/751/753/755/52、无水杯残留；标准池路径未实机补测，由静态审查覆盖。
- 本次修复「水杯卡手」：Relaxed 动画池与 `StablePoseOverrides` 默认白名单移除端杯/喝茶动作，统一为无道具动作 `752,50,51`。
- 更新玩家注意：旧 `BepInEx\config\com.username.chillaimod.cfg` 不会自动刷新；请删除该文件或把 `StablePoseOverrides` 的 Relaxed 白名单改为 `752,50,51`，否则修复不生效（详见《升级与更新指南》）。
- 安装：退出游戏与 SPP，按独立新目录解压或按包内说明覆盖程序文件；迁移旧记忆见仓库 README「更新版本后的记忆继承问题」。
