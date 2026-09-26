# AIChat 1.16.14 + SatonePromptProxy 5.8.23

这是两份最新正式插件包的统一分发版本，原 ZIP 未修改、未重新编译。安装包 SHA256 与各自源仓库的正式 Release 完全一致。

## 普通玩家下载

| 文件 | 怎么使用 |
|---|---|
| [AIChat_v1.16.14.zip](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.16.14_SPP-v5.8.23/AIChat_v1.16.14.zip) | 解压，把 `AIChat.dll` 放到游戏的 `BepInEx/plugins` 文件夹 |
| [SatonePromptProxy_v5.8.23.zip](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.16.14_SPP-v5.8.23/SatonePromptProxy_v5.8.23.zip) | 全部解压到固定目录，例如 `D:\LofiMOD\SatonePromptProxy`；运行 `SatonePromptProxy.exe` |
| 两个 `_SHA256.txt` | 与对应 ZIP 的 SHA256 比较；无需放进游戏 |
| `AIChat_LICENSE.txt` | AIChat 原 MIT 许可证与作者署名，随文件保留 |
| `AIChat_v1.16.14_SPP_v5.8.23.json` | 版本、来源、文件清单和校验记录；无需安装 |

第一次安装先阅读[完整使用方法](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/main/docs/INSTALL.zh-CN.md)。还需要安装 BepInEx、配置自己的 API Key；语音和麦克风需要额外程序、模型及参考音频，见[下载清单](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/main/docs/DOWNLOADS.zh-CN.md)和[语音设置](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/main/docs/VOICE_SETUP.zh-CN.md)。不要把 `Source code (zip)` 当成安装包，也不需要 Git。

## 版本与更新

- AIChat 1.16.14：源提交 `aeaa1b33598d68ead0b3d1353b3793e5df399cc2`。
- SPP 5.8.23：源提交 `916c61a71973f825266be7140d84c45afbd6bcaa`，配对 AIChat 1.16.14。
- AIChat 包内 `BUILD_INFO.json` 仍记录其构建时的 SPP 5.8.22；本次 SPP 5.8.23 继续配对同一份 AIChat，原包没有改写。
- SPP 5.8.23 调整记忆整理阈值：API 总输入 token 达到 32,000 时安排整理，粗估保留最近约 12,000 token；游戏内长对话验收仍待补齐。
- 更新前退出游戏与服务并备份个人数据。AIChat 替换唯一 DLL；SPP 保留自己的配置、人格、记忆、关系和音频。详见安装页末尾的更新说明。

## 校验与数据

```text
65684dac51fdae292d0e4676dc1a458396c5bb01a63e15472537f5c5b8143cf1  AIChat_v1.16.14.zip
bcad7805fa8193b8efd9a14e82ef8be16b65d9d9f6c86fad674719cc17150c6e  SatonePromptProxy_v5.8.23.zip
```

已核对实际 ZIP 文件清单，没有发现个人 CFG、运行用 config.json、runtime_paths.json、聊天 history、memory_profiles 或日志文件；保留包内官方模板和说明。哈希与文件清单检查不等于完整二进制安全审计。

更新 DLL 后仍显示旧 Key 或聊天记录，是读取本机独立保存的配置和历史；详见[本地数据与隐私](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/main/docs/DATA_AND_PRIVACY.zh-CN.md)。

本次发布时仓库仍为 Private，下载者需要本发布库的访问权限。将本发布库设为 Public 后，这里的安装包不依赖两个源码仓库的访问权限。本文未宣称已完成干净 Windows 全流程安装实测。
