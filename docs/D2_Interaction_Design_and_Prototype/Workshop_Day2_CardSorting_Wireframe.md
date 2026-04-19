# COMP7505 Workshop Day 2 — Completed

**Product:** AI Interview Copilot (InterviewAI)
**Track:** Track A — Smart Adaptive Interfaces
**Team Members:** [填写组员姓名]
**Date:** 2026-04-18

---

## Activity 1 — Card Sorting 卡片分类（20 min）

<!-- Card Sorting 是一种 UX 研究方法：把产品功能拆成一张张卡片，让用户自由分组并命名，
     从而发现用户心中的"分类逻辑"，用来指导菜单和导航设计。-->

### Step 1: Requirement Extraction 需求提取

<!-- 从 Day 1 的 9 条 User Story（用户故事）中，提炼出产品的核心功能。
     注意：下表前 5 行来自 User Story，后面的是额外识别的产品功能需求。
     总共 13 个核心功能，不是 13 条 User Story。-->

From Day 1 User Stories, extract core functions（从用户故事中提炼核心功能）:

| #    | 对应 User Story                              | Core Function 核心功能      | 中文说明                     |
| ---- | -------------------------------------------- | --------------------------- | ---------------------------- |
| 1    | US-1: Contextual feedback with reasoning     | AI Evaluation & Feedback    | AI 评估与反馈（含评分理由）  |
| 2    | US-2: Strong answer examples                 | Answer Reference            | 参考答案展示                 |
| 3    | US-3: Inline challenge controls              | Feedback Control            | 反馈控制（标记/覆盖/撤销）   |
| 4    | US-4: Graceful voice fallback                | Voice Input                 | 语音输入（含兜底方案）       |
| 5    | US-5: Smart practice recommendations         | Progress Tracking           | 进度追踪与智能推荐           |
| 6    | US-6: JD & Resume context awareness          | Job Context Setup           | 岗位上下文设置（JD+简历）    |
| 7    | US-7: Scenario-based question generation     | Question Generation         | 题目生成（基于JD+简历）      |
| 8    | US-1, US-7 的前提：用户必须能提交答案        | Answer Submission           | 文本答题提交                 |
| 9    | US-9: Recording upload & structured review   | Recording Upload            | 录音/录像上传                |
| 10   | US-9: Recording upload & structured review   | Recording Analysis          | 录音中提取 Q&A 对            |
| 11   | US-5: Smart practice recommendations         | History Review              | 历史练习记录回顾             |
| 12   | US-8: AI follow-up probing                   | Follow-Up Probing           | AI 追问机制                  |
| 13   | 产品基础需求：保存偏好、管理简历等            | Settings                    | 账户与偏好设置               |

<!-- Step 1 产出：13 个核心功能，其中 10 个直接来自 User Story，2 个是 US 的隐含前提，1 个是产品基础需求 -->

**映射说明：**
- **#8 Answer Submission**：不是独立 User Story，而是 US-1（需要反馈）和 US-7（需要答题）的**必要前提**——用户不提交答案，就无法获得反馈
- **#13 Settings**：是产品的**基础功能**（任何产品都需要账户管理），用户不会在调研中主动提，但是产品运行的必要条件
- 其余 11 项全部可以追溯到具体的 User Story

### Step 2: Card Decomposition 卡片分解

<!-- 把每个核心功能进一步拆成子功能，每个子功能写一张卡片。
     例如"岗位上下文设置"拆成：输入职位名称、粘贴JD、上传简历、查看解析摘要、编辑解析结果 -->

Break each core function into sub-functions (one per card):

**A. Job Context Setup 岗位上下文设置**

- A1 Input job title — 输入职位名称
- A2 Paste job description (JD) — 粘贴职位描述
- A3 Upload resume (PDF) — 上传简历
- A4 View JD/resume parsing summary — 查看 JD/简历解析摘要
- A5 Edit parsed context — 编辑解析结果

**B. Question Generation 题目生成**

- B1 Generate questions from JD + resume — 根据 JD + 简历生成题目
- B2 Select question category (behavioral / technical / system design) — 选择题目类别（行为面 / 技术面 / 系统设计）
- B3 Adjust difficulty level — 调整难度
- B4 View question one at a time — 逐题展示
- B5 Skip a question — 跳过当前题
- B6 Request more questions — 请求更多题目

**C. Answer Submission 答题提交**

- C1 Type answer (text input) — 文本输入答案
- C2 Record answer (voice input) — 语音录入答案
- C3 Voice-to-text fallback when recognition fails — 语音识别失败时自动转文字
- C4 Save draft answer — 保存草稿
- C5 Revise and resubmit answer — 修改并重新提交

**D. AI Evaluation & Feedback AI 评估与反馈**

- D1 View overall score — 查看总分
- D2 View sentence-level reasoning — 查看逐句评分理由
- D3 View confidence indicator (High / Medium / Low) — 查看 AI 置信度（高/中/低）
- D4 View strong answer example — 查看优秀答案示例
- D5 Compare my answer with strong answer — 对比我的答案与优秀答案

**E. Feedback Control 反馈控制（Track A 必需）**

- E1 Flag a feedback point — 标记某条反馈（表示不认同）
- E2 Add note explaining disagreement — 添加不同意的原因
- E3 Override AI score — 覆盖 AI 评分
- E4 Undo override (restore AI score) — 撤销覆盖，恢复 AI 评分
- E5 Discard entire evaluation — 丢弃整次评估

**F. Recording Upload & Analysis 录音上传与分析**

- F1 Upload audio/video file — 上传音频/视频文件
- F2 View extraction progress — 查看提取进度
- F3 Edit extracted Q&A pairs — 编辑提取出的问答对
- F4 View audio quality warning — 查看音频质量警告
- F5 Retry extraction on failure — 提取失败时重试

**G. Review Summary 复盘总结**

- G1 View structured performance summary — 查看结构化表现总结
- G2 Highlight rambles / vague answers — 高亮显示跑题/模糊的回答
- G3 Identify missed resume references — 标记未提到的简历亮点
- G4 Export summary (PDF) — 导出 PDF 报告

**H. History & Progress 历史与进度**

- H1 Browse past practice sessions — 浏览历史练习
- H2 View score trend charts — 查看分数趋势图
- H3 View recommendation for next focus area — 查看下次练习建议
- H4 Start new session from recommendation — 从建议开始新练习

**I. Settings 设置**

- I1 Edit profile (name, target role) — 编辑个人资料
- I2 Manage uploaded resumes — 管理已上传简历
- I3 Set default question preferences — 设置默认题目偏好
- I4 Toggle voice input on/off — 开关语音输入
- I5 Account & privacy settings — 账户与隐私设置

<!-- Step 2 产出：9 组共 40+ 张子功能卡片（A1–I5） -->

### Step 3: Classification Sorting 分类排序

<!-- 把 Step 2 的卡片按逻辑关联分组，每组命名为一个"模块"。
     这是 Card Sorting 的核心——模拟用户心中的分类方式。-->

Group sub-function cards by logical relevance into modules（按逻辑关联分组为模块）:

| Module 模块  | Cards Included 包含的卡片 | Rationale 分组理由                                                                 |
| ------------ | ------------------------- | ---------------------------------------------------------------------------------- |
| **Dashboard** | H1, H2, H3, H4            | 入口页面；展示历史概览和下一步推荐                                                 |
| **Practice** | A1–A5, B1–B6, C1–C5, D1–D5, E1–E5 | 核心练习流程：设置岗位 → 生成题目 → 答题 → AI反馈 → 用户控制                    |
| **Review**   | F1–F5, G1–G4              | 上传录音 → 提取分析 → 结构化复盘总结                                               |
| **History**  | H1–H4                     | 详细的历史记录与趋势图表（与 Dashboard 的精简快照不同）                             |
| **Settings** | I1–I5                     | 账户与偏好管理                                                                     |

<!-- Step 3 产出：5 个顶级模块（Dashboard / Practice / Review / History / Settings） -->

### Step 4: Hierarchy — Information Architecture (IA) 信息架构（页面树）

<!-- 把 5 个模块展开为完整的页面层级树，展示每个模块下面有哪些子页面。
     这就是最终产品的导航结构蓝图。-->

```
InterviewAI
├── Dashboard 仪表盘
│   ├── Welcome Card ("Start Your First Practice")  欢迎卡片
│   ├── Recent Sessions (last 3)                    最近 3 次练习
│   ├── Score Trend Charts (mini)                   分数趋势迷你图
│   └── Smart Recommendation Card                   智能推荐卡片
│
├── Practice 练习（核心流程）
│   ├── Step 1: Job Context 岗位上下文
│   │   ├── Input Job Title      输入职位名称
│   │   ├── Paste JD             粘贴职位描述
│   │   ├── Upload Resume        上传简历
│   │   └── Review Parsed Summary 查看/编辑解析摘要
│   ├── Step 2: Questions 题目
│   │   ├── View Current Question     查看当前题目
│   │   ├── Category / Difficulty Controls  类别/难度控制
│   │   └── Skip / Request More       跳过/请求更多
│   ├── Step 3: Answer 答题
│   │   ├── Text Input Area     文本输入区
│   │   ├── Voice Record Button 语音录制按钮
│   │   └── Voice Fallback Modal 语音失败兜底弹窗
│   ├── Step 4: Feedback AI 反馈
│   │   ├── Overall Score + Confidence   总分 + 置信度
│   │   ├── Sentence-Level Reasoning     逐句评分理由
│   │   ├── Strong Answer Example        优秀答案示例
│   │   ├── Compare Versions             对比版本
│   │   └── Flag / Override / Undo Controls  标记/覆盖/撤销控制
│   └── Step 5: Next or Save 下一步或保存
│       ├── Next Question     下一题
│       └── Save & Exit to Dashboard  保存并返回仪表盘
│
├── Review 录音复盘
│   ├── Step 1: Upload Recording 上传录音
│   │   ├── Drag & Drop / File Picker  拖拽上传/文件选择
│   │   └── Audio Quality Warning (if low)  音频质量警告
│   ├── Step 2: Extract & Edit Q&A 提取并编辑问答
│   │   ├── Extraction Progress Bar  提取进度条
│   │   ├── Edit Transcription       编辑转录文本
│   │   └── Retry on Failure         失败时重试
│   ├── Step 3: Summary 总结
│   │   ├── Performance Overview      表现概览
│   │   ├── Ramble / Vague Highlights 跑题/模糊高亮
│   │   ├── Missed Resume References  遗漏简历亮点
│   │   └── Export PDF                导出 PDF
│   └── Follow-Up: Start Practice (link to Practice)  后续：开始针对性练习
│
├── History 历史记录
│   ├── Session List (filterable)      练习列表（可筛选）
│   ├── Session Detail                 练习详情
│   │   ├── Questions & Answers        问答内容
│   │   ├── Scores & Feedback          评分与反馈
│   │   └── User Flags / Overrides     用户标记/覆盖
│   ├── Score Trend Charts (full)      完整分数趋势图
│   └── Recommendation Card → Start Session  推荐卡片 → 开始练习
│
└── Settings 设置
    ├── Profile (name, target role)     个人资料
    ├── Resumes (manage uploads)        简历管理
    ├── Question Preferences (defaults) 题目偏好
    ├── Voice Input Toggle              语音输入开关
    └── Account & Privacy               账户与隐私
```

<!-- Step 4 产出：完整的页面树（IA），是导航和原型的结构基础 -->

---

## Activity 2 — Sketch Low-Fidelity Wireframe & Prototype 低保真线框图与原型（40 min）

### Wireframe vs Prototype 线框图 vs 原型

| 维度 Dimension | Wireframe 线框图                   | Prototype 原型                                      |
| -------------- | ---------------------------------- | --------------------------------------------------- |
| **状态**       | 静态草图，只能看，不能点击         | 可交互：点击、弹窗、页面跳转都能用                  |
| **交互**       | 无                                 | 可点击导航，有弹窗、状态变化、页面跳转              |
| **视觉风格**   | 黑白线条、简单方框和文字           | 低保真：线框+交互；高保真：完整颜色、图标、真实 UI  |
| **核心目的**   | 定义布局、元素位置和内容层级       | 测试用户流程、验证可用性、跑通任务路径              |
| **用户体验**   | 像一张平面建筑图纸                 | 像一个简化版的能用的 App                             |

### Tool: Figma 工具

> Team Figma link: [填写 Figma 文件链接]

### Wireframe Sketches 线框图草图

<!-- 以下是 5 个核心页面的 ASCII 线框草图 -->

#### Screen 1: Dashboard 仪表盘

```
┌─────────────────────────────────────────────────────┐
│  ☰  InterviewAI                        [Settings]   │
├────────┬────────────────────────────────────────────┤
│        │                                            │
│  Dash  │  Welcome back, Kevin!                      │
│  Pract │  ┌────────────────────────────────────┐    │
│  Review│  │  ▶ Start Your First Practice        │    │
│  Hist  │  │  3 quick steps to tailored prep     │    │
│  Sett  │  └────────────────────────────────────┘    │
│        │                                            │
│        │  Recent Sessions                           │
│        │  ┌──────────┐ ┌──────────┐ ┌──────────┐   │
│        │  │ React    │ │ System   │ │ Behavior │   │
│        │  │ 7/10     │ │ 5/10     │ │ 8/10     │   │
│        │  │ Apr 16   │ │ Apr 14   │ │ Apr 12   │   │
│        │  └──────────┘ └──────────┘ └──────────┘   │
│        │                                            │
│        │  📊 Score Trends          🎯 Next Focus   │
│        │  [Line chart]             Technical Depth  │
│        │                           Score: 4/10      │
│        │                           [Start Session]  │
└────────┴────────────────────────────────────────────┘
```

#### Screen 2: Practice — Step 1: Job Context 练习 — 岗位上下文

```
┌─────────────────────────────────────────────────────┐
│  ☰  InterviewAI                        [Settings]   │
├────────┬────────────────────────────────────────────┤
│        │  Practice > Job Context                     │
│  Dash  │  ──────────────────────────────            │
│ ●Pract │                                            │
│  Review│  Job Title                                  │
│  Hist  │  ┌────────────────────────────────────┐    │
│  Sett  │  │ Front-end Developer               │    │
│        │  └────────────────────────────────────┘    │
│        │                                            │
│        │  Job Description                           │
│        │  ┌────────────────────────────────────┐    │
│        │  │ Paste JD text here...              │    │
│        │  │                                    │    │
│        │  └────────────────────────────────────┘    │
│        │                                            │
│        │  Resume                                    │
│        │  ┌────────────────────────────────────┐    │
│        │  │  📎 Upload PDF            [Browse] │    │
│        │  └────────────────────────────────────┘    │
│        │                                            │
│        │  Parsed Summary                            │
│        │  ┌────────────────────────────────────┐    │
│        │  │ Role: React Developer              │    │
│        │  │ Key skills: React, TypeScript, ...  │    │
│        │  │ [Edit Summary]                     │    │
│        │  └────────────────────────────────────┘    │
│        │                                            │
│        │                        [Next → Generate]   │
└────────┴────────────────────────────────────────────┘
```

#### Screen 3: Practice — Step 4: Feedback 练习 — AI 反馈

```
┌─────────────────────────────────────────────────────┐
│  ☰  InterviewAI                        [Settings]   │
├────────┬────────────────────────────────────────────┤
│        │  Practice > Feedback                        │
│  Dash  │  ──────────────────────────────            │
│ ●Pract │                                            │
│  Review│  Question 3 of 6                            │
│  Hist  │  "Describe your experience with React      │
│  Sett  │   hooks and state management."             │
│        │                                            │
│        │  ┌────────────────────────────────────┐    │
│        │  │  Your Answer                       │    │
│        │  │  "I have used useState and          │    │
│        │  │   useEffect in several projects..." │    │
│        │  │                      [View Full]    │    │
│        │  └────────────────────────────────────┘    │
│        │                                            │
│        │  ┌────────────────────────────────────┐    │
│        │  │  Score: 6/10  Confidence: ● Medium  │    │
│        │  │                                    │    │
│        │  │  Reasoning:                        │    │
│        │  │  • Lacks specific project example  │    │
│        │  │  • No mention of useReducer/Redux  │    │
│        │  │  • Good explanation of useEffect   │    │
│        │  │                                    │    │
│        │  │  [Flag] [Override Score] [Undo]    │    │
│        │  └────────────────────────────────────┘    │
│        │                                            │
│        │  ▼ View Strong Answer Example              │
│        │  ┌────────────────────────────────────┐    │
│        │  │  "In my e-commerce project, I used  │    │
│        │  │   useReducer for complex cart       │    │
│        │  │   state..."                         │    │
│        │  └────────────────────────────────────┘    │
│        │                                            │
│        │        [Revise Answer]  [Next Question →]  │
└────────┴────────────────────────────────────────────┘
```

#### Screen 4: Review — Upload & Analysis 录音复盘 — 上传与分析

```
┌─────────────────────────────────────────────────────┐
│  ☰  InterviewAI                        [Settings]   │
├────────┬────────────────────────────────────────────┤
│        │  Review > Upload Recording                  │
│  Dash  │  ──────────────────────────────            │
│  Pract │                                            │
│ ●Review│  Upload Interview Recording                │
│  Hist  │  ┌────────────────────────────────────┐    │
│  Sett  │  │                                    │    │
│        │  │    📁  Drag & drop or [Browse]     │    │
│        │  │    MP4, WAV, M4A — max 500MB       │    │
│        │  │                                    │    │
│        │  └────────────────────────────────────┘    │
│        │                                            │
│        │  ⚠️ Audio Quality: Low                     │
│        │  "Background noise detected. Extraction    │
│        │   accuracy may be reduced."                │
│        │                                            │
│        │  Extraction Progress                       │
│        │  ████████████░░░░░░░░  60%                │
│        │                                            │
│        │  Extracted Q&A (3 of 5 pairs)              │
│        │  ┌────────────────────────────────────┐    │
│        │  │ Q1: "Tell me about yourself"       │    │
│        │  │ A1: "I'm a CS grad from HKU..."    │    │
│        │  │                        [Edit ✏️]   │    │
│        │  │                                    │    │
│        │  │ Q2: "Why this company?"            │    │
│        │  │ A2: "I'm drawn to the startup..."  │    │
│        │  │                        [Edit ✏️]   │    │
│        │  └────────────────────────────────────┘    │
│        │                                            │
│        │                  [Retry] [Generate Summary] │
└────────┴────────────────────────────────────────────┘
```

#### Screen 5: History 历史记录

```
┌─────────────────────────────────────────────────────┐
│  ☰  InterviewAI                        [Settings]   │
├────────┬────────────────────────────────────────────┤
│        │  History                                    │
│  Dash  │  ──────────────────────────────            │
│  Pract │                                            │
│  Review│  Filter: [All] [Practice] [Review]         │
│ ●Hist  │                                            │
│  Sett  │  Score Trends                              │
│        │  ┌────────────────────────────────────┐    │
│        │  │  Structure    ████████████░░  8/10  │    │
│        │  │  Depth        ████░░░░░░░░░░  4/10  │    │
│        │  │  Relevance    ██████████░░░░  7/10  │    │
│        │  │  Clarity      ████████░░░░░░  6/10  │    │
│        │  └────────────────────────────────────┘    │
│        │                                            │
│        │  Past Sessions                             │
│        │  ┌────────────────────────────────────┐    │
│        │  │ React Dev Practice   Apr 16  7/10  │    │
│        │  │ System Design        Apr 14  5/10  │    │
│        │  │ Behavioral Qs        Apr 12  8/10  │    │
│        │  │ React Dev Practice   Apr 10  6/10  │    │
│        │  └────────────────────────────────────┘    │
│        │                                            │
│        │  🎯 Recommendation                         │
│        │  ┌────────────────────────────────────┐    │
│        │  │ Technical Depth is below target.    │    │
│        │  │ Focus your next session on          │    │
│        │  │ system design & deep tech Qs.       │    │
│        │  │ [Start Focused Session →]           │    │
│        │  └────────────────────────────────────┘    │
└────────┴────────────────────────────────────────────┘
```

### Prototype Navigation Map 原型导航地图

<!-- 展示用户从一个页面跳到另一个页面的完整路径，
     包括正常路径和异常路径（如语音失败弹窗）。-->

```
Dashboard 仪表盘 ──────────────────────────────────────
  │
  ├── [Start Practice] 开始练习 → Practice Step 1 (Job Context 岗位上下文)
  │                         │
  │                         ├── [Next] → Step 2 (Questions 题目)
  │                         │              │
  │                         │              ├── [Next] → Step 3 (Answer 答题)
  │                         │              │              │
  │                         │              │              ├── Voice Fallback Modal 语音失败弹窗 (on error)
  │                         │              │              │
  │                         │              │              └── [Submit] 提交 → Step 4 (Feedback 反馈)
  │                         │              │                              │
  │                         │              │                              ├── [Flag/Override/Undo] 标记/覆盖/撤销 (inline)
  │                         │              │                              ├── [View Strong Answer] 查看优秀答案 (expand)
  │                         │              │                              ├── [Revise] 修改答案 → back to Step 3
  │                         │              │                              └── [Next Question] 下一题 → Step 2
  │                         │              │                                           or
  │                         │              │                              [Save & Exit] 保存退出 → Dashboard
  │                         │              │
  │                         │              └── [Skip] 跳过 → next question
  │                         │
  │                         └── [Edit Summary] 编辑摘要 → inline edit
  │
  ├── [Start Review] 开始复盘 → Review Step 1 (Upload 上传)
  │                       │
  │                       ├── Audio Quality Warning 音频质量警告 (if low)
  │                       │
  │                       └── [Generate] 生成 → Step 2 (Extract & Edit 提取并编辑)
  │                                          │
  │                                          ├── Extraction Failure Modal 提取失败弹窗 → [Retry] 重试
  │                                          │
  │                                          └── [Generate Summary] 生成总结 → Step 3 (Summary 总结)
  │                                                                  │
  │                                                                  ├── [Export PDF] 导出 PDF
  │                                                                  └── [Practice These] 针对性练习 → Practice Step 1
  │
  └── [View History] 查看历史 → History
                         │
                         ├── [Session Detail] 练习详情 → expand
                         └── [Start Focused Session] 开始针对性练习 → Practice Step 1
```

---

## Summary 总结

| Activity 活动             | Output 产出                                                |
| ------------------------- | ---------------------------------------------------------- |
| **Card Sorting 卡片分类** | 13 个核心功能 → 40+ 张子功能卡片 → 5 个模块 → 完整 IA 页面树 |
| **Wireframe 线框图**      | 5 个核心页面草图 + 导航地图（待在 Figma 中构建原型）       |

**Next step:** Build interactive prototype in Figma based on these wireframes and the navigation map above.
