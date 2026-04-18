# Figures — internal notes (team only)

*Not part of the report text for instructors. Use for regenerating diagrams and exports.*

## Regenerate SVGs

After editing `generate_d2_diagrams.py`:

```bash
python3 generate_d2_diagrams.py
```

## File index

| File | Content |
|------|---------|
| `D2-1_interaction_model.svg` | 交互模型：透明、控制、降级 |
| `D2-2_information_architecture.svg` | 信息架构节选 + Practice 子步骤 + 异常 |
| `D2-3_navigation_table.svg` | 导航跳转表（节选 6 行） |
| `D2-4_practice_workflow.svg` | Practice 流程（主干 + 异常簇） |
| `D2-5_review_workflow.svg` | Review 流程（主干 + 异常） |
| `D2-6_prototype_core_path.svg` | 原型核心路径条带 |
| `D2-7_trackA_failures_limits.svg` | Track A：横幅 + 双故障模态 + 置信度/音质说明 |

## Exports (run from parent `docs/` folder)

HTML:

```bash
pandoc Deliverable2_Interaction_Design_and_Interactive_Prototype.md -o Deliverable2_Interaction_Design_and_Interactive_Prototype.html --standalone --include-in-header=pandoc-html-header.html --metadata title="COMP7505 — Deliverable 2"
```

Word:

```bash
pandoc Deliverable2_Interaction_Design_and_Interactive_Prototype.md -o Deliverable2_Interaction_Design_and_Interactive_Prototype.docx
```

If Word does not show SVG figures well, convert SVG to PNG and point image links in the Markdown to `.png` before pandoc.
