# Deliverable 2 — Figures (`figures/`)

SVG sources and **1920px-wide PNG** exports for **COMP7505** Group Project Report — *Interaction Design Solution & Interactive Prototype*.

**Regenerate:** from this directory run `python3 generate_d2_diagrams.py`, then:

```bash
for f in D2-*.svg; do rsvg-convert "$f" -o "${f%.svg}.png" -w 1920; done
```

(requires `rsvg-convert`, e.g. `brew install librsvg`)

---

## File index

| File | Content |
|------|---------|
| `D2-1_interaction_model.svg` / `.png` | 交互模型：透明、控制、降级 |
| `D2-2_information_architecture.svg` / `.png` | 信息架构节选 + Practice 子步骤 + 异常 |
| `D2-3_navigation_table.svg` / `.png` | 导航跳转表（节选 6 行） |
| `D2-4_practice_workflow.svg` / `.png` | Practice 流程（主干 + 异常簇） |
| `D2-5_review_workflow.svg` / `.png` | Review 流程（主干 + 异常） |
| `D2-6_prototype_core_path.svg` / `.png` | 原型核心路径条带 |
| `D2-7_trackA_failures_limits.svg` / `.png` | Track A：横幅 + 双故障模态 + 置信度/音质说明 |

---

## Parent document

Figures are embedded in `../Deliverable2_Interaction_Design_and_Interactive_Prototype.md` (Markdown image links).
