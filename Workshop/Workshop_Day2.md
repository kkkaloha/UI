# COMP7505 Workshop Day 2 — Completed

**Product:** AI Interview Copilot (InterviewAI)
**Track:** Track A — Smart Adaptive Interfaces
**Team Members:** [填写组员姓名]
**Date:** 2026-04-18

---

## Activity 1 — Card Sorting (20 min)

### Step 1: Requirement Extraction

From Day 1 User Stories, extract core functions:


| #    | User Story (source)                | Core Function            |
| ---- | ---------------------------------- | ------------------------ |
| US-1 | Contextual feedback with reasoning | AI Evaluation & Feedback |
| US-2 | Strong answer examples             | Answer Reference         |
| US-3 | Inline challenge controls          | Feedback Control         |
| US-4 | Graceful voice fallback            | Voice Input              |
| US-5 | Smart practice recommendations     | Progress Tracking        |
| —    | JD + resume input                  | Job Context Setup        |
| —    | AI-generated questions             | Question Generation      |
| —    | Text answer input                  | Answer Submission        |
| —    | Upload recording                   | Recording Upload         |
| —    | Extract Q&A from recording         | Recording Analysis       |
| —    | View past sessions                 | History Review           |
| —    | Account & preferences              | Settings                 |


### Step 2: Card Decomposition

Break each core function into sub-functions (one per card):

**A. Job Context Setup**

- A1 Input job title
- A2 Paste job description (JD)
- A3 Upload resume (PDF)
- A4 View JD/resume parsing summary
- A5 Edit parsed context

**B. Question Generation**

- B1 Generate questions from JD + resume
- B2 Select question category (behavioral / technical / system design)
- B3 Adjust difficulty level
- B4 View question one at a time
- B5 Skip a question
- B6 Request more questions

**C. Answer Submission**

- C1 Type answer (text input)
- C2 Record answer (voice input)
- C3 Voice-to-text fallback when recognition fails
- C4 Save draft answer
- C5 Revise and resubmit answer

**D. AI Evaluation & Feedback**

- D1 View overall score
- D2 View sentence-level reasoning
- D3 View confidence indicator (High / Medium / Low)
- D4 View strong answer example
- D5 Compare my answer with strong answer

**E. Feedback Control (Track A)**

- E1 Flag a feedback point
- E2 Add note explaining disagreement
- E3 Override AI score
- E4 Undo override (restore AI score)
- E5 Discard entire evaluation

**F. Recording Upload & Analysis**

- F1 Upload audio/video file
- F2 View extraction progress
- F3 Edit extracted Q&A pairs
- F4 View audio quality warning
- F5 Retry extraction on failure

**G. Review Summary**

- G1 View structured performance summary
- G2 Highlight rambles / vague answers
- G3 Identify missed resume references
- G4 Export summary (PDF)

**H. History & Progress**

- H1 Browse past practice sessions
- H2 View score trend charts
- H3 View recommendation for next focus area
- H4 Start new session from recommendation

**I. Settings**

- I1 Edit profile (name, target role)
- I2 Manage uploaded resumes
- I3 Set default question preferences
- I4 Toggle voice input on/off
- I5 Account & privacy settings

### Step 3: Classification Sorting

Group sub-function cards by logical relevance into modules:


| Module        | Cards Included                    | Rationale                                                               |
| ------------- | --------------------------------- | ----------------------------------------------------------------------- |
| **Dashboard** | H1, H2, H3, H4                    | Entry point; shows history overview and next-step recommendations       |
| **Practice**  | A1–A5, B1–B6, C1–C5, D1–D5, E1–E5 | Core practice flow: setup → generate → answer → feedback → control      |
| **Review**    | F1–F5, G1–G4                      | Upload recording → analyze → structured summary                         |
| **History**   | H1–H4                             | Detailed session archive with trends (separate from dashboard snapshot) |
| **Settings**  | I1–I5                             | Account and preference management                                       |


### Step 4: Hierarchy — Information Architecture (Page Tree)

```
InterviewAI
├── Dashboard
│   ├── Welcome Card ("Start Your First Practice")
│   ├── Recent Sessions (last 3)
│   ├── Score Trend Charts (mini)
│   └── Smart Recommendation Card
│
├── Practice
│   ├── Step 1: Job Context
│   │   ├── Input Job Title
│   │   ├── Paste JD
│   │   ├── Upload Resume
│   │   └── Review Parsed Summary
│   ├── Step 2: Questions
│   │   ├── View Current Question
│   │   ├── Category / Difficulty Controls
│   │   └── Skip / Request More
│   ├── Step 3: Answer
│   │   ├── Text Input Area
│   │   ├── Voice Record Button
│   │   └── Voice Fallback Modal
│   ├── Step 4: Feedback
│   │   ├── Overall Score + Confidence
│   │   ├── Sentence-Level Reasoning
│   │   ├── Strong Answer Example
│   │   ├── Compare Versions
│   │   └── Flag / Override / Undo Controls
│   └── Step 5: Next or Save
│       ├── Next Question
│       └── Save & Exit to Dashboard
│
├── Review
│   ├── Step 1: Upload Recording
│   │   ├── Drag & Drop / File Picker
│   │   └── Audio Quality Warning (if low)
│   ├── Step 2: Extract & Edit Q&A
│   │   ├── Extraction Progress Bar
│   │   ├── Edit Transcription
│   │   └── Retry on Failure
│   ├── Step 3: Summary
│   │   ├── Performance Overview
│   │   ├── Ramble / Vague Highlights
│   │   ├── Missed Resume References
│   │   └── Export PDF
│   └── Follow-Up: Start Practice (link to Practice)
│
├── History
│   ├── Session List (filterable)
│   ├── Session Detail
│   │   ├── Questions & Answers
│   │   ├── Scores & Feedback
│   │   └── User Flags / Overrides
│   ├── Score Trend Charts (full)
│   └── Recommendation Card → Start Session
│
└── Settings
    ├── Profile (name, target role)
    ├── Resumes (manage uploads)
    ├── Question Preferences (defaults)
    ├── Voice Input Toggle
    └── Account & Privacy
```

---

## Activity 2 — Sketch Low-Fidelity Wireframe & Prototype (40 min)

### Wireframe vs Prototype


| Dimension        | Wireframe                                           | Prototype                                                              |
| ---------------- | --------------------------------------------------- | ---------------------------------------------------------------------- |
| **Status**       | Static draft, view-only, no interaction             | Interactive, clickable, navigable                                      |
| **Interaction**  | None                                                | Clickable with pop-ups, state changes & page transitions               |
| **Visual Style** | Monochrome lines, simple boxes & text               | Low-fi: wireframe + interactions; High-fi: full colors, icons, real UI |
| **Core Purpose** | Define layout, element position & content hierarchy | Test user flows, verify usability, complete task journeys              |


### Tool: Figma

> Team Figma link: [填写 Figma 文件链接]

### Wireframe Sketches

#### Screen 1: Dashboard

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

#### Screen 2: Practice — Step 1: Job Context

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

#### Screen 3: Practice — Step 4: Feedback

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

#### Screen 4: Review — Upload & Analysis

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

#### Screen 5: History

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

### Prototype Navigation Map

```
Dashboard ──────────────────────────────────────────────
  │
  ├── [Start Practice] → Practice Step 1 (Job Context)
  │                         │
  │                         ├── [Next] → Step 2 (Questions)
  │                         │              │
  │                         │              ├── [Next] → Step 3 (Answer)
  │                         │              │              │
  │                         │              │              ├── Voice Fallback Modal (on error)
  │                         │              │              │
  │                         │              │              └── [Submit] → Step 4 (Feedback)
  │                         │              │                              │
  │                         │              │                              ├── [Flag/Override/Undo] (inline)
  │                         │              │                              ├── [View Strong Answer] (expand)
  │                         │              │                              ├── [Revise] → back to Step 3
  │                         │              │                              └── [Next Question] → Step 2
  │                         │              │                                           or
  │                         │              │                              [Save & Exit] → Dashboard
  │                         │              │
  │                         │              └── [Skip] → next question
  │                         │
  │                         └── [Edit Summary] → inline edit
  │
  ├── [Start Review] → Review Step 1 (Upload)
  │                       │
  │                       ├── Audio Quality Warning (if low)
  │                       │
  │                       └── [Generate] → Step 2 (Extract & Edit)
  │                                          │
  │                                          ├── Extraction Failure Modal → [Retry]
  │                                          │
  │                                          └── [Generate Summary] → Step 3 (Summary)
  │                                                                  │
  │                                                                  ├── [Export PDF]
  │                                                                  └── [Practice These] → Practice Step 1
  │
  └── [View History] → History
                         │
                         ├── [Session Detail] → expand
                         └── [Start Focused Session] → Practice Step 1
```

---

## Summary


| Activity                  | Output                                                        |
| ------------------------- | ------------------------------------------------------------- |
| **Card Sorting**          | 9 function groups → 5 top-level modules → full IA page tree   |
| **Wireframe & Prototype** | 5 key screen sketches + navigation map (to be built in Figma) |


**Next step:** Build interactive prototype in Figma based on these wireframes and the navigation map above.