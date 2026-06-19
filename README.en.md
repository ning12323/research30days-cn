# research30days-cn

**English** | [简体中文](./README.md)

**Chinese multi-source research Agent Skill** — one command to research what Zhihu, Bilibili, SSPAI, and the broader Chinese web are saying about any topic in the last 30 days, then output a structured report in Chinese.

![demo](media/demo.gif)

> Inspired by [last30days-skill](https://github.com/mvanhorn/last30days-skill), focused on Chinese internet data sources.

## Quick Start

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the engine

```bash
python skills/research30days-cn/scripts/research30days_cn.py "AI Agent tools" --emit compact
```

### 3. Use in Cursor

Install the skill into Cursor:

```bash
# Windows PowerShell
Copy-Item -Recurse skills/research30days-cn "$env:USERPROFILE\.cursor\skills\research30days-cn"

# macOS / Linux
cp -r skills/research30days-cn ~/.cursor/skills/research30days-cn
```

Then in Cursor, say:

```
/research30days-cn Cursor AI coding tools
```

Or in natural language:

```
Research what the Chinese web has been saying about "indie hacker going global" in the last 30 days
```

## Example output

The engine returns evidence clusters; the Agent synthesizes them into a report like:

```
🇨🇳 research30days-cn v0.1.0 · synced 2026-06-19

## 调研摘要
近 30 天中文社区对 AI Agent 工具的讨论集中在...

## 社区共识
1. **Cursor + MCP 成为默认组合** - ...
```

> Reports are written in **Chinese** by design — this skill targets Chinese-language sources and audiences.

## Data sources

| Source | Key | Description |
|--------|-----|-------------|
| Web | `web` | DuckDuckGo search (Chinese region) |
| Zhihu | `zhihu` | `site:zhihu.com` |
| Bilibili | `bilibili` | API + `site:bilibili.com` fallback |
| SSPAI | `sspai` | `site:sspai.com` |

## CLI options

```bash
python skills/research30days-cn/scripts/research30days_cn.py "topic" [options]

  --days 30              Lookback window in days
  --sources web,zhihu,bilibili   Limit sources
  --max-results 8        Max items per source
  --emit compact|json|md Output format
  --save ~/.research30days       Save raw report to disk
```

## Project structure

```
skills/research30days-cn/
├── SKILL.md                 # Agent skill contract
├── references/
│   └── output-template.md   # Report output template
└── scripts/
    ├── research30days_cn.py # CLI entrypoint
    └── lib/
        ├── sources.py       # Multi-source search
        ├── render.py        # Output rendering
        └── schema.py        # Data models
```

## Compatible platforms

Follows the open [Agent Skills](https://agentskills.io) format:

- Cursor
- Claude Code
- Codex CLI
- GitHub Copilot

## Development

```bash
pip install -e ".[dev]"
pytest tests/
```

## License

MIT
