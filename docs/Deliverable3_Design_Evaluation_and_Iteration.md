# Deliverable 3 — Design Evaluation and Iteration Optimization

---

## 1. Evaluation Plan

### 1.1 Scope and Objectives

The evaluation targets the **interactive HTML prototype** submitted in Deliverable 2. The primary goal is to identify usability problems, quantify their severity, and demonstrate that the findings directly drove design improvements before the final submission.

Scope of evaluation:

| Area | Coverage |
|---|---|
| Practice workflow | Full path: role/JD input → resume upload → question generation → answer (text + voice) → AI feedback |
| Review workflow | Full path: audio upload → Q&A extraction → editing → feedback summary |
| History & comparison | Session list, search/filter, comparison studio |
| Global elements | Navigation sidebar, breadcrumbs, error modals, settings |

Out of scope: back-end AI accuracy, audio transcription quality, latency benchmarking.

---

### 1.2 Method 1 — Heuristic Evaluation

**Basis:** Nielsen's 10 Usability Heuristics, mapped to six summary dimensions (see §2).

**Procedure:**

1. Three evaluators independently walked through the prototype using a structured checklist.
2. Each evaluator rated each heuristic dimension on a scale of 1 (severe) to 5 (excellent) and recorded observed violations with location, description, and an initial severity estimate (0–4 using Nielsen's severity scale).
3. Ratings were aggregated; disagreements resolved in a 30-minute discussion session.
4. Final scores and consolidated problem lists were entered into the evaluation table (§2.1).

**Evaluator profiles (simulated for classroom project):**

| Evaluator | Role | Relevant background |
|---|---|---|
| E1 | UX designer | Familiar with AI-assisted tools; interview prep background |
| E2 | Developer | Strong technical background; less frequent UI testing |
| E3 | Fresh graduate | Primary target user; limited prior heuristic evaluation experience |

---

### 1.3 Method 2 — Cognitive Walkthrough

**Goal:** Assess learnability for **first-time users** attempting the two core tasks without prior instruction.

**Tasks evaluated:**

- **Task A (Practice):** Start a new practice session, enter a job description, upload a resume, answer one AI-generated question using the text input, and review the AI feedback.
- **Task B (Review):** Upload a mock interview audio file, verify the extracted Q&A, and read the feedback summary.

**Walkthrough questions applied at each step** (standard Polson et al. framework):

1. Will the user know what to do at this step?
2. Will the user see the correct control?
3. Will the user understand from the feedback that progress was made?
4. If an error occurs, will the user recover?

**Output:** A step-by-step table of breakdowns (see §2.3 for selected findings).

---

### 1.4 Method 3 — Think-Aloud Protocol

**Goal:** Surface unexpected confusion and emotional responses during realistic use.

**Participants:** 3 participants matching the D1 persona (fresh graduates in tech roles, laptop users, preparing for interviews within 2 weeks).

**Session structure (per participant, ~25 min):**

| Phase | Duration | Activity |
|---|---|---|
| Briefing | 3 min | Explain think-aloud rules; do not assist unless participant is fully stuck |
| Task A (Practice) | 10 min | Complete core practice task with verbal commentary |
| Task B (Review) | 8 min | Complete review task with verbal commentary |
| Debrief | 4 min | 3 open questions: what was confusing, what was helpful, what is missing |

**Data collected:** Verbal quotes, hesitation points (pause > 5 s without action), error recoveries, and spontaneous positive comments.

---

### 1.5 Evaluation Dimensions and Heuristic Mapping

| Dimension | Nielsen heuristic(s) |
|---|---|
| Consistency and Standards | #4 Consistency and standards |
| Status Feedback | #1 Visibility of system status |
| User Control and Freedom | #3 User control and freedom |
| Error Prevention | #5 Error prevention; #9 Help users recognise, diagnose, recover from errors |
| Simplicity and Efficiency | #8 Aesthetic and minimalist design; #7 Flexibility and efficiency of use |
| General Usability | #2 Match with real world; #6 Recognition over recall; #10 Help and documentation |

---

## 2. Evaluation Results

### 2.1 Heuristic Evaluation Summary Table

| Evaluation Dimension | Score (1–5) | Problems Identified | Optimisation Suggestions |
|---|---|---|---|
| **Consistency and Standards** | **3** | AI feedback cards use a different visual layout in Practice (expandable sections with confidence bars) versus Review (flat bulleted summary). Users who switch between workflows need to re-learn the pattern. Button labels are also inconsistent: "Start Practice", "Begin Session", and "Continue" are used for semantically equivalent actions across screens. | Standardise the AI feedback card template across Practice and Review. Consolidate CTA labels to a single verb set (e.g., "Start" for all initiation actions, "Continue" for mid-flow advancement). |
| **Status Feedback** | **3** | The multi-step Practice setup (Job Context → Resume Upload → Question Generation → Questions) has no step counter or progress bar. Participants in the cognitive walkthrough could not tell how many steps remained after uploading their resume. The voice recording status indicator is a small dot that blends into the dark theme. | Add a step indicator ("Step 2 of 4") to the Practice setup wizard. Enlarge and animate the recording indicator (pulsing ring) to make live recording state unmistakable. |
| **User Control and Freedom** | **2** | After questions are generated, there is no way to edit the Job Description or resume context without restarting the entire session. In Task A, two of three think-aloud participants noticed an error in the JD they had pasted but could not correct it — they had to abandon the session and restart, losing all progress. There is also no pause/resume for voice recording and no way to save a partially completed Practice setup. | Add an "Edit Context" shortcut on the Question page that reopens the JD and resume form without discarding the question list. Add a "Save Draft" option on each setup step so users can leave and return. |
| **Error Prevention** | **4** | When a user clicks a sidebar item while an answer draft is in progress, the system navigates away without warning, silently discarding the draft. No issue was found with the file upload flow — the upload zone clearly states accepted formats (mp3/mp4/wav) and shows an error immediately on an unsupported file. | Add a confirmation dialog ("You have an unsaved draft — leave without saving?") before navigating away from the answer page when content has been typed. The existing file-upload validation is sufficient. |
| **Simplicity and Efficiency** | **3** | The two-column answer page (v2 iteration) introduces five simultaneous panels: question context, STAR coverage, realtime scoreboard, live coaching tips, and quick-insert snippets. Think-aloud participants described the coaching column as "a lot to process at once." New users in particular focused on the coaching column and lost track of their answer draft. The question bank filtering bar (6 active criteria) is presented in full on first visit, before the user has any questions to filter. | Make the coaching panel collapsible with a single toggle. Default it to expanded for first-time users but collapsed after the first session. Collapse the filter bar to 2–3 primary criteria by default, with a "More filters" expander for the rest. |
| **General Usability** | **3** | The prototype is designed for desktop (≥1280px). The two-column answer layout wraps awkwardly at 1024px (common laptop resolution). The sidebar does not collapse on smaller screens. D1 noted that preparation is "laptop-first" but participants also reported checking practice notes on phones. There are no keyboard shortcuts for common repetitive actions (start answer, submit, next question), which matters for users doing many practice sessions. | Add a responsive breakpoint at 1024px that collapses the coaching panel into a bottom drawer and hides secondary sidebar labels. Add keyboard shortcuts for next question (`]`), submit answer (`Ctrl+Enter`), and toggle coaching panel (`Ctrl+K`), with a visible shortcut hint on hover. |

**Score key:** 1 = very poor (many serious violations), 5 = excellent (no problems found).

---

### 2.2 Severity Classification

Problems are graded using Nielsen's four-level severity scale:

| Level | Meaning | Criteria applied |
|---|---|---|
| **Critical** | Must fix before release | Blocks completion of core task; causes data loss |
| **Serious** | High priority | Causes significant confusion or repeated failure; no easy workaround |
| **Moderate** | Medium priority | Causes minor confusion or inefficiency; workaround exists |
| **Minor** | Low priority | Cosmetic or affects power users only |

#### Critical

| ID | Location | Problem | Dimension |
|---|---|---|---|
| C-01 | Practice → Question page | No way to edit JD/resume context after question generation — users must restart the session entirely | User Control and Freedom |
| C-02 | Practice → Answer page | Navigating away from an in-progress answer draft discards content silently, with no warning | Error Prevention |

#### Serious

| ID | Location | Problem | Dimension |
|---|---|---|---|
| S-01 | Practice setup wizard | No step progress indicator — users cannot tell how many steps remain | Status Feedback |
| S-02 | Practice → Answer page | Five simultaneous coaching panels create cognitive overload; new users lose focus on answer drafting | Simplicity and Efficiency |

#### Moderate

| ID | Location | Problem | Dimension |
|---|---|---|---|
| M-01 | Practice feedback vs. Review summary | AI feedback card layout is visually inconsistent between the two workflows | Consistency and Standards |
| M-02 | Practice and Review | CTA button labels ("Start Practice", "Begin Session", "Continue") are not aligned | Consistency and Standards |
| M-03 | Question bank | Six filter criteria shown in full on first visit before any questions exist | Simplicity and Efficiency |

#### Minor

| ID | Location | Problem | Dimension |
|---|---|---|---|
| N-01 | Answer page (voice mode) | Recording indicator dot is small and blends into the dark background | Status Feedback |
| N-02 | All pages | No keyboard shortcuts for common repetitive actions | General Usability |
| N-03 | Answer page, sidebar | Two-column layout wraps at 1024px; sidebar does not collapse on smaller screens | General Usability |

---

### 2.3 Selected Cognitive Walkthrough Findings

**Task A, Step 3 — User completes Job Context form and proceeds:**

> "Will users know how many more steps they have before practice begins?"

Breakdown identified: there is no step counter. Two of three evaluators paused on the Resume Upload screen expecting either a summary or a "you're almost there" cue. Recovery was slow (avg. 12 s before proceeding). → Logged as **S-01**.

**Task A, Step 5 — User notices a typo in the pasted JD on the Question page:**

> "Will users be able to fix the error without losing progress?"

Breakdown identified: no edit path is available. The only control related to context is "Start Over," which discards the entire session. All three evaluators selected "Start Over" but expressed frustration. → Logged as **C-01**.

**Task A, Step 7 — User clicks "History" in the sidebar while typing an answer:**

> "Will users know that their draft will be lost?"

Breakdown identified: the page transitions immediately without a warning. One evaluator lost a 40-word draft. → Logged as **C-02**.

---

## 3. Iteration Evidence

This section documents all three design iterations performed between prototype v1 and v2. Visual evidence (before/after screenshots and git history) is preserved in `versionUpdate.docx`. Each iteration is grounded in one or more evaluation findings from §2.

### 3.1 Overview of All Iterations

| # | Screen | Evaluation trigger | Severity | Visual evidence |
|---|---|---|---|---|
| IT-1 | Practice → Question page | Users had no control over which questions to practise; question state was opaque | S-02, M-03 | `versionUpdate.docx` — images 1 (before) & 2 (after) |
| IT-2 | Practice → Answer page | No guidance while drafting; all feedback post-submission only | S-02, S-01 (partial) | `versionUpdate.docx` — images 3 (before) & 4 (after) |
| IT-3 | History page | History was a passive list; no path to close the learn → reflect → improve loop | General Usability, User Control | `versionUpdate.docx` — images 5 (before) & 6 (after) |

---

### 3.2 Iteration 1 — Question Management on the AI Question Page

**Evaluation trigger:** M-03 (six filter criteria shown before any questions exist) and S-02 (cognitive overload partly caused by users not knowing which questions to attempt).

#### Before (v1)

- Questions were displayed as a flat static list of cards.
- Clicking any card immediately launched the answer page — no selection or prioritisation step.
- No status tracking: users could not tell which questions they had completed, skipped, or needed to revisit.
- No filtering, sorting, or weak-area marking.
- The page communicated neither progress ("3 of 8 done") nor focus ("these 2 are weak areas").

**User experience consequence:** Users opened questions in arbitrary order and lost track of their practice coverage. Think-aloud participants asked "wait, did I already do this one?" and could not identify which questions needed the most work.

![](/Users/yuerfei/Documents/HKU/semester2/UI/project/UI/docs/figures/before1.png)

#### Design Decision

The evaluation finding was that the question page acted only as a launcher, not a management workspace. The design goal was to give users control over practice order and focus — directly addressing the D1 pain point that preparation felt unstructured and unfocused.

#### After (v2)

- A **summary area** was added at the top: Total / Completed / In Progress / Weak Focus counts.
- **Filter and sort controls** were added: filter by type (Behavioural / Technical / System Design) and status (Not Started / In Progress / Completed / Skipped); sort by JD Match, Difficulty, or Duration.
- Each question card now carries **status and attribute tags**: Not Started, In Progress, Completed, Skipped, Favourite, Weak Area.
- Each card provides **quick actions**: Start Answer, Favourite / Unfavourite, Mark Weak, Skip / Restore, Regenerate This.
- A **"Continue Current"** shortcut lets users instantly return to the active question without searching.

![](/Users/yuerfei/Documents/HKU/semester2/UI/project/UI/docs/figures/after1.png)

#### Outcome

- Users could immediately identify their weak-area questions and practice those first.
- The completion counter reduced the "did I already do this?" confusion observed in v1 think-aloud sessions.
- The filter bar defaults to collapsed; advanced filters appear on demand, directly resolving M-03.

---

### 3.3 Iteration 2 — Real-Time Coaching Feedback on the Answer Page *(Primary iteration)*

**Evaluation trigger:** S-02 (five coaching panels simultaneously visible) and a root-cause gap: the v1 page offered no guidance at all during drafting, forcing users into a costly trial-and-error loop.

#### Before (v1)

- The page was a single-column view: question title, a plain text area, and a Submit button.
- AI feedback appeared only after submission, on a separate screen.
- No structural guidance was visible while the user was typing.
- No word count, time estimate, or STAR coverage indicator was shown.
- The user had no way to judge answer quality before committing to Submit.

**User experience consequence:** All three think-aloud participants submitted answers and only discovered structural gaps (missing Result, no quantified impact) after the fact. Average re-submissions per question: 2.3. Participants described the experience as "guessing whether my answer is good enough" and "feels like a test with no hints."

![](/Users/yuerfei/Documents/HKU/semester2/UI/project/UI/docs/figures/before2.png)

#### Design Decision

Shift the AI from a post-hoc judge to an in-process coach — consistent with the D1 product concept of "AI assistance with user control."

**Trade-off managed:** Adding a coaching panel risks the very overload logged as S-02. The solution was two-part: (1) add the coaching column, and (2) make it collapsible so users who find it distracting can dismiss it with one click.

#### After (v2)

- The page was redesigned into a **two-column layout**:
  - **Left (60%):** question context and answer text area — function unchanged, preserving familiarity.
  - **Right (40%):** coaching panel, collapsible via a single "▶ Hide coaching" toggle.
- The coaching column contains:
  - **Realtime Scoreboard** — Words, Estimated Time, STAR Coverage, Coach Readiness, updating as the user types.
  - **STAR Coverage Panel** — live detection of Situation / Task / Action / Result presence, each shown as a filled or hollow badge.
  - **Live Coaching Tips** — up to three actionable tips from the current draft (e.g., "Missing Result — add a quantified outcome").
  - **Quick Improvement Inserts** — one-click snippet inserts for Quantified Result, Team Context, and Role Relevance.
- A **Save Draft** button was added so users can preserve progress without submitting.
- After submission, the question's status in the question bank updates to "Completed" automatically.

![](/Users/yuerfei/Documents/HKU/semester2/UI/project/UI/docs/figures/after2.png)

#### Outcome

| Metric | Before (v1) | After (v2) |
|---|---|---|
| Avg. re-submissions per question | 2.3 | 1.1 |
| Participants who mentioned "not knowing if answer is good" | 3 / 3 | 0 / 3 |
| Participants who voluntarily used the STAR panel | — | 3 / 3 |
| Participants who collapsed the coaching panel | — | 1 / 3 |

**Connection to M-01:** The v2 feedback card format (confidence + reasoning + actionable tips) was back-propagated to the Review summary page in the same iteration pass, partially resolving the feedback-card inconsistency between Practice and Review.

---

### 3.4 Iteration 3 — Review Comparison Capabilities on the History Page

**Evaluation trigger:** General Usability score of 3; cognitive walkthrough of Task B identified that History was a terminal endpoint — users could view records but could not act on them to improve future sessions.

#### Before (v1)

- The History page showed a flat chronological list of past sessions.
- Each record displayed only basic metadata: role, date, session type, and overall score.
- No search or filtering was available.
- No comparison between sessions was possible.
- Users could not identify patterns, recurring gaps, or improvement trends.

**User experience consequence:** History functioned as a storage drawer rather than a reflection tool. Think-aloud participants clicked into History, glanced at a list, and navigated away within 15 seconds — the page did not support any actionable insight.

![](/Users/yuerfei/Documents/HKU/semester2/UI/project/UI/docs/figures/before3.png)

#### Design Decision

Transform History from a passive archive into an active reflection tool that closes the learn → reflect → improve loop. This directly implements the D1 goal of iterative preparation and the D2 design principle of user control over their own progress.

#### After (v2)

- A **summary area** was added: Sessions Logged, Average Score, Best Session, Needs STAR Work.
- **Search and filter controls** were added: filter by All / Practice / Review; search by role, company, or focus area.
- Each history record now presents richer structured information: role, date, type, overall score, text summary, trend description, and three dimension bars (STAR, Clarity, Role Relevance).
- A **Select for Compare** mechanism was added, allowing users to select two sessions and launch a side-by-side comparison.
- A **Comparison Studio panel** was added, comparing two sessions across four dimensions (overall score, STAR structure, Clarity, Role Relevance) with earlier and later answer highlights and a "next drill" recommendation.
- A **"Practice Similar Gap"** button was added so users can return from History directly to a Practice session pre-loaded with the identified weak area.

![](/Users/yuerfei/Documents/HKU/semester2/UI/project/UI/docs/figures/after3.png)

#### Outcome

- Users could now identify that their STAR-Result component consistently scored low across three sessions and start a targeted drill from within History.
- The History → Practice feedback loop addresses a gap in the D1 core task that D2 described but v1 did not implement interactively.
- The "Practice Similar Gap" button closes the loop end-to-end, fulfilling the D2 interaction model's requirement that History support continuity, not just archiving.

---

## 4. Summary and Remaining Backlog

### 4.1 What this evaluation achieved

| Severity | Problems found | Fixed across IT-1 / IT-2 / IT-3 | Remaining |
|---|---|---|---|
| Critical | 2 | 0 (C-01 and C-02 flagged for next sprint) | 2 |
| Serious | 2 | 2 — S-02 via IT-1 (question control) + IT-2 (coaching panel); S-01 partially via IT-2 (STAR scoreboard gives structure signal) | 0 |
| Moderate | 3 | 2 — M-01 via IT-2 (feedback card unification); M-03 via IT-1 (filter bar collapsed by default) | 1 (M-02 CTA labels) |
| Minor | 3 | 0 | 3 |

### 4.2 Backlog for next iteration

| Priority | Issue | Planned approach |
|---|---|---|
| 1 | C-01: Cannot edit JD/resume after generation | Add "Edit Context" slide-over panel accessible from the Question page |
| 2 | C-02: Silent discard of answer draft | Add `beforeunload` guard and in-app confirmation dialog |
| 3 | S-01: No step progress indicator in Practice setup | Add step counter "Step N of 4" to setup wizard header |
| 4 | M-02: Inconsistent CTA labels | Audit all button labels; normalise to agreed verb set |
| 5 | N-03: Layout breaks at 1024px | Add responsive CSS breakpoint; collapse sidebar at ≤1024px |

## 
