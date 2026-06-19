# research30days-cn

[简体中文](./README.md) | [English](./README.en.md) | [繁體中文](./README.zh-TW.md) | [日本語](./README.ja.md) | [한국어](./README.ko.md) | [Español](./README.es.md) | [Français](./README.fr.md) | **Deutsch** | [Português](./README.pt.md) | [Русский](./README.ru.md)

**Chinesischer Multi-Source-Recherche Agent Skill** — ein Befehl, um zu recherchieren, was Zhihu, Bilibili, SSPAI und das chinesische Web in den letzten 30 Tagen zu einem Thema sagen, und einen strukturierten Bericht auf Chinesisch auszugeben.

![demo](media/demo.gif)

> Inspiriert von [last30days-skill](https://github.com/mvanhorn/last30days-skill), fokussiert auf chinesische Internet-Datenquellen.

## Schnellstart

### 1. Abhängigkeiten installieren

```bash
pip install -r requirements.txt
```

### 2. Engine ausführen

```bash
python skills/research30days-cn/scripts/research30days_cn.py "AI Agent Tools" --emit compact
```

### 3. In Cursor verwenden

Skill in Cursor installieren:

```bash
# Windows PowerShell
Copy-Item -Recurse skills/research30days-cn "$env:USERPROFILE\.cursor\skills\research30days-cn"

# macOS / Linux
cp -r skills/research30days-cn ~/.cursor/skills/research30days-cn
```

Dann in Cursor sagen:

```
/research30days-cn Cursor AI Programmierwerkzeuge
```

Oder in natürlicher Sprache:

```
Recherchiere, was das chinesische Web in den letzten 30 Tagen über „Indie Hacker Global Expansion“ gesagt hat
```

## Beispielausgabe

Die Engine liefert Evidenz-Cluster; der Agent fasst sie zu einem Bericht wie folgt zusammen:

```
🇨🇳 research30days-cn v0.1.0 · synced 2026-06-19

## 调研摘要
近 30 天中文社区对 AI Agent 工具的讨论集中在...

## 社区共识
1. **Cursor + MCP 成为默认组合** - ...
```

> Berichte werden **auf Chinesisch** ausgegeben — dieser Skill zielt auf chinesische Quellen und Zielgruppen ab.

## Datenquellen

| Quelle | Schlüssel | Beschreibung |
|--------|-----------|--------------|
| Web | `web` | DuckDuckGo-Suche (chinesische Region) |
| Zhihu (知乎) | `zhihu` | `site:zhihu.com` |
| Bilibili | `bilibili` | API + Fallback `site:bilibili.com` |
| SSPAI (少数派) | `sspai` | `site:sspai.com` |

## CLI-Optionen

```bash
python skills/research30days-cn/scripts/research30days_cn.py "Thema" [Optionen]

  --days 30              Rückblick in Tagen
  --sources web,zhihu,bilibili   Quellen einschränken
  --max-results 8        Maximum pro Quelle
  --emit compact|json|md Ausgabeformat
  --save ~/.research30days       Rohen Bericht speichern
```

## Projektstruktur

```
skills/research30days-cn/
├── SKILL.md                 # Agent-Skill-Vertrag
├── references/
│   └── output-template.md   # Berichtsvorlage
└── scripts/
    ├── research30days_cn.py # CLI-Einstiegspunkt
    └── lib/
        ├── sources.py       # Multi-Source-Suche
        ├── render.py        # Ausgabe-Rendering
        └── schema.py        # Datenmodelle
```

## Kompatible Plattformen

Folgt dem offenen [Agent Skills](https://agentskills.io)-Format:

- Cursor
- Claude Code
- Codex CLI
- GitHub Copilot

## Entwicklung

```bash
pip install -e ".[dev]"
pytest tests/
```

## License

MIT
