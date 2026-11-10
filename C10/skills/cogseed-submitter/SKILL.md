---
name: cogseed-submitter
description: 通过 CogSeed 平台的 eduseed-student-submit 技能完成挑战提交：prepare-submission 打包交付物、submit-project 提交、get-evaluation 查评审结果、list-my-submissions 核对记录。Use when 需要向 CogSeed 平台提交挑战、查询评审状态、或核对历史提交记录。
---

# CogSeed 平台提交器

输入：challengeId + 交付物工作目录（必须含 challenge.yaml 要求的交付物文件名模式）+ GitHub 仓库链接。
输出：平台提交记录 +（可选）评审结果。

## 步骤

1. 核对挑战 ID（平台 challenge.yaml 中的 id）；
2. 核对工作目录：交付物文件名必须包含该挑战 deliverables_pattern 的全部子串（如 C5 需要 README.md / *repo链接* / *AI日志* / *拿来说明*）；
3. `prepare-submission` 打包 → `submit-project` 提交（payload：challengeId、githubRepoUrl、projectTitle、aarText、selfEvaluationText、projectSummary、workdir、requiredDeliverables）；
4. `list-my-submissions` 核对提交状态；`get-evaluation` 查评分与评审反馈。

## 环境依赖（半自动）

- 提交 API 需要平台注入的 `EDUSEED_API_KEY`（环境变量，不落盘）；
- Key 未注入时的备选路径：请本人打开 CogSeed 应用或经本人确认后从授权渠道注入。

## 迭代记录（CHANGELOG）

- v1（2026-10 初）：手写 payload 提交 → 字段易漏（workdir/requiredDeliverables 忘填）。
- v2（2026-10-04）：固化为 `_run.js` 调用模式（run-skill.cjs + 环境变量四件套），C4C 提交成功并拿到评审 84 分。
- v3（2026-11-10）：增加「提交前 deliverables_pattern 全量核对」步骤——用脚本检查文件名子串，避免平台退回 needs_revision。

## 约束

- 提交前必须人工核对提交内容（对外发布行为）；
- 平台 Key 只从环境读取，不写入任何文件。
