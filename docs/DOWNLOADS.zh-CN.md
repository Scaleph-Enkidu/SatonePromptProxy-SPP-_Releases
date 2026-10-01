# 下载清单：AIChat 1.17.0 + SPP 5.9.0

[返回首页](../README.md) · **[打开四阶段安装教程](INSTALL.zh-CN.md)** · [语音配置](VOICE_SETUP.zh-CN.md)

更新日期：**2026-10-01**。[本次配对 Release](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/tag/AIChat-v1.17.0_SPP-v5.9.0) 的推荐下载仍为下列两类 ZIP。**新玩家先下约 11 MB 的文档修订 1 主程序配对包即可**；模型可跳过，不默认启用。GitHub 自动生成的 Source code ZIP 不是安装包。

**文档修订 1** 仅补齐包内可独立阅读的 README、安装与版本改动正文，程序版本仍为 AIChat 1.17.0 + SPP 5.9.0，程序和模型不变。原正式 ZIP 保留，已安装用户无需升级；选装模型继续使用原文件、原 URL 与原 SHA-256，不需重下。原 `INSTALL_zh-CN.md` 附件保持原发布字节，新指南以[当前安装页](INSTALL.zh-CN.md)与 `docs_r1` ZIP 为准。

| 文件 | 是否需要 | 放置位置 |
|---|---|---|
| [SatoneMod_AIChat_1.17.0_SPP_5.9.0_Windows_x64_docs_r1.zip](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.17.0_SPP-v5.9.0-docs-r1/SatoneMod_AIChat_1.17.0_SPP_5.9.0_Windows_x64_docs_r1.zip)（约 11 MB） | 必需；已同时包含 AIChat 与 SPP | `AIChat/AIChat.dll` 与 PDB 放入游戏 `BepInEx/plugins`；整个 `SatonePromptProxy` 文件夹放到固定运行目录 |
| [Satone_Semantic_E5_small_int8_ORT_1.30.0_Windows_x64.zip](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.17.0_SPP-v5.9.0/Satone_Semantic_E5_small_int8_ORT_1.30.0_Windows_x64.zip)（约 94 MB） | 可选；需要按意思查找旧对话时再安装 | 把 `models` 文件夹放在 SPP EXE 旁，再 Verify → Enable → 重启 → 发首次查询 |

私有源码库的 AIChat／SPP 单组件包用于组件构建与来源记录，**不是玩家必须额外下载的文件**。TTS 与 ASR 的外部下载列在下方；它们都不依赖这个 ONNX 选装包。

## 大小、SHA-256 与来源

文档修订 1 的精确字节数、SHA-256、包内成员和来源见[修订校验清单](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/main/releases/AIChat_v1.17.0_SPP_v5.9.0_docs_r1.json)；原资产身份继续保留在[原配对清单](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/AIChat-v1.17.0_SPP-v5.9.0/releases/AIChat_v1.17.0_SPP_v5.9.0.json)。包内的 `BUILD_INFO.json`／`COMPONENT.json` 记录各自文件清单和组件身份；ZIP 自身校验以包外发布清单为准。约 11／94 MB 是下载量提示，不是运行内存或显存。

下载后，在文件所在文件夹打开 PowerShell，执行：

```powershell
Get-FileHash -LiteralPath '.\SatoneMod_AIChat_1.17.0_SPP_5.9.0_Windows_x64_docs_r1.zip' -Algorithm SHA256
Get-FileHash -LiteralPath '.\Satone_Semantic_E5_small_int8_ORT_1.30.0_Windows_x64.zip' -Algorithm SHA256
```

将结果与发布清单对应文件的 SHA-256 比较。只下主程序时只执行第一条。已有同一模型组件且校验通过，兼容的主程序更新无需再下载模型；不要把不同版本的模型、tokenizer 和 ORT DLL 混在一起。

## 阶段一：游戏与加载器

- 在 Steam 安装 **Chill with You : Lo-Fi Story**。
- 将 [BepInEx 5.4.23.5 Windows x64](https://github.com/BepInEx/BepInEx/releases/tag/v5.4.23.5) 安装到游戏 EXE 同层。已有 BepInEx 时核对版本和其他插件，不要清空现有 Mod。
- 配对主程序包已包含默认人格、程序工具与 `mayuri-voice/refs/MAY_1158_Neutral.wav`。文字聊天和关键词回忆无需 Python。

**下一阶段：** [② ONNX 模型选装](INSTALL.zh-CN.md#stage-2)，或跳到 [③ 聪音发音](INSTALL.zh-CN.md#stage-3)。

## 阶段二：本地 ONNX 模型（选装）

组件为 E5 small int8、tokenizer 与 **Windows x64 ONNX Runtime CPU 1.30.0**，目录为 `models/multilingual-e5-small`。模型来源是 [intfloat/multilingual-e5-small 的固定 revision](https://huggingface.co/intfloat/multilingual-e5-small/tree/614241f622f53c4eeff9890bdc4f31cfecc418b3)，运行时来源是 [ONNX Runtime v1.30.0](https://github.com/microsoft/onnxruntime/releases/tag/v1.30.0)。组件包保留模型说明、E5 项目 MIT 许可、ORT 许可与第三方声明；完整来源和支持文件 hash 见组件内 `COMPONENT.json` 与 `licenses`。

只解压不会启用；[阶段二安装](INSTALL.zh-CN.md#stage-2)与[ONNX 专页](ONNX_SETUP.zh-CN.md)说明校验、启用、首次暖机与 `/recall/status` 验收。旧 Python Embedding 教程不适用于本组件。

**下一阶段：** [③ 聪音发音](INSTALL.zh-CN.md#stage-3)。

## 阶段三：外装 GPT-SoVITS 与声线

- [GPT-SoVITS 官方项目](https://github.com/RVC-Boss/GPT-SoVITS)及[Windows 整合包列表](https://huggingface.co/lj1995/GPT-SoVITS-windows-package/tree/main)，选择支持实际设备和声线版本的环境。
- 本项目现有示例使用[后藤一里 gotoh-v1-3-1 的 v2ProPlus 声线](https://huggingface.co/lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models/tree/main/models/Hitori_Gotoh/v2ProPlus/gotoh-v1-3-1)的 GPT `.ckpt` 与 SoVITS `.pth` 两份权重；不要混用 v4 权重。
- **Neutral 参考音频已经在主程序包内**；其余情绪录音是可选补充。声线模型的[原作者页面](https://huggingface.co/lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models)标注 CC BY-NC-SA 4.0，Neutral 音频的[原项目](https://huggingface.co/SteinsGateSg/mayuri-voice)标注 `License: other`。按各来源条件使用。

主程序包不附带 GPT-SoVITS 环境或声线权重。文件名、配置、启动和试听见[语音页阶段三](VOICE_SETUP.zh-CN.md#stage-3)。

**下一阶段：** [④ 玩家语音识别](INSTALL.zh-CN.md#stage-4)，不需要麦克风可停在本阶段。

## 阶段四：外装 Fun-ASR

麦克风需要 [Fun-ASR 项目](https://github.com/QwenAudio/Fun-ASR)、[Fun-ASR-Nano-2512 模型](https://huggingface.co/FunAudioLLM/Fun-ASR-Nano-2512)和匹配的独立 Python／Torch 环境。包内 `satone_funasr_server_v1.py` 只是服务脚本，不等于环境与模型已经安装。[语音页阶段四](VOICE_SETUP.zh-CN.md#stage-4)提供放置、设置、启动与 F8 验收步骤。

## 其他工具与回退

[SatoneStateCatalog（F10）](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/main/tools/SatoneStateCatalog/README_中文.md)是独立可选外观采集器，使用说明与预编译 DLL 在工具目录；不是主安装前置依赖。

[上一配对 AIChat 1.16.65 + SPP 5.8.42](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/tag/AIChat-v1.16.65_SPP-v5.8.42)保留供回退；先备份并成对恢复程序和升级前个人数据，详见[升级与回退](INSTALL.zh-CN.md#upgrade)。
