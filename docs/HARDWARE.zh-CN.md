# 运行开销与显卡兼容说明

[返回首页](../README.md) · [安装步骤](INSTALL.zh-CN.md) · [语音设置](VOICE_SETUP.zh-CN.md)

核查日期：2026-09-27。适用的正式配对：AIChat 1.16.14 + SPP 5.8.23。本次更新说明文档，没有发布降显存补丁，也没有修改玩家电脑的设备选择。

## 1. 先按使用方式选择配置

本项目暂时建议：**游戏、GPT-SoVITS 与 Fun-ASR 同时使用本机 GPU 时，8 GB 显存作为建议起点，12 GB 或以上优先。** 6 GB 应优先评估“GPU 合成语音、CPU 识别语音”；4 GB 或以下优先使用文字聊天或测试 CPU 语音。

这是根据当前读数为桌面与推理峰值预留空间的工程建议，不是最低配置测试结果。显存容量不能代替显卡速度、驱动兼容性或模型适配。大分辨率、多显示器、浏览器、不同声线模型、精度和同时运行的服务都会改变占用。不包含本地大语言模型；当前教程的主聊天模型通过云端 API 运行。

| 组件 | 工作内容 | 是否需要 CUDA／显存 |
|---|---|---|
| 游戏与 AIChat 界面 | 渲染、字幕、录音、播放、动画与交互 | 游戏会使用 GPU；AIChat 不在 DLL 内运行主聊天或 ASR 大模型 |
| SPP 主程序 | 请求编排、人格、记忆、文件与服务管理 | Go 主程序不通过 CUDA 进行模型推理；它启动的 Python 服务应另计 |
| 云端聊天 API | 生成回答以及处理所需辅助请求 | 模型在服务端运行，不在玩家显存中加载；玩家承担 API 用量 |
| GPT-SoVITS | 生成聪音的声音 | 选择 CUDA 时使用 NVIDIA GPU；CPU 是另一条运行路径，会消耗系统内存和 CPU 时间 |
| Fun-ASR | 将玩家的录音转成文字 | 取决于实际 Python 环境和模型设备；当前随包脚本没有固定为 CPU |
| 本地语义检索 | 为旧对话计算检索向量 | 当前随包 worker 明确使用 CPU；这与 ASR 是不同的模型和设置 |
| Windows 桌面、浏览器等 | 桌面合成与各自任务 | 会占用 GPU 资源，不能全部算入 Mod |

模型即使暂时没有推理，也可能保留已加载的权重和框架缓存。CPU／GPU 利用率暂时为零，不意味着显存已经释放。关闭网页标签页也不等于停止它背后的 Python 推理进程。

## 2. 当前截图能说明什么

维护者在 2026-09-27 提供的任务管理器截图，显示了以下“专用 GPU 内存”读数。按 Windows 此处的 K 以 1024 换算为 GiB，保留两位小数：

| 进程 | 当时的 PID | 截图原始读数 | 约合 |
|---|---:|---:|---:|
| python.exe | 25164 | 2,274,520 K | 2.17 GiB |
| python.exe | 45612 | 2,016,496 K | 1.92 GiB |
| Chill With You.exe | 12832 | 664,188 K | 0.63 GiB |
| dwm.exe | 15924 | 1,185,484 K | 1.13 GiB |
| steamwebhelper.exe | 32852 | 146,284 K | 0.14 GiB |

两个 Python 行的读数算术相加约为 4.09 GiB，但还不能认定它们各自是哪种服务。也不能由这张截图得出“TTS 恒定占 2.17 GiB”“ASR 恒定占 1.92 GiB”或“游戏最多只占 0.63 GiB”。

还需要注意：

- 此图没有完整记录声线、精度、服务命令行、显示设置以及截图处于空闲还是推理阶段，不能当作标准性能测试。
- 任务管理器按进程统计时，跨进程共用的 GPU 资源可能重复计数。整卡占用应查看“性能 → 对应 GPU → 专用 GPU 内存”，不能把所有进程行直接相加。微软的原文提醒是“memory shared across processes will be counted multiple times”。
- “共享 GPU 内存”来自系统内存，不是额外的等速专用显存。“提交大小”也不是该进程的显存读数。
- `dwm.exe` 是 Windows 桌面窗口管理器。游戏退出后它仍会工作；排查 Mod 时应关闭已确认的模型服务，不应结束它来节省显存。

出处：[Microsoft：GPUs in the task manager](https://devblogs.microsoft.com/directx/gpus-in-the-task-manager/)。

## 3. 当前哪些部分会使用 CUDA

CUDA 是 NVIDIA 的 GPU 计算平台。安装了 CUDA 版 PyTorch，不代表程序的每一步都在 GPU 上运行；关键还在于模型和数据实际被放到什么设备。仅凭显存截图不能判断某次运算具体用了 CUDA 核心还是 Tensor 核心。

**Fun-ASR 的设备选择目前有一个容易误解的地方。** SPP 5.8.23 的随包脚本加载模型时使用：

```python
model = AutoModel(model=model_dir, trust_remote_code=True)
```

它没有传入 `device="cpu"`。本次核查的上游 FunASR 使用以下默认值：

```python
device = kwargs.get("device", "cuda")
```

因此，有可用 CUDA 环境时，不能把这条加载路径称为“CPU 识别”。实际行为仍取决于玩家安装的 FunASR 版本、模型配置及是否复用了一个已经运行的 ASR 服务。上游存在设备不可用时回退 CPU 的逻辑，但这不等于所有 Nano 依赖组合都已通过本项目的 CPU 验证。

**记忆检索确实另有 CPU 设置。** 当前 `embedding_worker.py` 明确调用 `self.model.to("cpu")`。修改 SPP 的 `embedding_device` 不会给 Fun-ASR 指定设备。

AIChat 的 ASR 客户端将 WAV 通过 HTTP 发给 `/asr`；录音、VAD 和音频转发本身不等于在游戏 DLL 中加载第二套 CUDA 识别模型。外部服务究竟启动了几份，仍应按进程命令行核对。

本次实现依据保存在[维护者核查记录](MAINTAINER_STATUS.zh-CN.md#运行开销与设备选择核查2026-09-27)。公开上游依据：[FunASR AutoModel](https://github.com/modelscope/FunASR/blob/main/funasr/auto/auto_model.py)、[GPT-SoVITS 推理配置](https://github.com/RVC-Boss/GPT-SoVITS/blob/main/GPT_SoVITS/configs/tts_infer.yaml)、[NVIDIA CUDA 说明](https://developer.nvidia.com/cuda/toolkit)。

## 4. 非 NVIDIA 显卡可以怎样使用

| 环境 | 可采用的路线 | 当前验证边界 |
|---|---|---|
| NVIDIA + 兼容驱动 | 使用匹配的 CUDA 环境；TTS 与 ASR 分别核对设备 | 本教程的主要 GPU 路线，仍需核对各整合包／依赖组合 |
| AMD、Intel 或集成显卡 | 先使用游戏、文字聊天和云端 API；语音选择 CPU 环境再测试 | CPU 语音的延迟、稳定性和内存峰值尚未形成完整验收结果 |
| AMD GPU 加速 | 必须另行选择支持该显卡、系统和模型的后端 | 不能直接使用 NVIDIA CUDA 安装包；本项目未验证完整流程 |
| Intel GPU 加速 | 同样需要适配的框架、算子和设备设置 | 本项目未验证完整流程 |

这里讨论的是 Windows 游戏。上游某项 Linux ROCm 或其他设备支持，不能直接作为本教程已经支持 Windows AMD／Intel GPU 的证据。也不能只把 `cuda` 改成一个未经后端支持的设备字符串。

GPT-SoVITS 上游 Windows 安装脚本列出的设备选项原文为 `CU126|CU128|CPU`，说明 CPU 安装路径存在；但玩家使用的整合包仍须支持所选声线与依赖。CPU 推理要同时核对 `device: cpu` 和 `is_half: false`，不要保留 NVIDIA 半精度配置。

Fun-ASR 上游提供 CPU 示例，但其中原生 Transformers／GGUF 路线与本项目使用的 `funasr.AutoModel` 接口不同，不能只换模型目录就直接接入。当前接口下的 CPU 试验步骤见[语音设置 B5](VOICE_SETUP.zh-CN.md#b5-需要让-fun-asr-使用-cpu-时)。

上游依据：[GPT-SoVITS Windows 安装脚本](https://github.com/RVC-Boss/GPT-SoVITS/blob/main/install.ps1)、[Fun-ASR 官方说明](https://github.com/QwenAudio/Fun-ASR/blob/main/README_zh.md)、[PyTorch 安装选择器](https://pytorch.org/get-started/locally/)。

## 5. 优先尝试哪些降占用方法

以下是排查顺序，尚未承诺在每台电脑上能节省多少显存：

1. **先确认两个 Python 的身份。** 在任务管理器“详细信息”页加入“命令行”列，或在 PowerShell 运行下面的只读命令。重启后 PID 会改变，按实际路径和脚本判断：

   ```powershell
   Get-CimInstance Win32_Process |
     Where-Object { $_.Name -match '^python(w)?\.exe$' } |
     Select-Object ProcessId, ParentProcessId, ExecutablePath, CommandLine |
     Format-List
   ```

   `api_v2.py` 通常是 GPT-SoVITS API，`satone_funasr_server_v1.py` 是随包 ASR，`embedding_worker.py` 是检索；其他脚本需继续核对，不能仅按占用大小猜测。

2. **关闭重复加载模型的服务。** 用 API 给游戏合成语音时，不需要保留另一份已加载声线的 WebUI 推理实例。不使用麦克风时，可关闭持续通话，并禁用 ASR 自动启动、正常停止对应 ASR 服务。只关闭持续通话按钮不等于模型进程已经退出。
3. **优先测试 ASR 使用 CPU、TTS 保留 GPU。** 这样可以减少 ASR 模型的 GPU 占用，但会增加 CPU／内存负担和识别等待时间；先测试 F8 短句，再测试持续通话和较长音频。若无法在现有超时内完成，不能宣称方案可用。
4. **核对 TTS 精度与实际模型。** 在该模型和显卡支持的前提下，半精度通常有助于降低占用；CPU 路线不要强制半精度。更换较轻的兼容声线／模型版本需要重新验证声音和性能，不能把不兼容权重混用。
5. **按阶段记录整卡峰值。** 分别测桌面空闲、仅游戏、加入 TTS、加入 ASR，以及连续数轮识别／合成后的峰值。使用同一分辨率、模型和音频样本，保留版本与设备配置；同时记录从说完到识别结束、从回答到声音开始的延迟。

模型卸载、低精度识别、GGUF 后端和其他 GPU 后端可以继续评估，但本次没有实现这些功能。PyTorch 的 `empty_cache()` 只能释放未使用的缓存，不能清掉仍被模型引用的权重；官方原文是“doesn't increase the amount of GPU memory available for PyTorch”。

依据：[PyTorch empty_cache](https://docs.pytorch.org/docs/stable/generated/torch.cuda.memory.empty_cache.html)。
