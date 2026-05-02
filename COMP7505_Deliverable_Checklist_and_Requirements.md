# COMP7505 Group Project 交付清单与当前报告符合度评价

评价对象：

- 项目说明：`../COMP7505 Group Project Description.pdf`
- 当前报告：`COMP7505_Group_Project_Report.docx`
- 当前产品方向：`InterviewAI — Your AI Interview Prep Coach`
- 当前赛道：`Track A: Smart Adaptive Interfaces`

评价结论：当前报告对 `D1-D4` 和 `Track A` 要求覆盖较完整，整体约 `87%` 符合课程项目说明。已根据 `docs/D2_Interaction_Design_and_Prototype/Deliverable2_Interaction_Design_and_Interactive_Prototype.md` 补强报告 D2：增加 D1-to-D2 traceability、原型提交说明、Track A 能力边界细化，以及 D2 对评分标准的证据映射。Roadshow PPT 附件已存在于 `slides/InterviewAI_Pitch_Deck.pptx`，应作为最终提交包中的独立附件提交；当前主要缺口变为报告正文中 `Deliverable 5` 尚未引用该 PPT，也未补充 Demo Script、Core Value Proposition 和提交包说明。

## 1. 必交材料总览

| 序号 | 必交组件 | PDF 原文参考 | 当前报告符合度 | 评价 |
|---|---|---|---:|---|
| D1 | User Requirement & Project Definition | “all teams must submit the following five core deliverable components”; “Target User Personas”; “Core User Tasks”; “Project Scope & Boundaries” | `90%` | 已有 persona、痛点、核心任务、成功标准、范围边界，结构清晰。 |
| D2 | Interaction Design Solution & Interactive Prototype | “Interaction Design Specification”; “Full Workflow of Core Tasks”; “Interactive Prototype ... fully covers the entire core task workflow” | `95%` | 已补强 D1-to-D2 追踪关系、原型提交说明、导航反馈、Track A 能力边界和评分证据映射；D2 已基本达到完整交付水平。 |
| D3 | Design Evaluation & Iteration Optimization | “Evaluation Plan”; “Evaluation Results”; “Iteration Evidence”; “at least one full design iteration” | `92%` | 已有混合评估方法、参与者、指标、严重度分级、三轮迭代和前后对比。 |
| D4 | Design Principles & Product Development Roadmap | “no fewer than 3 reusable interaction design principles”; “at least three stages” | `95%` | 已有 3 条可复用设计原则和 3 阶段路线图，符合要求。 |
| D5 | Product Roadshow Materials | “Roadshow PPT”; “Prototype Demo Script”; “Core Value Proposition” | `55%` | `slides/InterviewAI_Pitch_Deck.pptx` 已作为 PPT 附件存在，且包含 14 页；报告正文仍需要 D5 章节引用该附件，并补 Demo Script 与 Core Value Proposition。 |
| Track A | Smart Adaptive Interfaces 最低要求 | “full compliance required; zero points for the module if unmet” | `92%` | 已覆盖能力边界、用户控制、至少两类失败处理、限制沟通机制，并在报告 D2 中补充更明确的能力边界和原型证据说明。 |
| 最终提交 | Portfolio + Prototype + PPT | “submit your project portfolio (one comprehensive written report + interactive prototype) and a completed roadshow PPT by May 3rd 23:59” | `82%` | 报告 D2 已写明 `index.html, Tab 3: Prototype`，PPT 附件已在 `slides/InterviewAI_Pitch_Deck.pptx`；仍需在 D5 或提交说明中明确 Demo Script 和最终提交清单。 |

## 2. 课程原文要求摘录

### 2.1 项目核心定位

> “Students will execute the full product design workflow: User Requirement Definition → Interaction Design → Prototyping → Usability Evaluation → Iterative Optimization → Product Roadshow.”

对应要求：报告不能只展示功能点，必须呈现从用户需求、交互设计、原型、评估、迭代到路演的完整链路。

### 2.2 禁止事项

> “Simple feature stacking is strictly prohibited. All designs must be backed by clear user needs and interaction design rationales.”

对应要求：每个功能或页面都应能追溯到用户痛点、核心任务或交互设计理由。

### 2.3 五个必交组件

> “Regardless of the track selected, all teams must submit the following five core deliverable components, which form the primary basis for grading.”

必交组件：

1. `User Requirement & Project Definition`
2. `Interaction Design Solution & Interactive Prototype`
3. `Design Evaluation & Iteration Optimization`
4. `Design Principles & Product Development Roadmap`
5. `Product Roadshow Materials`

### 2.4 最终提交物与截止时间

> “You will need to submit your project portfolio (one comprehensive written report + interactive prototype) and a completed roadshow PPT by May 3rd 23:59”

最终提交包建议包含：

- `COMP7505_Group_Project_Report.docx`：综合书面报告
- `index.html` 或 Figma/Axure 链接：交互原型
- `slides/InterviewAI_Pitch_Deck.pptx`：Roadshow PPT，建议作为独立附件随报告和原型一起提交
- Demo script：可放在报告 D5、PPT 备注页，或单独文档

当前已整理到最终提交文件夹：`COMP7505_Final_Submission/`

备用在线原型地址：如果本地 HTML 无法打开，可访问 `https://ui-mocha-seven.vercel.app`

## 3. 详细交付清单与当前报告评价

### D1. User Requirement & Project Definition

PDF 原文参考：

> “Target User Personas: Define core user groups, user characteristics, and key pain points.”
>
> “Core User Tasks: Specify at least one end-to-end core user task and clear success criteria for task completion.”
>
> “Project Scope & Boundaries: Clarify key constraints ... design assumptions, and excluded requirements.”

清单：

- [x] 定义目标用户群体
- [x] 定义用户特征
- [x] 明确关键痛点
- [x] 至少一个端到端核心任务
- [x] 每个核心任务有成功标准
- [x] 明确使用场景、设备限制、技术前提
- [x] 明确设计假设
- [x] 明确排除范围

当前报告评价：`高度符合，约 90%`

已覆盖内容：

- 报告 `1.1 Target User Persona` 定义 Kevin Li，包含年龄、职业、地点、求职状态、目标和痛点。
- 报告 `1.2 Core User Tasks` 定义 `Practice` 和 `Review` 两条端到端任务，并分别给出成功标准。
- 报告 `1.3 Project Scope & Boundaries` 覆盖使用场景、设备、技术约束、设计假设和排除需求。

改进建议：

- 如果有原始问卷或访谈数据，建议在附录或图表中列出样本概况与关键问题，增强用户研究可信度。
- Persona 可以补充“环境/情境”和“一天中的使用时机”，帮助后续交互场景更扎实。

### D2. Interaction Design Solution & Interactive Prototype

PDF 原文参考：

> “Interaction Design Specification: Define the product’s interaction model, overall information architecture, and navigation structure.”
>
> “Full Workflow of Core Tasks: Deliver complete end-to-end interaction flowcharts ... corresponding to the core user tasks in Deliverable 1.”
>
> “Interactive Prototype: Develop a prototype with appropriate fidelity ... that fully covers the entire core task workflow.”

清单：

- [x] 定义交互模型
- [x] 定义整体信息架构
- [x] 定义导航结构
- [x] 对应 D1 核心任务给出完整端到端流程
- [x] 流程包含页面跳转、操作反馈、异常分支
- [x] 提供交互原型覆盖核心任务
- [x] 在报告或提交包中明确原型访问方式、文件路径、版本

当前报告评价：`高度符合，约 95%`

已覆盖内容：

- 报告 `2.1 Interaction Model` 明确 human-AI collaborative model，并强调透明度、用户控制、降级处理。
- 报告 `2.2 Information Architecture` 覆盖 Dashboard、Practice、Review、History、Settings 和异常状态。
- 报告 `2.3 Navigation Structure` 说明侧边栏与两条线性流程。
- 报告 `2.4 Core Task Workflows` 覆盖 Practice 和 Review 工作流，并提到异常分支。
- 报告已新增 `D1-to-D2 Traceability`，说明问卷/访谈、persona、核心任务与 D2 交互结构之间的对应关系。
- 报告 `2.5 Interactive Prototype` 已明确原型为 `index.html, Tab 3: Prototype`，覆盖完整 Practice、Review、History、Settings、失败弹窗和控制动作。
- 报告已新增 `2.7 Alignment with Interaction Design & Prototype Quality`，把 D2 内容映射到交互逻辑、信息架构、原型完整性和核心任务流程完整性。

缺口与风险：

- 原型访问方式已在报告 D2.5 补充，原先“老师不知道如何进入 `index.html tab 3`”的风险已降低。
- 仍需人工确认最终 `.docx` 中 D2 图片是否清晰、可读，且每张图和正文要求直接对应。
- 如果最终提交平台不支持本地 HTML 文件，仍建议提供线上静态链接或压缩包说明作为备用路径。

改进建议：

- 如有线上原型或演示视频，补充链接和备用访问方式。
- 在最终提交说明中再次列出 `Report + index.html + PPT`，避免 D2 信息与 D5/提交包脱节。

### D3. Design Evaluation & Iteration Optimization

PDF 原文参考：

> “Evaluation Plan: Adopt structured evaluation methods ... and specify the evaluation process, participants, and indicators.”
>
> “Evaluation Results: Summarize all identified usability issues by severity levels (critical / severe / moderate / minor).”
>
> “Iteration Evidence: Propose actionable optimization solutions ... provide supporting materials for at least one full design iteration.”

清单：

- [x] 有结构化评估方法
- [x] 说明评估流程
- [x] 说明参与者/评估者
- [x] 说明评估指标
- [x] 按严重度汇总问题
- [x] 针对关键问题提出可执行优化方案
- [x] 至少提供一轮完整设计迭代证据
- [x] 有 before/after 或迭代记录

当前报告评价：`高度符合，约 92%`

已覆盖内容：

- 报告 `3.1 Evaluation Plan` 使用 Heuristic Evaluation、Cognitive Walkthrough、Think-Aloud Protocol，说明参与者、任务场景、流程和指标。
- 报告 `3.2 Evaluation Results` 按 Critical、Serious、Moderate、Minor 分类列出问题、证据和响应。
- 报告 `3.3 Iteration Evidence` 给出 Question Management、Real-Time Coaching、History Comparison Studio 三项迭代，并列出 before/after 与度量变化。

改进建议：

- PDF 使用 `severe`，报告使用 `Serious`；建议统一为 `Severe/Serious` 并说明等价，避免评分时被认为分类不一致。
- 若篇幅允许，补充一张“问题 ID → 改动位置 → 原型截图”的映射表，会更像完整证据链。

### D4. Design Principles & Product Development Roadmap

PDF 原文参考：

> “Reusable Design Principles: Summarize no fewer than 3 reusable interaction design principles tailored to the track features and user profiles of the product.”
>
> “Product Development Roadmap: Create a phased product expansion plan covering at least three stages.”

清单：

- [x] 至少 3 条可复用交互设计原则
- [x] 原则贴合赛道特点
- [x] 原则贴合目标用户
- [x] 每条原则有设计案例解释
- [x] 路线图至少 3 个阶段
- [x] 每个阶段有核心目标
- [x] 覆盖场景、用户或交互形式扩展方向

当前报告评价：`高度符合，约 95%`

已覆盖内容：

- 报告 `4.1 Reusable Design Principles` 给出 `Transparency of AI Reasoning`、`User Control Over AI Outputs`、`Graceful Degradation` 三条原则。
- 每条原则都包含 Principle、Rationale、Reusable application，且与 Track A 高度相关。
- 报告 `4.2 Product Development Roadmap` 包含 Phase 1、Phase 2、Phase 3。

改进建议：

- Roadmap 表格可以补充每个阶段的主要用户、主要风险和评估指标，使“扩展方向”更具体。

### D5. Product Roadshow Materials

PDF 原文参考：

> “Roadshow PPT: Fully cover the product's core value, user pain points, solutions, interaction design highlights, evaluation and iteration process, and future plans.”
>
> “Prototype Demo Script: Prepare a step-by-step on-site demonstration workflow for core tasks to ensure a smooth presentation.”
>
> “Core Value Proposition: Define the product's differentiated highlights, all rooted in user experience and interaction design rather than simple feature addition.”

清单：

- [x] Roadshow PPT 覆盖核心价值
- [x] Roadshow PPT 覆盖用户痛点
- [x] Roadshow PPT 覆盖解决方案
- [x] Roadshow PPT 覆盖交互设计亮点
- [x] Roadshow PPT 覆盖评估与迭代
- [x] Roadshow PPT 覆盖未来计划
- [ ] Demo script 提供逐步现场演示流程
- [ ] Core value proposition 明确差异化亮点
- [~] 明确 D5 与 PPT/原型文件的对应关系

当前报告评价：`部分符合，约 55%`

已覆盖内容：

- 报告目录包含 `Deliverable 5: Product Pitch Materials`、`5.1 Pitch Deck Overview`、`5.2 Demo Script`、`5.3 Core Value Proposition`。
- PPT 附件已存在：`slides/InterviewAI_Pitch_Deck.pptx`，共 14 页，结构覆盖 Problem、Solution、Design、Track A、Evaluation、Demo、Roadmap。

主要缺口：

- 当前报告正文在 `Deliverable 4` 后结束，未看到 `Deliverable 5` 正文内容；需要在报告中明确引用 `slides/InterviewAI_Pitch_Deck.pptx`。
- 没有逐步 demo script。
- 没有单独总结 core value proposition。
- 没有在报告正文中说明 PPT 文件名、页数、路演结构或演示路径。

建议补充内容：

- 增加 `Deliverable 5: Product Pitch Materials` 正文章节。
- `5.1 Pitch Deck Overview`：引用 `slides/InterviewAI_Pitch_Deck.pptx`，说明共 14 页，并列出 PPT 结构，例如 Problem、Solution、Design、Track A、Evaluation、Demo、Roadmap。
- `5.2 Demo Script`：按 6 分钟演示流程写出每一步要点，例如 Dashboard → Practice setup → Answer coaching → Feedback → History comparison → Failure recovery。
- `5.3 Core Value Proposition`：建议写成一句主张加三点证据，例如 `InterviewAI turns generic AI interview feedback into transparent, context-aware, user-controllable coaching.`

## 4. Track A 专项最低要求

PDF 原文参考：

> “Minimum Mandatory Standards (full compliance required; zero points for the module if unmet)”

Track A 最低要求：

| Track A 要求 | PDF 原文参考 | 当前报告证据 | 符合度 |
|---|---|---|---:|
| 明确系统能力边界 | “Clearly define the system’s capability boundaries” | `2.6 Track A Compliance` 明确 Can / Cannot / Limited | `95%` |
| 全面的用户控制机制 | “manual override of AI results, secondary confirmation ... review / one-click undo” | `2.1` 和 `2.6` 提到 flag inaccurate、override scores、undo、discard、edit extracted Q&A、confirm sensitive actions | `90%` |
| 至少两类系统失败界面方案 | “Pre-design interface solutions for at least two types of system failures” | `2.6` 覆盖 voice recognition failure、AI generation error、extraction failure、invalid upload | `95%` |
| 至少一种系统限制沟通机制 | “Integrate at least one mechanism to communicate system limitations” | confidence indicators、low-confidence copy、audio-quality warning、capability-boundary banners | `90%` |
| 建议评估重点 | “User trust ... interaction transparency ... cognitive load ... error recovery ... user control protection” | `3.1` 评估目标覆盖 trust/transparency、control、cognitive load、failure handling | `90%` |

Track A 总评：`高度符合，约 92%`

建议：

- 报告 D2 已补充能力边界细化和 `Figure D2-7` 的证据说明；最终仍建议人工确认图示中是否能直接看到 limitation banner、confidence cue、failure modal 等界面证据。
- 若时间允许，可在 `Figure D2-7` caption 或图旁增加原型操作路径，让评分者更快复现 Track A 证据。

## 5. Roadshow 与投资人互评要求

PDF 原文参考：

> “Total roadshow time per team is strictly limited to maximum 8 minutes (6 minutes for presentation + 2 minutes for Q&A).”
>
> “All roadshows must include two core segments: explanation of the product’s core value and design logic, and on-site prototype demonstration of core tasks.”
>
> “Roadshow content must correspond to the mandatory deliverables; empty conceptual explanations without design rationales are prohibited.”

Roadshow 检查项：

- [ ] 6 分钟 presentation 内容已排练
- [ ] 2 分钟 Q&A 预案已准备
- [ ] 解释产品核心价值
- [ ] 解释设计逻辑
- [ ] 现场演示核心任务
- [ ] 路演内容对应 D1-D5
- [ ] 避免空泛概念，所有主张有用户需求或设计依据

投资人互评五个维度：

1. 用户痛点与产品任务设计是否匹配
2. 原型质量与交互设计依据是否充分
3. 设计评估与迭代证据是否完整
4. 方案可行性与风险管理能力
5. 基于用户体验的差异化亮点，而不是功能堆砌

当前报告对应情况：

- 痛点与任务匹配：`较强`
- 原型与交互依据：`较强`
- 评估与迭代证据：`较强`
- 风险管理：`中上`，Track A 失败处理较好，但隐私保护、可访问性可以补充
- 差异化亮点：`中上`，已有透明 AI、用户控制、上下文感知反馈，但 D5 中需要凝练成更有力的路演话术

## 6. 主评分标准对应评价

PDF 原文参考：

> “Main Grading Criteria”

| 评分模块 | PDF 评分点 | 当前报告评价 | 符合程度 |
|---|---|---|---:|
| Requirement & Project Definition | persona 准确性、痛点深度、任务和边界清晰度 | 结构完整，persona 和痛点清晰，任务成功标准明确 | `90%` |
| Interaction Design & Prototype Quality | 交互逻辑合理性、IA 清晰度、原型完整性、核心任务流程完整性 | 已根据 D2 文档补强 traceability、原型访问方式、评分证据映射，说明更完整 | `95%` |
| Design Evaluation & Iteration Optimization | 方法规范、严重度分级合理、迭代方案可行、证据完整 | 方法和证据链强，建议统一 severity 用词 | `92%` |
| Roadshow & Deliverable Completeness | 路演逻辑、原型演示效果、完整提交、差异化价值表达 | PPT 附件已存在，但报告 D5 正文仍缺 Demo Script、价值主张和提交包说明 | `65%` |
| Track-Specific Compliance | 未满足最低要求会扣分，严重时模块为零 | Track A 文字覆盖充分，能力边界与 `Figure D2-7` 证据说明已增强 | `92%` |

综合判断：

- 若只看 `COMP7505_Group_Project_Report.docx`，当前最可能被扣分的是 `D5 Roadshow Materials` 正文缺失；D2 原型访问与证据映射风险已明显降低。
- PPT 附件已在 `slides/InterviewAI_Pitch_Deck.pptx`，仍建议在报告 D5 中显式引用，避免评分者找不到附件证据。
- 当前报告已经较好避免“simple feature stacking”，因为大多数功能都能回到用户痛点、Track A 原则和评估结果。

## 7. 最终提交前优先修复清单

高优先级：

- [ ] 补齐报告 `Deliverable 5` 正文。
- [x] 在报告中明确 `interactive prototype` 的访问方式，例如 `index.html -> Tab 3: Prototype`。
- [ ] 在 D5 中列出 Roadshow PPT 文件名 `slides/InterviewAI_Pitch_Deck.pptx` 和每页内容对应关系。
- [ ] 增加逐步 Demo Script，覆盖至少一个核心任务，最好覆盖 `Practice` 主流程和一个失败恢复场景。
- [ ] 写清 Core Value Proposition，并明确差异化不来自功能堆砌，而来自透明、可控、上下文感知的 AI 交互体验。

中优先级：

- [x] 把 Track A 四个最低要求分别映射到图号、页面名或原型状态。
- [ ] 统一 `Serious` / `Severe` 严重度命名。
- [ ] 补充隐私保护和可访问性风险管理，呼应投资人互评第 4 点。
- [ ] 在 Roadmap 中补充每阶段风险和验证指标。

建议 D5 最小可用结构：

```text
Deliverable 5: Product Pitch Materials
5.1 Pitch Deck Overview
5.2 Prototype Demo Script
5.3 Core Value Proposition
5.4 Submission Package Checklist
```

建议一句话价值主张：

```text
InterviewAI helps computing graduates turn generic AI interview preparation into transparent, context-aware, and user-controllable coaching, so they can practice, revise, and track improvement with confidence.
```
