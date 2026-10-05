# 升级与更新指南（更新玩家必读）

[返回首页](../README.md) · [完整安装教程](INSTALL.zh-CN.md) · [下载与校验清单](DOWNLOADS.zh-CN.md)

> 这一页写给**已经在使用旧版本、现在要更新**的玩家。第一次安装请看[完整安装教程](INSTALL.zh-CN.md)。

> **版本要求：** 本页关于「水杯卡手」的修复说明与配置刷新要求，适用于 **AIChat 1.18.28 及更新版本**。如果你更新后的版本仍是 1.18.27 或更早，删除配置只会重置设置，暂不包含该修复。

## 一、更新前准备

1. 退出游戏，并确认 `SatonePromptProxy.exe` 也已经关闭（托盘图标或任务管理器）。
2. 把下面两处复制一份到安全位置（例如 `D:\Backup`）：
   - 旧 SPP 目录里的 `memory_profiles\`（聪音的记忆、关系、归档记录）；
   - 游戏目录里的 `BepInEx\config\`（按键、API、聊天历史与日志）。
3. 游戏本体、`BepInEx\core\`、`BepInEx.cfg` 不要删除。

## 二、更新步骤

1. 把新版本解压到**独立的新目录**，不要直接覆盖旧目录。
2. 进入游戏、启动新版 SPP 后，按首页「更新版本后的记忆继承问题」把旧记忆导入新 SPP。
3. **刷新 AIChat 的旧配置**（含动画修复的版本必须做，原因与方法见下一节）。
4. 进入游戏，检查设置、语音与对话是否正常。

## 三、为什么更新后要刷新 AIChat 配置

BepInEx 插件只会在配置文件里**没有**对应条目时写入新默认值。旧版本生成的 `BepInEx\config\com.username.chillaimod.cfg` 会把旧默认值原样带过来，其中包含本次修复前的默认动画姿势池：

```text
StablePoseOverrides = Relaxed=256,751,753,755,52;...
```

这个旧默认值会让聪音在 Relaxed 回复时固定端起水杯/茶杯，而动画结束后道具不会自动回收，也就是「水杯卡手」。**不刷新旧配置，这个修复不会生效。**

### 方法 A：删除配置文件（推荐，全量刷新）

删除：

```text
BepInEx\config\com.username.chillaimod.cfg
```

重启游戏后，插件会用新默认值重新生成这份配置。

注意：按键、API、窗口、阈值、SPP 启动路径等所有 AIChat 设置都会恢复默认，需要重新设置一遍——所以请先完成「更新前准备」里的备份。删除后如果 SPP 没有自动启动，请在 AIChat UI 的「SPP 与记忆（人格代理）」中重新填写 SPP 启动文件路径。

### 方法 B：只改一行（保留现有设置）

用记事本打开 `BepInEx\config\com.username.chillaimod.cfg`，找到 `StablePoseOverrides` 一行，把开头的：

```text
Relaxed=256,751,753,755,52
```

改成：

```text
Relaxed=752,50,51
```

其余部分保持原样，保存后重启游戏。

### 不要删除的文件

| 文件 | 原因 |
| --- | --- |
| `BepInEx.cfg`、`BepInEx\core\` | BepInEx 本体，不是插件配置 |
| `BepInEx\config\AIChatSatoneUX.history` | 聊天历史 |
| `BepInEx\config\SatoneInputHistory.v2.jsonl` | 输入历史 |
| `BepInEx\config\AIChat.spp-*.json` | 本地服务记录与连接状态 |
| 旧 SPP 目录的 `memory_profiles\` | 聪音的记忆与关系 |

## 四、更新后自检

- 随意聊几轮轻松的话题，确认不再出现端水杯/喝茶动作，也没有水杯留在手上；
- 按 **F9** 打开 AIChat UI，确认 SPP 路径、LLM 与语音设置正确；
- 打开 SPP 目录里的 `Open_Dashboard.bat`，确认记忆档案已经导入。

## 五、常见问题

**更新后聪音还是端水杯？**
先确认第三节已经执行：旧配置里的 `Relaxed=256,751,753,755,52` 会覆盖新默认值，必须删除配置文件或改成 `Relaxed=752,50,51`。

**删除配置后，记忆和好感度会丢吗？**
不会。记忆在 SPP 目录的 `memory_profiles\`，聊天历史在 `BepInEx\config\` 的独立文件里；本页只要求删除 AIChat 的插件配置文件本身。

**SPP 目录需要删除重装吗？**
一般不需要。保留原 SPP 目录并在其中运行新版 SPP，导入记忆后把 AIChat 里的 SPP 路径指到它即可。
