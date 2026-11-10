# ZhouYan_C8_proposal：项目申请书

> 申请项目：**Project C — 课程生产体系**
> 申请人：周岩（2024102310451）｜日期：2026-11-10

---

## 1. 项目选择

- **我选择的项目**：C（课程生产体系）
- **为什么适合我**：
  - **我的相关经验**：本课程 C1 我完成了英文课程资料（cs146s-vibe-coding）的全文翻译与术语处理——这就是「把已有教学内容重新生产」的最小闭环；C6A 我构建了「数据 → 仪表盘」的自动生成管线，正是「自动化 + 可复用」思维的直接实践。
  - **我在 C1–C7 中展示的相关能力**：
    | 挑战 | 与 Project C 的对应能力 |
    |---|---|
    | C1 资料翻译 | Syllabus 侧：理解课程内容结构，产出结构化文档 |
    | C4C 作业自动求解与排版（评审 84 分） | Content 侧：把重复性内容生产自动化 |
    | C5/C6 AAR 生成器 | Agent 侧：把模板+素材固化为可复用工具（KSTAR → ILT 任务的同构物） |
    | C6A 数据管线 | Delivery/Portfolio 侧：一键生成产物 + 作品集归档 |
  - **我对这个领域的理解**：课程生产流水线的核心矛盾是「每门课都从头搭」——而 Syllabus→Content→Agent→Delivery→Portfolio 五段的本质是把**一次性的教学设计固化为可复跑的生产线**。我理解它的难点不在单段（每段都有现成工具），而在**段与段之间的接口标准化**（大纲怎么自动变成内容框架、内容怎么自动变成互动任务）。

## 2. 拿来主义分析

### 参考来源

| 来源 | 链接 | 核心思想 |
|---|---|---|
| KSTAR skill ecosystem（课程推荐技术栈） | C8 挑战规范「技术栈参考」 | 用技能生态承载教学方法：教学方法 = 可复用技能 |
| NEOLAF neo-agent-design + run-module | C8 挑战规范「技术栈参考」 | Agent 设计原则 + 可运行模块化交付 |
| 我在 C5A 深度分析的 neoskills | https://github.com/neolaf2/neoskills | 技能 = 目录 + 契约；部署用链接；治理层（ontology） |
| C6A 数据管线（我自己的产物） | https://github.com/ZhouYan05/elite20-submission-dashboard | 单一事实源 + 生成器模式：数据改一处，产物全更新 |
| cs146s-vibe-coding（C1 翻译对象） | C1 交付物 | 一门真实课程的完整结构（供流水线做输入样例） |

### 拿来的部分

- **直接复用**：「技能 = 目录 + frontmatter + 使用记录」的结构（neoskills）——课程内容的最小可复用单元就是「周次 = 技能目录」；
- **直接复用**：「单一事实源 + 生成器」模式（C6A 管线）——大纲是唯一事实源，内容框架/ILT 任务/归档清单全部生成，杜绝多副本漂移；
- **直接复用**：KSTAR 复盘结构——流水线本身的周度 AAR 也用它，与课程要求一致。

### 修改 / 删除 / 重构的部分

- **去掉**：neoskills 的「多智能体适配层」（adapters 支持 Claude Code/OpenCode/OpenClaw）——课程生产流水线面向的是「学员的交付物」，不是多个 agent CLI，适配层复杂度在本项目是负资产；
- **去掉**：企业级本体建模（OWL/RDF/SKOS，来自 Project B 技术栈）——教学场景不需要形式化程度那么高的语义层，轻量 YAML 元数据足够；
- **重构**：把 neoskills 的 ontology「技能间依赖」改造成「周次间依赖」（第 3 周内容依赖第 1 周概念）——教学序列的依赖图就是课程版 ontology；
- **新增**：「段接口标准化」层——定义 Syllabus→Content 的输入输出契约（周/主题/目标/素材 → 目标/大纲/ILT/归档），这是五个工作流能串成流水线的关键，参考来源里没有现成答案，需要我设计。

## 3. 执行方案（KSTAR）

### K（Knowledge）：我已有的知识和资源

- 相关技能：C10 技能库 6 个（kstar-aar-generator / github-publisher / data-dashboard / doc-bundle-writer / headless-verifier / cogseed-submitter）；
- 可用工具：Python 3.13 + openpyxl、gh CLI + GitHub Pages、headless Edge 验证、Claude Code；
- 协作资源：课程群（可用真实反馈验证产出）、C10 智能体系统（复用其 L4 工具层）。

### S（Situation）：当前问题是什么

- 现状：课程内容生产高度依赖人工逐周编写，每开一门新课从零开始；
- 痛点：大纲 → 内容框架 → 互动任务 → 交付 → 归档，五段之间靠人肉搬运，格式不一致、更新不同步；
- 约束条件：8 周执行期；学员端零安装（浏览器即可用）；我单人主 Builder。

### T（Task）：我要解决什么

- 核心目标：交付一条**可复用到任意课程**的生产流水线原型：输入大纲 Markdown → 自动产出内容框架 + ILT 任务 + 交付页面 + 作品集归档清单。
- 子任务分解：
  1. Stage 1 接口契约 + Syllabus→Content 原型（Week 1-2）✅ 已有早期验证物
  2. Content→Agent：内容框架自动转 ILT 任务（Week 3-4）
  3. Agent→Delivery：交付页面自动生成（Week 5-6）
  4. Delivery→Portfolio + 全流水线打通 + 用第二门课验证复用性（Week 7-8）

### Â（Action Plan）：怎么做

| 子任务 | 执行步骤 | AI/工具 | 输入 → 输出 |
|---|---|---|---|
| Stage 1 | 定义大纲字段契约；写解析+生成脚本；用 2 份真实大纲跑通 | Claude Code + Python | 大纲.md → content_framework.md |
| Stage 2 | 定义 ILT 任务模板（问答拆解/自测题/实操）；接入可选 AI 润色 | Claude Code + OpenAI 兼容 API（可选，无 Key 回退模板） | 内容框架 → ILT 任务清单 |
| Stage 3 | 用 github-publisher 部署周次页面（静态，学员零安装） | gh + GitHub Pages + headless-verifier | ILT 任务 → 在线交付页 |
| Stage 4 | 归档清单生成 + 第二门课（如 C1 翻译的课程）全流程复跑 | data-dashboard 模式 + doc-bundle-writer | 学员交付物 → 作品集目录 |

### R̂（Expected Result）：预计产出什么

- 可交付物清单：
  1. 可运行流水线（pipeline 脚本集，开源仓库）；
  2. 1 门示例课程的完整产物（大纲→内容→任务→交付页→归档清单）；
  3. 第二门课的复跑记录（证明「可复用」，含每段时间成本）；
  4. 周度 AAR ×8 与段接口契约文档。
- 成功标准：第二门课复跑时，除大纲外的全部产物自动生成，人工总耗时 ≤ 大纲撰写耗时；
- 验证方法：周度 AAR 的 R̂ vs R 对比；交付页可公开访问；邀请课程群同学用交付页完成一次 ILT 任务并反馈。

## 4. 我的角色

- 角色定义：**主 Builder，兼 Architect**（单阶段内我设计接口 + 亲手实现；Operator/Researcher 按需兼任）
- 我负责的具体模块：段接口契约设计、Syllabus→Content 与 Content→Agent 两段的实现、全流水线集成；
- 我的边界（我不负责什么）：不负责企业级部署与运维（无服务器资源，交付走 GitHub Pages）；不负责多语言/无障碍等生产级需求；
- 我需要的支持：课程群的真实使用反馈（每次 ILT 任务至少 1 条真实反馈）；评审对「接口契约」设计的反馈。

## 5. 早期验证（Proof of Capability）

- **验证物**：`pipeline_prototype/` 可运行原型（GitHub 可见，见 demo 链接）
  - `syllabus2content.py`：输入大纲 Markdown（周/主题/目标/素材）→ 输出内容框架（目标/大纲/ILT 建议/归档建议）；支持可选 AI 润色（环境变量注入 Key，无 Key 自动回退模板）；
  - `sample_syllabus.md` → `sample_output.md`：3 周示例大纲实测跑通（解析 3 周、产物完整）。
- 对应流水线位置：**Syllabus → Content 段**（Stage 1）。
- 质量自评：接口契约（周/主题/目标/素材 → 目标/大纲/ILT/归档）已经以代码形式固化，是后续三段的地基。

---

*申请提交人：周岩。AI 使用过程见 `ZhouYan_C8_AI日志.md`。*
