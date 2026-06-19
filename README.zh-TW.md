# research30days-cn

[简体中文](./README.md) | [English](./README.en.md) | **繁體中文** | [日本語](./README.ja.md) | [한국어](./README.ko.md) | [Español](./README.es.md) | [Français](./README.fr.md) | [Deutsch](./README.de.md) | [Português](./README.pt.md) | [Русский](./README.ru.md)

**中文多源調研 Agent Skill** — 一條命令，調研某個話題在知乎、B 站、少數派和全網近 30 天的討論，輸出結構化中文報告。

![demo](media/demo.gif)

> 靈感來自 [last30days-skill](https://github.com/mvanhorn/last30days-skill)，專注中文網際網路資料來源。

## 快速開始

### 1. 安裝依賴

```bash
pip install -r requirements.txt
```

### 2. 執行引擎

```bash
python skills/research30days-cn/scripts/research30days_cn.py "AI Agent 工具" --emit compact
```

### 3. 在 Cursor 中使用

將 Skill 安裝到 Cursor：

```bash
# Windows PowerShell
Copy-Item -Recurse skills/research30days-cn "$env:USERPROFILE\.cursor\skills\research30days-cn"

# macOS / Linux
cp -r skills/research30days-cn ~/.cursor/skills/research30days-cn
```

然後在 Cursor 中說：

```
/research30days-cn Cursor AI 編程工具
```

或：

```
調研一下近 30 天中文社群對「獨立開發出海」的討論
```

## 範例輸出

引擎回傳證據簇，Agent 綜合後輸出：

```
🇨🇳 research30days-cn v0.1.0 · synced 2026-06-19

## 調研摘要
近 30 天中文社群對 AI Agent 工具的討論集中在...

## 社群共識
1. **Cursor + MCP 成為預設組合** - ...
```

## 支援的資料來源

| 來源 | 鍵名 | 說明 |
|------|------|------|
| 全網 | `web` | DuckDuckGo 中文檢索 |
| 知乎 | `zhihu` | site:zhihu.com |
| B 站 | `bilibili` | API + site:bilibili.com 雙通道 |
| 少數派 | `sspai` | site:sspai.com |

## CLI 參數

```bash
python skills/research30days-cn/scripts/research30days_cn.py "主題" [選項]

  --days 30              回溯天數
  --sources web,zhihu,bilibili   限定來源
  --max-results 8        每源條數
  --emit compact|json|md 輸出格式
  --save ~/.research30days       儲存原始報告
```

## 專案結構

```
skills/research30days-cn/
├── SKILL.md                 # Agent 技能契約
├── references/
│   └── output-template.md   # 報告輸出模板
└── scripts/
    ├── research30days_cn.py # CLI 入口
    └── lib/
        ├── sources.py       # 多源檢索
        ├── render.py        # 輸出渲染
        └── schema.py        # 資料模型
```

## 相容平台

遵循 [Agent Skills](https://agentskills.io) 開放格式，支援：

- Cursor
- Claude Code
- Codex CLI
- GitHub Copilot

## 開發

```bash
pip install -e ".[dev]"
pytest tests/
```

## License

MIT
