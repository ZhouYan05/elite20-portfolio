# ZhouYan_C10_demo：一次完整 KSTAR 循环的执行记录（文本 Demo）

> 说明：录屏工具不可用，以「逐条执行记录」代替 mp4（C10 规范：Demo 视频或录屏；本记录保留完整链路与真实命令、输出）。执行时间：2026-11-10 20:04–20:08。

## 循环对象：C5A 交付物截图验证

### 1. P（感知）

- 输入：C5A 需要「Fork 截图 + 分支截图 + commit 历史截图」三张证据。
- 目标 URL：https://github.com/ZhouYan05/neoskills 及其分支页、commit 页。

### 2. P（计划）

- 匹配技能：`headless-verifier`（SKILL.md 已加载）。
- 计划：每页「截图 + DOM 验证」双证据；用独立 user-data-dir 规避 segfault；验证词分别取「forked from neolaf2/neoskills」「docs-zh-cn-quickstart」「Chinese quickstart」。

### 3. E（执行）

```
msedge --headless --disable-gpu --no-sandbox \
  --user-data-dir=D:/edge_tmp_profile \
  --window-size=1400,1600 --virtual-time-budget=7000 \
  --screenshot=fork_page.png https://github.com/ZhouYan05/neoskills
→ 173830 bytes written

msedge --headless --no-sandbox --virtual-time-budget=6000 \
  --dump-dom https://github.com/ZhouYan05/neoskills | grep "forked from neolaf2/neoskills"
→ 命中（fork 关系确认渲染）

…（分支页、commit 页同法）
→ branch_page.png（174986 B）、commit_page.png（115814 B）
→ commit 页 DOM 命中 "Chinese quickstart" ×6；分支页 DOM 命中 ×34
```

- 卡点：branch/commit 两次调用 stderr 报 segfault，但文件已写出——按技能 v3 判据「以文件大小 + DOM 验证为准」，继续验证通过。

### 4. R（反思，KSTAR）

- **S**：C5A Level 2/3 需要三张公开页面的截图证据。
- **T**：产出 3 张截图 + DOM 验证记录。
- **A**：按 headless-verifier v3 步骤执行（独立 profile、virtual-time-budget、双验证）。
- **R**：3 张截图落盘，2 处 DOM 验证命中（6 次 / 34 次）。
- **ΔR**：预期「无报错」，实际 stderr 有 segfault 噪音（但产物完整）——技能 v3 已覆盖该情形，无需新改进。
- **失败分析**：无新增失败；segfault 为已知噪音（见技能 CHANGELOG v2→v3）。
- **下周计划**：若需批量截图，把「截图+验证」串成一条命令脚本，纳入 L4 工具层。

### 5. S（沉淀）

- headless-verifier 的 USAGE.md 追加本次 2 条使用记录（#4、#5）；
- 截图归档至 `C5A/ZhouYan_C5A_screenshots/`；
- 「批量截图脚本」写入 L4 工具层候选清单（未满 2 次使用，按设计决策 3 暂不脚本化）。

## 循环输出物（真实文件）

- `C5A/ZhouYan_C5A_screenshots/fork_page.png`（174 KB）
- `C5A/ZhouYan_C5A_screenshots/branch_page.png`（175 KB）
- `C5A/ZhouYan_C5A_screenshots/commit_page.png`（116 KB）
- 技能使用记录：#4、#5（2026-11-10）
