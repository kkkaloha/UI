# COMP7505 Workshop Day 4 — Completed

**Product:** AI Interview Copilot (InterviewAI)
**Track:** Track A — Smart Adaptive Interfaces
**Team Members:** [填写组员姓名]
**Date:** 2026-04-18

---

## Activity 1 — From Google Stitch to Figma (45 min)

### Step 1: Migration

| Step | Action |
|------|--------|
| 1 | Open Google Stitch project |
| 2 | Select pages to export: Dashboard, Practice Feedback, Review Upload |
| 3 | Click **Export** → Choose **Figma** → Click **Convert** |
| 4 | Open Figma → New design file → **Paste** |

### Step 2: Figma Prototype Link

> [填写 Figma 文件链接，确保 Comment 权限已开启]

### Step 3: Interactive Enhancements

#### Page Jumps (Linked Interactions)

| From Screen | Element | Trigger | To Screen | Transition |
|-------------|---------|---------|-----------|------------|
| Dashboard | "Start Your First Practice" card | Click | Practice Step 1 (Job Context) | Slide left |
| Practice Step 1 | [Next → Generate] button | Click | Practice Step 2 (Questions) | Slide left |
| Practice Step 2 | [Skip] button | Click | Practice Step 2 (next question) | Fade |
| Practice Step 3 (Answer) | [Submit] button | Click | Practice Step 4 (Feedback) | Slide left |
| Practice Step 3 | Voice failure auto-trigger | Timeout | Voice Failure Modal | Fade overlay |
| Practice Step 3 | Modal [Switch to Text] | Click | Practice Step 3 (text mode) | Modal close |
| Practice Step 4 (Feedback) | [Revise Answer] button | Click | Practice Step 3 (Answer) | Slide right |
| Practice Step 4 | [Next Question →] button | Click | Practice Step 2 (Questions) | Slide left |
| Practice Step 4 | [Save & Exit] button | Click | Dashboard | Slide right |
| Practice Step 4 | [Flag] button | Click | Flag inline panel (expand) | Expand |
| Practice Step 4 | [Override Score] button | Click | Override input (inline) | Expand |
| Practice Step 4 | [Undo] button | Click | Original score restored | Swap |
| Practice Step 4 | [View Strong Answer] | Click | Strong answer section (expand) | Expand |
| Review Step 1 | Upload zone (drag file) | Drop | Review Step 2 (Extract & Edit) | Slide left |
| Review Step 1 | Audio quality warning | Auto | Warning banner appears | Fade in |
| Review Step 2 | [Retry] button (on failure) | Click | Review Step 2 (re-extract) | Loading spinner |
| Review Step 2 | [Generate Summary] button | Click | Review Step 3 (Summary) | Slide left |
| Review Step 3 | [Export PDF] button | Click | Download confirmation toast | Fade |
| Review Step 3 | [Practice These] button | Click | Practice Step 1 (Job Context) | Slide left |
| Dashboard | Session card | Click | History (session detail) | Slide left |
| History | [Start Focused Session] button | Click | Practice Step 1 | Slide left |
| Any screen | Sidebar item | Click | Corresponding module | Instant |

#### Interactive States Added

| Element | Normal | Hover | Active / Pressed |
|---------|--------|-------|-------------------|
| Primary button | Gradient purple | Brightness +10%, shadow glow | Scale 0.98 |
| Ghost button | Transparent border | Border + background tint | Scale 0.98 |
| Sidebar nav item | Text muted | Background tint | Gradient highlight + underline |
| Session card | Subtle border | Border purple glow, lift 2px | Scale 0.99 |
| Flag / Override / Undo | Text link | Underline + purple | Background tint |
| Upload zone | Dashed border | Border solid, background tint | — |
| Confidence badge | Colored background | — | — |

#### Visual Details Fixed in Figma

| Issue (from Stitch output) | Fix Applied |
|-----------------------------|-------------|
| Card border-radius inconsistent (some 12px, some 16px) | Unified to 16px |
| Score trend chart missing axis labels | Added category labels below bars |
| Voice failure modal had no close button | Added [×] top-right + [Switch to Text] CTA |
| Feedback reasoning bullets had no left margin | Added 1rem left padding |
| Sidebar active state missing underline | Added gradient underline bar |
| Upload zone drag state not shown | Added hover + active states |

---

## Activity 2 — Peer Evaluation (15 min)

### Team Pairing

| Our Group | Paired Group |
|-----------|-------------|
| InterviewAI (our team) | [填写对方组名] |
| Our Figma link | [填写] |
| Their Figma link | [填写] |

### Roles

| Role | Name |
|------|------|
| Presenter (our side) | [填写] |
| Evaluator (our side) | [填写] |

### Evaluation of Their Prototype

> [根据实际互评结果填写]

| # | Problem Identified | Evaluation Dimension | Optimization Suggestion |
|---|--------------------|---------------------|------------------------|
| 1 | [填写] | [维度] | [建议] |
| 2 | [填写] | [维度] | [建议] |
| 3 | [填写] | [维度] | [建议] |

### Feedback Received on Our Prototype

> [根据对方组的反馈填写]

| # | Problem Identified | Evaluation Dimension | Optimization Suggestion | Priority |
|---|--------------------|---------------------|------------------------|----------|
| 1 | [填写] | [维度] | [建议] | [P0/P1/P2] |
| 2 | [填写] | [维度] | [建议] | [P0/P1/P2] |
| 3 | [填写] | [维度] | [建议] | [P0/P1/P2] |

### Combined Issue Tracker (Day 3 Self-Eval + Day 4 Peer-Eval)

| # | Source | Dimension | Issue | Suggestion | Priority | Status |
|---|--------|-----------|-------|-----------|----------|--------|
| 1 | Day 3 self | Status Feedback | Voice failure — no error state | Add failure modal with fallback | P0 | Pending |
| 2 | Day 3 self | Error Prevention | Empty answer can be submitted | Disable Submit when empty | P0 | Pending |
| 3 | Day 3 self | Error Prevention | No upload file type restriction | Restrict file picker to .pdf | P1 | Pending |
| 4 | Day 3 self | Status Feedback | No parsing/generation loading indicator | Add spinner + progress text | P1 | Pending |
| 5 | Day 3 self | User Control | No exit confirmation during practice | Add "Leave?" dialog | P1 | Pending |
| 6 | Day 3 self | User Control | Undo button too small | Place Undo next to overridden score | P2 | Pending |
| 7 | Day 3 self | Simplicity | Dashboard trend overload | Show top 2 only, full in History | P2 | Pending |
| 8 | Day 3 self | Simplicity | No keyboard shortcuts | Add Enter/Ctrl+Z/Esc | P2 | Pending |
| 9 | Day 4 peer | [填写] | [填写] | [填写] | [填写] | Pending |
| 10 | Day 4 peer | [填写] | [填写] | [填写] | [填写] | Pending |

---

## Summary

| Activity | Output |
|----------|--------|
| **Stitch → Figma** | Interactive prototype with 20+ page jumps, hover/active states, visual fixes |
| **Peer Evaluation** | Cross-group feedback collected + combined issue tracker (8 self + peer items) |

**Next workshop (Day 5) will iterate on all accumulated issues.** Save this document!
