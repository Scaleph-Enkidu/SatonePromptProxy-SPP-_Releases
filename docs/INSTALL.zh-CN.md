# 安装 AIChat 1.16.23 + SPP 5.8.26

[返回首页](../README.md) · [下载清单](DOWNLOADS.zh-CN.md) · [语音设置](VOICE_SETUP.zh-CN.md)

适用 Steam Windows 版《放松时光：与你共享 Lo-Fi 故事》。本文更新于 **2026-09-28**。请从[本次配对发布页](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/tag/AIChat-v1.16.23_SPP-v5.8.26)的 Assets 下载 **AIChat 1.16.23** 与 **SPP 5.8.26** 两个 ZIP；GitHub 的 Source code ZIP 不是安装包。外部依赖和来源见[下载清单](DOWNLOADS.zh-CN.md)。在线聊天还需要自己准备 OpenAI 或 DeepSeek 的 API Key 与可用额度。

## 先选使用方式

| 使用方式 | 还需安装什么 |
|---|---|
| 只打字聊天 | 游戏、BepInEx、AIChat、SPP，以及一个可用的云端 API Key |
| 听聪音说话 | 再安装 GPT-SoVITS 程序和兼容的声线模型权重；SPP 包已有默认 Neutral 参考音频 |
| 用麦克风交谈 | 再安装 Fun-ASR 的 Python 环境和模型 |
| 按意思查找很久以前的聊天 | 可选装本地 Embedding 检索模型 |

完整本地语音会额外占用显存。硬件建议和 CPU 路线的限制见[运行开销说明](HARDWARE.zh-CN.md)。先让文字聊天工作，再逐项加上朗读和麦克风，定位问题会更容易。

## 1. 安装游戏插件

1. 在 Steam 中运行游戏一次，再退出。右击游戏 →“管理”→“浏览本地文件”，找到游戏 EXE 所在目录。
2. 按[下载清单](DOWNLOADS.zh-CN.md)安装 BepInEx Windows x64 5.4.23.5。解压后，游戏 EXE 同层应有 `BepInEx` 和 `winhttp.dll`。启动游戏一次，确认生成 `BepInEx/LogOutput.log` 与 `BepInEx/plugins`。
3. 从 AIChat ZIP 取出 `AIChat.dll` 和配套 `AIChat.pdb`，放进 `游戏目录/BepInEx/plugins`。只保留一份可加载的 AIChat DLL；旧 `AIChatSatoneUXPatch.dll` 也移出插件目录。
4. 启动游戏，进入场景按 **F9**，核对窗口版本 **1.16.23**。

## 2. 安装本地 SPP

1. 把 SPP ZIP **完整解压**到固定目录，例如 `D:\LofiMOD\SatonePromptProxy`。确保 EXE 同层有 `config.example.json`、`SatonePersona_v4.5.txt`、语音／ASR 辅助脚本和 `mayuri-voice/refs/MAY_1158_Neutral.wav`；不要只复制 EXE。
2. 运行 `SatonePromptProxy.exe`。新目录首次启动会从示例创建 `config.json`，不需要迁移玩家记忆才能启动。
3. 打开本机 [SPP 首页](http://127.0.0.1:11435/)；核对版本 **5.8.26**。语音或检索尚未安装时的相关提示不等于 SPP 主服务失败。
4. 在 AIChat 设置中核对 **SPP 程序路径**指向这个 EXE。安装目录以后不变时，切换模型无须再改此路径或本地聊天地址。

已有安装升级时，请先退出游戏与 SPP，备份原程序和个人数据，再替换 DLL／PDB 与 SPP 程序文件。**保留自己的 `config.json`、API Key、AIChat CFG、记忆档案、人格修改和模型路径**；不要用 `config.example.json` 覆盖。首次使用新版记忆时可选择导入旧记录或跳过；跳过不会删除旧记录。

## 3. 配置聊天模型

游戏内打开 **LLM（聊天模型与连接）**，展开想使用的公司：

1. 选择 **OpenAI** 或 **DeepSeek**，将该公司的 API Key 复制到对应输入框。Key 默认隐藏，需要时点“显示 API Key”。
2. 新配置的 OpenAI 模型名称预填 `gpt-6-luna`，DeepSeek 预填 `deepseek-flash`，可自行修改。界面示例标注 **截至 2026-09-28**；模型名称会变，请核对 [OpenAI 官方模型页](https://developers.openai.com/api/docs/models/gpt-6-luna)或 [DeepSeek 官方接口页](https://api-docs.deepseek.com/api/create-chat-completion/)。已有自定义名称会保留。
3. 若使用第三方中转站，改选 **中转站（第三方 API）**，填它提供的 API 地址、Key 和模型名称；不要把官方服务的 Key 当作中转站 Key 使用。
4. 点击界面常驻的 **“保存并应用配置”**。编辑和勾选只改草稿，保存前当前聊天仍使用原服务；正在进行的回复完成后才切换。界面显示“正在使用”后再发新消息。

同一时间只使用一家服务，但同一记忆档案可在 OpenAI 和 DeepSeek 之间延续话题。更换公司、Key 或模型不要求退出游戏、手工迁移存档。ChatGPT 网页订阅不包含 OpenAI API 用量，DeepSeek 也需要其自己的账户与额度。若提示“对话暂时无法完成”，先核对当前选择的 API 链接、Key 与模型名称，仍失败再看日志。

## 4. 让聪音发声，再启用麦克风

SPP 包已附带默认 Neutral 参考音频。已有 GPT-SoVITS 程序及运行环境时，可从[“孤独摇滚”模型项目](https://huggingface.co/lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models)另下载匹配版本的 GPT 与 SoVITS 权重，并按[语音教程 A 部分](VOICE_SETUP.zh-CN.md)加载。其他情绪录音未随包提供，缺失时使用 Neutral 回退；如果旧配置的 `emotion_tts.ref_root` 仍指向包外目录，请清空或改向包内 `mayuri-voice/refs`。直接生成并播放一段测试 WAV，确认权重与录音实际工作。

需要麦克风时，再按[语音教程 B 部分](VOICE_SETUP.zh-CN.md)安装 Fun-ASR。先按住 **F8** 测试识别，再自行开启持续通话；持续通话默认关闭。未使用麦克风可跳过这部分。GPT-SoVITS、Fun-ASR 和声线权重不在两份 Mod ZIP 内。

## 5. 检查、回退和求助

- F9 打开窗口；键盘 Enter 发送、Shift+Enter 换行。发送、按住说话和持续通话在模型思考时显示红色“思考中”，开始朗读／字幕后显示黄色“回复中”。
- 如果游戏中 F9 无反应，查 `游戏目录/BepInEx/LogOutput.log`、插件层级和重复 DLL。SPP 启动失败时查 SPP 目录里的运行日志和 `config.json` 的 JSON 格式。
- API 401 通常先查 Key，404 先查模型名或 URL，429 先查额度与频率；以实际日志中的服务商错误为准。分享日志前移除密钥、私人对话与机器路径。
- 有文字却没声音时，检查 GPT-SoVITS 9880、模型权重、SPP 的 `emotion_tts.ref_root` 和 Neutral WAV。服务显示“就绪”仍需实际生成音频验证。
- 回退时先退出程序，再成对恢复原 DLL／EXE 和原配置备份。不要删除记忆来切换模型。数据位置和卸载范围见[本地数据与隐私](DATA_AND_PRIVACY.zh-CN.md)。

1.16.22 + 5.8.26 的主要功能已由维护者实机使用；1.16.23 的默认模型和文档变更通过本地 CI，仍请安装后验证所选真实 API 与本机语音效果。
