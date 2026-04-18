# InterviewAI Prototype Iteration Log

## Document Information

| Item | Content |
|---|---|
| Project | InterviewAI |
| Prototype File | `index.html` |
| Iteration Version | v2 |
| Iteration Date | 2026-04-15 |
| Record Type | Before/After Comparison and Version Iteration Log |

---

## Iteration Goals

This iteration focused on improving three core areas of the prototype:

1. Add question management capabilities to the AI question page
2. Add real-time coaching feedback to the answer page
3. Add review comparison capabilities to the History page

The update was implemented directly in the existing single-file high-fidelity prototype `index.html`. The purpose was not to change the product concept, but to upgrade several previously presentation-oriented screens into a more realistic interactive prototype.

---

## Version Overview

### Characteristics Before the Update

- The prototype already contained a complete page structure, including Dashboard, Practice, Review, History, and Settings.
- The visual fidelity of the interface was already relatively high.
- However, some key features were still closer to a static demonstration than a realistic product interaction flow.
- Users could navigate between screens, but there was limited interaction depth in question management, in-progress answer guidance, and history-based reflection.

### Characteristics After the Update

- The prototype was upgraded from a mainly static click-through demo into a more state-driven interactive prototype.
- Users can now filter, mark, favorite, skip, and regenerate questions on the AI question page.
- Users receive live structural feedback, word/time estimation, STAR coverage updates, and coaching prompts while drafting answers.
- Users can search, filter, and compare two past records in the History page to support reflection and progress tracking.

---

## Iteration Item 1: Add Question Management to the AI Question Page

### Before

- The question page displayed AI-generated questions as static cards.
- Users could click a question card and immediately enter the answer page.
- There was no real classification or status management for questions.
- The page did not support favoriting, skipping, marking weak questions, or regenerating an individual question.
- The interface did not clearly communicate progress, such as how many questions had been completed or which ones needed repeated practice.

### After

- A summary area was added to show:
  - Total questions in the bank
  - Number of completed questions
  - Number of in-progress questions
  - Number of weak-focus questions
- Filtering and sorting options were added:
  - Filter by type: Behavioral / Technical / System Design
  - Filter by status: Not Started / In Progress / Completed / Skipped
  - Sort by: JD Match, Difficulty, Duration
- Each question now includes status and attribute tags:
  - Not Started
  - In Progress
  - Completed
  - Skipped
  - Favorite
  - Weak Area
- Each question now provides quick actions:
  - Start Answer
  - Favorite / Unfavorite
  - Mark Weak
  - Skip / Restore
  - Regenerate This
- A “Continue Current” action was added so users can quickly return to the currently active question.

### Improvement Value

- The page evolved from “AI gives a list of questions and the user opens them one by one” to “the user manages and prioritizes a practice question bank.”
- This increases user control over practice order and focus.
- It better supports repeated practice and targeted weak-area improvement, which are important for interview preparation workflows.

---

## Iteration Item 2: Add Real-Time Coaching Feedback to the Answer Page

### Before

- The answer page mainly contained the question title, input mode switch, a text area, and a submit button.
- AI feedback only appeared after the answer was submitted.
- Users had no way to tell whether their answer structure was complete while typing.
- The page did not provide process-level feedback such as word count, estimated length, structure coverage, or keyword relevance.

### After

- The page was redesigned into a two-column layout:
  - Left side for question context and answer drafting
  - Right side for real-time feedback and coaching
- A Realtime Scoreboard was added to display:
  - Words
  - Estimated Time
  - STAR Coverage
  - Coach Readiness
- A STAR Coverage panel was added to detect whether the answer contains:
  - Situation
  - Task
  - Action
  - Result
- A Live Coaching panel was added to provide dynamic suggestions during typing, such as:
  - Missing Result
  - Missing teamwork or stakeholder context
  - Weak role relevance
  - Answer too short or too long
  - For technical questions, missing trade-off or performance discussion
- A Quick Improvement Inserts panel was added so users can instantly insert enhancement snippets, including:
  - Quantified Result
  - Team Context
  - Role Relevance
- A Save Draft button was added so users can preserve progress before submitting.
- After submission, the question status is updated to Completed and the question list reflects this change.

### Improvement Value

- The experience changed from “users only discover problems after submission” to “users receive coaching while drafting.”
- This reduces trial-and-error cost during practice.
- It also shifts the AI from being only a scoring tool to being a process-oriented interview coach, which better matches the product concept.

---

## Iteration Item 3: Add Review Comparison Capabilities to the History Page

### Before

- The History page only displayed a simple list of past records.
- Users could only see basic metadata such as role, date, type, and score.
- There was no search or filtering.
- Users could not compare two sessions or view changes across dimensions.
- As a result, History functioned more like a storage page than a reflection page.

### After

- A summary area was added to display:
  - Sessions Logged
  - Average Score
  - Best Session
  - Needs STAR Work
- Search and filtering capabilities were added:
  - Filter by All / Practice / Review
  - Search by role, company, or focus area
- Each history record now presents richer structured information:
  - Role and company
  - Session type
  - Date
  - Practice focus
  - Overall score
  - Text summary
  - Trend description
  - Three dimension bars for STAR, Clarity, and Role Relevance
- A Select for Compare mechanism was added:
  - Users can select two sessions for comparison
  - Users can clear the comparison state
- A Comparison Studio panel was added to compare two sessions with:
  - Overall score change
  - STAR structure change
  - Clarity change
  - Role relevance change
  - Earlier answer highlight
  - Later answer highlight
  - Progress, recurring gap, and next drill recommendations
- A Practice Similar Gap button was added so users can return from History to Practice and work on the identified weak area.

### Improvement Value

- The page evolved from “viewing old records” to “analyzing learning progress.”
- History is no longer a passive archive; it becomes an active reflection tool.
- This creates a stronger learning loop: review history, identify gaps, and return to practice.

---

## Overall Structural Changes Across Pages

### Before

- The Questions, Answer, and History pages were mainly composed of relatively static information cards.
- The pages could navigate to one another, but state linkage across them was limited.
- The prototype emphasized flow presentation more than stateful interaction.

### After

- The Questions page now includes question data state and filtering logic.
- The Answer page now includes real-time calculation and live coaching logic.
- The History page now includes comparison state management and a reflection panel.
- Stronger page-to-page linkage was introduced:
  - Question status changes based on saving and submitting answers
  - Completed answers support moving to the next question
  - Weak areas identified in History can feed back into Practice

---

## Technical Implementation Summary

This iteration still preserves the single-file prototype structure. The main updates were implemented directly in `index.html`, including:

- Extending CSS to support:
  - Question management UI
  - Real-time answer feedback UI
  - History comparison UI
- Refactoring the HTML structure of the Questions, Answer, and History sections
- Adding new front-end state and interaction logic, including:
  - `questionBank`
  - `historyRecords`
  - `questionFilters`
  - `historyFilters`
  - `selectedHistoryIds`
- Adding core interactive functions such as:
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

## Conclusion of This Version

This iteration did not change the core product direction of InterviewAI. Instead, it strengthened three important areas within the existing high-fidelity prototype:

1. User control over question practice management
2. Real-time guidance during answer drafting
3. Reflective comparison of past performance

Compared with the previous version, this prototype now better represents the interaction logic of a realistic product and more clearly expresses the design idea of “AI assistance with user control.”

---

## Possible Next Iteration Directions

- Make the feedback page scores dynamically respond to the current answer instead of remaining fixed
- Add trend charts and weak-area statistics to the History page
- Add batch planning capabilities to the Questions page
- Add simulated live transcription for voice mode on the Answer page

