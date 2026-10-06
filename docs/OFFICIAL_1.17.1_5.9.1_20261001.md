# 正式合并发布：AIChat 1.17.1 / SPP 5.9.1（2026-10-01）

## 正式发布完成（2026-10-01）

AIChat 1.17.1 + SPP 5.9.1 已正式发布，三处均确认非草稿、非预发布与 Latest；全部 30 个附件下载逐字节及 manifest 验证通过。代码/包受测结果、两轮失败和用户授权的第 3 轮文档门禁在下方保留，未补跑远端 CI。

- [公开配对版](https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/releases/tag/AIChat-v1.17.1_SPP-v5.9.1)（13 附件）
- [AIChat 私库](https://github.com/Scaleph-Enkidu/SatoneAIChat_Remake/releases/tag/AIChat-v1.17.1)（9 附件）
- [SPP 私库](https://github.com/Scaleph-Enkidu/SatonePromptProxy/releases/tag/SPP-v5.9.1)（8 附件）
- [安装教程](zh-CN/INSTALL.md) · [准确发布回执](AIChat_1.17.1_SPP_5.9.1_PUBLICATION_20261001.json)

标签提交：AIChat `4c7387d43e26a1112135a939122ea86b71ba634a` / SPP `11ceaa5b84ec92a42e48ac80b0cc9ae28c9c06b1` / public `0d20f387c1799c69b5719f0fdde4974e5f6dff91`。运行受测/构建 SHA 仍是 AIChat `32a0aa7a4ea98664c700e1bb7d0919acca77a5f6` / SPP `4ff7e3a27afd2ac0879ae8c6db695b3b5e44009a`；发布后的收尾只改文档，已发布标签、30 附件及安装 ZIP 均保持原样。

当前阶段：正式合并、构建、验证与三仓发布完成；自审完成；本地 CI 第 1 轮失败、第 2 轮代码/包通过但最后文档门禁失败，冻结后用户明确授权第 3 轮文档/清单验证通过；门禁通过。真实 Unity 画面与玩家环境的安装反馈单独记录，未假称已覆盖全部场景。

下一阶段：正式版安装与实机反馈；进入条件（本地门禁、草稿下载回查、三处正式状态）已满足。阶段原新增建议按本档案 2026-10-01 版本沿用 6.1-Sol / 极高，复杂度/风险没有扩大到新增运行功能；建议模型 gpt-6.1-sol、推理 xhigh，保持合并来源与问题复现上下文，最终按用户设置执行。大 WAL 冷启动或掉帧优化需另定开发范围，本次未修复其根因。

以下准备与本地检查记录为当时状态：

---


授权：用户要求找到其他 Codex 对话完成的四个 BAT 与最新安装教程，与本对话 UI/同步/标题修改一起打包，正式上传两个私库和发布库。该授权允许本次统一 Git 推送与三处正式 Release，覆盖其他对话此前合并前暂缓上传的停点；保留所有原版本资产与标签。

合并来源：SPP 四 BAT 来自 09485720 / 6b2dd19e 及对应已验证补丁，教程来自三仓最新 INSTALL（SPP 07063f66 / AIChat 9b43f63c / public 80f3dfcd）；AIChat 最新标题候选 58569c38，布局完整受测 3b0d4694。远端 main 只多一份相同教程提交，安全合并保留双方历史。

完成条件：稳定版本标识、三仓教程与包内 README/版本改动正确；重新构建 EXE/DLL；本地 Go/客户端测试、已编译元数据/标题、四 BAT 字节/CRLF与实际 cmd 隔离验收、ZIP/hash/无玩家资料/资料保留通过；三份程序包和独立模型附件有固定 manifest。先上传草稿，下载每个附件逐字节回查后再转为正式、非预发布、Latest；源码与 manifest 同步到三个仓库。

本检查点适用最多两轮本地 CI，保存全部结果和失败；第一轮失败自修，第二轮仍失败按既有工作流暂停交接。前任务历史结果不重置或冒称当前实机通过。只运行本地 CI；新推送 tip 使用 [skip ci]，不触发远端流程。公开/私库发布校验工具继续复用已验证实现。

程序与语义模型独立分发，原模型 ZIP 字节复用，不发布新模型版本。所有测试服务在隔离目录/临时端口运行，只停止本次创建的进程；不调用真实收费模型、不改变玩家存档。大 WAL 冷启动和掉帧根因未修复，正式说明保留限制。

阶段原新增建议：沿用当前 6.1-Sol / 极高，合并与三仓发布复杂度中高；同一设置便于保持来源与验证范围。下一阶段是正式版本下载/安装与玩家实机反馈，进入条件为本地门禁、草稿附件回查与三处正式状态确认。


## 本地门禁完成，待草稿附件回查

实际代码受测/构建候选：AIChat `32a0aa7a4ea98664c700e1bb7d0919acca77a5f6` / SPP `4ff7e3a27afd2ac0879ae8c6db695b3b5e44009a`。后续版本说明相对链接和发布 manifest 属文档变化，生产代码字节未变，未把新文档 HEAD 冒称成新代码套件受测 SHA。

第 1 轮：AIChat 11/12、SPP 5/6、公开校验器 1/1；两项失败来自 Windows PowerShell 5.1 读取无 BOM 中文验证脚本和 Windows Python Store 执行别名。其余 6 套客户端测试、Release DLL/EXE、3 项资源/设置检查、Go 格式/vet、54 项发布工具测试及 3 项 BAT 打包测试通过。第一轮完整日志与结果保留。

第 2 轮：验证脚本写 UTF-8 BOM，测试进程 PATH 选随附真实 Python；实际编译标题/BepInEx 数值版本通过，Go 全量 519 顶层 / 1028 带子项 PASS，8 项需独立环境的用例 SKIP（含真实云 API），没有失败。生产源码不变；同候选的第一轮通过项目引用原日志，无第三轮代码 CI。第二轮准备时辅助模块路径拼写导致任何包检查开始前导入阻塞，依工作流允许的可恢复工具准备处理；原 stderr 与 SETUP_CORRECTION.md 保留，没有覆盖失败或重跑生产套件。

第二轮新增正式包检查通过：四 ZIP 哈希/CRC/成员/许可/无玩家资料，教程完整正文及本地链接、四 BAT 源哈希/ASCII/CRLF、三程序包相同受测运行字节；中文空格路径实际解压保留六个合成玩家文件；四 BAT 实际 cmd 共 15 分支；新 5.9.1 EXE 在空 PATH 的原生关键词/ONNX 实际安装共 11 分支，覆盖缓存重启、缺坏模型回退、独立模型安装、运行中禁改启用配置及程序覆盖保留 17 文件。未调用真实收费 API，未执行 Unity 画面或真实语音推理。

DLL SHA-256：`aeef8764eb301291ecb6d49487e643bd06ac5fb1f4e415647c5f9e54ac6e08eb`；EXE：`837f0d2c3d2925ce27bdb28f3e8620f8dffb56c936498a723491b591d9dd9efe`。模型 ZIP 复用原 `88c77b40c89df19e316aebf497ff30fc4d5504138955ba92e0f2d4875b639d8d`。

本地交付：`D:/SatoneDev/deliverables/AIChat-1.17.1-SPP-5.9.1-Official-20261001`。原始日志在 `Evidence/round1` / `Evidence/round2`，准确 JSON 为 `Evidence/LOCAL_VERIFICATION.json`；各正式 Release 均附同一 `LOCAL_VERIFICATION.json`。公开配对 / 模型与两个自身程序分别使用新 schema 2 manifest，上传草稿后再下载全部附件逐字节回查，确认正式状态才记录发布完成。所有旧 tag/Release/附件保留。


## 用户授权追加文档 / 清单门禁

第二轮最后的源码文档检查误把两条 UI partial class 字面量都限定在 AIMod.cs，实际位置分别为 `AIChat/Satone/SatoneChatAppearance.cs:77` 与 `AIChat/Satone/SatoneConversation.cs:788`。按两轮规则冻结后，用户明确回复「允许修正校验并继续正式发布」。第 3 轮只修正验证工具定位并追加文档 / 完整 manifest 验证，不修改或重编生产代码、不重跑代码套件，四份 ZIP 字节保持第二轮原值。原检查器、stderr 和冻结报告位于 Evidence/round2；授权与追加结果位于 Evidence/round3。正式发布仍须草稿附件逐字节回查。


追加第 3 轮完成：修正后的文档定位/本地链接/实际 UI 字面量与三仓运行源码一致性通过；三个最终 manifest 全部附件/成员/哈希/许可/程序身份通过。用户授权范围内四份 ZIP 未变，代码套件沿用准确原 SHA；未运行第三轮全代码测试或远端 CI。下一步按授权上传草稿并逐字节下载回查。
