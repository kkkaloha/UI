# COMP7505 Workshop Day 1 — Completed

**Product:** AI Interview Copilot (InterviewAI)
**Track:** Track A — Smart Adaptive Interfaces
**Team Members:** [填写组员姓名]
**Date:** 2026-04-18

---

## Workshop Overview

In this workshop we conduct short user interviews and turn collected data into **personas**, **user journey maps**, and **user stories**.

Our project focuses on building an **AI Interview Copilot** — a tool that helps fresh graduates prepare for job interviews using AI-generated questions, contextual feedback, and interview recording review.

---

## Activity 1 — User Needs Research (10 min)

### Research Method

We distributed a **5-question survey** to 9 respondents (all CS-related fresh graduates, mostly HKU master's students) to understand their pain points with existing AI interview tools and what they truly need. This is **needs discovery**, not product evaluation — we surveyed users before building anything.

### Survey Findings Summary

**Q1 — When do you use AI interview tools?** (multiple choice)
- BCD (prepare questions, modify answers, pre-interview prep) dominated
- Respondent 3 also mentioned real interview recording review

**Q2 — Most common operations?** (max 2)
- Top: generate questions (A), evaluate/polish answers (B/C)

**Q3 — Biggest pain points?** (top 1–2)
- A: Not sure if AI feedback is reliable
- B: Feedback too generic, not targeted
- C: AI doesn't understand my background
- D: Suggestions feel like "standard answers", not authentic
- E: Don't know whether to adopt AI suggestions

**Q4 — Most frustrating part?** (open-ended, key quotes)
- "Providing context is long and complex — hard to express my situation"
- "AI responses don't sound like what a real person would say"
- "Generated questions lack JD-specific scenario questions"
- "Feedback only gives scores and vague comments, no actionable suggestions"
- "AI only uses templates, doesn't dig into project details like a real interviewer"

**Q5 — Ideal AI interview assistant?** (open-ended, key themes)
- "Like a real person" (7/9 mentioned)
- Deep resume/JD understanding + personalized questions
- Structured, logical feedback with actionable improvements
- Simulate real interview pressure with follow-up probing

### Anonymized User Profile (from survey data)

**Q1: What are the core scenarios where you use this type of product/service?**

> "I mainly use interview prep tools when I get an interview invitation. I need to prepare for a specific role — like a front-end developer position. I'd paste the JD and my resume, and hope the tool gives me questions that actually match that role, not generic 'tell me about yourself' stuff."

> "I record myself doing mock interviews and want to review how I did. Like, did I ramble? Did I answer the question? It's hard to self-evaluate."

**Q2: What are the 3 most frequent actions you take during use?**

> 1. "Inputting the job description and my resume"
> 2. "Practicing answers to AI-generated questions"
> 3. "Reviewing feedback and trying to improve my answer"

**Q3: Which step frustrates you the most? Why?**

> "The feedback is the most frustrating part. It gives me a score like 7/10 but doesn't tell me WHY. It says 'your answer could be more structured' — okay, but HOW? It feels like getting a grade without the rubric."

> "Sometimes the AI clearly didn't read my resume. It asks me things I already addressed in my CV, or gives feedback that contradicts what's in my JD. That breaks trust immediately."

**Q4: What would your ideal user experience look like?**

> "I want the AI to actually understand the role I'm applying for. If it's a React developer role, ask me React-specific questions, not 'what are your strengths.' And when it gives feedback, I want to see the reasoning — like 'your answer lacked a specific example, here's what a stronger version could look like.'"

> "I want to be able to push back on the feedback. If I think the AI is wrong about something, I should be able to flag it, not just accept the score."

### Observer Notes (Non-verbal Cues)

- Interviewee hesitated significantly when discussing AI feedback — suggests deep frustration with current tools
- Leaned forward and spoke faster when describing "ideal experience" — indicates high motivation for a better solution
- Explicitly mentioned "trust" multiple times — this is a core emotional theme
- Used air quotes when saying "feedback" — implies current feedback feels inauthentic

### Anonymized User Profile (from survey data)

| Field | Details |
|-------|---------|
| Age / Profession | 22–24, CS-related fresh graduate (mostly HKU master's students) |
| Core Usage Scenario | Prepare for specific role interviews; refine answers before interview; review mock interview recordings |
| Key Behaviors | Generate questions → practice answers → iterate; use AI for polishing; prepare the night before or morning of interview |
| Core Needs | Role-specific, scenario-based questions; actionable feedback with reasoning; realistic interview simulation with follow-up probing |
| Pain Points / Complaints | Feedback too generic (6/9); AI ignores personal background (4/9); can't simulate real interviewer pressure (5/9); suggestions feel templated, not authentic |
| Unmet Expectations | AI should act like a real interviewer: context-aware, able to probe deeper, and provide trustworthy, actionable feedback (7/9) |

*Full survey data: see `questionnaire.pdf`*

---

## Activity 2 — Build Personas (15 min)

### What is a Persona?

A persona is a fictional yet realistic "character" created to represent a real group of a product's target users. It is built on real user data.

### Our Primary Persona: Kevin Li

#### Demographics

| Attribute | Detail |
|-----------|--------|
| **Name** | Kevin Li |
| **Age** | 23 |
| **Occupation** | Fresh Computer Science graduate |
| **Location** | Hong Kong |
| **Education** | BSc in Computer Science |
| **Job-seeking status** | Actively interviewing for front-end / full-stack developer roles |

#### Background

Kevin graduated six months ago and has been applying to tech companies across Hong Kong and Shenzhen. He has had 4 interviews — passed 1 initial screening, failed 2 technical rounds, declined 1 offer. He prepares intensely before each interview, spending 2–3 hours the night before practicing answers. He currently uses a mix of YouTube mock interview videos and ChatGPT, but finds both lacking — YouTube is passive, and ChatGPT's feedback is too generic and doesn't know his resume or the specific job.

#### Core Goals

1. Practice answering **role-specific** interview questions tailored to the JD and his resume
2. Receive **actionable feedback** with clear reasoning, not just a score
3. Track his **improvement** across multiple practice sessions
4. Feel **confident** that the AI understands his context and isn't giving boilerplate advice

#### Pain Points

| # | Pain Point | Severity |
|---|-----------|----------|
| 1 | AI feedback feels generic — "your answer could be better" without saying HOW | High |
| 2 | No transparency — can't tell if the AI actually read the JD/resume or is guessing | High |
| 3 | Can't push back on wrong evaluations — has to accept whatever score the AI gives | Medium |
| 4 | No way to review past sessions or see progress over time | Medium |
| 5 | Voice input fails frequently, but there's no fallback — just a dead end | Low |

#### Behavioral Traits

- **Device:** Laptop-first (MacBook Pro), occasionally checks phone for interview tips
- **Tech comfort:** High — uses VS Code, GitHub, ChatGPT daily
- **Preparation style:** Iterative — prefers to practice, review, refine, repeat
- **Trust attitude:** Skeptical of AI — wants to see reasoning before accepting advice
- **Time pressure:** Usually prepares the night before or morning of an interview

#### User Quote

> "I don't need the AI to tell me I'm a 7 out of 10. I need it to tell me *why* I'm a 7, and *what specifically* would make it an 8. If I can't trust the feedback, the whole thing is useless."

#### Why This Persona?

Kevin represents our primary user segment: fresh graduates in tech-facing roles who are actively interviewing and need AI-assisted preparation that is **trustworthy, contextual, and iterative**. This persona is grounded in our survey of 9 CS fresh graduates.

---

## Activity 3 — Sketch User Journey Map (15 min)

### Setup

- **Persona:** Kevin Li
- **Core Goal:** Prepare for a React Developer interview using AI-generated questions and receive actionable feedback
- **Emotion Key:** 😊 Positive | 😐 Neutral | 😫 Frustrated

### Journey Map

| Stage | User Action | Emotion & Thoughts | Pain Points | Design Opportunities |
|--------|-------------|-------------------|-------------|---------------------|
| **1. Onboarding** | Signs up and lands on Dashboard | 😐 "Looks clean, but where do I start?" | No clear first-step guidance; empty dashboard feels intimidating | Add a **"Start Your First Practice"** guided card |
| **2. Setup Context** | Inputs job title, pastes JD, uploads resume | 😊 "Good, it's asking for my JD and resume — feels personalized" | No confirmation that AI "understood" the JD; resume upload may fail for non-standard PDFs | Show a **JD/resume summary** after upload for verification |
| **3. Generate Questions** | AI generates role-specific interview questions | 😊 "These questions are actually relevant to React!" | Questions too generic; no scenario-based or JD-specific questions (问卷 3/9); no way to adjust difficulty or focus area | Generate **scenario-based questions from JD**; add **question preference controls** (difficulty, category) |
| **4. Answer Questions** | Types answers; optionally uses voice input | 😐 "Typing is fine, but I wish I could practice speaking too" | Voice recognition fails mid-sentence with no recovery | Provide **graceful fallback** to text input with clear message |
| **5. Review Feedback** | Receives AI evaluation: score + reasoning + confidence | 😫 "Score is 6/10. Reasoning says 'lacks structure' — but what does that mean concretely?" | Feedback reasoning still vague; no example of a "good" answer | Show a **"Strong Answer Example"** alongside feedback |
| **6. Deep Follow-up** | AI asks follow-up questions based on answer | 😊 "This feels like a real interviewer pushing back!" | No follow-up questioning — feels flat, not like real interview pressure (问卷 5/9: 模拟不出真人追问) | Add **AI follow-up probing** based on weak points in the answer |
| **7. Save & Review** | Ends session; checks History for trends and structured summary | 😊 "I can see my structure score trending up. But technical depth is still low." | History shows averages but doesn't suggest next steps | Add **smart recommendations** + **structured performance summary** |
| **8. Recording Review** | Uploads a mock interview recording for analysis | 😐 "I recorded a mock with my friend, can the tool review it?" | No way to review real/mock interview recordings; manual self-review is unreliable (问卷 respondent 3) | **Upload recording → extract Q&A → structured summary** with highlights |

### Emotion Curve

```
😊  |      ★2     ★3                ★6                    ★8
😐  | ★1                                          ★4
😫  |                            ★5
    |________________________________________________________________
      Onboard  Setup   Generate  Answer  Review  Follow-up  Save  Recording
               Context  Questions         Feedback           Review
```

### Key Insights

**Top Pain Points:**
1. Vague feedback (Stage 5) — reasoning lacks concrete examples (问卷 6/9)
2. Questions too generic, not JD-specific (Stage 3) — AI不了解我的背景 (问卷 4/9)
3. Voice failure with no recovery (Stage 4) — dead-end breaks flow
4. No follow-up questioning (Stage 6) — 模拟不出真人面试官的追问深度 (问卷 5/9)
5. No next-step guidance after review (Stage 7)

**Top Opportunities:**
1. Show strong answer examples alongside feedback
2. Generate scenario-based questions from JD + resume
3. Graceful fallback when voice fails
4. AI follow-up probing to simulate real interviewer pressure
5. Smart recommendations based on weak areas
3. Smart recommendations based on weak areas

---

## Activity 4 — Draft User Stories (10 min)

### Template

> As a **[user role]**, I want to **[something]**, so that **[reason / benefit]**

### User Stories (from Journey Map pain points)

**US-1 — Contextual Feedback with Reasoning** *(from Stage 5)*

> As a **job seeker preparing for a specific role**, I want the AI to show **sentence-level reasoning alongside each feedback point** with a confidence indicator, so that I can understand exactly why my answer was rated a certain way and decide whether to trust the feedback.

- **Acceptance Criteria:** Each feedback point links to specific sentences in the answer; confidence badge (High/Medium/Low) visible; clicking feedback highlights the relevant sentence.

**US-2 — Strong Answer Examples** *(from Stage 5)*

> As a **candidate iterating on interview answers**, I want to see a **"Strong Answer Example"** tailored to my JD/resume context alongside each feedback block, so that I have a concrete reference for what an improved response looks like.

- **Acceptance Criteria:** "View Strong Answer" expandable section below each feedback; example is context-aware, not a generic template.

**US-3 — Inline Challenge Controls** *(from Stage 5–6)*

> As a **user receiving AI evaluations**, I want to **flag, override, or undo** any feedback point directly inline, so that I can challenge incorrect evaluations and maintain agency over my own assessment.

- **Acceptance Criteria:** Each feedback point has Flag / Override / Undo actions; flagging opens a text field; overridden scores are visually distinguished.

**US-4 — Graceful Voice Fallback** *(from Stage 4)*

> As a **user practicing with voice input**, I want the system to **automatically fall back to text input** when voice recognition fails, with a clear explanation message, so that I don't lose my practice flow.

- **Acceptance Criteria:** On voice failure, modal says "Voice unavailable — switched to text"; partial transcript preserved in text field; user can retry or continue typing.

**US-5 — Smart Practice Recommendations** *(from Stage 7)*

> As a **candidate tracking preparation progress**, I want the History page to show **trend charts and recommend my next practice focus** based on weak areas, so that I make the most of limited prep time.

- **Acceptance Criteria:** Line charts for key score categories; recommendation card suggests focus area; clicking starts a new weighted session.

**US-6 — JD & Resume Context Awareness** *(from Stage 2–3, 问卷: AI不了解我的背景)*

> As a **job seeker preparing for a specific role**, I want to see a **parsed summary of my JD and resume** after uploading, so that I can verify the AI correctly understands my background before it generates questions or feedback.

- **Acceptance Criteria:** After JD + resume upload, show extracted summary (role, key skills, experience highlights); summary is editable; AI questions/feedback reference the parsed context.

**US-7 — Scenario-Based Question Generation** *(from Stage 3, 问卷: 问题过于泛化)*

> As a **candidate targeting a specific job**, I want the AI to generate **scenario-based questions grounded in the JD** (not generic "tell me about yourself"), so that practice feels realistic and relevant to the actual interview.

- **Acceptance Criteria:** Questions reference JD keywords and resume projects; user can select category (behavioral / technical / system design); difficulty is adjustable.

**US-8 — AI Follow-Up Probing** *(from Stage 6, 问卷: 模拟不出真人追问)*

> As a **user practicing interview answers**, I want the AI to **ask follow-up questions** when my answer is shallow or vague, so that the experience feels like a real interviewer who pushes for depth and catches weak spots.

- **Acceptance Criteria:** After initial answer, AI generates 1–2 follow-up questions based on weak points; follow-up is optional (user can skip); probing depth matches difficulty setting.

**US-9 — Recording Upload & Structured Review** *(from Stage 8, 问卷 respondent 3)*

> As a **candidate who records mock interviews**, I want to **upload a recording and get a structured performance summary**, so that I can review my real/mock interview performance without manual transcription.

- **Acceptance Criteria:** Accept audio/video upload; extract Q&A pairs with editable transcription; show summary highlighting rambles, vague answers, and missed resume references; export to PDF.

### Priority

| Priority | Story | Rationale | Source |
|----------|-------|-----------|--------|
| P0 | US-1 Contextual Feedback | Core value — without it, feedback is useless | Journey Stage 5 |
| P0 | US-3 Challenge Controls | Track A requirement (user control) | Track A spec |
| P0 | US-4 Voice Fallback | Track A requirement (failure handling) | Track A spec |
| P0 | US-6 Context Awareness | Trust foundation — 4/9 问卷: AI不了解背景 | 问卷 Q3 |
| P1 | US-2 Strong Answer Examples | High impact on learning — 7/9 most valued feature | 问卷 Q5 |
| P1 | US-5 Smart Recommendations | Supports iterative use | Journey Stage 7 |
| P1 | US-7 Scenario-Based Questions | 3/9 问卷: 问题过于泛化 | 问卷 Q3-Q4 |
| P1 | US-8 Follow-Up Probing | 5/9 问卷: 模拟不出真人追问 | 问卷 Q4-Q5 |
| P2 | US-9 Recording Review | Secondary flow — valuable but not core | 问卷 respondent 3 |

---

## Take-Home Message

```
Persona (WHO) → Journey Map (HOW) → User Stories (WHAT)
```

> **People come first, then the journey, and then the tasks to be done along the journey.**

- **Persona:** Kevin Li — fresh graduate, skeptical of AI, needs trustworthy feedback
- **Journey Map:** 8 stages from onboarding to recording review — key breakpoints at feedback & follow-up stages
- **User Stories:** 9 stories covering transparency, user control, graceful degradation, context awareness, realistic simulation, and progress tracking

The next workshop (Day 2) will build on today's outputs. Save this document!
