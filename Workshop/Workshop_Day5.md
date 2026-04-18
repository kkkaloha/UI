# COMP7505 Workshop Day 5 — Completed

**Product:** AI Interview Copilot (InterviewAI)
**Track:** Track A — Smart Adaptive Interfaces
**Team Members:** [填写组员姓名]
**Date:** 2026-04-18

---

## Activity 1 — Test Objective Setting (15 min)

### Step 1: Scenario Detection

3 core scenarios: **2 normal + 1 abnormal**.

| Type | Scenario | Description |
|------|----------|-------------|
| Normal 1 | **Practice Flow — JD/Resume Context Feedback** | User inputs a JD + uploads resume → AI generates role-specific questions → user answers → receives score with reasoning + confidence |
| Normal 2 | **Review Flow — Recording Upload & Extraction** | User uploads an interview recording → system extracts Q&A → user edits transcription → views structured performance summary |
| Abnormal | **Voice Failure Fallback** | User attempts voice input → recognition fails → system falls back to text mode with partial transcript preserved |

### Step 2: Objective Writing

Template: **Action + Test Object + Feedback to Collect + Final Judgment**

**Objective 1 (Normal — Practice):**

> Verify the **clarity and actionability** of the Practice Feedback screen, collect user feedback on whether the **sentence-level reasoning, confidence badge, and strong answer example** are easy to understand and useful for improvement, and confirm whether the feedback design needs to be simplified or supplemented with additional explanation.

**Objective 2 (Normal — Review):**

> Verify the **efficiency** of the Review Upload & Analysis flow, collect user feedback on whether the **drag-drop upload, extraction progress, and editable Q&A editing** feel intuitive and smooth, and confirm whether the extraction workflow needs fewer steps or clearer progress communication.

**Objective 3 (Abnormal — Voice Failure):**

> Verify the **graceful degradation** behavior when voice recognition fails, collect user feedback on whether the **failure modal message, auto-switch to text, and preserved partial transcript** reduce frustration and maintain practice flow, and confirm whether the fallback mechanism needs to be more prominent or offer different recovery options.

### Step 3: Objective Calibration

> Peer calibration notes (to be completed in class):
> - [ ] Objective 1: Is "clarity and actionability" specific enough? → Yes, tied to 3 concrete UI elements
> - [ ] Objective 2: Is "efficiency" measurable? → Should add time-to-completion benchmark
> - [ ] Objective 3: Is "graceful degradation" too abstract? → Rewritten to reference specific modal and transcript behavior

---

## Activity 2 — Survey Design (15 min)

### Questionnaire Link

> [填写问卷链接，推荐用 Google Forms / Qualtrics / 问卷星]

### Design Principles

- Completion time: **≤ 10 minutes**
- Mix **quantitative (rating scales)** + **qualitative (open-ended)**
- Include lightweight industry metric: **SEQ (Simplified Ease of Question)**

### Questionnaire

#### Part 1: Basic Profile

| # | Question | Type |
|---|----------|------|
| 1 | What is your age range? | Multiple choice (18–22 / 23–26 / 27–30 / 30+) |
| 2 | What is your current status? | Multiple choice (Student / Fresh graduate / Working professional) |
| 3 | Have you used any AI-assisted interview preparation tools before? | Multiple choice (Yes / No) |
| 4 | How many job interviews have you had in the past year? | Multiple choice (0 / 1–3 / 4–6 / 7+) |

#### Part 2: Usability Ratings

**After completing Practice Flow (Scenario 1):**

| # | Question | Type |
|---|----------|------|
| 5 | How easy was it to input your JD and resume? | SEQ (1 = Very difficult → 7 = Very easy) |
| 6 | How understandable was the AI feedback (reasoning + confidence)? | Likert 1–5 (Strongly disagree → Strongly agree) |
| 7 | The strong answer example helped me understand how to improve. | Likert 1–5 |
| 8 | I felt I could challenge or override AI feedback when I disagreed. | Likert 1–5 |

**After completing Review Flow (Scenario 2):**

| # | Question | Type |
|---|----------|------|
| 9 | How easy was it to upload and extract the interview recording? | SEQ (1–7) |
| 10 | The extracted Q&A was accurate enough to review. | Likert 1–5 |
| 11 | The performance summary clearly highlighted my strengths and weaknesses. | Likert 1–5 |

**After Voice Failure (Scenario 3):**

| # | Question | Type |
|---|----------|------|
| 12 | How clearly did the system communicate the voice failure? | SEQ (1–7) |
| 13 | The fallback to text input felt smooth and didn't interrupt my flow. | Likert 1–5 |

#### Part 3: Open Feedback

| # | Question | Type |
|---|----------|------|
| 14 | What was the most confusing or frustrating part of the experience? | Open text |
| 15 | What feature or information did you wish was available but wasn't? | Open text |
| 16 | Any other suggestions for improving the tool? | Open text |

---

## Activity 3 — Usability Study Design: Semi-structured Interview (25 min)

### Step 1: Informed Consent Form

> Consent form link: [填写]
>
> Template reference:
> - HKU Research Service: https://www.rss.hku.hk/integrity/ethics-compliance/hrec-forms
> - NNg Example: https://media.nngroup.com/media/articles/attachments/NNg_Example_Consent_Form.pdf

**Key consent points:**
- Participation is voluntary; participant can withdraw at any time
- Session will be recorded (screen + audio) for analysis only
- Data is anonymized; no personally identifiable information will be published
- Estimated duration: 30–40 minutes
- No right or wrong answers — we are testing the system, not the participant

### Step 2: Usability Study Script

#### A. Introduction + Consent (2 min)

> "Thank you for participating! We're testing an AI Interview Preparation tool. You'll be asked to complete a few tasks using a prototype. There are no wrong answers — we want to find problems with the design, not with you. Before we start, please read and sign this consent form. Do you have any questions?"

#### B. Background Knowledge (2 min)

| Question | Purpose |
|----------|---------|
| "What's your current job-seeking status?" | Verify they match our persona |
| "Have you practiced for interviews before? How?" | Understand their preparation habits |
| "Have you used AI tools for interview prep?" | Gauge prior experience with similar products |

#### C. Think-Aloud Training (1 min)

> "During the tasks, I'd like you to **think out loud** — say whatever comes to mind as you use the tool. For example, if you're looking for a button, say 'I'm looking for the start button.' If something is confusing, say 'I'm not sure what this means.' This helps us understand your thought process. Don't worry about being polite — honest feedback is the most helpful."

#### D. Tasks + Post-task Questions (20 min)

**Task 1: Practice Flow (10 min)**

> "Imagine you just received an interview invitation for a React Developer role at a fintech startup. Please use the tool to prepare for this interview. Start from the Dashboard and go through the practice flow. Remember to think out loud."

Post-task questions:
1. "Was there any point where you felt unsure about what to do next?"
2. "How did you feel about the AI feedback? Was it helpful? Trustworthy?"
3. "Did you notice the confidence indicator? What did it mean to you?"
4. "Would you have wanted to challenge any of the feedback? Did you see how?"

**Task 2: Review Flow (5 min)**

> "Now imagine you recorded a mock interview with a friend. Upload this sample recording and review your performance."

Post-task questions:
1. "How easy was it to upload and get the Q&A extracted?"
2. "Was the performance summary clear? Did it tell you what to improve?"
3. "What would you do next after seeing this summary?"

**Task 3: Voice Failure (3 min)**

> "Now try answering a question using voice input. We'll simulate a recognition failure."

Post-task questions:
1. "What happened when voice failed? Did you understand the message?"
2. "How did you feel about the switch to text input?"
3. "Was your partial answer preserved?"

#### E. Data Collection

| Data Type | Method | What It Measures |
|-----------|--------|------------------|
| Task completion time | Timer (start → end per task) | Efficiency |
| Error clicks | Screen recording analysis | Navigation confusion |
| Think-aloud transcript | Audio recording | Cognitive process, pain points |
| SEQ scores | Post-task questionnaire | Perceived ease of use |
| Likert ratings | Post-task questionnaire | Specific feature satisfaction |
| Open responses | Post-task questionnaire | Unstructured feedback |

#### F. Post-study Questions + Closing (3 min)

1. "Overall, how would you rate your experience with this tool on a scale of 1–10?"
2. "Would you use this tool to prepare for a real interview? Why or why not?"
3. "What's the ONE thing you would change about this tool?"
4. "Any other comments?"

> "Thank you so much for your time and honest feedback! Your input will directly shape the next version of this tool."

---

## Summary

| Activity | Output |
|----------|--------|
| **Test Objectives** | 3 test objectives (2 normal + 1 abnormal scenario) |
| **Survey** | 16-question questionnaire (4 profile + 9 rating + 3 open) |
| **Usability Study Script** | Full semi-structured interview script with 3 tasks, post-task questions, and data collection plan |

**Save this document — the next session will use the survey and script to conduct actual usability testing!**
