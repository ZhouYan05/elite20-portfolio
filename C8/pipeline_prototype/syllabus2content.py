# -*- coding: utf-8 -*-
"""
C8 早期验证物：Syllabus → Content 流水线原型（Stage 1）
输入：教学大纲 Markdown（按周 + 主题 + 目标 + 素材清单）
输出：课程内容框架（每周：学习目标 / 内容大纲 / ILT 任务建议 / 作品集归档建议）
用法：python syllabus2content.py <syllabus.md> [--out content_framework.md]
可选 AI 增强：设置环境变量 OPENAI_BASE_URL/OPENAI_API_KEY/MODEL 后，
把 --ai 传入即可对每节大纲做润色（失败时自动回退为模板输出，不阻塞流水线）。
"""
import argparse
import os
import re
import sys
import urllib.request
import json

WEEK_RE = re.compile(r"^##\s*第\s*(\d+)\s*周", re.M)
TOPIC_RE = re.compile(r"^- \*\*主题\*\*：(.+)$", re.M)
GOAL_RE = re.compile(r"^- \*\*目标\*\*：(.+)$", re.M)
MAT_RE = re.compile(r"^- \*\*素材\*\*：(.+)$", re.M)


def parse_syllabus(text: str):
    weeks = []
    for m in WEEK_RE.finditer(text):
        start = m.end()
        nxt = WEEK_RE.search(text, start)
        block = text[start:nxt.start() if nxt else len(text)]
        topic = (TOPIC_RE.search(block) or [None]) and TOPIC_RE.search(block)
        goal = GOAL_RE.search(block)
        mat = MAT_RE.search(block)
        weeks.append({
            "week": int(m.group(1)),
            "topic": topic.group(1).strip() if topic else "（未填写主题）",
            "goal": goal.group(1).strip() if goal else "（未填写目标）",
            "materials": mat.group(1).strip() if mat else "（未填写素材）",
        })
    return weeks


def ai_polish(topic: str, goal: str) -> str:
    """可选 AI 增强：对本周内容大纲做润色。任何异常都回退为模板输出。"""
    base = os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1")
    key = os.environ.get("OPENAI_API_KEY", "")
    model = os.environ.get("MODEL", "gpt-4o-mini")
    if not key:
        return ""
    prompt = (f"你是课程设计师。主题：{topic}；学习目标：{goal}。"
              "请用 5 个要点列出本周内容大纲，每点不超过 25 字，纯文本输出。")
    try:
        req = urllib.request.Request(
            base.rstrip("/") + "/chat/completions",
            data=json.dumps({"model": model, "messages": [
                {"role": "user", "content": prompt}]}).encode("utf-8"),
            headers={"Content-Type": "application/json",
                     "Authorization": f"Bearer {key}"})
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)["choices"][0]["message"]["content"].strip()
    except Exception:
        return ""


def build_framework(weeks, use_ai=False):
    out = ["# 课程内容框架（由 syllabus2content.py 生成）\n"]
    for w in weeks:
        outline = ""
        if use_ai:
            outline = ai_polish(w["topic"], w["goal"])
        if not outline:
            outline = (f"- 理解「{w['topic']}」的核心概念与适用边界\n"
                       f"- 动手完成一个与主题对应的最小练习\n"
                       f"- 用 AI 结对完成一次主题相关的实操任务")
        out.append(f"## 第 {w['week']} 周：{w['topic']}\n")
        out.append(f"**学习目标**：{w['goal']}\n")
        out.append("**内容大纲**：")
        out.append(outline + "\n")
        out.append("**ILT 任务建议**：")
        out.append(f"- 互动任务：基于本周素材（{w['materials']}）完成一次问答式拆解，提交 300 字小结")
        out.append("- 互动任务：用 AI 生成本周主题的 3 道自测题并作答，记录 AI 参与度\n")
        out.append("**作品集归档建议**：")
        out.append(f"- 归档物：week{w['week']}_summary.md（小结 + 自测题 + 截图）\n")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("syllabus", help="教学大纲 Markdown 文件")
    ap.add_argument("--out", default="content_framework.md")
    ap.add_argument("--ai", action="store_true",
                    help="用环境变量配置的 OpenAI 兼容 API 润色大纲（可选）")
    args = ap.parse_args()
    try:
        text = open(args.syllabus, encoding="utf-8").read()
    except OSError as e:
        print(f"读取大纲失败: {e}", file=sys.stderr)
        sys.exit(1)
    weeks = parse_syllabus(text)
    if not weeks:
        print("未解析到「## 第N周」结构，请检查大纲格式", file=sys.stderr)
        sys.exit(1)
    framework = build_framework(weeks, use_ai=args.ai)
    open(args.out, "w", encoding="utf-8").write(framework)
    print(f"OK：解析 {len(weeks)} 周 → 生成 {args.out}")


if __name__ == "__main__":
    main()
