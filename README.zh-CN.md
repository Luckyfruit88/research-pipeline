# Research Pipeline · 计算研究实施与验证

[English](README.md) | [简体中文](README.zh-CN.md)

**用于计算研究设计、实施和验证的 Codex skill。**

这个技能帮助你从现有数据和研究问题出发，完整完成一个可审查的阶段。它分别判断工程进展、科学证据和执行授权。某个验证标签不足，可以限制相应科学结论，同时继续完成不依赖它的已授权开发。

## 适用任务

- 根据已有资源确定可检验的问题、测量终点和可行性。
- 设计明确分析单位、标准化与汇总顺序、依赖关系、泄漏控制和不确定性的对照。
- 搭建或修复研究 pipeline，保留原生工具语义及失败记录。
- 验证真实运行、共享计算资源预算、恢复能力、产物和最终回执。
- 恢复长期任务，正确处理阶段变更、旧限制和未解决问题。

方法采用工程控制论的思路：观测现状，明确目标与约束，执行，测量反馈，纠偏。它是一套定性的设计方法，不代表已经完成数学稳定性或最优性证明。

## 使用示例

~~~text
用 $research-pipeline 根据现有数据设计研究。
明确可测量终点、替代解释和可行性检查。
~~~

~~~text
用 $research-pipeline 完整实施已批准的缺失输出预测阶段。
分别报告软件能力和生物学验证状态。
~~~

~~~text
用 $research-pipeline 检查中断的批次。
恢复有效产物，对完整目标清单核账，并验证修复结果。
~~~

范围明确的研究问题只检查相关输入，复用仍有效的检查，达到本轮交付条件后停止。

独立事实查询、翻译或纯文字润色通常不触发。它可配合已有领域、统计、NGS、规格设计和写作技能使用，不依赖安装某个大套件。

## 安装到 Codex

安装脚本需要 Python 3.10+ 和 Git。技能本身不依赖 Python 运行环境、服务、付费 API 或特定模型。

~~~bash
git clone https://github.com/Luckyfruit88/research-pipeline.git
cd research-pipeline
python3 scripts/install.py
~~~

脚本将运行所需文件复制到用户技能目录，通常为 ~/.agents/skills/research-pipeline。已有不同内容会被保留；更新需要显式添加 --replace，并生成备份。

设为后续研究设计和研究 pipeline 任务的默认工作流：

~~~bash
python3 scripts/install.py --set-default
~~~

这会在个人 Codex AGENTS.md 中添加一段带标记、可移除的默认指令，保留原有正文，不修改模型、服务商、凭证或审批配置。实际工作范围仍由当前用户和项目要求决定。agents/openai.yaml 已开启自动匹配；已经打开的任务可能需要重新载入上下文。

使用 --remove-default 可仅移除这段默认指令，保留技能和备份。更新过程中若进程被强制杀死或机器断电，可能需要从保留的 research-pipeline.backup-* 目录恢复；安装脚本不声称提供跨文件的断电事务保证。

自定义位置：

~~~bash
python3 scripts/install.py --skill-home /path/to/skills --agents-file /path/to/AGENTS.md --set-default
~~~

手动安装时，将 SKILL.md、agents/、references/ 和 templates/ 一起复制到已配置技能目录下的 research-pipeline 文件夹。位置以宿主当前的[技能文档](https://learn.chatgpt.com/docs/build-skills)为准。

## “验证通过”的含义

技能会要求代理使用真实证据和项目的可执行检查。它本身不是权限沙箱、工作流引擎或科学认证系统。

- 软件测试通过，不代表生物学或因果结论成立。
- 哈希一致，不证明数据真实性或独立性。
- 多个模型意见一致，不替代独立证据。
- 方案已写、作业已提交和运行已验收，是不同状态。

优先复用已有 schema 和回执，只为重要的新失败模式添加确定性检查，避免维护重复台账。

## 验证与开发

~~~bash
python3 scripts/check_package.py
python3 -m unittest discover -s tests -v
~~~

包检查覆盖内部链接、运行文件与元数据。安装测试仅使用临时目录。[行为测试](evals/README.md)采用虚构数据，不连接真实集群。本次补丁的范围与限制见 [0.1.1 评估记录](evals/results/v0.1.1.md)；原先独立前向测试仍记于 [0.1.0 评估记录](evals/results/v0.1.0.md)，不混合两者的验证范围。

修改后保持主入口简洁，将条件性细节放入 references，并重跑相关行为用例。通过几个回归用例不能证明模型在所有研究任务中可靠。

## 文件说明

| 路径 | 用途 |
|---|---|
| SKILL.md | 主指令和触发范围 |
| references/ | 设计、证据、执行及恢复指南 |
| templates/ | 可选阶段记录 |
| agents/openai.yaml | Codex 元数据与自动调用策略 |
| scripts/install.py | 本地安装及可选默认指令 |
| evals/ | 虚构行为用例及评估记录 |

## 设计依据与许可

指令提炼自计算研究和 pipeline 工程中的重复需求。公开示例均为虚构材料，包内不包含私有项目日志、未发表研究记录、凭证或机构专用路径。

概念参考包括 [Claude Scholar 的研究契约](https://github.com/Galaxy-Dawn/claude-scholar/blob/codex/skills/research-ideation/references/research-contract.md)、[OpenSpec](https://github.com/Fission-AI/OpenSpec)、[W3C PROV-DM](https://www.w3.org/TR/prov-dm/) 和 [Agent Skills 规范](https://agentskills.io/specification)，未打包上游实现。

采用 [MIT License](LICENSE)。
