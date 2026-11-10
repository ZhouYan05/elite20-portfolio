# 使用记录（headless-verifier）

| # | 日期 | 输入 | 实际效果 | ΔR | 改进 |
|---|---|---|---|---|---|
| 1 | 2026-11-10 | C6A 仪表盘（本地 index.html） | 首拍空白 → 发现 JS 未执行 | 预期直接可用，实际加预算参数才行 | v1→v2：加 --virtual-time-budget |
| 2 | 2026-11-10 | C6A 仪表盘（GitHub Pages） | DOM 验证「完成率」渲染成功，截图交付 | 无 | — |
| 3 | 2026-11-10 | C6 app 在线版 | 截图 + DOM 验证（AAR/KSTAR 8 处命中） | 无 | — |
| 4 | 2026-11-10 | C5A fork/分支/commit 三页 | 三张截图产出；中途 segfault 但文件已写出 | 预期无报错，实际 stderr 有 segfault 噪音 | v2→v3：独立 profile + 以文件/DOM 为准 |
| 5 | 2026-11-10 | C5A commit 页 / 分支页 DOM | 验证「Chinese quickstart」与分支名渲染 | 无 | — |

累计使用：5 次（截至 2026-11-10）。最近一次效果：分支页 DOM 命中 34 处，验证通过。
