# InterviewAI 原型版本迭代日志

## 文档信息

| 项目 | 内容 |
|---|---|
| 项目名称 | InterviewAI |
| 原型文件 | `index.html` |
| 迭代版本 | v2 |
| 迭代日期 | 2026-04-15 |
| 记录类型 | 功能优化前后对比 / 版本迭代日志 |

---

## 本次迭代目标

本次迭代主要围绕原型中的 3 个核心页面进行优化：

1. AI 题目页增加“题目管理能力”
2. 答题页增加“实时辅助反馈”
3. History 页增加“复盘对比能力”

本次修改基于原有单文件高保真原型 `index.html` 进行，目标不是改变产品定位，而是将原本偏静态展示的页面，升级为更接近真实产品体验的可交互原型。

---

## 版本概述

### 修改前版本特征

- 原型已经具备 Dashboard、Practice、Review、History、Settings 等完整页面框架。
- 页面视觉完成度较高，但部分关键功能仍偏“展示型原型”。
- 用户可以点击页面跳转，但在题目管理、答题引导、历史复盘方面缺乏更深入的交互闭环。

### 修改后版本特征

- 原型从“静态页面演示”提升为“带状态变化的交互式流程原型”。
- 用户在题目页可筛选、标记、收藏、跳过和重生成题目。
- 用户在答题过程中可实时看到结构反馈、字数与时长估计、STAR 覆盖度与即时建议。
- 用户在历史记录页可搜索、筛选并选择两条记录进行对比分析，形成更完整的复盘闭环。

---

## 迭代项 1：AI 题目页增加“题目管理能力”

### 修改前

- 题目页以静态题卡形式展示 AI 生成的问题。
- 用户点击题卡后直接进入答题页面。
- 页面缺少对题目的分类管理与状态管理。
- 不支持收藏、跳过、标记弱项、单题重生成等操作。
- 页面无法体现当前练习进度，例如已完成几题、哪些题需要重点复练。

### 修改后

- 新增题目统计摘要区，显示：
  - Question Bank 总数
  - Completed 数量
  - In Progress 数量
  - Weak Focus 数量
- 新增筛选与排序能力：
  - 按题型筛选：Behavioral / Technical / System Design
  - 按状态筛选：Not Started / In Progress / Completed / Skipped
  - 按逻辑排序：JD Match、Difficulty、Duration
- 每道题新增状态标签与属性标签：
  - Not Started
  - In Progress
  - Completed
  - Skipped
  - Favorite
  - Weak Area
- 每道题新增快捷操作：
  - Start Answer
  - Favorite / Unfavorite
  - Mark Weak
  - Skip / Restore
  - Regenerate This
- 新增“Continue Current”入口，用户可以快速回到当前作答中的题目。

### 功能改进价值

- 由“AI 给题，用户逐个点击进入”升级为“用户可主动管理题库”。
- 提高了用户对练习顺序和练习重点的掌控感。
- 更符合面试训练产品中“反复练习、针对弱项强化”的使用场景。

---

## 迭代项 2：答题页增加“实时辅助反馈”

### 修改前

- 答题页主要包含题目标题、输入方式切换、文本框和提交按钮。
- AI 反馈只在提交答案后出现。
- 用户在输入过程中无法判断自己的答案结构是否完整。
- 页面缺少字数、时长、结构覆盖度、关键词命中等过程反馈。

### 修改后

- 页面改为左右双栏布局：
  - 左侧为题目与作答区
  - 右侧为实时反馈与建议区
- 新增 Realtime Scoreboard，动态展示：
  - Words
  - Estimated Time
  - STAR Coverage
  - Coach Readiness
- 新增 STAR Coverage 检查区，实时判断以下结构是否出现：
  - Situation
  - Task
  - Action
  - Result
- 新增 Live Coaching 区，在用户输入过程中动态提示：
  - 是否缺少 Result
  - 是否缺少团队协作表达
  - 是否与目标岗位相关性不足
  - 是否回答过短或过长
  - 技术题是否缺少 trade-off / performance 说明
- 新增 Quick Improvement Inserts 区，用户可一键插入补强片段：
  - Quantified Result
  - Team Context
  - Role Relevance
- 新增 Save Draft 按钮，支持作答草稿保存。
- 提交答案后，题目状态会同步更新为 Completed，并影响题目页的状态显示。

### 功能改进价值

- 由“提交后才知道问题”升级为“边作答边获得教练式反馈”。
- 降低了用户试错成本。
- 让 AI 从“评分工具”转变为“过程辅导工具”，更符合智能面试教练的定位。

---

## 迭代项 3：History 页增加“复盘对比能力”

### 修改前

- History 页仅展示历史记录列表。
- 用户只能看到岗位、日期、类型和分数等基础信息。
- 缺少搜索与筛选能力。
- 不支持两条记录对比，也无法查看维度变化与成长趋势。
- History 更像“存档页”，而不是“复盘页”。

### 修改后

- 新增历史统计摘要区，展示：
  - Sessions Logged
  - Average Score
  - Best Session
  - Needs STAR Work
- 新增筛选与搜索能力：
  - 按 All / Practice / Review 切换
  - 支持关键词搜索 role、company、focus area
- 每条历史记录新增更完整的信息结构：
  - 角色与公司
  - Session 类型
  - 日期
  - 本次练习焦点
  - 总分
  - 文字摘要
  - 趋势描述
  - STAR / Clarity / Role Relevance 三个维度的条形展示
- 新增 Select for Compare 机制：
  - 可选择两条记录进入对比模式
  - 可清空比较对象
- 新增 Comparison Studio，对两条记录进行对比分析，展示：
  - Overall score change
  - STAR structure change
  - Clarity change
  - Role relevance change
  - Earlier answer highlight
  - Later answer highlight
  - Progress、Recurring gap、Next drill
- 新增 Practice Similar Gap 按钮，可从 History 页面直接回到 Practice，针对弱项继续练习。

### 功能改进价值

- 由“查看记录”升级为“分析成长轨迹”。
- 让 History 页面从被动存档转为主动复盘。
- 构建了“历史复盘 -> 发现问题 -> 返回练习”的学习闭环。

---

## 页面结构层面的整体变化

### 修改前

- Questions、Answer、History 三个页面都以相对静态的信息卡片为主。
- 页面之间虽然可以跳转，但状态联动较弱。
- 原型更强调“流程展示”，较少体现“交互中的状态变化”。

### 修改后

- Questions 页面加入题目数据状态与过滤逻辑。
- Answer 页面加入实时计算与动态提示逻辑。
- History 页面加入对比状态管理与复盘面板。
- 三个页面之间形成联动：
  - 题目状态会随着作答保存和提交而改变
  - 完成题目后可自动跳转下一题
  - History 里的弱项可回流到 Practice 再练习

---

## 技术实现摘要

本次迭代仍保持单文件原型结构，主要在 `index.html` 中完成以下更新：

- 扩展 CSS，新增题目管理区、实时反馈区、历史对比区所需样式
- 重构 Questions、Answer、History 三个页面的 HTML 结构
- 新增前端状态数据与交互逻辑，包括：
  - 题目数据 `questionBank`
  - 历史记录数据 `historyRecords`
  - 题目筛选状态 `questionFilters`
  - 历史筛选状态 `historyFilters`
  - 历史对比选择状态 `selectedHistoryIds`
- 新增核心交互函数，包括：
  - `renderQuestions()`
  - `openQuestion()`
  - `toggleFavorite()`
  - `toggleWeak()`
  - `skipQuestion()`
  - `regenerateQuestion()`
  - `renderAnswerPage()`
  - `handleAnswerInput()`
  - `updateRealtimeFeedback()`
  - `submitAnswer()`
  - `renderHistory()`
  - `toggleHistorySelection()`
  - `renderHistoryCompare()`

---

## 本次版本结论

本次迭代没有改变 InterviewAI 的核心产品方向，而是在原有高保真原型的基础上，重点强化了以下三个方面：

1. 用户对题目练习过程的管理能力
2. 用户在作答过程中的即时反馈体验
3. 用户对历史表现的复盘与对比能力

相较于上一版，本次原型更接近真实产品中的关键交互逻辑，也更能体现“AI 辅助 + 用户主导”的设计思路。

---

## 后续可继续迭代的方向

- 让反馈页分数与当前答题内容实时联动，而不是保持固定展示
- 为 History 页增加时间趋势图与弱项统计图
- 为 Questions 页增加批量加入练习计划的能力
- 为 Answer 页增加语音模式下的实时转写模拟

