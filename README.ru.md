# research30days-cn

[简体中文](./README.md) | [English](./README.en.md) | [繁體中文](./README.zh-TW.md) | [日本語](./README.ja.md) | [한국어](./README.ko.md) | [Español](./README.es.md) | [Français](./README.fr.md) | [Deutsch](./README.de.md) | [Português](./README.pt.md) | **Русский**

**Agent Skill для мультиисточникового исследования на китайском** — одна команда, чтобы узнать, что Zhihu, Bilibili, SSPAI и китайский интернет говорят о любой теме за последние 30 дней, и получить структурированный отчёт на китайском языке.

![demo](media/demo.gif)

> Вдохновлено [last30days-skill](https://github.com/mvanhorn/last30days-skill), с фокусом на источники китайского интернета.

## Быстрый старт

### 1. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 2. Запуск движка

```bash
python skills/research30days-cn/scripts/research30days_cn.py "инструменты AI Agent" --emit compact
```

### 3. Использование в Cursor

Установите skill в Cursor:

```bash
# Windows PowerShell
Copy-Item -Recurse skills/research30days-cn "$env:USERPROFILE\.cursor\skills\research30days-cn"

# macOS / Linux
cp -r skills/research30days-cn ~/.cursor/skills/research30days-cn
```

Затем в Cursor скажите:

```
/research30days-cn инструменты программирования Cursor AI
```

Или естественным языком:

```
Исследуй, что китайский интернет говорил об «indie hackers и выходе на глобальный рынок» за последние 30 дней
```

## Пример вывода

Движок возвращает кластеры доказательств; Agent синтезирует отчёт вида:

```
🇨🇳 research30days-cn v0.1.0 · synced 2026-06-19

## 调研摘要
近 30 天中文社区对 AI Agent 工具的讨论集中在...

## 社区共识
1. **Cursor + MCP 成为默认组合** - ...
```

> Отчёты выводятся **на китайском** по задумке — skill ориентирован на китайские источники и аудиторию.

## Источники данных

| Источник | Ключ | Описание |
|----------|------|----------|
| Веб | `web` | Поиск DuckDuckGo (китайский регион) |
| Zhihu (知乎) | `zhihu` | `site:zhihu.com` |
| Bilibili | `bilibili` | API + резерв `site:bilibili.com` |
| SSPAI (少数派) | `sspai` | `site:sspai.com` |

## Параметры CLI

```bash
python skills/research30days-cn/scripts/research30days_cn.py "тема" [опции]

  --days 30              Период поиска в днях
  --sources web,zhihu,bilibili   Ограничить источники
  --max-results 8        Максимум на источник
  --emit compact|json|md Формат вывода
  --save ~/.research30days       Сохранить сырой отчёт
```

## Структура проекта

```
skills/research30days-cn/
├── SKILL.md                 # Контракт Agent skill
├── references/
│   └── output-template.md   # Шаблон отчёта
└── scripts/
    ├── research30days_cn.py # Точка входа CLI
    └── lib/
        ├── sources.py       # Мульти-источниковый поиск
        ├── render.py        # Рендеринг вывода
        └── schema.py        # Модели данных
```

## Совместимые платформы

Следует открытому формату [Agent Skills](https://agentskills.io):

- Cursor
- Claude Code
- Codex CLI
- GitHub Copilot

## Разработка

```bash
pip install -e ".[dev]"
pytest tests/
```

## License

MIT
