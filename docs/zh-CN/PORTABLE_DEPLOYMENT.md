[简体中文](PORTABLE_DEPLOYMENT.md) | [English](../en/PORTABLE_DEPLOYMENT.md) | [日本語](../ja/PORTABLE_DEPLOYMENT.md)

# SPP 迁移部署

[安装](INSTALL.md) · [升级](UPGRADE.md) · [数据备份](DATA_AND_PRIVACY.md)

本页以当前 5.10.8 为准，替换包内过时的 CP14/CP23 混合说明。推荐短路径，例如 `D:\LofiMOD\SatonePromptProxy`，外部环境放在相邻的 `FunASR-Runtime`、`Fun-ASR-Nano-2512`、`GPT-SoVITS`。整包包含默认人格 `SatonePersona_v4.6.txt`；遗漏人格会导致首次启动 `/persona` 不可用，不能只复制 EXE。

## 首次启动与路径

已存在 `config.json` 时使用个人配置；否则从 `config.example.json` 生成。两者都缺失或 JSON 损坏时会明确报错。历史 5.8.23 曾把旧默认整理阈值 24000 备份后迁至 32000；这不表示升级时应该覆盖所有自定义字段。

ASR 路径解析优先使用有效的显式配置，服务脚本其次可用包内 `satone_funasr_server_v1.py`，再参考有效的 `runtime_paths.json` 与标准目录发现。标准布局可为 `AI/FunASR-Runtime`、`AI/Fun-ASR-Nano-2512` 或不带 `AI` 的同名相邻目录。过期机器路径会重新发现；缓存不是记忆。为避免机器差异，首次安装建议按教程明确填写 Python、脚本和模型路径。

`http://127.0.0.1:11435/asr/status` 显示解析后的路径及 `path_source`（manual/cached/discovered/mixed）。CPU 必须指向加了 `device="cpu"` 的当前脚本副本。9881 已有服务时可能继续使用旧服务，改配置前先确认并停止旧实例。

## 参考音频与搬家

保持包内 `mayuri-voice/refs/MAY_1158_Neutral.wav` 相对布局。SPP 可查找自身目录及上一级的参考目录，独立存放时设置真实 `emotion_tts.ref_root`。旧配置指向失效外部路径时应清空或修正。在 `/tts/status` 核对实际路径与验证；其他情绪音频仍需自行补充。

迁移必须保存整个 SPP 个人运行目录：权威 `local_v1`、所有档案、旧 JSON/数据库、关系、记忆、凭据、人格和统计，不能只照旧版文件短表复制。原作进度与 `.prev` 恢复副本也保留，新电脑仍须重新验证 Steam 身份。游戏端配置和历史另备份。`runtime_paths.json` 可重建，但 `local_v1` 不能当缓存删除。

复制或重装语音环境、权重、参考音频和可选 ONNX 模型；Python 虚拟环境未必可以直接跨电脑复制。旧 Python embedding 模型仅为回退保留，现行关键词/ONNX 不使用它。新版本放新目录，通过旧记忆继承导入；验证后再调整长期使用路径，避免在导入前覆盖旧数据。

## 故障与热词

可选 TTS/ASR/ONNX 不可用时，状态页报告对应错误，已配置文字不应因此依赖这些组件。无效核心配置、非 loopback 监听地址、无法安全初始化的核心状态或端口占用仍可能阻止 SPP 启动。

热词检查包括 `hotwords_version=1`、`hotwords_count>0`、`hotwords_backend_supported=true` 与实际脚本路径；只有词库文件不等于模型采用了热词。`asr.language=auto` 可发送中日词，强制语言按配置选择。热词不保证准确率，仍需 F8 实际识别。参考游戏 ASR 日志与 SPP 日志，详见[语音排错](VOICE_SETUP.md#asr-troubleshooting)。
