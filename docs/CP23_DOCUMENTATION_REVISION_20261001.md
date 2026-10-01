# CP23 包内说明正文修订完成（2026-10-01）

用户反馈AIChat包根README.md、版本与改动.md原来只有标题与链接。已补成可独立阅读的正文，并同步SPP根说明和两私库组件包。首次安装、真实设置按钮、功能、F9/F8/Enter、四阶段选装、实际本版改动、升级保留与排错已齐全。

## 当前入口

- [公开文档修订1（Latest）](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/tag/AIChat-v1.17.0_SPP-v5.9.0-docs-r1)：8附件。
- [SPP私库原版本Release](https://github.com/Scaleph-Enkidu/SatonePromptProxy/releases/tag/SPP-v5.9.0)：10附件，推荐SatonePromptProxy_v5.9.0_docs_r2.zip。
- [AIChat私库原版本Release](https://github.com/Scaleph-Enkidu/SatoneAIChat_Remake/releases/tag/AIChat-v1.17.0)：10附件，推荐AIChat_v1.17.0_docs_r2.zip。
- [AIChat README完整正文](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.17.0_SPP-v5.9.0-docs-r1/AIChat_README_zh-CN.md) / [AIChat版本与改动完整正文](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/download/AIChat-v1.17.0_SPP-v5.9.0-docs-r1/AIChat_CHANGELOG_zh-CN.md)，已安装用户可以只保存文档，无需更新程序或模型。

## 固定代码与字节

程序版本仍1.17.0/5.9.0，运行代码和全部非Markdown/非BUILD_INFO文件保持原受测字节。公开45个、SPP42个、AIChat3个运行及支持文件逐项恒等。EXE `a05d6cdbd157152165a45b13046f95118d568f09bf1d6ea2a19c3761d56c421c`，DLL `963d8b74ceaa9b54947f44b26cf624cdfe1f3d88d7ec4fee08d85137a5803050`。

原运行源码：SPP `5232d58882668fc1cf446db923fc8822fec2a810` / AIChat `c5da60b686766189c30ed7d69b71dab41098f6d2`；Go/.NET/推理/大WAL/实机结果只引用其原受测范围，没有在文档HEAD重新跑。模型整个ZIP恒等，SHA `88c77b40c89df19e316aebf497ff30fc4d5504138955ba92e0f2d4875b639d8d`。

| 当前程序ZIP | 字节数 | SHA-256 |
|---|---:|---|
| SatoneMod_AIChat_1.17.0_SPP_5.9.0_Windows_x64_docs_r1.zip | 10883404 | `8f6e5d41d77994b67f2d0946866fb223b248fae3841db7e881a3509e189b016f` |
| SatonePromptProxy_v5.9.0_docs_r2.zip | 10186140 | `ce59ac6bdefefa52bdb65c6a183a6e4a9a2a8042d30eca43454a4a8237a26040` |
| AIChat_v1.17.0_docs_r2.zip | 645148 | `06373067f09b1ad1991ecafa50f96b665f535ca64faa2c3aa0fe2be3fabc444d` |

## 两轮本地检查与发布操作

自审及只读复审：修正先完成旧记忆选择再等待连接启用的顺序、F8设置入口误导、独立MD附件README链接。第一次封包预检也保留，未当正式CI。

第一轮54项发布工具测试、原/R1清单、旧schema1、工作流均通过；综合FAIL来自文档核对脚本误要求私库独有安装说明.md也在配对包中。修正共用文件恒等、私库独有旧文件保留的核对范围，未改变程序或受测R1 ZIP。

第二轮13组检查／54项工具测试PASS；正文行数与字节、相对路径和四阶段锚点、CRC/member/filehash、禁入玩家资料、历史清单兼容、完整资产集合与manual-only工作流均通过。未运行第三轮代码CI或远端CI。第二轮固定候选：
- public: `ad7c22d6ceba5da332efc2fff77b4685d1390dff`
- SPP: `b64370587e6228161a080df38c205a2749aab09e`
- AIChat: `80b23423b875e43839bbfd8a67dad964c0bd9182`

随后发布操作发现公开原Release不可变，GitHub追加返回HTTP422；这不是自动审批拒绝。两私库R1追加已成功，保留其全部资产。公开采用独立文档修订Tag，修正公开下载目标；私库再追加R2以同步链接，不覆盖R1或原版。所有后续改动限文档链接、工作流默认目标和BUILD_INFO/manifest身份，不修改受测校验器实现或运行代码。使用第二轮通过的工具对当前传输清单和字节核验，不重复全代码CI。

公开草稿最后发现BUILD_INFO.release_tag残留旧值，正式发布前修正并保留三份草稿旧字节证据；仅在草稿期替换ZIP/sha/JSON，最终公开Tag固定 `b62a32b47f60555f2de47fba9fd07f031913b426`。旧正式Tag固定SPP `012285c468509966d8b15893006e15b07a28f998`、AIChat `34202000b8aa9d83ded6abfcf03426420dd06d43`、旧public `08481af11c838f5d05067a64f2c580fc17d0c1cf`，均未移动。

公开新8+私库10+10共28附件下载逐字节回查PASS；原公开8附件另行下载恒等，私库原版与R1全部7附件保留。新公开页复用同一模型ZIP字节，原模型地址仍有效；没有发布新模型版本、把模型并入主程序或改默认启用。三处当前Release均正式、非预发布且Latest核对通过。

私库R2 manifest的package_directory沿用历史源目录提示，paired_release_tag指原运行配对；私库实际校验始终要求显式--assets-dir，新公开文档发布目标见publication_adjustment.public_release_tag。安装不使用这两个历史字段。

证据：原两轮 `D:/SatoneDev/deliverables/CP23-Docs-R1-20261001/Evidence/local-ci-round1` 和`local-ci-round2`；发布适配、HTTP422前状态、草稿身份修正、远端下载与回执 `D:/SatoneDev/deliverables/CP23-Docs-R1-Publication-20261001/Evidence`。程序文件未重编；495秒冷启动／944MB整管线限制不变，350MB作用域不扩大。

## 下一阶段与建议

当前阶段完成，门禁通过。下一步为玩家阅读新正文并在出现实际问题时提供复现，不自动开始功能开发。进入条件：本步骤两轮门禁和发布字节回查通过，现已满足。新增文档步骤建议复杂度中，原CP23 D中高建议保留；本任务沿用用户6.1-Sol/极高。后续开发范围另定后再给档位建议，不自动更换模型。
