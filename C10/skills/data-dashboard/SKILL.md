---
name: data-dashboard
description: 把提交记录类数据（JSON 单一事实源）一键生成 CSV、Excel 五表报表、前端仪表盘数据（data.js）与周报摘要。Use when 需要给数据做可视化仪表盘、生成带条件格式的 Excel 报表、或让数据「一次更新、多处产物」。
---

# 数据仪表盘生成器

输入：`submissions.json`（单一事实源）+ `challenges.json`（目录）。
输出：dashboard_data.json、data.js、submissions.csv、五表 Excel（总览/按学生/按挑战/时间线/缺失项）、weekly_summary.md。

## 步骤

1. 数据源只改 JSON（不直接改任何产物）；
2. `python gen_report.py <data_dir>` 一键重生成全部产物；
3. 仪表盘 `index.html` 加载 data.js，file:// 与 GitHub Pages 均可运行；
4. 交付：Excel 报表 + 线上仪表盘链接。

## 迭代记录（CHANGELOG）

- v1（2026-11-10）：初版生成器，遇 `stats` 未初始化报错（UnboundLocalError）→ 修复；
- v2（2026-11-10）：恢复被误删的 total_challenges 统计行；产物五表 + 条件格式（partial 标黄红）稳定；
- v3（2026-11-10）：增加「提交后回填实际 submissionId」流程——平台提交完成后刷新 submissions.json 并重生成。

## 约束

- 数据必须真实（来自平台记录/本地交付物扫描/GitHub 仓库树），不编造提交；
- 状态枚举固定：checked/submitted/partial/missing/skipped，含义与 C6A 仪表盘图例一致。
