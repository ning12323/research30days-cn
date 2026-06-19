# research30days-cn

[简体中文](./README.md) | [English](./README.en.md) | [繁體中文](./README.zh-TW.md) | [日本語](./README.ja.md) | [한국어](./README.ko.md) | [Español](./README.es.md) | **Français** | [Deutsch](./README.de.md) | [Português](./README.pt.md) | [Русский](./README.ru.md)

**Agent Skill de recherche multilingue chino** — une commande pour explorer ce que Zhihu, Bilibili, SSPAI et le web chinois disent sur un sujet au cours des 30 derniers jours, puis produire un rapport structuré en chinois.

![demo](media/demo.gif)

> Inspiré par [last30days-skill](https://github.com/mvanhorn/last30days-skill), axé sur les sources de données de l'internet chinois.

## Démarrage rapide

### 1. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 2. Lancer le moteur

```bash
python skills/research30days-cn/scripts/research30days_cn.py "outils AI Agent" --emit compact
```

### 3. Utiliser dans Cursor

Installez le skill dans Cursor :

```bash
# Windows PowerShell
Copy-Item -Recurse skills/research30days-cn "$env:USERPROFILE\.cursor\skills\research30days-cn"

# macOS / Linux
cp -r skills/research30days-cn ~/.cursor/skills/research30days-cn
```

Puis dans Cursor, dites :

```
/research30days-cn outils de codage Cursor AI
```

Ou en langage naturel :

```
Recherche ce que le web chinois a dit sur « indie hackers à l'international » ces 30 derniers jours
```

## Exemple de sortie

Le moteur renvoie des clusters de preuves ; l'Agent les synthétise en un rapport comme :

```
🇨🇳 research30days-cn v0.1.0 · synced 2026-06-19

## 调研摘要
近 30 天中文社区对 AI Agent 工具的讨论集中在...

## 社区共识
1. **Cursor + MCP 成为默认组合** - ...
```

> Les rapports sont rédigés en **chinois** par conception — ce skill cible des sources et un public chinois.

## Sources de données

| Source | Clé | Description |
|--------|-----|-------------|
| Web | `web` | Recherche DuckDuckGo (région chinoise) |
| Zhihu (知乎) | `zhihu` | `site:zhihu.com` |
| Bilibili | `bilibili` | API + repli `site:bilibili.com` |
| SSPAI (少数派) | `sspai` | `site:sspai.com` |

## Options CLI

```bash
python skills/research30days-cn/scripts/research30days_cn.py "sujet" [options]

  --days 30              Fenêtre de recherche en jours
  --sources web,zhihu,bilibili   Limiter les sources
  --max-results 8        Maximum par source
  --emit compact|json|md Format de sortie
  --save ~/.research30days       Enregistrer le rapport brut
```

## Structure du projet

```
skills/research30days-cn/
├── SKILL.md                 # Contrat du skill Agent
├── references/
│   └── output-template.md   # Modèle de rapport
└── scripts/
    ├── research30days_cn.py # Point d'entrée CLI
    └── lib/
        ├── sources.py       # Recherche multisource
        ├── render.py        # Rendu de sortie
        └── schema.py        # Modèles de données
```

## Plateformes compatibles

Conforme au format ouvert [Agent Skills](https://agentskills.io) :

- Cursor
- Claude Code
- Codex CLI
- GitHub Copilot

## Développement

```bash
pip install -e ".[dev]"
pytest tests/
```

## License

MIT
