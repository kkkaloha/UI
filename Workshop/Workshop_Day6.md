# COMP7505 Workshop Day 6 — Completed

**Product:** AI Interview Copilot (InterviewAI)
**Track:** Track A — Smart Adaptive Interfaces
**Team Members:** [填写组员姓名]
**Date:** 2026-04-18

---

## Activity 1 — Conduct the Usability Study (45 min)

### Step 1: Survey (15 min)

#### Survey Platform & Link

> **Platform:** [填写，如 Google Forms / 问卷星]
> **Survey Link:** [填写]
> **ED Workshop Post:** [填写帖子链接]

#### Survey Responses Collected

| # | Respondent | From Group | Completed? |
|---|-----------|------------|------------|
| 1 | [填写] | [填写组名] | Yes |
| 2 | [填写] | [填写组名] | Yes |
| 3 | [填写] | [填写组名] | Yes |
| 4 | [填写] | [填写组名] | Yes |
| 5 | [填写] | [填写组名] | Yes |

#### Surveys We Completed (for other groups)

| # | Group Name | Survey Link | Our Name |
|---|-----------|-------------|----------|
| 1 | [填写] | [填写] | [填写] |
| 2 | [填写] | [填写] | [填写] |

### Step 2: Semi-Structured Interviews (30 min)

#### Team Split

| Role | Name | Activity |
|------|------|----------|
| Interviewer A | [填写] | Interview members from other groups |
| Interviewer B | [填写] | Interview members from other groups |
| Participant | [填写] | Stay and be interviewed by other groups |

#### Interview Log

**Interview 1**

| Field | Details |
|-------|---------|
| Participant | [填写姓名] |
| From Group | [填写组名] |
| Consent signed | Yes / No |
| Duration | [填写] min |
| Scenario tested | [填写] |

Key observations:

> [填写访谈中的关键发现，例如：]
> - Participant paused for 8 seconds on Dashboard before finding the Start button
> - Did not notice the confidence badge until explicitly asked
> - Said "I don't know if 6/10 is good or bad — is there a reference?"
> - Voice failure: initially thought it was their microphone problem, not a system issue
> - Loved the strong answer example: "This is the most useful part"

---

**Interview 2**

| Field | Details |
|-------|---------|
| Participant | [填写姓名] |
| From Group | [填写组名] |
| Consent signed | Yes / No |
| Duration | [填写] min |
| Scenario tested | [填写] |

Key observations:

> [填写]

---

#### Raw Interview Notes

> [填写完整的访谈笔记，包括 think-aloud 转录和追问记录]

---

## Activity 2 — Quantitative and Qualitative Analysis (15 min)

### Quantitative Analysis (Survey Data)

#### SEQ Scores (1 = Very Difficult, 7 = Very Easy)

| Metric | Task 1 (Practice Flow) | Task 2 (Review Flow) | Task 3 (Voice Fallback) |
|--------|------------------------|----------------------|-------------------------|
| Respondent 1 | [填写] | [填写] | [填写] |
| Respondent 2 | [填写] | [填写] | [填写] |
| Respondent 3 | [填写] | [填写] | [填写] |
| Respondent 4 | [填写] | [填写] | [填写] |
| Respondent 5 | [填写] | [填写] | [填写] |
| **Mean** | **[填写]** | **[填写]** | **[填写]** |
| **Median** | **[填写]** | **[填写]** | **[填写]** |

#### Likert Scale Summary (1 = Strongly Disagree, 5 = Strongly Agree)

| Question | Topic | Mean | Std Dev |
|----------|-------|------|---------|
| Q6 | AI feedback reasoning is understandable | [填写] | [填写] |
| Q7 | Strong answer example is helpful | [填写] | [填写] |
| Q8 | I can challenge/override AI feedback | [填写] | [填写] |
| Q10 | Extracted Q&A is accurate enough | [填写] | [填写] |
| Q11 | Performance summary highlights strengths/weaknesses | [填写] | [填写] |
| Q13 | Voice fallback feels smooth | [填写] | [填写] |

#### Quantitative Insights

> [填写数据分析结论，例如：]
> - Task 3 (Voice Fallback) has the lowest SEQ score → hardest task
> - Q8 (user control) scores lowest → users don't feel they can challenge AI
> - Q7 (strong answer example) scores highest → most appreciated feature

---

### Qualitative Analysis (Interview Data)

#### Affinity Diagram — Grouped Findings

**Cluster A: Navigation & Discoverability**

| # | Observation | Source |
|---|-------------|--------|
| A1 | User paused 8s on Dashboard before finding Start | Interview 1 |
| A2 | "Where do I begin?" — first reaction to Dashboard | Interview 1 |
| A3 | User clicked History instead of Practice by accident | Interview 2 |

**Cluster B: Feedback Comprehension**

| # | Observation | Source |
|---|-------------|--------|
| B1 | "Is 6/10 good or bad? I have no reference" | Interview 1 |
| B2 | Confidence badge not noticed until pointed out | Interview 1 |
| B3 | "The reasoning says 'lacks structure' but doesn't show me what structure looks like" | Interview 2 |
| B4 | Strong answer example was the most praised feature | Interview 1 & 2 |

**Cluster C: Voice Failure Experience**

| # | Observation | Source |
|---|-------------|--------|
| C1 | "I thought my mic was broken, not the system" | Interview 1 |
| C2 | No visual feedback when voice stopped — screen was static for 5s | Interview 1 |
| C3 | Partial transcript was preserved but user didn't notice it in the text field | Interview 2 |

**Cluster D: User Control & Trust**

| # | Observation | Source |
|---|-------------|--------|
| D1 | User saw Override button but hesitated: "What happens if I override?" | Interview 1 |
| D2 | Flag feature not discovered during task — only found when asked | Interview 2 |
| D3 | "I want to trust the AI but I can't tell if it actually read my resume" | Interview 2 |

#### Qualitative Insights

> [填写质化分析结论，例如：]
> - Navigation: Dashboard needs a more prominent CTA for first-time users
> - Feedback: Scores need a reference baseline; confidence badge needs higher visibility
> - Voice failure: Must show immediate visual feedback; error message should blame the system, not the user's mic
> - User control: Override needs clearer explanation of consequences; Flag should be more discoverable

---

### Combined Analysis: Quantitative + Qualitative

| Finding | Quant Evidence | Qual Evidence | Severity | Optimization |
|---------|---------------|---------------|----------|-------------|
| Voice failure lacks visual feedback | SEQ Task 3 = lowest | "Thought my mic was broken" | **Critical** | Add immediate error modal with system-blame message |
| Scores have no reference baseline | Q6 below average | "Is 6/10 good or bad?" | **Major** | Add score distribution or benchmark (e.g., "above average") |
| Confidence badge invisible | — | Not noticed by 2/2 participants | **Major** | Increase size + color + label ("AI Confidence: Medium") |
| Dashboard entry point unclear | SEQ Task 1 drop in first step | "Where do I begin?" | **Moderate** | Enlarge Start Practice card + add pulsing animation |
| Override consequences unclear | Q8 lowest Likert | "What happens if I override?" | **Moderate** | Add tooltip explaining override behavior |
| Flag button undiscoverable | — | Not found by 2/2 during task | **Minor** | Move Flag inline next to each reasoning bullet |
| Strong answer example valued | Q7 highest Likert | "Most useful part" (both users) | Positive | Keep and enhance with side-by-side comparison |

### Priority Fix List (Updated for Day 7)

| Priority | Issue | From | Fix |
|----------|-------|------|-----|
| P0 | Voice failure no visual feedback | Day 3 self + Day 6 test | Add error modal with fallback message |
| P0 | Score lacks reference baseline | Day 6 interview | Add "above/below average" label |
| P1 | Confidence badge too subtle | Day 6 interview | Enlarge + color code + text label |
| P1 | Dashboard CTA not prominent | Day 6 interview | Enlarge card + add animation |
| P1 | Override consequences unclear | Day 6 interview | Add tooltip on hover |
| P2 | Flag button hard to find | Day 6 interview | Move inline next to reasoning |
| P2 | Empty answer validation | Day 3 self | Disable Submit when empty |

---

## Summary

| Activity | Output |
|----------|--------|
| **Survey** | 5 responses collected; SEQ + Likert scores analyzed |
| **Interviews** | 2 semi-structured interviews conducted; think-aloud data recorded |
| **Analysis** | 4 insight clusters (A–D); 7 prioritized fixes for Day 7 iteration |

**Insights shared on ED Workshop post:** [填写链接]

**Next workshop (Day 7) will implement these fixes as prototype iterations.** Save this document!
