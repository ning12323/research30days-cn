# research30days-cn

[简体中文](./README.md) | [English](./README.en.md) | [繁體中文](./README.zh-TW.md) | [日本語](./README.ja.md) | [한국어](./README.ko.md) | [Español](./README.es.md) | [Français](./README.fr.md) | [Deutsch](./README.de.md) | **Português** | [Русский](./README.ru.md)

**Agent Skill de pesquisa multicanal em chinês** — um comando para pesquisar o que Zhihu, Bilibili, SSPAI e a web chinesa dizem sobre qualquer tema nos últimos 30 dias, gerando um relatório estruturado em chinês.

![demo](media/demo.gif)

> Inspirado em [last30days-skill](https://github.com/mvanhorn/last30days-skill), focado em fontes de dados da internet chinesa.

## Início rápido

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

### 2. Executar o motor

```bash
python skills/research30days-cn/scripts/research30days_cn.py "ferramentas AI Agent" --emit compact
```

### 3. Usar no Cursor

Instale o skill no Cursor:

```bash
# Windows PowerShell
Copy-Item -Recurse skills/research30days-cn "$env:USERPROFILE\.cursor\skills\research30days-cn"

# macOS / Linux
cp -r skills/research30days-cn ~/.cursor/skills/research30days-cn
```

Depois no Cursor, diga:

```
/research30days-cn ferramentas de codificação Cursor AI
```

Ou em linguagem natural:

```
Pesquise o que a web chinesa disse sobre "indie hackers indo global" nos últimos 30 dias
```

## Exemplo de saída

O motor retorna clusters de evidências; o Agent sintetiza em um relatório como:

```
🇨🇳 research30days-cn v0.1.0 · synced 2026-06-19

## 调研摘要
近 30 天中文社区对 AI Agent 工具的讨论集中在...

## 社区共识
1. **Cursor + MCP 成为默认组合** - ...
```

> Os relatórios são escritos em **chinês** por design — este skill visa fontes e público em idioma chinês.

## Fontes de dados

| Fonte | Chave | Descrição |
|-------|-------|-----------|
| Web | `web` | Busca DuckDuckGo (região chinesa) |
| Zhihu (知乎) | `zhihu` | `site:zhihu.com` |
| Bilibili | `bilibili` | API + fallback `site:bilibili.com` |
| SSPAI (少数派) | `sspai` | `site:sspai.com` |

## Opções CLI

```bash
python skills/research30days-cn/scripts/research30days_cn.py "tópico" [opções]

  --days 30              Janela de busca em dias
  --sources web,zhihu,bilibili   Limitar fontes
  --max-results 8        Máximo por fonte
  --emit compact|json|md Formato de saída
  --save ~/.research30days       Salvar relatório bruto
```

## Estrutura do projeto

```
skills/research30days-cn/
├── SKILL.md                 # Contrato do skill Agent
├── references/
│   └── output-template.md   # Modelo de relatório
└── scripts/
    ├── research30days_cn.py # Ponto de entrada CLI
    └── lib/
        ├── sources.py       # Busca multicanal
        ├── render.py        # Renderização de saída
        └── schema.py        # Modelos de dados
```

## Plataformas compatíveis

Segue o formato aberto [Agent Skills](https://agentskills.io):

- Cursor
- Claude Code
- Codex CLI
- GitHub Copilot

## Desenvolvimento

```bash
pip install -e ".[dev]"
pytest tests/
```

## License

MIT
