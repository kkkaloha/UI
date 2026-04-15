#!/usr/bin/env python3
"""Generate Deliverable 2 figures (SVG) for COMP7505 — InterviewAI. Style 1 Flat Icon."""
import os

OUT = os.path.dirname(os.path.abspath(__file__))

# Shared defs
DEFS = """
  <defs>
    <marker id="arrB" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#2563eb"/>
    </marker>
    <marker id="arrR" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#dc2626"/>
    </marker>
    <marker id="arrG" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#059669"/>
    </marker>
  </defs>
"""

STYLE = """
  <style>
    text { font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", Arial, "PingFang SC", sans-serif; }
    .t { fill: #111827; font-size: 14px; }
    .st { fill: #6b7280; font-size: 11px; }
    .ttl { fill: #111827; font-size: 18px; font-weight: 600; }
    .sub { fill: #111827; font-size: 13px; font-weight: 600; }
  </style>
"""


def wrap(title, vb, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" width="960">
{STYLE}
{DEFS}
<rect width="10000" height="10000" x="-5000" y="-5000" fill="#ffffff"/>
<text x="480" y="36" text-anchor="middle" class="ttl">{title}</text>
{body}
</svg>'''


def save(name, content):
    path = os.path.join(OUT, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Wrote", path)


# --- D2-1 Interaction model ---
def fig_d2_1():
    body = """
<text x="480" y="58" text-anchor="middle" class="st">Human–AI collaborative model (Track A)</text>
<rect x="300" y="78" width="360" height="44" rx="8" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1.5"/>
<text x="480" y="104" text-anchor="middle" class="sub">User retains authority over scores &amp; interpretations</text>
<!-- three pillars -->
<rect x="40" y="160" width="260" height="130" rx="8" fill="#ffffff" stroke="#d1d5db" stroke-width="1.5"/>
<text x="170" y="188" text-anchor="middle" class="sub">Transparency</text>
<text x="170" y="210" text-anchor="middle" class="st">Reasoning + confidence</text>
<text x="170" y="232" text-anchor="middle" class="st">beside every AI score</text>

<rect x="350" y="160" width="260" height="130" rx="8" fill="#faf5ff" stroke="#e9d5ff" stroke-width="1.5"/>
<text x="480" y="188" text-anchor="middle" class="sub">User control</text>
<text x="480" y="210" text-anchor="middle" class="st">Flag · Override · Undo · Discard</text>

<rect x="660" y="160" width="260" height="130" rx="8" fill="#f0fdf4" stroke="#bbf7d0" stroke-width="1.5"/>
<text x="790" y="188" text-anchor="middle" class="sub">Graceful degradation</text>
<text x="790" y="210" text-anchor="middle" class="st">Text fallback · general Qs · retry</text>

<line x1="480" y1="122" x2="170" y2="160" stroke="#2563eb" stroke-width="1.5" marker-end="url(#arrB)"/>
<line x1="480" y1="122" x2="480" y2="160" stroke="#2563eb" stroke-width="1.5" marker-end="url(#arrB)"/>
<line x1="480" y1="122" x2="790" y2="160" stroke="#2563eb" stroke-width="1.5" marker-end="url(#arrB)"/>
<text x="480" y="330" text-anchor="middle" class="st">Capability limits stated in plain language (Design Spec + banners)</text>
"""
    return wrap("Figure D2-1 — Interaction model", "0 0 960 360", body)


# --- D2-2 IA ---
def fig_d2_2():
    body = """
<!-- root -->
<rect x="380" y="70" width="200" height="48" rx="8" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>
<text x="480" y="100" text-anchor="middle" class="sub">InterviewAI</text>
<!-- row modules -->
<rect x="40" y="180" width="120" height="44" rx="8" fill="#ffffff" stroke="#d1d5db" stroke-width="1.5"/>
<text x="100" y="206" text-anchor="middle" class="t">Dashboard</text>
<line x1="480" y1="118" x2="100" y2="180" stroke="#2563eb" stroke-width="1.5" marker-end="url(#arrB)"/>

<rect x="180" y="160" width="140" height="80" rx="8" fill="#fef3c7" stroke="#f59e0b" stroke-width="1.5"/>
<text x="250" y="188" text-anchor="middle" class="sub">Practice</text>
<text x="250" y="208" text-anchor="middle" class="st">linear flow</text>
<line x1="480" y1="118" x2="250" y2="160" stroke="#2563eb" stroke-width="1.5" marker-end="url(#arrB)"/>

<rect x="340" y="160" width="140" height="80" rx="8" fill="#e0e7ff" stroke="#6366f1" stroke-width="1.5"/>
<text x="410" y="188" text-anchor="middle" class="sub">Review</text>
<text x="410" y="208" text-anchor="middle" class="st">upload → extract</text>
<line x1="480" y1="118" x2="410" y2="160" stroke="#2563eb" stroke-width="1.5" marker-end="url(#arrB)"/>

<rect x="500" y="180" width="120" height="44" rx="8" fill="#ffffff" stroke="#d1d5db" stroke-width="1.5"/>
<text x="560" y="206" text-anchor="middle" class="t">History</text>
<line x1="480" y1="118" x2="560" y2="180" stroke="#2563eb" stroke-width="1.5" marker-end="url(#arrB)"/>

<rect x="640" y="180" width="120" height="44" rx="8" fill="#ffffff" stroke="#d1d5db" stroke-width="1.5"/>
<text x="700" y="206" text-anchor="middle" class="t">Settings</text>
<line x1="480" y1="118" x2="700" y2="180" stroke="#2563eb" stroke-width="1.5" marker-end="url(#arrB)"/>

<!-- practice sub -->
<rect x="120" y="290" width="88" height="32" rx="6" fill="#ffffff" stroke="#d1d5db" stroke-width="1"/>
<text x="164" y="310" text-anchor="middle" class="st">Job · Resume</text>
<rect x="220" y="290" width="88" height="32" rx="6" fill="#ffffff" stroke="#d1d5db" stroke-width="1"/>
<text x="264" y="310" text-anchor="middle" class="st">Questions</text>
<rect x="320" y="290" width="88" height="32" rx="6" fill="#ffffff" stroke="#d1d5db" stroke-width="1"/>
<text x="364" y="310" text-anchor="middle" class="st">Answer</text>
<rect x="420" y="290" width="88" height="32" rx="6" fill="#ffffff" stroke="#d1d5db" stroke-width="1"/>
<text x="464" y="310" text-anchor="middle" class="st">Feedback</text>
<line x1="250" y1="240" x2="164" y2="290" stroke="#6b7280" stroke-width="1" marker-end="url(#arrB)"/>
<path d="M 208 306 L 220 306" stroke="#6b7280" stroke-width="1" marker-end="url(#arrB)"/>
<path d="M 308 306 L 320 306" stroke="#6b7280" stroke-width="1" marker-end="url(#arrB)"/>
<path d="M 408 306 L 420 306" stroke="#6b7280" stroke-width="1" marker-end="url(#arrB)"/>

<!-- exceptions -->
<rect x="80" y="360" width="100" height="36" rx="6" fill="#fef2f2" stroke="#fecaca" stroke-width="1" stroke-dasharray="4 2"/>
<text x="130" y="382" text-anchor="middle" class="st">Voice fail</text>
<rect x="200" y="360" width="100" height="36" rx="6" fill="#fef2f2" stroke="#fecaca" stroke-width="1" stroke-dasharray="4 2"/>
<text x="250" y="382" text-anchor="middle" class="st">AI error</text>
<line x1="250" y1="240" x2="130" y2="360" stroke="#dc2626" stroke-width="1" stroke-dasharray="4 3" marker-end="url(#arrR)"/>
<line x1="250" y1="240" x2="250" y2="360" stroke="#dc2626" stroke-width="1" stroke-dasharray="4 3" marker-end="url(#arrR)"/>

<text x="700" y="340" text-anchor="middle" class="st">Exception routes included in IA (not afterthought)</text>
"""
    return wrap("Figure D2-2 — Information architecture (excerpt)", "0 0 960 420", body)


# --- D2-3 Nav table ---
def fig_d2_3():
    rows = [
        ("Dashboard", "Job Input", "Start Practice", "slide"),
        ("Job Input", "Resume Upload", "Next (valid)", "slide"),
        ("Resume", "Questions", "Generate", "fade+load"),
        ("Questions", "Answer", "Select Q", "slide"),
        ("Answer", "Feedback", "Submit", "fade+load"),
        ("Any", "History", "Sidebar", "fade"),
    ]
    body = '<text x="480" y="58" text-anchor="middle" class="st">Primary navigation transitions (excerpt)</text>\n'
    # header
    y0 = 80
    for i, h in enumerate(["From", "To", "Trigger", "Transition"]):
        x = 40 + i * 220
        body += f'<rect x="{x}" y="{y0}" width="210" height="36" fill="#eff6ff" stroke="#bfdbfe"/>\n'
        body += f'<text x="{x+105}" y="{y0+24}" text-anchor="middle" class="sub">{h}</text>\n'
    for r, row in enumerate(rows):
        y = y0 + 40 + r * 36
        for c, cell in enumerate(row):
            x = 40 + c * 220
            fill = "#ffffff" if r % 2 == 0 else "#f9fafb"
            body += f'<rect x="{x}" y="{y}" width="210" height="34" fill="{fill}" stroke="#e5e7eb"/>\n'
            body += f'<text x="{x+8}" y="{y+22}" class="t">{cell}</text>\n'
    return wrap("Figure D2-3 — Navigation transition table (excerpt)", "0 0 960 400", body)


def box(x, y, w, h, title, sub=None):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="#ffffff" stroke="#d1d5db" stroke-width="1.5"/>'
    s += f'<text x="{x+w/2}" y="{y+22}" text-anchor="middle" class="sub">{title}</text>'
    if sub:
        s += f'<text x="{x+w/2}" y="{y+42}" text-anchor="middle" class="st">{sub}</text>'
    return s


def fig_d2_4():
    # Vertical flowchart simplified
    nodes = [
        (400, 70, 160, 44, "Start", None),
        (400, 130, 160, 44, "Job / JD input", "validate"),
        (400, 190, 160, 44, "Resume upload", "file OK?"),
        (400, 250, 160, 44, "AI questions", "network / AI OK?"),
        (400, 310, 160, 44, "Answer", "text or voice"),
        (400, 370, 160, 44, "AI evaluation", "scores + confidence"),
        (400, 430, 160, 44, "User control", "flag / override / undo"),
        (400, 490, 160, 44, "Next Q or Save", "→ Dashboard"),
    ]
    body = ""
    py = 70
    for i, (x, y, w, h, t, sub) in enumerate(nodes):
        body += box(x, y, w, h, t, sub)
        if i < len(nodes) - 1:
            body += f'<line x1="480" y1="{y+h}" x2="480" y2="{nodes[i+1][1]}" stroke="#2563eb" stroke-width="1.5" marker-end="url(#arrB)"/>'
    # exception branch
    body += '<rect x="620" y="250" width="140" height="100" rx="8" fill="#fef2f2" stroke="#fecaca" stroke-width="1.5"/>'
    body += '<text x="690" y="278" text-anchor="middle" class="sub">Exceptions</text>'
    body += '<text x="690" y="300" text-anchor="middle" class="st">Invalid file</text>'
    body += '<text x="690" y="318" text-anchor="middle" class="st">Network / AI error</text>'
    body += '<text x="690" y="336" text-anchor="middle" class="st">Voice → text fallback</text>'
    body += '<path d="M 560 270 L 620 290" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="5 3" fill="none" marker-end="url(#arrR)"/>'
    body += '<text x="480" y="560" text-anchor="middle" class="st">Practice journey — happy path (centre) · recovery (right)</text>'
    return wrap("Figure D2-4 — Practice workflow (simplified)", "0 0 960 580", body)


def fig_d2_5():
    nodes = [
        (400, 70, 160, 44, "Upload audio", "format check"),
        (400, 130, 160, 44, "Extract Q&amp;A", "ASR / NLP"),
        (400, 190, 160, 44, "Review / edit", "low quality warn"),
        (400, 250, 160, 44, "AI summary", "network OK?"),
        (400, 310, 160, 44, "Export / practice gaps", "save"),
    ]
    body = ""
    for i, (x, y, w, h, t, sub) in enumerate(nodes):
        body += box(x, y, w, h, t, sub)
        if i < len(nodes) - 1:
            body += f'<line x1="480" y1="{y+h}" x2="480" y2="{nodes[i+1][1]}" stroke="#2563eb" stroke-width="1.5" marker-end="url(#arrB)"/>'
    body += '<rect x="620" y="130" width="150" height="120" rx="8" fill="#fef2f2" stroke="#fecaca" stroke-width="1.5"/>'
    body += '<text x="695" y="158" text-anchor="middle" class="sub">Exceptions</text>'
    body += '<text x="695" y="182" text-anchor="middle" class="st">Invalid file → re-upload</text>'
    body += '<text x="695" y="202" text-anchor="middle" class="st">Extract fail → manual</text>'
    body += '<text x="695" y="222" text-anchor="middle" class="st">Audio unclear → warn</text>'
    body += '<path d="M 560 152 L 620 170" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="5 3" fill="none" marker-end="url(#arrR)"/>'
    body += '<text x="480" y="400" text-anchor="middle" class="st">Review journey — aligned with Deliverable 1 task names</text>'
    return wrap("Figure D2-5 — Review workflow (simplified)", "0 0 960 440", body)


def fig_d2_6():
    screens = [
        ("Dashboard", "entry"),
        ("Practice", "job→resume"),
        ("Questions", "AI list"),
        ("Answer", "text/voice"),
        ("Feedback", "scores"),
    ]
    body = '<text x="480" y="58" text-anchor="middle" class="st">Prototype tab — core path (left to right)</text>\n'
    x = 40
    for i, (title, sub) in enumerate(screens):
        body += f'<rect x="{x}" y="100" width="160" height="100" rx="10" fill="#ffffff" stroke="#2563eb" stroke-width="1.5"/>'
        body += f'<text x="{x+80}" y="145" text-anchor="middle" class="sub">{title}</text>'
        body += f'<text x="{x+80}" y="168" text-anchor="middle" class="st">{sub}</text>'
        if i < len(screens) - 1:
            body += f'<line x1="{x+160}" y1="150" x2="{x+175}" y2="150" stroke="#2563eb" stroke-width="2" marker-end="url(#arrB)"/>'
        x += 175
    body += '<text x="480" y="240" text-anchor="middle" class="st">High-fidelity click-through · index.html Prototype tab</text>'
    return wrap("Figure D2-6 — Key prototype screens (core path)", "0 0 960 280", body)


def fig_d2_7():
    body = """
<text x="480" y="52" text-anchor="middle" class="st">Track A — failure handling &amp; limitation communication</text>
<!-- banner -->
<rect x="40" y="75" width="880" height="40" rx="6" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1.5"/>
<text x="60" y="100" class="t">Limitation banner: AI evaluates structure / expression — not domain depth or interviewer intent</text>
<!-- modals -->
<rect x="80" y="150" width="360" height="160" rx="12" fill="#ffffff" stroke="#dc2626" stroke-width="2"/>
<text x="260" y="185" text-anchor="middle" class="sub">Voice recognition failed</text>
<text x="260" y="215" text-anchor="middle" class="st">Fallback: switch to text · progress kept</text>
<text x="260" y="245" text-anchor="middle" class="st">Actions: Retry voice · Use text</text>

<rect x="520" y="150" width="360" height="160" rx="12" fill="#ffffff" stroke="#dc2626" stroke-width="2"/>
<text x="700" y="185" text-anchor="middle" class="sub">AI generation error</text>
<text x="700" y="215" text-anchor="middle" class="st">Fallback: general question bank</text>
<text x="700" y="245" text-anchor="middle" class="st">Actions: Retry · Use general Qs</text>

<!-- confidence -->
<rect x="200" y="340" width="560" height="56" rx="8" fill="#f9fafb" stroke="#d1d5db" stroke-width="1.5"/>
<text x="480" y="365" text-anchor="middle" class="sub">Confidence &amp; low-audio warning (extraction / scoring)</text>
<text x="480" y="385" text-anchor="middle" class="st">Progress bar · “55% — reduced due to audio quality” (example)</text>
"""
    return wrap("Figure D2-7 — Failure UI &amp; limitations (Track A)", "0 0 960 420", body)


def main():
    os.makedirs(OUT, exist_ok=True)
    figures = [
        ("D2-1_interaction_model.svg", fig_d2_1),
        ("D2-2_information_architecture.svg", fig_d2_2),
        ("D2-3_navigation_table.svg", fig_d2_3),
        ("D2-4_practice_workflow.svg", fig_d2_4),
        ("D2-5_review_workflow.svg", fig_d2_5),
        ("D2-6_prototype_core_path.svg", fig_d2_6),
        ("D2-7_trackA_failures_limits.svg", fig_d2_7),
    ]
    for name, fn in figures:
        save(name, fn())


if __name__ == "__main__":
    main()
