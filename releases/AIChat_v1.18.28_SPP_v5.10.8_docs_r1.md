# AIChat 1.18.28 + SPP 5.10.8 · N15 · Trilingual docs r1

## [简体中文](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/main/docs/zh-CN/README.md) · [English](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/main/docs/en/README.md) · [日本語](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/main/docs/ja/README.md)

**2026-10-06 文档修订 / Documentation revision / 文書改訂**

[下载 / Download / ダウンロード: trilingual program ZIP](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.18.28_SPP-v5.10.8-docs-r1/SatoneMod_AIChat_1.18.28_SPP_5.10.8_Windows_x64_docs_r1.zip) · [SHA-256](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.18.28_SPP-v5.10.8-docs-r1/SatoneMod_AIChat_1.18.28_SPP_5.10.8_Windows_x64_docs_r1.zip.sha256) · [Manifest](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/main/releases/AIChat_v1.18.28_SPP_v5.10.8_docs_r1.json)

中文：正文按语言分目录，安装包根目录和 AIChat/SPP 各自都有三语 README 入口，包含可离线阅读的指南。本次只修改文档，原 N15 程序、脚本、配置、人格和参考录音逐字节保留，不需要为文档重装。原 ZIP 和原 SHA-256 附件保留。完整本地语音需额外 CPU、RAM 和数 GB 显存；8 GB 是评估起点，12 GB 以上更有余量，并非验证过的最低配置。大档冷启动和掉帧问题仍有未解决部分，见[硬件说明](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/main/docs/zh-CN/HARDWARE.md)。

English: Guides are organized by language. The package root and AIChat/SPP folders each have a trilingual README entrance, with offline documentation. This revision changes documentation only; the original N15 programs, scripts, configuration, persona and reference audio remain byte-identical. Existing users need not reinstall for these guides. The original ZIP and checksum remain available. Full local voice adds CPU/RAM demand and several GB of VRAM; 8 GB is an evaluation starting point and 12 GB+ gives headroom, not a validated minimum. Large-history startup and frame-rate issues remain partly unresolved; see [hardware limits](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/main/docs/en/HARDWARE.md).

日本語：本文を言語別に整理し、パッケージのルートと AIChat/SPP 各フォルダーに三言語 README を設け、オフライン説明を同梱しました。文書だけの改訂で、元 N15 のプログラム、スクリプト、設定、人格、参考音声はバイト一致します。説明のための再導入は不要で、元 ZIP とチェックサムも保持します。ローカル音声一式には追加の CPU・RAM と数 GB の VRAM が必要です。8 GB は検討開始点、12 GB 以上は余裕の目安で、検証済み最低要件ではありません。大規模履歴の起動とフレーム低下には未解決の部分があり、[ハードウェア説明](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/main/docs/ja/HARDWARE.md)を確認してください。

### N15 runtime fix / 程序修复 / 実行版の修正

中文：2026-10-05 的 N15 修复 Relaxed 端杯残留，将动画池与默认 `StablePoseOverrides` 从 `256,751,753,755,52` 改为 `752,50,51`。旧配置必须按[升级指南](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/main/docs/zh-CN/UPGRADE.md)刷新。独立审查通过；六套件为 900/16/262/39/95/196；两次 net472 重建逐字节一致；封存 attempt-19。实机证据覆盖白名单两轮 id:50/id:752，无端杯残留；标准池此前只做静态审查。本次文档工作不增加实机验收声明。

English: N15 (2026-10-05) removes cup/tea actions `256,751,753,755,52` from Relaxed and its default whitelist, using prop-free `752,50,51`. Existing users must [refresh configuration](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/main/docs/en/UPGRADE.md). Independent review approved it; six suites recorded 900/16/262/39/95/196, two net472 rebuilds matched, and the seal was attempt-19. In-game evidence covers two whitelist turns (id:50/id:752), without residual cups; the standard pool had static review only. This documentation work adds no new in-game acceptance claim.

日本語：2026-10-05 の N15 は Relaxed と標準ホワイトリストからコップ動作 `256,751,753,755,52` を外し、`752,50,51` に統一しました。既存ユーザーは[設定更新](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/main/docs/ja/UPGRADE.md)が必要です。独立審査承認、6 スイート 900/16/262/39/95/196、net472 の 2 回構築が一致し、封存は attempt-19 です。実機証拠はホワイトリスト 2 回（id:50/id:752）で残留なし、標準プールは静的確認のみです。今回の文書更新で新たな実機合格を主張しません。

Runtime DLL SHA-256: `78c418ce77e13edec1826452b1649ebe4caf1cb941fd4277a4ffc16d6c8c0f44`

Runtime PDB SHA-256: `9ed7977780dbfb3f70fd8055fa86741a1fb8777e78d1bd1342814786c50203b4`

[N15 original manifest](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/main/releases/AIChat_v1.18.28_SPP_v5.10.8.json) · [Original archive](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.18.28_SPP-v5.10.8/SatoneMod_AIChat_1.18.28_SPP_5.10.8_Windows_x64.zip)
