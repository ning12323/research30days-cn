---
name: research30days-cn
version: "0.1.0"
description: >-
  调研某个话题在中文互联网近 30 天的讨论与热点。从知乎、B站、少数派和全网检索内容，
  综合成结构化中文报告。Use when the user asks about 近30天、中文调研、知乎/B站讨论、
  国内热点、竞品舆情、或 mentions research30days-cn / 中文 last30days.
allowed-tools: Bash, Read, Write, WebSearch
license: MIT
user-invocable: true
compatibility: Requires Python 3.10+ and network access. Run pip install -r requirements.txt first.
---

# research30days-cn

中文多源调研 Skill。用户给主题，引擎拉取近 30 天证据，Agent 综合成报告。

## 触发词

- `/research30days-cn {主题}`
- 「调研一下近 30 天中文社区对 XXX 的讨论」
- 「知乎和 B 站最近怎么说 XXX」

## 工作流

### Step 1: 定位 Skill 目录

`SKILL_DIR` = 本文件所在目录（含 `scripts/` 的文件夹）。

### Step 2: 安装依赖（首次）

```bash
pip install -r "$SKILL_DIR/requirements.txt"
```

### Step 3: 运行引擎

```bash
python "$SKILL_DIR/scripts/research30days_cn.py" "{主题}" --days 30 --emit compact
```

可选参数：

| 参数 | 说明 |
|------|------|
| `--sources web,zhihu,bilibili,sspai` | 限定来源，默认前三项 |
| `--max-results 8` | 每源条数 |
| `--save ~/.research30days` | 保存原始报告 |
| `--emit json` | 机器可读输出 |

**示例：**

```bash
python scripts/research30days_cn.py "Cursor AI 编程" --days 30 --emit compact
python scripts/research30days_cn.py "独立开发 出海" --sources zhihu,bilibili --emit compact
```

### Step 4: 综合输出

1. 阅读引擎 stdout 中的 `## 证据簇` 区块（仅供 Agent 阅读）
2. 按 [references/output-template.md](references/output-template.md) 撰写中文报告
3. **禁止**原样粘贴证据簇给用户
4. 第一行必须是 badge：`🇨🇳 research30days-cn v0.1.0 · synced {今天日期}`

## 输出规则

- 用「调研摘要 / 社区共识 / 争议与分歧 / 值得跟进的 5 条」结构
- 结论必须对应证据中的具体条目
- 检索失败时在「来源覆盖」中说明，不要编造
- 对比类问题（A vs B）：在共识后增加「对比结论」小节

## 故障排除

| 现象 | 处理 |
|------|------|
| 0 条结果 | 缩短主题词、加 `--sources web,zhihu,bilibili,sspai`、稍后重试 |
| duckduckgo 报错 | 检查网络；可暂时只用 `--sources bilibili` |
| bilibili API 失败 | 引擎会回退到 DDG site:bilibili.com 结果 |

## 附加资源

- 输出模板: [references/output-template.md](references/output-template.md)
- 引擎源码: [scripts/research30days_cn.py](scripts/research30days_cn.py)
