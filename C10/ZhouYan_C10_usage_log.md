# ZhouYan_C10_usage_log：真实使用记录汇总

> 六个技能各自的使用记录见 `ZhouYan_C10_skills/<技能>/USAGE.md`。本文件是汇总 + 三个典型场景的详细版（按 C10 规范格式）。

## 汇总（截至 2026-11-10）

| 技能 | 使用次数 | 最近使用 | 最近效果 |
|---|---|---|---|
| kstar-aar-generator | 3 | 2026-11-10 | C10 系统级 AAR 结构完整度 100% |
| github-publisher | 4 | 2026-11-10 | elite20-portfolio 一次发布成功（清单驱动无返工） |
| headless-verifier | 5 | 2026-11-10 | 分支页 DOM 命中 34 处，验证通过 |
| cogseed-submitter | 11+ | 2026-10-04 | C4C 提交获评审 84 分 |
| data-dashboard | 3 | 2026-11-10 | C6A 仪表盘在线可用 |
| doc-bundle-writer | 4 | 2026-11-10 | C6 五件套一次通过模式核对 |

## 典型场景 1：用 cogseed-submitter 提交 C4C

- 日期：2026-10-04
- 输入：「C4C 作业自动求解与排版」交付物工作目录 + 挑战 ID k82c4m
- 调用的 Skill：cogseed-submitter
- 实际效果：提交成功，平台校验通过，评审 84 分（反馈原文见 C6A 数据集）
- ΔR：预期「一次提交直接过」，实际之前版本因 payload 缺字段被平台退回过（needs_revision），v2 用固定模板后一次通过
- 改进：把 payload 字段清单固化为模板，并在 v3 增加「提交前 deliverables_pattern 全量核对」

## 典型场景 2：用 headless-verifier 验证 C6A 仪表盘

- 日期：2026-11-10
- 输入：本地 index.html + GitHub Pages URL，验证词「完成率」
- 调用的 Skill：headless-verifier
- 实际效果：DOM 验证通过（数据已渲染），产出交付截图
- ΔR：预期「截图即验证」，实际第一张截图全空白——JS 未执行；加 `--virtual-time-budget` 后正常。教训：HTTP 200 ≠ 内容渲染，验证必须到 DOM 层
- 改进：技能固化为「截图 + DOM grep 双验证」，截图只作证据不作唯一判据

## 典型场景 3：用 data-dashboard 生成 C6A 全套产物

- 日期：2026-11-10
- 输入：submissions.json（9 条真实提交）+ challenges.json（21 挑战）
- 调用的 Skill：data-dashboard
- 实际效果：五表 Excel + data.js + CSV + 周报一次生成，仪表盘部署上线
- ΔR：预期「一次跑通」，实际首跑 UnboundLocalError（stats 未初始化）+ 一次误删统计行；修复后产物与数据源一致
- 改进：生成器增加自检输出（各表行数打印），异常时立即可见

## 结论

六个技能全部来自本课程真实工作流（C4C 提交、C5/C6/C6A 发布与验证、C5A 分析、各挑战文档交付），每个都有 ≥2 次使用记录与至少一次迭代改进记录。无「为凑数临时编写」的技能。
