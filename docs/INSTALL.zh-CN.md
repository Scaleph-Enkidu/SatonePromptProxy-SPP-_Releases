# 从零安装：AIChat 1.17.1 + SPP 5.9.1

[返回首页](../README.md) · [下载清单](DOWNLOADS.zh-CN.md)

适用于 Steam Windows 版《放松时光：与你共享 Lo-Fi 故事》。更新日期：2026-10-01。当前下载为授权修订 r1，程序版本和安装步骤不变；[许可与署名范围](../LICENSE_SCOPE.zh-CN.md)。

**先完成阶段一，就能和聪音进行文字聊天。** 后面三个阶段按自己的需要选择：不安装 ONNX，也可以安装发音和语音识别；只想听聪音说话，不必安装语音识别；只想用麦克风说话，也不必安装发音。

| 阶段 | 完成后能做什么 |
|---|---|
| [① 文字聊天](#stage-1) | 输入文字，收到聪音的回复；保存聊天和记忆 |
| [② ONNX 模型（选装）](#stage-2) | 按话题的意思查找以前的聊天 |
| [③ 聪音发音](#stage-3) | 输入文字后，听到聪音朗读回复 |
| [④ 玩家语音识别](#stage-4) | 对着麦克风说话，把识别出的文字发送给聪音 |

每个阶段的必要步骤都写在正文里。完成后可以直接进入下一阶段；后面的“进阶说明（可跳过）”留给想进一步调整的玩家。

本教程统一用 `D:\LofiMOD` 举例。电脑没有 D 盘时，可以改用例如 `C:\LofiMOD`；后面的文件路径、配置和命令也要一起换成自己实际使用的位置。

<a id="stage-1"></a>
## 阶段一：文字聊天

### 1. 下载并安装游戏插件

1. 退出游戏。在 Steam 游戏库中，右击《放松时光：与你共享 Lo-Fi 故事》，依次点击 **管理 → 浏览本地文件**。打开的文件夹就是下面所说的“游戏文件夹”。
2. 下载 [BepInEx_win_x64_5.4.23.5.zip](https://github.com/BepInEx/BepInEx/releases/download/v5.4.23.5/BepInEx_win_x64_5.4.23.5.zip)。把压缩包里的文件解压到游戏文件夹中，让 `BepInEx` 文件夹、`winhttp.dll` 和游戏的启动程序放在同一层。安装完成后启动一次游戏随后退出，插件会自动建立配置文件，供下一步安装使用。如果已经安装过这个版本的 BepInEx，可以跳过这一步。
3. 下载 [SatoneMod_AIChat_1.17.1_SPP_5.9.1_Windows_x64_license_r1.zip](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.17.1_SPP-v5.9.1-license-r1/SatoneMod_AIChat_1.17.1_SPP_5.9.1_Windows_x64_license_r1.zip)，并解压。打开里面的 `AIChat` 文件夹，把 `AIChat.dll` 和 `AIChat.pdb` 复制到游戏文件夹中的 `BepInEx\plugins`。如果没有 `plugins` 文件夹，在 `BepInEx` 中新建一个名为 `plugins` 的文件夹。如果安装过旧版 AIChat，替换原来的同名文件。
4. 你可以把解压出来的整个 `SatonePromptProxy` 文件夹复制到任意位置。如果希望继续安装聪音发音组件与玩家语音识别，推荐单独建立一个文件夹进行统一管理，例如 `D:\LofiMOD`。**不建议路径中包含中文。** 之后可以在游戏的 **AIChat UI** 中配置这个程序的路径，让 SPP 随游戏自动启动，具体操作见下面第 3 节。

### 2. 第一次启动 SPP

打开刚才放好的 `SatonePromptProxy` 文件夹，双击 **SatonePromptProxy.exe**。保持它运行，然后启动游戏。

打开的黑色窗口是 SPP 的运行日志窗口。底部出现 `Listening: http://127.0.0.1:11435/v1/chat/completions`，表示聊天服务已启动。这个窗口不会出现用于输入命令的目录提示符，属于正常现象；使用聊天功能时保持它运行。

### 3. 在 AIChat UI 中设置自动启动

1. 进入游戏后，按 **F9** 打开 **AIChat UI**，点击 **展开设置**。
2. 展开 **SPP 与记忆（人格代理）**。
3. 打开自己电脑上的 `SatonePromptProxy` 文件夹，点击资源管理器上方的地址栏，按 **Ctrl+C** 复制文件夹路径。回到 AIChat UI，将路径粘贴进 **SPP 启动文件路径：** 输入框，再在末尾加上 `\SatonePromptProxy.exe`。例如：

   ```text
   D:\LofiMOD\SatonePromptProxy\SatonePromptProxy.exe
   ```

4. 勾选 **启动游戏时自动运行 SPP**。稍后点击“保存并应用配置”后，以后启动游戏就会自动启动 SPP。
5. 确认这个栏目显示 **SPP 状态：运行中**。如果显示“未检测到”，先回到文件夹双击 `SatonePromptProxy.exe`，等显示运行中后再继续。

### 4. 设置聊天服务

聊天需要一个聊天服务账户，以及该服务提供的 **API Key（接口密钥）** 和可用的 **模型名称**。请先到自己使用的服务商网站获取；游戏和 Mod 下载不包含 API 额度。费用可查看[聊天费用说明](API_COST.zh-CN.md)。

1. 在 AIChat UI 的设置中，展开 **LLM（聊天模型与连接）**。
2. 按照自己使用的服务，完成下面对应的一组操作；只选一组。

   | 使用的服务 | 在这个栏目中怎么操作 |
   |---|---|
   | OpenAI | 展开 **OpenAI**，勾选 **选择 OpenAI（保存后生效）**。将密钥粘贴到 **API Key（接口密钥）**，将账户可用的模型名称填入 **模型名称（可修改）**。 |
   | DeepSeek | 展开 **DeepSeek**，勾选 **选择 DeepSeek（保存后生效）**。将密钥粘贴到 **API Key（接口密钥）**，将账户可用的模型名称填入 **模型名称（可修改）**。 |
   | 中转站 | 展开 **中转站（第三方 API）**，勾选 **选择 中转站（第三方 API）（保存后生效）**。填写该中转站给你的 **API Key（接口密钥）**、**模型名称（可修改）** 和 **中转站 API 地址**。地址也使用中转站提供的地址。 |

   输入框中已有的模型名称可以修改；请使用自己账户实际能调用的名称。
3. 点击 AIChat UI 下方的 **保存并应用配置**。**修改设置后，需要点击这个按钮才会生效。**
4. 如果出现旧记忆选择：想继续以前的聊天，就点击 **带入旧版记忆并继续**；想从新记忆开始，就点击 **跳过旧版记忆，继续使用**。跳过不会删除旧文件。首次安装没有旧记录时，会自动准备新档案。
5. 等待所选聊天服务旁显示 **（正在使用）**，再开始发送消息。如果仍显示“待应用”，说明这次设置还没有完成应用，先处理界面中的提示。

### 5. 发一句话试试

用 **F9** 打开 **AIChat UI**，在下方对话框中输入一句普通问候，例如“你好，今天过得怎么样？”，然后按 **Enter** 发送。默认 **Shift + Enter** 可以换行。

收到聪音的回复，并且下方对话框可以继续输入，就说明文字聊天已经安装成功。

**现在就可以直接进行文字聊天了！**

<details>
<summary>进阶说明（可跳过）</summary>

- **自动关闭 SPP：** 在 **展开设置 → SPP 与记忆（人格代理）** 中，可以勾选 **退出游戏时自动关闭 SPP**，然后点击 **保存并应用配置**。
- **记忆档案：** 同一个栏目中的 **记忆档案：** 可以选择记忆1、记忆2、记忆3。三个档案分别保存聊天和关系；只想继续当前聊天时保持原来的选择即可。同一档案可以更换聊天服务。
- **其他聊天服务：** LLM 栏目也提供其他连接选项。展开所用服务后，根据它显示的字段填写，再选择该服务并保存。以服务商说明的接口和模型名称为准。
- **修改人格：** `SatonePersona_v4.6.txt` 位于 SPP 文件夹中。修改会影响三个记忆档案；先备份再修改。
- **备份和隐私：** 见[数据与隐私说明](DATA_AND_PRIVACY.zh-CN.md)。

</details>

**下一步：** [② ONNX 模型（选装）](#stage-2)。不需要安装模型，可以直接看 [③ 聪音发音](#stage-3) 或 [④ 玩家语音识别](#stage-4)，也可以停在这里使用文字聊天。

<a id="stage-2"></a>
## 阶段二：ONNX 模型（选装）

这个模型帮助聪音按意思查找以前的聊天。**它不会默认启用，需要按下面的步骤安装和启用。** 不需要这个功能，可以直接跳到下一阶段。

### 1. 先留下一条聊天记录

先按阶段一完成文字聊天，并在想使用的记忆档案里和聪音聊一件具体的事情，例如“我最近在练习钢琴”。等她回复完，再退出游戏。这条记录稍后用来检查模型是否可以找到旧聊天。

如果档案里已经有聊天记录，可以直接用其中一个话题，不必重新聊天。**空档案没有内容可供检索，不能用来验证模型是否准备好了。**

### 2. 停止 SPP，放好模型

1. 打开自己的 `SatonePromptProxy` 文件夹，双击 **Stop_SatonePromptProxy.bat**。看到 `SatonePromptProxy stopped.` 或提示没有运行后，按任意键关闭窗口。这个工具会停止正在运行的 SPP，所以请在上一轮回复结束、退出游戏后使用。
2. 下载 [Satone_Semantic_E5_small_int8_ORT_1.30.0_Windows_x64.zip](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.17.1_SPP-v5.9.1-license-r1/Satone_Semantic_E5_small_int8_ORT_1.30.0_Windows_x64.zip)，约 94 MB，然后解压。
3. 把解压出来的整个 **models** 文件夹复制到自己的 `SatonePromptProxy` 文件夹中。使用示例位置时，放好后应是：

   ```text
   D:\LofiMOD\SatonePromptProxy\SatonePromptProxy.exe
   D:\LofiMOD\SatonePromptProxy\models\multilingual-e5-small\model.onnx
   ```

   模型放在 SPP 文件夹中，不要放到游戏的 `BepInEx\plugins` 中。如果打开 `models` 后又看到一个 `models`，把里面那层移出来，避免多套一层文件夹。

### 3. 校验并启用模型

1. 在 `SatonePromptProxy` 文件夹中，双击 **Verify_Semantic_Recall.bat**。看到 **语义组件文件校验通过。** 后，按任意键关闭窗口。
2. 双击 **Enable_Semantic_Recall.bat**。看到 **语义回忆已启用。** 的提示后，按任意键关闭窗口。
3. 双击 **SatonePromptProxy.exe**，重新启动 SPP。看到日志窗口底部出现 `Listening:` 后，再继续下一步。

如果校验失败，先重新检查上一步的文件位置，必要时重新解压模型包；不要继续启用。如果提示 SPP 仍在运行，先重新停止 SPP，再执行校验和启用。**只复制模型文件，还没有完成启用。**

如果双击校验或启用脚本后窗口一闪就关闭，没有机会看到结果，请按[脚本闪退时的处理步骤](#semantic-script)在命令窗口中执行，不要把窗口关闭当成操作成功。

### 4. 查找刚才的聊天

1. 在 `SatonePromptProxy` 文件夹中，双击 **Open_Dashboard.bat**，浏览器会打开 **本地记忆管理** 页面。
2. 在页面上方的 **查看档案** 中，选择刚才聊天使用的档案。例如刚才使用记忆1，这里也选择记忆1。这个下拉栏用来查看档案，不会切换游戏正在使用的档案。
3. 找到 **Recall 检索**，在输入框里填写刚才聊过的话题。例如聊过钢琴，可以输入“钢琴练习”，然后点击 **检索**。
4. 点击旁边的 **索引状态**。首次准备需要一些时间；等一会儿再点击一次，查看最新结果。页面会显示一段状态文字，其中下面两项表示模型已经加载、当前档案已经准备完成：

   ```json
   "model_loaded": true,
   "semantic_state": "ready"
   ```

   这是要查找的两项状态示例，不是需要填写的设置。同时确认 `semantic_scope` 对应所选档案：记忆1是 `local:memory1`，记忆2是 `local:memory2`，记忆3是 `local:memory3`。如果还是其他档案，再对自己选中的档案点击 **检索**，等待后重新查看状态。

   首次显示 `waiting`、`loading` 或 `building` 时，先等待，再点击 **索引状态**。记录较多时准备会更久，期间仍可使用关键词检索。仅打开页面而不点击“检索”，不会开始准备模型。
5. 再点击 **检索**，查看返回的聊天内容。结果中的 `user_text` 是玩家说过的话，`assistant_text` 是聪音的回复。可以再换一种说法查询，看看能否找到同一段聊天。

模型显示已准备完成，并且可以查到确实聊过的内容，就完成了这一阶段。**按意思检索不保证每种说法都能找到；可以换成更具体的话题重试。**

第一次查询时可能显示 `semantic_ready: false`，这表示模型还在准备，本次先使用已有的关键词检索。空档案一直显示 `waiting` 时，先回到游戏完成一轮聊天再查。提示服务忙碌时，等当前聊天结束后重试。

<details>
<summary>进阶说明（可跳过）</summary>

- **暂时停用模型：** 退出游戏并停止 SPP，双击 **Disable_Semantic_Recall.bat**，再双击 **SatonePromptProxy.exe**。停用后仍可使用文字聊天和关键词回忆；不会删除模型和聊天记录。停用脚本闪退时，按下方[命令窗口操作](#semantic-script)使用停用命令。
- **其他状态怎么处理：** `disabled` 表示没有启用；`missing` 表示缺少组件文件；`failed` 表示准备失败。对应的处理步骤、更新模型和缓存说明见 [ONNX 进阶说明](ONNX_SETUP.zh-CN.md)。
- **文件校验与资源开销：** 见[下载校验](DOWNLOADS.zh-CN.md)和[硬件说明](HARDWARE.zh-CN.md)。

</details>

**下一步：** [③ 聪音发音](#stage-3)。不需要聪音发音，可以直接看 [④ 玩家语音识别](#stage-4)，也可以停在这里使用文字聊天和回忆。

<a id="stage-3"></a>
## 阶段三：让聪音读出回复（GPT-SoVITS）

**做到这里，聪音就能把回复读出来。** 先完成[阶段一文字聊天](#stage-1)；[阶段二 ONNX](#stage-2)可以跳过。本阶段不需要安装第四阶段的语音识别。以下使用后藤一里 v2ProPlus 声线和程序包内的 Neutral 参考录音，其他情绪以后再加。

### 3.1 下载并放好 GPT-SoVITS

1. 退出游戏。下载并安装 [7-Zip 的 Windows x64 版](https://www.7-zip.org/)，用它解压下方的 .7z 文件。
2. 打开 [GPT-SoVITS 官方 Windows 整合包列表](https://huggingface.co/lj1995/GPT-SoVITS-windows-package/tree/main)，按自己的设备只下载一份：

   | 运行设备 | 本阶段下载的完整文件名 | 后续设置 |
   |---|---|---|
   | NVIDIA 显卡，非 RTX 50 系列 | [GPT-SoVITS-v2pro-20250604.7z](https://huggingface.co/lj1995/GPT-SoVITS-windows-package/resolve/main/GPT-SoVITS-v2pro-20250604.7z?download=true)，约 8.19 GB | 下方 GPU 配置 |
   | NVIDIA RTX 50 系列 | [GPT-SoVITS-v2pro-20250604-nvidia50.7z](https://huggingface.co/lj1995/GPT-SoVITS-windows-package/resolve/main/GPT-SoVITS-v2pro-20250604-nvidia50.7z?download=true)，约 8.84 GB | 下方 GPU 配置 |
   | 没有 NVIDIA 显卡，或希望 TTS 使用 CPU | 同上方标准包 GPT-SoVITS-v2pro-20250604.7z | 下方 CPU 配置；合成会更慢 |

   NVIDIA 路线先安装适用于自己显卡的 [NVIDIA 官方驱动](https://www.nvidia.com/Download/index.aspx?lang=cn)。这里使用整合包自带的 Python；不用另装 Python，也不要在这个环境里安装 Fun-ASR。

3. 在资源管理器中打开 D:\LofiMOD，新建 GPT-SoVITS 文件夹。用 7-Zip 打开下载的压缩包，将实际程序内容解压／复制进去，最终应直接存在：

   ~~~text
   D:\LofiMOD\GPT-SoVITS\api_v2.py
   D:\LofiMOD\GPT-SoVITS\runtime\python.exe
   D:\LofiMOD\GPT-SoVITS\GPT_SoVITS\configs\tts_infer.yaml
   ~~~

   如果路径成了 GPT-SoVITS\GPT-SoVITS-v2pro-20250604\api_v2.py，把内层的程序内容移到 D:\LofiMOD\GPT-SoVITS。先确认上面三个文件的位置，再继续。

4. 下载这两个**后藤一里 v2ProPlus** 文件。在 D:\LofiMOD\GPT-SoVITS 中新建表内的权重文件夹，再把下载文件复制进去：

   | 下载文件 | 复制后的完整路径 |
   |---|---|
   | [gotoh-v1-3-1-e16.ckpt](https://huggingface.co/lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models/resolve/main/models/Hitori_Gotoh/v2ProPlus/gotoh-v1-3-1/GPT/gotoh-v1-3-1-e16.ckpt?download=true) | D:\LofiMOD\GPT-SoVITS\GPT_weights_v2ProPlus\gotoh-v1-3-1-e16.ckpt |
   | [gotoh-v1-3-1_e8_s368.pth](https://huggingface.co/lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models/resolve/main/models/Hitori_Gotoh/v2ProPlus/gotoh-v1-3-1/SoVITS/gotoh-v1-3-1_e8_s368.pth?download=true) | D:\LofiMOD\GPT-SoVITS\SoVITS_weights_v2ProPlus\gotoh-v1-3-1_e8_s368.pth |

   只下载这两个文件，按表格保留原文件名。声线作者是 [lpkpaco](https://huggingface.co/lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models)，许可为 CC BY-NC-SA 4.0；音频来源与使用说明见[语音进阶页](VOICE_SETUP.zh-CN.md#voice-sources)。

5. 确认整合包中的下列基础模型仍在原位：

   ~~~text
   D:\LofiMOD\GPT-SoVITS\GPT_SoVITS\pretrained_models\chinese-roberta-wwm-ext-large\
   D:\LofiMOD\GPT-SoVITS\GPT_SoVITS\pretrained_models\chinese-hubert-base\
   D:\LofiMOD\GPT-SoVITS\GPT_SoVITS\pretrained_models\sv\pretrained_eres2netv2w24s4ep4.ckpt
   ~~~

   两个文件夹内部应有模型文件，不能只有空文件夹。若单独缺最后一个 .ckpt，从[官方地址下载](https://huggingface.co/lj1995/GPT-SoVITS/resolve/main/sv/pretrained_eres2netv2w24s4ep4.ckpt?download=true)，新建 sv 文件夹并放入。若前两个文件夹缺失，先用 7-Zip 重新完整解压刚才的整合包。

### 3.2 用记事本配置实际 API

1. 在资源管理器中找到 D:\LofiMOD\GPT-SoVITS\GPT_SoVITS\configs\tts_infer.yaml，复制一份作为 tts_infer.yaml.bak。
2. 右键 tts_infer.yaml → **打开方式 → 记事本**。按 Ctrl+A 全选，按自己设备选择下方**一份完整内容**替换。custom: 顶格，其余各行前面是两个空格；保持路径中的正斜杠。

**NVIDIA GPU 路线：**

~~~yaml
custom:
  bert_base_path: GPT_SoVITS/pretrained_models/chinese-roberta-wwm-ext-large
  cnhuhbert_base_path: GPT_SoVITS/pretrained_models/chinese-hubert-base
  device: cuda
  is_half: true
  t2s_weights_path: GPT_weights_v2ProPlus/gotoh-v1-3-1-e16.ckpt
  version: v2ProPlus
  vits_weights_path: SoVITS_weights_v2ProPlus/gotoh-v1-3-1_e8_s368.pth
~~~

**CPU 路线：**

~~~yaml
custom:
  bert_base_path: GPT_SoVITS/pretrained_models/chinese-roberta-wwm-ext-large
  cnhuhbert_base_path: GPT_SoVITS/pretrained_models/chinese-hubert-base
  device: cpu
  is_half: false
  t2s_weights_path: GPT_weights_v2ProPlus/gotoh-v1-3-1-e16.ckpt
  version: v2ProPlus
  vits_weights_path: SoVITS_weights_v2ProPlus/gotoh-v1-3-1_e8_s368.pth
~~~

3. 按 Ctrl+S 保存，关闭记事本。这份文件由 api_v2.py 读取；[官方配置](https://github.com/RVC-Boss/GPT-SoVITS/blob/main/GPT_SoVITS/configs/tts_infer.yaml)与[读取实现](https://github.com/RVC-Boss/GPT-SoVITS/blob/main/GPT_SoVITS/TTS_infer_pack/TTS.py)支持上面的 custom 配置及两种设备值。

### 3.3 新建启动脚本并首次启动

1. 从 Windows 开始菜单打开**记事本**，粘贴以下全部内容：

   ~~~bat
   @echo off
   cd /d "%~dp0"
   "runtime\python.exe" -s api_v2.py -a 127.0.0.1 -p 9880 -c "GPT_SoVITS/configs/tts_infer.yaml"
   pause
   ~~~

2. 选择**文件 → 另存为**。保存到 D:\LofiMOD\GPT-SoVITS；“文件名”填 run_api.bat，“保存类型”选**所有文件**，“编码”选 UTF-8，再点保存。
3. 在资源管理器开启**文件扩展名**：Windows 11 为“查看 → 显示 → 文件扩展名”；Windows 10 为“查看 → 文件扩展名”。确认文件叫 run_api.bat，完整路径是 D:\LofiMOD\GPT-SoVITS\run_api.bat。若显示 run_api.bat.txt，重命名为 run_api.bat，并确认更改扩展名。
4. 双击 run_api.bat。第一次会读取模型，保留这个黑色窗口。成功时应看到 Application startup complete，以及 Uvicorn running on http://127.0.0.1:9880；启动配置应显示 v2ProPlus 和刚才的两个后藤权重路径。GPU 路线若出现 CUDA is not available，不算 GPU 已就绪，先处理驱动或改用上方 CPU 配置。
5. 用普通浏览器打开 [API 页面](http://127.0.0.1:9880/docs)，应看到 Swagger UI 与 /tts 接口。如果窗口停在报错和“请按任意键继续”，先看报错中的文件路径或依赖，修复后重新运行。网页推理的 go-webui.bat 此时不用启动。

### 3.4 检查 SPP 的包内参考录音

1. 确认 D:\LofiMOD\SatonePromptProxy\mayuri-voice\refs\MAY_1158_Neutral.wav 存在；双击它，用 Windows 播放器确认能听到录音。它已在主程序包内，第一次安装不用再下载。
2. 保持 SPP 运行，用浏览器打开 [TTS 状态页](http://127.0.0.1:11435/tts/status)。找到 `validation` 中的 `Neutral`，确认其中 `valid` 为 `true`，`resolved_path` 指向刚才的 `MAY_1158_Neutral.wav`。可以用浏览器 Ctrl+F 搜索 `validation`，再看里面的 `Neutral`。
3. **首次安装使用包内默认配置时，保留原设置，直接进入 3.5。** 如果使用旧配置，或者上一步显示 `valid: false`，才按下面的方法纠正。主程序只附带 Neutral；其他情绪缺录音会使用这段默认录音，不影响基本朗读。

**只有旧配置不同或录音检查失败时，才做下面的操作：**

1. 退出游戏，双击 D:\LofiMOD\SatonePromptProxy\Stop_SatonePromptProxy.bat 停止 SPP。先复制 config.json 为 config.json.bak，再右键 config.json → **打开方式 → 记事本**。要编辑的是正在使用的 config.json。
2. 按 Ctrl+F 查找 "emotion_tts"。在这个对象内部修改下列值，保留其他字段、情绪项和逗号：

   | 所在位置 | 应有值 |
   |---|---|
   | emotion_tts → enabled | true |
   | emotion_tts → upstream_url | "http://127.0.0.1:9880" |
   | emotion_tts → ref_root | "" |
   | emotion_tts → fallback_profile | "Neutral" |
   | emotion_tts → profiles → Neutral → path | "MAY_1158_Neutral.wav" |
   | emotion_tts → profiles → Neutral → lang | "ja" |
   | emotion_tts → profiles → Neutral → prompt | 下方完整日语台词 |

   Neutral 的 prompt 应为：

   ~~~text
   嫌がってるのに無理やり着せたりしてねトラウマになっちゃったら良くないもん。
   ~~~

   JSON 的字符串要保留两侧英文双引号；true 不加引号。用包内默认录音时保留这句台词，旧配置指向其他目录的玩家也改回表内的 ref_root 和 path。

3. 按 Ctrl+S 保存并关闭记事本，双击 D:\LofiMOD\SatonePromptProxy\SatonePromptProxy.exe。
4. 再打开 TTS 状态页，按 F5 刷新，确认 `validation` 中的 `Neutral` 显示 `valid: true`，然后继续 3.5。

### 3.5 在游戏中保存设置并听到回复

1. 保留 GPT-SoVITS 与 SPP 的窗口，启动游戏，按 **F9 → 展开设置 → TTS（文字转语音）**。
2. 在 **TTS 启动脚本路径：**填 D:\LofiMOD\GPT-SoVITS\run_api.bat，勾选**启动游戏时自动运行 TTS 服务**。
3. **语音服务地址（默认连接 SPP 的 TTS 与 ASR 代理）：**新安装默认是 http://127.0.0.1:11435，保持即可；只有旧配置改过地址时才恢复这个值。**TTS 朗读语言：**填 ja，**TTS 朗读音量：**调到大于 0，例如 1.00。
4. 点常驻操作栏的**保存并应用配置**，等待设置应用完成，再收起设置。首次测试的 GPT-SoVITS 已由你手动启动；自动运行设置在下次启动游戏时使用。
5. 在聊天框发一句“请用日语向我问好”，等聪音回复。**看到回复文字，并从游戏中听到对应朗读，才是本阶段完成。** 如果只有文字，先检查 9880 的窗口是否还在运行，再看[语音排错](VOICE_SETUP.zh-CN.md#tts-troubleshooting)。CPU 首次合成可能需要较长等待。
6. 首次成功后，退出游戏，关闭先前手动打开的 GPT-SoVITS 窗口。下一次启动游戏，检查 TTS 自动启动并再次听到朗读，确认填写的脚本路径有效。

<details>
<summary>进阶说明（可跳过）</summary>

基本朗读完成后，可在[语音进阶页](VOICE_SETUP.zh-CN.md)补齐 26 种情绪参考音频、单独试听 TTS、设置服务联动或查看排错方法。

</details>

**下一阶段：** [④ 玩家语音识别](#stage-4)。只想打字并听回复，可以停在这里。

<a id="stage-4"></a>
## 阶段四：让聪音听懂你的话（Fun-ASR）

**做到这里，你可以按住 F8 说话，松开后让聪音回复。** 先完成[阶段一文字聊天](#stage-1)；ONNX 和 GPT-SoVITS 都可以不装。没装第三阶段时，仍可用麦克风发送文字，并在游戏中阅读回复。

本阶段建立独立的 Fun-ASR 环境，使用官方 Fun-ASR-Nano-2512 模型。下面命令按 Python 3.12 与官方依赖范围编写；先完成依赖检查，再以 F8 的实际识别结果确认安装。

### 4.1 安装 Python，打开命令提示符 CMD

1. 下载 [Python 3.12.10 的 Windows 64 位安装程序](https://www.python.org/ftp/python/3.12.10/python-3.12.10-amd64.exe)，文件名为 python-3.12.10-amd64.exe。[官网发行页](https://www.python.org/downloads/release/python-31210/)也列有同名的 Windows installer (64-bit)。已装 Python 3.12 的玩家，可先做第 4 步检查。
2. 双击安装程序，首页勾选 **Add python.exe to PATH**，保留 Python 启动器 py 的安装选项，点 **Install Now**。等待 Setup was successful，再点 Close。不要使用名为 embeddable package 的 ZIP 代替安装程序。
3. 用资源管理器打开 D:\LofiMOD，新建 FunASR-Runtime 文件夹并打开它。在这个文件夹的**地址栏**输入 cmd，按回车。出现命令提示符窗口，提示符当前目录应是 D:\LofiMOD\FunASR-Runtime>。本阶段全部命令都在这个 **CMD** 窗口中逐行粘贴并回车；代码框中的 > 提示符不用输入。
4. 先执行：

   ~~~bat
   py -3.12 --version
   ~~~

   应显示 Python 3.12.x。若提示 py 不是命令，重新打开安装程序，选择 Modify，补选 py launcher 和 pip，完成后关闭旧 CMD，再按第 3 步打开新 CMD。若提示找不到 Python 3.12，先完成第 1、2 步。

5. 在同一个 CMD 中依次执行：

   ~~~bat
   py -3.12 -m venv .venv
   .venv\Scripts\python.exe -m pip install --upgrade pip
   ~~~

   完成后，资源管理器中应有 D:\LofiMOD\FunASR-Runtime\.venv\Scripts\python.exe。后面都用它安装依赖，与 GPT-SoVITS 自带的 runtime 分开。

### 4.2 选择 GPU 或 CPU，只执行自己的分支

**GPU 路线：适用于 NVIDIA RTX 20／30／40／50 系列，使用 CUDA 12.8 版依赖。**

先安装适用于自己显卡的 [NVIDIA 官方驱动](https://www.nvidia.com/Download/index.aspx?lang=cn)，重启 Windows 后按 4.1 第 3 步重新打开 CMD。然后执行：

~~~bat
.venv\Scripts\python.exe -m pip install torch==2.9.1 torchaudio==2.9.1 --index-url https://download.pytorch.org/whl/cu128
~~~

**CPU 路线：没有上述 NVIDIA 显卡，或希望把显存留给游戏和 TTS。**

执行：

~~~bat
.venv\Scripts\python.exe -m pip install torch==2.9.1 torchaudio==2.9.1 --index-url https://download.pytorch.org/whl/cpu
~~~

CPU 识别可能更慢。本教程不配置 AMD／Intel GPU 加速，使用这些显卡时选择 CPU 分支。两条命令来自 [PyTorch 2.9.1 官方安装组合](https://pytorch.org/get-started/previous-versions/)；不用另装 CUDA Toolkit。

**两条路线接下来都执行以下命令：**

~~~bat
.venv\Scripts\python.exe -m pip install funasr==1.3.26 transformers==4.51.3 huggingface_hub==0.36.0 zhconv whisper_normalizer pyopenjtalk-plus==0.4.1.post8 compute-wer openai-whisper
.venv\Scripts\python.exe -m pip check
.venv\Scripts\python.exe -c "import torch,torchaudio,funasr,transformers; print('torch:',torch.__version__); print('torchaudio:',torchaudio.__version__); print('transformers:',transformers.__version__); print('CUDA available:',torch.cuda.is_available())"
~~~

等每条命令执行结束、重新出现当前目录提示符，再执行下一条。出现报错就先停在该条，保留最后的错误文字。

**依赖检查的成功标志：**

- pip check 显示 No broken requirements found。
- torch 与 torchaudio 都显示 2.9.1，末尾分别应同为 +cu128 或同为 +cpu。
- transformers 显示 4.51.3，导入过程没有 Traceback。
- GPU 路线的 CUDA available 为 True；CPU 路线为 False，属于正常结果。

这些版本满足 [Fun-ASR 官方 requirements.txt](https://github.com/QwenAudio/Fun-ASR/blob/main/requirements.txt)的版本范围。GPU 分支出现 False 时，先处理驱动或重新选择 CPU 分支；不要继续按 GPU 已就绪来设置。

### 4.3 下载完整模型到指定文件夹

在同一个 CMD 中执行下面**一整行**：

~~~bat
.venv\Scripts\python.exe -c "from huggingface_hub import snapshot_download; snapshot_download(repo_id='FunAudioLLM/Fun-ASR-Nano-2512', local_dir='D:/LofiMOD/Fun-ASR-Nano-2512')"
~~~

这是从[官方模型仓库](https://huggingface.co/FunAudioLLM/Fun-ASR-Nano-2512/tree/main)下载完整模型，不需要 Git。下载过程中保持联网；若网络中断，在同一窗口重执行这条命令，已有下载会继续利用。

等命令结束，再打开 D:\LofiMOD\Fun-ASR-Nano-2512，确认直接有：

~~~text
D:\LofiMOD\Fun-ASR-Nano-2512\config.yaml
D:\LofiMOD\Fun-ASR-Nano-2512\configuration.json
D:\LofiMOD\Fun-ASR-Nano-2512\model.pt
D:\LofiMOD\Fun-ASR-Nano-2512\multilingual.tiktoken
D:\LofiMOD\Fun-ASR-Nano-2512\Qwen3-0.6B\
~~~

Qwen3-0.6B 文件夹内也应有实际文件。只下载 model.pt、只创建空文件夹、下载 Git LFS 指针文本，都不算模型下载完成。当前随包脚本使用 funasr.AutoModel；不要把 Fun-ASR-Nano-2512-hf、GGUF 或 Faster Whisper 文件改名放进这里。

### 4.4 GPU／CPU 的启动脚本选择

1. 退出游戏，双击 D:\LofiMOD\SatonePromptProxy\Stop_SatonePromptProxy.bat 停止 SPP。确认包内有 D:\LofiMOD\SatonePromptProxy\satone_funasr_server_v1.py。
2. **GPU 路线**使用这个随包脚本，接着去 4.5，在 server_script 填它的完整路径。
3. **CPU 路线**必须再做下面各步。只安装 CPU 版 PyTorch 不能代替明确选择模型设备。

<a id="asr-cpu"></a>
**CPU 路线的必需脚本副本：**

1. 在资源管理器中复制 D:\LofiMOD\SatonePromptProxy\satone_funasr_server_v1.py，粘贴到 D:\LofiMOD\FunASR-Runtime。
2. 开启文件扩展名显示：Windows 11“查看 → 显示 → 文件扩展名”；Windows 10“查看 → 文件扩展名”。把副本重命名为 satone_funasr_server_cpu_v1.py，确认没有 .txt 后缀。
3. 右键这个副本 → **打开方式 → 记事本**。按 Ctrl+F 搜索下面原行：

   ~~~python
   model = AutoModel(model=model_dir, trust_remote_code=True)
   ~~~

4. 只将这行替换为下方内容，保持它前面的空格缩进及其他代码不变，再按 Ctrl+S 保存：

   ~~~python
   model = AutoModel(model=model_dir, trust_remote_code=True, device="cpu")
   ~~~

   [官方模型说明](https://huggingface.co/FunAudioLLM/Fun-ASR-Nano-2512)明确提供 cpu 设备值。SPP 5.9.1 通过已有 server_script 字段使用这份副本；它没有 asr.device 设置。

### 4.5 编辑实际 config.json，交给 SPP 启动

1. 在 D:\LofiMOD\SatonePromptProxy 中复制 config.json 为 config.json.bak，然后右键 config.json → **打开方式 → 记事本**。
2. 按 Ctrl+F 找到 "asr"。只修改这个对象中对应字段的值，保留其他字段和逗号。路径使用表内正斜杠，字符串两侧保留英文双引号：

   | asr 内的字段 | 所填值 |
   |---|---|
   | enabled | true |
   | auto_start | true |
   | auto_restart | true |
   | stop_with_proxy | true |
   | python | "D:/LofiMOD/FunASR-Runtime/.venv/Scripts/python.exe" |
   | model_path | "D:/LofiMOD/Fun-ASR-Nano-2512" |
   | upstream_url | "http://127.0.0.1:9881" |
   | language | "auto" |
   | server_script，GPU 路线 | "D:/LofiMOD/SatonePromptProxy/satone_funasr_server_v1.py" |
   | server_script，CPU 路线 | "D:/LofiMOD/FunASR-Runtime/satone_funasr_server_cpu_v1.py" |

   server_script 只填自己路线的一项。没有装第三阶段 TTS 的玩家，也可原样完成这里。两个服务的设备设置互不改变。

3. 按 Ctrl+S 保存并关闭记事本。双击 D:\LofiMOD\SatonePromptProxy\SatonePromptProxy.exe，等它加载模型。SPP 会自动启动配置中的 ASR Python 服务；不用双击 .py 文件。
4. 用普通浏览器打开 [SPP 的 ASR 状态页](http://127.0.0.1:11435/asr/status)，加载期间按 F5 刷新。成功时应有 ready: true，且 python、model_path、server_script 都显示刚才填写的路径。CPU 路线的 server_script 必须显示 cpu 副本。
5. 再打开 [ASR 后端健康页](http://127.0.0.1:9881/health)，应看到 ok: true。第一次模型加载较慢；若状态的 last_error 有内容，或健康页一直打不开，查看 D:\LofiMOD\SatonePromptProxy\SatonePromptProxy_v5.9.1.log 中的第一条 Python 错误，再按[ASR 排错](VOICE_SETUP.zh-CN.md#asr-troubleshooting)处理。

如果 9881 已有之前手动运行的 ASR，SPP 可能直接使用它。关闭自己之前启动的那份 ASR 窗口，再停止／重新启动 SPP，避免 CPU 分支实际连着旧 GPU 服务。

### 4.6 选择麦克风，用 F8 实际识别

1. 在 Windows **设置**里搜索“麦克风隐私设置”。打开麦克风访问，以及允许桌面应用访问麦克风的选项。确认 Windows 的输入设备是你要用的麦克风，避免选成显示器／耳机的无效输入。
2. 启动游戏，按 **F9 → 展开设置 → 持续通话 → 选择麦克风（按住说话与持续通话共用）**。在列表中点击自己的麦克风名称。
3. 点**保存并应用配置**，等待应用完成。选麦克风不需要先开启持续通话。
4. 新安装的共用**语音服务地址**默认是 http://127.0.0.1:11435，保持即可。若旧配置改过地址，进入 **TTS（文字转语音） → 语音服务地址（默认连接 SPP 的 TTS 与 ASR 代理）：**恢复这个值，再点**保存并应用配置**；即使没装 TTS，ASR 也通过这个地址连接 SPP。
5. 收起设置，在游戏里按住 **F8**，说一句“聪音，今天过得怎么样？”，说完松开。也可按住聊天界面中的**按住说话 (F8)** 按钮、说完松开。**自己的语音被识别为聊天文字、聪音收到并回复，才是本阶段完成。** 已装第三阶段时还可听到回复；未装时看文字即可。
6. F8 成功后，如需免按键说话，再到 **展开设置 → 持续通话**，勾选**启用持续通话模式（保存后生效）**，点**保存并应用配置**。说话后停顿，确认出现识别文字；结束时取消该选项再保存，或点击聊天界面的**结束持续通话**。每次启动游戏默认关闭持续通话。

<details>
<summary>进阶说明（可跳过）</summary>

需要调整说话检测、保存诊断录音、检查热词或排查服务冲突时，见[语音进阶与排错](VOICE_SETUP.zh-CN.md#asr-troubleshooting)。之后升级 SPP 时，CPU 用户要把随包脚本的更新同步到自己的 CPU 副本。

</details>

**下一步：** 使用你已经完成的功能。需要更新时看[升级与回退](#upgrade)，搬迁时看[数据备份](DATA_AND_PRIVACY.zh-CN.md)。

<a id="upgrade"></a>
## 已经安装过：更新、备份与排错

### 更新前先备份

1. 等当前聊天结束，退出游戏、SPP 和自己打开的语音程序。
2. 新建一个备份文件夹，放在游戏插件目录之外。将整个 `SatonePromptProxy` 文件夹、游戏中的 `BepInEx\config` 文件夹，以及现有的 `AIChat.dll` 和 `AIChat.pdb` 都复制进去。旧 DLL 不要留在 `BepInEx\plugins` 中作为备份，避免同时加载两份插件。
3. 解压新版安装包，把新版 `AIChat.dll` 和 `AIChat.pdb` 放到原来的 `BepInEx\plugins` 中，替换同名文件。
4. 将新版 `SatonePromptProxy` 文件夹中的程序和配套工具复制到原运行位置。**保留自己的 `config.json`、记忆文件夹、修改过的人格文件、模型和语音资源。** 不要先删除整个旧文件夹，也不要把 `config.example.json` 当成自己的配置覆盖进去。
5. 启动 SPP 和游戏，先发一句文字确认聊天正常，再检查自己已经安装的语音功能。

更新失败时，退出所有相关程序，恢复升级前备份的 AIChat 文件、SPP 文件夹和 `BepInEx\config`。需要核对具体数据位置时，查看[数据与备份说明](DATA_AND_PRIVACY.zh-CN.md)。

### 常见问题先查这里

| 遇到的问题 | 先做什么 |
|---|---|
| 按 F9 没有打开 AIChat UI | 检查 `AIChat.dll` 是否放在游戏的 `BepInEx\plugins` 中，BepInEx 是否和游戏启动程序在同一层；已有旧版时不要留下第二份 AIChat DLL。 |
| 显示 SPP 未检测到 | 回到 SPP 文件夹双击 `SatonePromptProxy.exe`，再核对 UI 中填写的完整启动文件路径。 |
| 校验、启用或停用 BAT 一闪就关闭 | 按[命令窗口操作](#semantic-script)执行，看到明确结果后再继续。 |
| 停止 SPP 后游戏掉帧，或启动 BAT 后仍未恢复 | 直接双击同一文件夹中的 `SatonePromptProxy.exe`。安装、校验模型前先退出游戏；日常聊天保持 SPP 运行。详细步骤见[启动窗口与掉帧](#spp-start-window)。 |
| 发送文字后没有正常回复 | 检查聊天服务是否显示“正在使用”，密钥和模型名称是否属于这个服务，服务商账户是否有可用额度。修改后重新点击“保存并应用配置”。 |
| ONNX 没有准备完成 | 确认当前档案有聊天记录，再按[阶段二](#stage-2)完成校验、启用和一次检索。进一步排查见 [ONNX 进阶说明](ONNX_SETUP.zh-CN.md)。 |
| 有文字回复却没有声音 | 按[阶段三](#stage-3)检查 GPT-SoVITS 是否已经启动，TTS 朗读语言和音量是否正确。进一步排查见[语音进阶说明](VOICE_SETUP.zh-CN.md#stage-3)。 |
| 按 F8 说话没有识别 | 按[阶段四](#stage-4)检查 ASR 启动结果、Windows 麦克风权限和游戏中选择的麦克风。进一步排查见[语音识别进阶说明](VOICE_SETUP.zh-CN.md#stage-4)。 |
| 提示“有因重启或会话切换而保留的语音输入；未自动转发到新会话。” | 按[保留语音的处理步骤](#preserved-voice)选择恢复文字、保存录音或移除旧输入。 |

<a id="semantic-script"></a>
### 校验、启用或停用脚本闪退：在命令窗口中操作

1. 等聪音回复结束，退出游戏。打开自己的 `SatonePromptProxy` 文件夹，双击 **Stop_SatonePromptProxy.bat** 停止 SPP。
2. 点击这个文件夹上方的地址栏，输入 **cmd**，按 **Enter**。命令窗口会在当前文件夹中打开；不要把下面的命令输入 SPP 的运行日志窗口。
3. 复制下面一行到命令窗口，按 **Enter**：

   ```bat
   SatonePromptProxy.exe --semantic-component verify
   ```

   看到 **语义组件文件校验通过。** 才继续。若显示校验失败，按上方原因检查模型文件位置与完整性；若显示 `already active or locked`，说明 SPP 仍在运行，先停止再重试。
4. 需要启用时，复制下面一行并按 **Enter**：

   ```bat
   SatonePromptProxy.exe --semantic-component enable
   ```

   看到 **语义回忆已启用。** 才算启用成功。若这次是要停用模型，执行下面这一行代替启用命令：

   ```bat
   SatonePromptProxy.exe --semantic-component disable
   ```

5. 关闭命令窗口，双击 **SatonePromptProxy.exe**，然后按[阶段二的检索检查](#stage-2)查看模型是否准备完成。文件校验通过与模型实际加载完成是两次不同的检查。

<a id="spp-start-window"></a>
### 启动窗口不同，或停止 SPP 后游戏掉帧

直接双击 **SatonePromptProxy.exe** 即可启动完整 SPP。`Start_Text_Chat.bat` 是启动同一程序的便捷工具；旧安装包中的工具会另开最小化日志窗口，外观可能与直接打开 EXE 不同。安装步骤统一使用 EXE，不要求使用这个工具。

如果使用启动工具后聊天服务没有恢复，或游戏帧数仍然很低：

1. 打开自己的 `SatonePromptProxy` 文件夹，双击 **SatonePromptProxy.exe**。
2. 查看打开的窗口，底部应出现 `Listening: http://127.0.0.1:11435/v1/chat/completions`。若出现其他错误，保留完整错误文字，不要只根据窗口是否打开判断成功。
3. 点回游戏，按 F9 打开 **AIChat UI → 展开设置 → SPP 与记忆（人格代理）**，确认 **SPP 状态：运行中**，再尝试聊天。

停止 SPP 后掉帧的具体原因仍在排查；重新启动 SPP 是临时恢复方式。安装模型、调整模型启用状态或更新程序时，先等回复结束并退出游戏，再停止 SPP。使用聊天功能时保持 SPP 运行。

<a id="preserved-voice"></a>
### 重启后提示有保留的语音输入

这条提示表示之前的一段语音被保留了，尚未自动发送到当前会话。SPP 重启、切换记忆档案或切换会话后可能出现；它不表示 ONNX 安装失败。重新启动 SPP 不会自动清掉这条提示，需要自己决定如何处理旧输入。

1. 先启动 **SatonePromptProxy.exe**。在游戏中按 **F9** 打开 **AIChat UI**，确认 SPP 已运行，并且当前选择的聊天服务显示 **（正在使用）**。
2. 点击 **展开设置 → 持续通话**。不用开启持续通话模式，在这个栏目中找到 **保留的语音输入：**，查看条数、原档案和文字。
3. 根据自己是否需要这条旧输入，选择对应操作：

   | 想怎么处理 | 点击哪个按钮，以及接下来做什么 |
   |---|---|
   | 还想发送已识别出的这句话 | 点 **复制这条发言到输入框（不发送）**。确认当前记忆档案正确，核对下方输入框中的文字，再手动发送。复制不会清掉原队列；发送后按下一行移除旧输入。 |
   | 不需要这条旧输入，或聪音已经回复过它 | 点 **从保留队列移除这条输入（不发送）**。它只移除这一条保留输入，不会发送消息，也不会删除已有聊天或记忆。 |
   | 只有录音，还没识别出文字，需要留一份 | 点 **导出这条保留语音（不发送）**。录音保存到游戏文件夹中的 `BepInEx\config\AIChat.preserved-inputs`；保存后可移除旧输入。这个按钮只导出录音，不会自动重新识别或发送；需要继续聊天时重新说一次，或自己输入文字发送。 |

4. 有多条保留输入时，每次只处理当前显示的这一条，逐条确认，直到条数归零。这些按钮立即处理队列，不需要再点击“保存并应用配置”。清理完成后，旧提示可能还会显示几秒，随后自行消失。

仍不能解决，可以到[项目 Issues](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/issues)描述“在哪一步、做了什么、出现什么提示”，并附版本号和报错截图或日志。分享前隐藏 API Key 和私人聊天内容。
