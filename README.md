# research30days-cn

**简体中文** | [English](./README.en.md)

**中文多源调研 Agent Skill** — 一条命令，调研某个话题在知乎、B站、少数派和全网近 30 天的讨论，输出结构化中文报告。
![demo](media/demo.gif)

> 灵感来自 [last30days-skill](https://github.com/mvanhorn/last30days-skill)，专注中文互联网数据源。

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 运行引擎

```bash
python skills/research30days-cn/scripts/research30days_cn.py "AI Agent 工具" --emit compact
```

### 3. 在 Cursor 中使用

将 Skill 安装到 Cursor：

```bash
# Windows PowerShell
Copy-Item -Recurse skills/research30days-cn "$env:USERPROFILE\.cursor\skills\research30days-cn"

# macOS / Linux
cp -r skills/research30days-cn ~/.cursor/skills/research30days-cn
```

然后在 Cursor 中说：

```
/research30days-cn Cursor AI 编程工具
```

或：

```
调研一下近 30 天中文社区对「独立开发出海」的讨论
```

## 示例输出

引擎返回证据簇，Agent 综合后输出：

```
🇨🇳 research30days-cn v0.1.0 · synced 2026-06-19

## 调研摘要
近 30 天中文社区对 AI Agent 工具的讨论集中在...

## 社区共识
1. **Cursor + MCP 成为默认组合** - ...
```

## 支持的数据源

| 来源 | 键名 | 说明 |
|------|------|------|
| 全网 | `web` | DuckDuckGo 中文检索 |
| 知乎 | `zhihu` | site:zhihu.com |
| B站 | `bilibili` | API + site:bilibili.com 双通道 |
| 少数派 | `sspai` | site:sspai.com |

## CLI 参数

```bash
python skills/research30days-cn/scripts/research30days_cn.py "主题" [选项]

  --days 30              回溯天数
  --sources web,zhihu,bilibili   限定来源
  --max-results 8        每源条数
  --emit compact|json|md 输出格式
  --save ~/.research30days       保存原始报告
```

## 项目结构

```
skills/research30days-cn/
├── SKILL.md                 # Agent 技能契约
├── references/
│   └── output-template.md   # 报告输出模板
└── scripts/
    ├── research30days_cn.py # CLI 入口
    └── lib/
        ├── sources.py       # 多源检索
        ├── render.py        # 输出渲染
        └── schema.py        # 数据模型
```

## 兼容平台

遵循 [Agent Skills](https://agentskills.io) 开放格式，支持：

- Cursor
- Claude Code
- Codex CLI
- GitHub Copilot

## 开发

```bash
pip install -e ".[dev]"
pytest tests/
```

## License

MIT
