# 下载清单

[返回首页](../README.md) · [按步骤安装](INSTALL.zh-CN.md)

核查日期：2026-09-26。“已核实”指仓库、发布页或 Release 元数据可查询，不代表已在全新 Windows 电脑上测试每个包。

## 游戏与两个 Mod

| 文件或入口 | 用途和放置位置 | 当前状态 |
|---|---|---|
| Steam 库中的 Chill with You : Lo-Fi Story | 正常安装并运行一次游戏 | 玩家自行购买 |
| [BepInEx 5.4.23.5 发布页](https://github.com/BepInEx/BepInEx/releases/tag/v5.4.23.5)；[Windows x64 ZIP](https://github.com/BepInEx/BepInEx/releases/download/v5.4.23.5/BepInEx_win_x64_5.4.23.5.zip) | 解压内容放在游戏 EXE 同一层 | 公开；本项目编译引用此版本。不要选 x86、Patcher 或 BepInEx 6 IL2CPP |
| [AIChat 1.16.14 发布页](https://github.com/Scaleph-Enkidu/SatoneAIChat_Remake/releases/tag/AIChat-v1.16.14)；[AIChat_v1.16.14.zip](https://github.com/Scaleph-Enkidu/SatoneAIChat_Remake/releases/download/AIChat-v1.16.14/AIChat_v1.16.14.zip) | 将其中 AIChat.dll 放进游戏的 BepInEx/plugins | **私库，普通玩家当前不可直接下载**；277,086 字节 |
| [AIChat SHA256](https://github.com/Scaleph-Enkidu/SatoneAIChat_Remake/releases/download/AIChat-v1.16.14/AIChat_v1.16.14_SHA256.txt) | 校验对应 ZIP | 同上 |
| [SPP 5.8.23 发布页](https://github.com/Scaleph-Enkidu/SatonePromptProxy/releases/tag/SPP-v5.8.23)；[SatonePromptProxy_v5.8.23.zip](https://github.com/Scaleph-Enkidu/SatonePromptProxy/releases/download/SPP-v5.8.23/SatonePromptProxy_v5.8.23.zip) | 全部解压到固定的 SPP 文件夹 | **私库，普通玩家当前不可直接下载**；8,739,688 字节 |
| [SPP SHA256](https://github.com/Scaleph-Enkidu/SatonePromptProxy/releases/download/SPP-v5.8.23/SatonePromptProxy_v5.8.23_SHA256.txt) | 校验对应 ZIP | 同上 |
| [本仓库 Releases](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases) | 计划中的统一下载入口 | 核查时没有 Release，尚不可作为玩家安装包入口 |

在 GitHub 发布页展开 **Assets**，点击表中的 ZIP 文件。不要下载 `Source code (zip)` 或 `Source code (tar.gz)` 作为 Mod 安装包。源码不会替你生成 DLL/EXE，也无需安装 GitHub Desktop。请按发布说明配对版本，不要把页面最上面的历史条目自动当作推荐版。

## 朗读需要的文件

| 入口 | 用途 | 是否包含在 Mod ZIP 中 |
|---|---|---|
| [GPT-SoVITS 官方项目](https://github.com/RVC-Boss/GPT-SoVITS) | 本地语音合成程序 | 否 |
| [官方 Windows 整合包列表](https://huggingface.co/lj1995/GPT-SoVITS-windows-package/tree/main) | 本文参考 v2Pro 系列；普通包 `GPT-SoVITS-v2pro-20250604.7z` 约 8.19 GB，`…-nvidia50.7z` 约 8.84 GB，按原发布说明选择兼容 GPU/驱动的包 | 否；不要下载整个 118 GB 仓库 |
| [GPT-SoVITS 基础模型](https://huggingface.co/lj1995/GPT-SoVITS/tree/main) | 整合包缺模型时，补齐与配置匹配的基础权重和文本模型 | 否；整合包是否齐全需实际检查 |
| 选定声线的 `.ckpt`、`.pth` 与原发布说明 | 使用第三方训练声线时，需要匹配 GPT-SoVITS 版本 | **当前两库尚未核实开发者声线的准确发布链接，待补** |
| 参考 `.wav` 与逐字台词 | 自己的录音或有明确使用许可的录音 | **不包含**；模板中的 `MAY_*.wav` 只是文件名 |
| [7-Zip](https://www.7-zip.org/) | 解压 `.7z`；Windows x64 电脑选择 x64 安装器 | 否 |

声线权重和参考录音是不同资源。安装 GPT-SoVITS 并不会自动得到开发者演示中的同一声音。要复现该声音，还需补齐准确来源、文件名、版本和参考录音，不能根据角色名随便下载同名模型。

## 麦克风识别需要的文件

| 入口 | 用途和注意事项 |
|---|---|
| [Python Windows 下载](https://www.python.org/downloads/windows/) | 为 Fun-ASR 建立独立环境，选择普通 64 位安装方式，不选 embeddable 包 |
| [PyTorch 安装选择器](https://pytorch.org/get-started/locally/) | 选择与 GPU/驱动相容的 torch 和 torchaudio，同时核对 Fun-ASR 要求 |
| [Fun-ASR 官方项目](https://github.com/QwenAudio/Fun-ASR)；[依赖清单](https://github.com/QwenAudio/Fun-ASR/blob/main/requirements.txt) | 下载官方源码 ZIP 以取得依赖清单，无需 Git |
| [Fun-ASR-Nano-2512 模型](https://huggingface.co/FunAudioLLM/Fun-ASR-Nano-2512)；[文件列表](https://huggingface.co/FunAudioLLM/Fun-ASR-Nano-2512/tree/main) | 下载整个模型快照，约 1.99 GB，不含 Python/Torch。适配器使用 funasr.AutoModel，不要替换成 `-hf` 或 GGUF 版 |
| [同名 ModelScope 模型](https://www.modelscope.cn/models/FunAudioLLM/Fun-ASR-Nano-2512) | 官方模型卡列出的另一下载源；两站快照可能不同，不要混合零散文件。本文命令使用 Hugging Face |
| SPP 包内 `satone_funasr_server_v1.py`、`SatoneASRHotwords_v1.json` | 专用 ASR 服务脚本和热词，**不等于** Python 环境和模型 |

GPU、驱动与 Python 依赖组合尚未在本教程中完成全新安装验收。键盘聊天可先跳过麦克风部分。

## 在线 AI 与可选记忆检索

| 入口 | 用途 |
|---|---|
| [OpenAI Platform](https://platform.openai.com/)；[API Key](https://platform.openai.com/api-keys) | 创建自己的密钥 |
| [API 计费](https://platform.openai.com/settings/organization/billing/overview)；[用量](https://platform.openai.com/usage) | 确认额度，查看实际账单 |
| [模型列表](https://developers.openai.com/api/docs/models)；[GPT-6 Luna](https://developers.openai.com/api/docs/models/gpt-6-luna)；[价格](https://developers.openai.com/api/docs/pricing) | 本文填写示例为 gpt-6-luna，权限以账户实际情况为准 |
| [multilingual-e5-small](https://huggingface.co/intfloat/multilingual-e5-small) | 可选的本地旧聊天语义检索模型，与主聊天模型不同 |

SPP 内部需要 Responses **及** Conversations/items；不能把任何标有“OpenAI 兼容”的中转服务都视为兼容。服务地区与付费条件以服务商当前规则为准。

## 校验 ZIP

在下载文件夹的地址栏输入 `powershell`，回车后执行：

```powershell
Get-FileHash .\AIChat_v1.16.14.zip -Algorithm SHA256
Get-FileHash .\SatonePromptProxy_v5.8.23.zip -Algorithm SHA256
```

与相同版本的 SHA256 文本比较，字母大小写不影响比较。哈希检查文件一致性，不证明软件已经通过安全审计。此次文档核查未重新下载并逐字节检查 Release ZIP。
