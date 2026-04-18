# COMP7505 Workshop Day 3 — Completed

**Product:** AI Interview Copilot (InterviewAI)
**Track:** Track A — Smart Adaptive Interfaces
**Team Members:** [填写组员姓名]
**Date:** 2026-04-18

---

## Activity 1 — Google Stitch AI (35 min)

### Step 1: Tool Setup

- **Tool:** Google Stitch — https://stitch.withgoogle.com/
- **Account:** Google Account login
- **VPN:** Opera browser built-in VPN (free)
- **Credits:** 400 free generations / month
- **Mode:** Standard

### Step 2: DESIGN.md Specification

Design spec ensures **consistency** across all AI-generated pages.

```
# DESIGN.md — InterviewAI

## Colors
- Primary: #6C63FF (Purple)
- Primary Hover: #4F46E5
- Accent: #7C3AED
- Background: #0F172A (Dark)
- Surface: #1E293B
- Text Primary: #F8FAFC
- Text Secondary: #CBD5E1
- Text Muted: #94A3B8
- Success: #10B981
- Warning: #F59E0B
- Error: #EF4444
- Info: #3B82F6

## Typography
- Font: Inter (Google Fonts)
- H1: 1.75rem, weight 800
- H2: 1.25rem, weight 700
- Body: 0.875rem, weight 400
- Caption: 0.75rem, weight 600

## Spacing
- Page padding: 2rem
- Card padding: 1.5rem
- Grid gap: 1.25rem
- Section gap: 2.5rem

## Components
- Card: border-radius 16px, border 1px rgba(255,255,255,0.1), glassmorphism background
- Button Primary: gradient 135deg (#6C63FF → #7C3AED), border-radius 10px
- Button Ghost: transparent, border 1px rgba(255,255,255,0.1)
- Input: background #1E293B, border-radius 10px, border 1px rgba(255,255,255,0.1)
- Badge: border-radius 6px, font-size 0.75rem

## Layout
- Navigation: Persistent left sidebar (width: 240px)
- Main content: max-width 1400px, centered
- Multi-step flows: Breadcrumb + Next/Back buttons
```

### Step 3: Prompt

```
Create a high-fidelity UI design for AI Interview Copilot (InterviewAI).

Platform: Web desktop (dark theme)

Style: Modern, clean, minimal — dark background (#0F172A) with purple accent (#6C63FF).
Glassmorphism cards. Inter font.

Core pages to generate:

1. Dashboard
   - Welcome card with "Start Your First Practice" CTA
   - 3 recent session cards (role name, score, date)
   - Mini score trend chart
   - Smart recommendation card ("Technical Depth below target — start focused session")

2. Practice — Feedback Screen
   - Question text at top
   - Collapsible user answer panel
   - Score display with confidence badge (High=green, Medium=yellow, Low=red)
   - Sentence-level reasoning list (bulleted, each linked to answer text)
   - Inline action buttons: Flag / Override Score / Undo
   - Expandable "View Strong Answer Example" section
   - Bottom: [Revise Answer] [Next Question →]

3. Review — Upload & Analysis
   - Drag-and-drop upload zone (MP4, WAV, M4A, max 500MB)
   - Audio quality warning banner (yellow, when quality is low)
   - Extraction progress bar
   - Editable Q&A pair list with [Edit] button per pair
   - Bottom: [Retry] [Generate Summary]

Requirements:
- Persistent left sidebar with 5 items: Dashboard, Practice, Review, History, Settings
- Active nav item highlighted with gradient background
- Breadcrumbs for multi-step flows (e.g., Practice > Feedback)
- All feedback points have visible Flag / Override / Undo actions (Track A)
- Voice failure modal: "Voice input unavailable — switched to text mode" with partial transcript preserved
- Confidence indicator uses color coding: green/yellow/red
- Capability boundary banner on evaluation views
- Clean layout, clear visual hierarchy, modern interaction design
```

### Step 4: Generation Results

> [填写 Figma / Stitch 生成后的截图链接]

**Follow-up Prompts Used:**
1. "Add a voice failure modal overlay on the Practice Answer screen"
2. "Make confidence badges color-coded: green for High, yellow for Medium, red for Low"
3. "Add capability boundary banner at the top of the Feedback screen: 'AI feedback is advisory — always use your own judgment'"

---

## Activity 2 — Heuristic Evaluation (25 min)

### Evaluation Framework

Combined: **Nielsen's 10 Heuristics + Shneiderman's 8 Golden Rules**
Condensed into 5 evaluation dimensions. Score each 1–5.

| Score | Meaning |
|-------|---------|
| 1 | Catastrophic — prevents task completion |
| 2 | Major — causes significant confusion or errors |
| 3 | Minor — noticeable problem but workaround exists |
| 4 | Cosmetic — small polish needed |
| 5 | Excellent — fully meets the principle |

### Evaluation Results

#### Dimension 1: Consistency and Standards

> *Nielsen #4: Consistency and standards. Shneiderman #4: Consistency.*
> Same actions/options should look and behave the same everywhere.

| Item | Assessment |
|------|-----------|
| **Score** | 4 |
| **Problems** | Dashboard session cards use rounded thumbnails, but History list uses plain text rows — visual inconsistency between two views of the same data |
| **Optimization** | Unify session display: use the same card component in both Dashboard (recent 3) and History (full list), only differing in density |

#### Dimension 2: Status Feedback

> *Nielsen #1: Visibility of system status. Shneiderman #1: Informative feedback.*
> User always knows what's happening.

| Item | Assessment |
|------|-----------|
| **Score** | 3 |
| **Problems** | (1) JD/resume upload has no parsing progress indicator — user doesn't know if AI is processing. (2) Voice recording stops silently on failure — no error state shown. (3) Question generation has no loading state — blank screen for 3-5 seconds |
| **Optimization** | (1) Add inline spinner + "Parsing your documents..." after upload. (2) Show voice failure modal immediately with fallback message. (3) Add skeleton screen or progress bar during question generation |

#### Dimension 3: User Control Freedom

> *Nielsen #3: User control and freedom. Shneiderman #3: Easy reversibility.*
> Users can undo, redo, go back, exit at any time.

| Item | Assessment |
|------|-----------|
| **Score** | 4 |
| **Problems** | Flag and Override are visible, but Undo button is small and positioned far from the overridden score — hard to find. No "Exit Practice" confirmation — user might accidentally leave and lose progress |
| **Optimization** | (1) Place Undo button directly next to the overridden score badge. (2) Add exit confirmation dialog: "You have unsaved answers. Leave anyway?" |

#### Dimension 4: Error Prevention

> *Nielsen #5: Error prevention. Shneiderman #5: Prevent errors.*
> Design prevents mistakes before they happen.

| Item | Assessment |
|------|-----------|
| **Score** | 3 |
| **Problems** | (1) Resume upload accepts non-PDF files — error only shows after upload completes. (2) No confirmation before overriding an AI score — user might click accidentally. (3) Empty answer can be submitted — no validation |
| **Optimization** | (1) Restrict file picker to .pdf only. (2) Add small confirmation tooltip: "Override AI score to X/10?" before applying. (3) Disable Submit button when answer is empty; show "Please type your answer" hint |

#### Dimension 5: Simplicity and Efficiency

> *Nielsen #2: Match real world, #7: Flexibility, #8: Aesthetic & minimalist. Shneiderman #2: Universal usability, #6: Track progress, #7: Keep it simple.*
> Interface is clean, efficient, and doesn't overload users.

| Item | Assessment |
|------|-----------|
| **Score** | 4 |
| **Problems** | (1) Dashboard shows all 4 trend dimensions by default — information overload for first-time users. (2) No keyboard shortcut for power users (e.g., Enter to submit answer, Tab to next question) |
| **Optimization** | (1) Show only the top 2 trends on Dashboard; full charts in History. (2) Add keyboard shortcuts: Enter=Submit, Ctrl+Z=Undo last action, Escape=Close modal |

### Score Summary

| Dimension | Score |
|-----------|-------|
| Consistency and Standards | 4 / 5 |
| Status Feedback | 3 / 5 |
| User Control Freedom | 4 / 5 |
| Error Prevention | 3 / 5 |
| Simplicity and Efficiency | 4 / 5 |
| **Average** | **3.6 / 5** |

### Priority Fix List

| Priority | Issue | Dimension | Effort |
|----------|-------|-----------|--------|
| P0 | Voice failure — no error state shown | Status Feedback | Medium |
| P0 | Empty answer can be submitted | Error Prevention | Low |
| P1 | No upload file type restriction | Error Prevention | Low |
| P1 | No parsing/generation loading indicator | Status Feedback | Low |
| P1 | No exit confirmation during practice | User Control | Low |
| P2 | Undo button too small / misplaced | User Control | Low |
| P2 | Dashboard trend overload | Simplicity | Low |
| P2 | No keyboard shortcuts | Simplicity | Medium |

---

## Summary

| Activity | Output |
|----------|--------|
| **Google Stitch AI** | DESIGN.md + prompt → AI-generated high-fi UI (3 core screens) |
| **Heuristic Evaluation** | 5-dimension scoring (avg 3.6/5) + 8 prioritized fixes |

**Next workshop (Day 4) will iterate on these findings.** Save this document!
