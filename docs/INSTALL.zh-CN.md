# 从 Steam 游戏开始安装

[返回首页](../README.md) · [下载清单](DOWNLOADS.zh-CN.md)

适用：AIChat 1.16.14 + SPP 5.8.23。教程草稿 v3，2026-09-26。

**安装前必读：** 先查看[首页的 API 付费要求与安装难度声明](../README.md)及[费用估算](API_COST.zh-CN.md)，确认自己有可用的 OpenAI API 计费账户，并愿意承担复杂安装与使用成本。推荐模型为 `gpt-6-luna`，ChatGPT 订阅不能替代本 Mod 的 API 用量。

**先核对硬件路线：** 完整本地语音暂建议 8 GB 显存起步、12 GB 或以上更有余量；这是建议值，未做最低配置验收。非 NVIDIA 玩家可先使用文字聊天，语音需要 CPU 或其他经过适配的后端，不能照搬 CUDA 安装步骤。当前 Fun-ASR 随包脚本没有强制使用 CPU。请先看[运行开销与显卡兼容说明](HARDWARE.zh-CN.md)，再按自己的设备选择安装路线。

**确认后再下载两个文件：** [AIChat_v1.16.14.zip](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.16.14_SPP-v5.8.23/AIChat_v1.16.14.zip) 和 [SatonePromptProxy_v5.8.23.zip](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.16.14_SPP-v5.8.23/SatonePromptProxy_v5.8.23.zip)。也可以打开[配对发布页](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/tag/AIChat-v1.16.14_SPP-v5.8.23)，在 Assets 中下载这两个 ZIP；不要选 Source code。校验文件与其他依赖见[下载清单](DOWNLOADS.zh-CN.md)。

**当前访问限制：** 安装包已集中到本发布库，但本库仍为 Private，未获得权限的玩家会看到 404；公开本库后即可直接按本文下载，不需访问两个源码仓库。

## 0. 先了解要安装什么

| 名称 | 作用 | 是否需要 |
|---|---|---|
| BepInEx | 让游戏加载插件 | 必须 |
| AIChat.dll | 游戏内聊天、字幕、动画 | 必须 |
| SPP | 管理人格、记忆、好感与服务连接 | 本教程需要 |
| OpenAI API | 在线生成回答 | 本教程需要自己的 API 账户与额度 |
| GPT-SoVITS、模型、参考 WAV | 把回答变成声音 | 完整朗读体验需要 |
| Fun-ASR、Python 环境、模型 | 把麦克风声音变成文字 | 语音输入需要，键盘聊天可跳过 |
| Embedding 模型 | 根据含义查找旧对话 | 可选，最后配置 |

按顺序操作，每一步先检查成功标志。本文示例根目录为 `D:\LofiMOD`；没有 D 盘就统一改为自己可写的实际目录，例如 `C:\LofiMOD`。外部模型远大于两个 Mod，需要为下载、解压和缓存预留空间。

## 1. 找到游戏根目录

1. 在 Steam 中安装并正常运行一次游戏，再退出。
2. 在 Steam 库右击游戏，选择“管理 → 浏览本地文件”。
3. 找到 `Chill With You.exe` 所在的一层。这就是游戏根目录，不是 `Chill With You_Data` 内部。
4. 若已有其他 Mod，先备份其插件和配置；不需要别人的游戏存档或 100% 存档。

在资源管理器开启“查看 → 显示 → 文件扩展名”，避免误存为 `.bat.txt` 或 `.json.txt`。

## 2. 安装 BepInEx

1. 下载 `BepInEx_win_x64_5.4.23.5.zip`，见[清单](DOWNLOADS.zh-CN.md)。
2. 解压，将包内内容复制到游戏根目录。游戏 EXE 同层应出现 `BepInEx`、`winhttp.dll` 和 `doorstop_config.ini`，不能多套一层压缩包名称的文件夹。
3. 从 Steam 启动游戏一次，再正常退出。
4. 检查 `BepInEx\LogOutput.log`、`BepInEx\config`、`BepInEx\plugins`。

**成功标志：** 出现日志和配置目录。未出现就先修正包的架构和解压层级，再往下做。已有 BepInEx 时需核对与其他 Mod 的兼容性，不能直接清空它。

## 3. 安装 AIChat

1. 下载并解压 [AIChat_v1.16.14.zip](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.16.14_SPP-v5.8.23/AIChat_v1.16.14.zip)。
2. 将 `AIChat.dll` 放到 `游戏根目录\BepInEx\plugins\AIChat.dll`。
3. 检查 plugins 及其子目录，只留一份 AIChat。旧 DLL 即使改名仍可能加载，要移出 plugins。
4. 如果有旧 `AIChatSatoneUXPatch.dll`，也移出 plugins，其功能已整合。
5. 从 Steam 启动游戏，进入场景后按 **F9**。

**成功标志：** 窗口显示 1.16.14。现在出现“等待 TTS 服务”并不奇怪，语音还没配置。F10 留给独立外观采集工具，普通玩家无需安装该工具。

## 4. 安装 SPP

1. 下载 [SatonePromptProxy_v5.8.23.zip](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.16.14_SPP-v5.8.23/SatonePromptProxy_v5.8.23.zip)，新建 `D:\LofiMOD\SatonePromptProxy`，将 ZIP **全部**解压进去。
2. 确认 EXE 同层有 `config.example.json`、`SatonePersona_v4.5.txt`、`satone_funasr_server_v1.py`、`SatoneASRHotwords_v1.json`、`embedding_worker.py`、`profiles_26.csv`。
3. 双击 `SatonePromptProxy.exe`，保持窗口开启。首次运行自动生成 `config.json`。
4. 打开 [SPP 主页](http://127.0.0.1:11435/) 和 [Dashboard](http://127.0.0.1:11435/dashboard)。

`127.0.0.1` 是这台电脑自身；这些链接只在 SPP 运行时有效，在手机打开会指向手机自己。

**成功标志：** 主页显示 5.8.23，Dashboard 可以打开。未安装语音和检索环境时出现相关警告，不代表主服务没启动。

当前正式 ZIP **未包含**源码里的 `Start_AIChat_Services.bat`、`Open_Dashboard.bat` 等便捷脚本；按本文直接运行 EXE、打开链接即可。

## 5. 准备在线 AI 账户

1. 登录 [OpenAI Platform](https://platform.openai.com/)，创建或选择用于 Mod 的项目。
2. 在 [API Key 页面](https://platform.openai.com/api-keys)创建自己的密钥。
3. 在 [API 计费页](https://platform.openai.com/settings/organization/billing/overview)确认付款与额度，设置合适的用量提醒。预算提醒不一定是立即停止请求的硬限制。
4. 将 Key 保存在自己的安全位置，下一步填入 AIChat；不要贴到 GitHub、群聊或截图中。

API Key 是程序调用凭据，不是登录密码。游戏购买和 ChatGPT 网页订阅不能代替这里的 API 配置。本文示例为 `gpt-6-luna`，以自己的账户权限和[模型页](https://developers.openai.com/api/docs/models/gpt-6-luna)为准。

## 6. 连接游戏与 SPP

F9 → 展开设置，填写：

| 位置 | 项目 | 内容 |
|---|---|---|
| 连接与模型 | API URL | `http://127.0.0.1:11435/v1/chat/completions` |
| 连接与模型 | API Key | 自己的 OpenAI API Key |
| 连接与模型 | 模型名称 | `gpt-6-luna` 或已确认可用的模型 ID |
| 语音与 TTS | TTS 服务 URL | `http://127.0.0.1:11435`，**不加 /tts** |
| 语音与 TTS | 合成语音语言 | `ja` |
| 语音与 TTS | 自动运行 TTS | 首次排查先关闭，完成语音配置后再启用 |
| SPP 配置 | SPP 路径 | `D:\LofiMOD\SatonePromptProxy\SatonePromptProxy.exe` |
| SPP 配置 | 自动运行 SPP | 手动验证时先关闭；验证成功后可启用 |
| SPP 配置 | 退出时自动关闭 SPP | 按习惯选择，首次测试可关闭 |
| 记忆档案 | 当前档案 | 先选“记忆1” |

点 **“保存 AIChat 本地配置”**。SPP config.json 中的 `openai_responses_url` 和 `openai_conversations_url` 默认指向 OpenAI 官方接口，使用官方账户时保留。

新安装的 AIChat 原始默认值仍指向 OpenRouter 和旧模型名称，必须按上表修改。11435 是 SPP，9880 是 GPT-SoVITS，不能全部互换。AIChat 会给 TTS URL 自动加 `/tts`。麦克风会按 SPP 连接规则使用其 ASR 入口，不需要把聊天地址改成 `/asr`。

**检查文字连接：** 等聪音在座位上且长剧情/教程结束，输入“你好”。SPP Dashboard/日志应显示请求与回复。没有安装 TTS 时，AIChat 仍会尝试生成语音，可能等待和重试；这个阶段仅用来检查连接，不能将其当作优化好的纯文字模式。

## 7. 配置朗读

按[语音设置 A 部分](VOICE_SETUP.zh-CN.md)安装 GPT-SoVITS，使用推荐的后藤一里 v2ProPlus 权重与 Mayuri 参考 WAV/台词，先生成并播放一段测试 WAV。完整 26 种情绪的原文件、复制命名和配置方法在该页 A6。

**成功标志：** 直接调用 GPT-SoVITS 能发声，经 SPP `/tts` 也能生成 WAV，最后游戏里能听到日文回答并看到中文字幕。“服务已就绪”本身不足以证明权重、参考录音与合成都正常。

之后可在“语音与 TTS”填写自己的 `run_api.bat` 路径，开启自动启动。不要让多个启动器同时启动同一服务。

## 8. 配置麦克风

键盘聊天正常后，按[语音设置 B 部分](VOICE_SETUP.zh-CN.md)安装 Fun-ASR。

1. 在 Windows 麦克风隐私设置允许桌面应用访问，在声音设置选对输入设备。
2. 等 Fun-ASR 就绪，先按住 **F8** 说话，再松开。
3. 核对识别文字，成功后再开“持续通话”。测试时使用耳机，避免把聪音播放的声音再次录入。

**成功标志：** F8 能识别并得到回复；持续通话能在停顿后提交，静音时不会不断误触发。ASR 加载、重启或剧情锁定时，按钮变黄/不可用是当前保护行为。

当前默认起声门槛 0.0005，结束门槛为其 0.4 倍。这是适配低电平输入的值，不是所有麦克风的通用标准。先看日志中的电平，区分“没触发录音”和“录到了但识别失败”，再调整。

## 9. 日常使用与记忆

- F9 开关窗口；默认 Enter 发送，Shift+Enter 换行。聪音的回复在朗读/字幕结束后写入界面历史。
- 记忆1/2/3分别保存对话与 AI 关系，人格文件独立。默认记忆3带测试用高好感预设，初次正常游玩先选记忆1。
- 通过 Steam 启动，让游戏运行时提供有效身份；缺失身份仅停用原版经历同步及叠加，AI 聊天和各档案 AI 好感仍可工作。
- 手动启动顺序可用：GPT-SoVITS → SPP（管理 Fun-ASR）→ Steam 游戏。自动启动设置成功后可交给 AIChat。
- SPP 5.8.23 在有效主聊天结束后，当 API 总输入 token 达到 32,000 时安排记忆整理，粗估保留最近约 12,000 token 对话。32,000 不是整理后的硬上限，也不是每句固定消耗。关系更新、修复和整理可能另发请求，实际费用查看 API 平台。
- 可选旧聊天语义检索：配置 SPP 的 `embedding_python`，用 Dashboard 安装/加载模型并检查 `/recall/status`。没有配好这一项时，不承诺任意旧话题都能找回。

## 常见问题

| 现象 | 先检查 |
|---|---|
| 下载 404 | 本发布库是否仍为 Private；是否使用有本库权限的账户；安装包不需要源码仓库权限 |
| F9 无反应 | BepInEx 日志、DLL 层级、重复旧 DLL |
| SPP 一闪就关 | 在其文件夹地址栏输入 cmd，再执行 SatonePromptProxy.exe；看 JSON、端口和日志错误 |
| 11435 页面打不开 | 是否运行 SPP，是否开了重复实例，是否在同一台电脑访问 |
| API 401 / 404 / 429 | 分别优先查 Key / 模型和地址 / 额度及频率，再看具体错误文本 |
| 有文字没声音 | 查 9880、SPP TTS URL、模型权重、Neutral WAV 与超时 |
| TTS 就绪却失败 | 探测可能把 400/422 也算服务有响应，必须实际生成 WAV |
| ASR 未就绪 | 查 Python、依赖、模型目录、首次加载和 9881；模型不是只有 model.pt |
| 持续通话无响应 | 先测 F8、Windows 输入设备和电平，再看 VAD 日志 |
| 发送不可用 | 等聪音回到座位、结束长剧情或教程 |
| 更新后仍有旧 Key/历史 | 独立配置与历史仍在，见隐私页 |

反馈时附两个版本、操作步骤、时间和脱敏日志片段。不要直接上传 CFG、整个记忆目录或游戏目录。

## 更新、回退、卸载

退出游戏与服务，按[数据页](DATA_AND_PRIVACY.zh-CN.md)备份。AIChat 只替换唯一 DLL；SPP 更新程序文件并保留自己的 config.json、人格、记忆、关系、模型和参考录音，不能拿 config.example.json 覆盖个人配置。

SPP 5.8.23 会将旧默认 24,000 阈值备份到 `config.json.before_v5.8.23`，再一次性改成 32,000；该备份也属于个人数据。阈值回退可继续使用 AIChat 1.16.14，恢复 SPP 5.8.22 和原阈值；其他回退按对应配对说明进行。

只禁用本 Mod：移出 AIChat.dll，停止 SPP、GPT-SoVITS 和 Fun-ASR，保留数据便于恢复。不要删除其他 Mod 共用的整个 BepInEx。彻底清理数据的范围见[隐私页](DATA_AND_PRIVACY.zh-CN.md)。
