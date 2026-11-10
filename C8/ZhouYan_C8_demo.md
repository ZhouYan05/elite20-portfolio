# ZhouYan_C8_demo：早期验证物说明

## 验证物：Syllabus → Content 流水线原型

**位置**：`pipeline_prototype/`（本目录，随交付包提交；同步到 GitHub）

### 文件

| 文件 | 说明 |
|---|---|
| `syllabus2content.py` | 流水线 Stage 1 实现：解析教学大纲 Markdown → 生成课程内容框架 |
| `sample_syllabus.md` | 示例输入：《AI 提示词入门》3 周大纲 |
| `sample_output.md` | 实测输出：3 周内容框架（目标/大纲/ILT 任务建议/作品集归档建议） |

### 运行方式（可复现）

```bash
python syllabus2content.py sample_syllabus.md --out sample_output.md
# 输出：OK：解析 3 周 → 生成 sample_output.md

# 可选 AI 增强（无 Key 自动回退模板输出，不阻塞流水线）：
python syllabus2content.py sample_syllabus.md --ai
```

### 实测记录（2026-11-10）

- 输入：3 周示例大纲（周/主题/目标/素材 四字段）
- 输出：内容框架，包含每周的学习目标、内容大纲、2 条 ILT 任务建议（问答拆解 + AI 自测题）、作品集归档建议
- 验证：脚本在 Python 3.13 下运行成功，产物结构与模板一致；缺字段的大纲自动回退占位文案并继续运行（不中断流水线）

### 与 C8 五段流水线的对应

本验证物实现了 **Syllabus → Content 段**，且以代码形式固化了段接口契约（周/主题/目标/素材 → 目标/大纲/ILT/归档），后续 Content→Agent、Agent→Delivery、Delivery→Portfolio 三段将复用同一契约。
