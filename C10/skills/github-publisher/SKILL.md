---
name: github-publisher
description: 把一个项目组织成「公开、可验证」的 GitHub 仓库并部署上线：创建仓库、按 C5 模板写 README、补齐 LICENSE/.gitignore/AI_LOG/ATTRIBUTION/CHANGELOG/CONTRIBUTING、开启 GitHub Pages、验证公开可访问。Use when 需要把项目发布到 GitHub、给挑战交付物建仓库、或部署静态站点。
---

# GitHub 发布器

输入：本地项目目录 + 公开/私有决策 + 是否要 Pages。
输出：公开可访问的仓库 +（可选）在线站点 + 验证结果。

## 步骤

1. `gh repo create <owner>/<name> --public --source . --push`；
2. 按 C5 模板核对文档六件套：README / LICENSE / AI_LOG / ATTRIBUTION / CHANGELOG / CONTRIBUTING + .gitignore；
3. 需要在线版：Settings → Pages（master 根目录），等待 1–2 分钟首次发布；
4. 验证：`curl -sI` 确认 200；headless 浏览器确认页面渲染（交给 headless-verifier 技能）；
5. 公开仓库涉及「对外发布」的决策必须由本人确认后才执行。

## 迭代记录（CHANGELOG）

- v1（2026-11-10）：直接 `gh repo create` + 手工补文档。
- v2（2026-11-10）：固化为本清单——每次发布按「文档六件套 + Pages + 双验证」走，不再遗漏项。改进动机：C5 发布时 CHANGELOG/CONTRIBUTING 是后来补的，说明「想到哪补到哪」不可靠，改为清单驱动。

## 约束

- 私有/公开的决策权只在本人；
- Key/账号信息绝不入库（.gitignore 先于首次 commit 检查）。
