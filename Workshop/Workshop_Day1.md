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

## Activity 1 — Mock Contextual Inquiry (10 min)

### Team Roles

| Role | Name |
|------|------|
| Researcher | [填写] |
| Recorder | [填写] |
| Observer(s) | [填写] |

### Interview Responses

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

### Anonymized User Profile

| Field | Details |
|-------|---------|
| Age / Profession | 23, fresh CS graduate seeking front-end / full-stack developer roles |
| Core Usage Scenario | Preparing for specific job interviews using JD + resume context |
| Key Behaviors | Iterative practice (try → review → refine); prefers typing over voice; uses laptop for preparation |
| Core Needs | Role-specific questions; actionable, contextual feedback; ability to track improvement over time |
| Pain Points / Complaints | Generic AI feedback; no reasoning behind scores; AI ignores resume/JD context; can't challenge incorrect evaluations; feels like a "black box" |
| Unmet Expectations | Wants to see AI's reasoning and confidence level; wants to compare answers across sessions; wants to know what the system CAN'T do |

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

Kevin represents our primary user segment: fresh graduates in tech-facing roles who are actively interviewing and need AI-assisted preparation that is **trustworthy, contextual, and iterative**.

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
| **3. Generate Questions** | AI generates role-specific interview questions | 😊 "These questions are actually relevant to React!" | No way to adjust difficulty or focus area | Add **question preference controls** (difficulty, category) |
| **4. Answer Questions** | Types answers; optionally uses voice input | 😐 "Typing is fine, but I wish I could practice speaking too" | Voice recognition fails mid-sentence with no recovery | Provide **graceful fallback** to text input with clear message |
| **5. Review Feedback** | Receives AI evaluation: score + reasoning + confidence | 😫 "Score is 6/10. Reasoning says 'lacks structure' — but what does that mean concretely?" | Feedback reasoning still vague; no example of a "good" answer | Show a **"Strong Answer Example"** alongside feedback |
| **6. Save & Exit** | Ends session; checks History for trends | 😊 "I can see my structure score trending up. But technical depth is still low." | History shows averages but doesn't suggest next steps | Add **smart recommendations** for next practice focus |

### Emotion Curve

```
😊  |      ★2     ★3                                           ★6
😐  | ★1                                          ★4
😫  |                            ★5
    |________________________________________________________
      Onboard  Setup   Generate  Answer   Review     Save
               Context  Questions          Feedback
```

### Key Insights

**Top Pain Points:**
1. Vague feedback (Stage 5) — reasoning lacks concrete examples
2. Voice failure with no recovery (Stage 4) — dead-end breaks flow
3. No next-step guidance after review (Stage 6)

**Top Opportunities:**
1. Show strong answer examples alongside feedback
2. Graceful fallback when voice fails
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

**US-5 — Smart Practice Recommendations** *(from Stage 6)*

> As a **candidate tracking preparation progress**, I want the History page to show **trend charts and recommend my next practice focus** based on weak areas, so that I make the most of limited prep time.

- **Acceptance Criteria:** Line charts for key score categories; recommendation card suggests focus area; clicking starts a new weighted session.

### Priority

| Priority | Story | Rationale |
|----------|-------|-----------|
| P0 | US-1 Contextual Feedback | Core value — without it, feedback is useless |
| P0 | US-3 Challenge Controls | Track A requirement (user control) |
| P0 | US-4 Voice Fallback | Track A requirement (failure handling) |
| P1 | US-2 Strong Answer Examples | High impact on learning |
| P1 | US-5 Smart Recommendations | Supports iterative use |
| P2 | US-6 Iteration Comparison | Nice-to-have for power users |

---

## Take-Home Message

```
Persona (WHO) → Journey Map (HOW) → User Stories (WHAT)
```

> **People come first, then the journey, and then the tasks to be done along the journey.**

- **Persona:** Kevin Li — fresh graduate, skeptical of AI, needs trustworthy feedback
- **Journey Map:** 6 stages from onboarding to save & review — key breakpoint at feedback stage
- **User Stories:** 5 stories covering transparency, user control, graceful degradation, and progress tracking

The next workshop (Day 2) will build on today's outputs. Save this document!
