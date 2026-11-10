---
name: headless-verifier
description: 用 headless Edge 验证网页真实渲染状态并产出截图证据：--dump-dom 检查关键文本是否渲染、--screenshot 产出交付截图。Use when 需要验证部署的页面是否真的可用、给交付物做截图证据、或排查「页面 200 但内容空白」的问题。
---

# Headless 页面验证器

输入：目标 URL + 关键文本（验证词）+ 截图需求。
输出：DOM 验证结果 + 截图文件。

## 步骤

1. 截图：`msedge --headless --disable-gpu --no-sandbox --user-data-dir=<临时目录> --window-size=1400,1600 --virtual-time-budget=7000 --screenshot=<输出> <URL>`
2. 验证：`--dump-dom <URL>` 后 grep 关键文本（如「完成率」「forked from」），确认 JS 已执行、内容已渲染；
3. 证据落盘：截图放入对应交付目录，DOM 验证结果记录在日志。

## 关键参数（踩坑记录）

- **必须加 `--virtual-time-budget=6000+`**：否则 JS 未执行，截图全空白（v1 的坑）；
- **`--user-data-dir` 必须指向独立临时目录**：与正在运行的 Edge 实例共用 profile 会 segfault（v2 的坑）；
- 个别 profile 仍偶发 segfault 但截图已写出：以文件大小 + DOM 验证为准，不以 stderr 为准。

## 迭代记录（CHANGELOG）

- v1（2026-11-10）：直接 `--headless --screenshot` → 空白图。
- v2（2026-11-10）：加 `--virtual-time-budget=6000` → 内容渲染，但复用默认 profile 偶发 segfault。
- v3（2026-11-10）：加 `--no-sandbox` + 独立 `--user-data-dir` → 稳定。每次验证后必须 grep DOM，截图只作证据不作唯一判据。

## 约束

- 截图目标必须是我自己的页面/仓库，不截他人私有内容。
