# research30days-cn

[简体中文](./README.md) | [English](./README.en.md) | [繁體中文](./README.zh-TW.md) | [日本語](./README.ja.md) | [한국어](./README.ko.md) | **Español** | [Français](./README.fr.md) | [Deutsch](./README.de.md) | [Português](./README.pt.md) | [Русский](./README.ru.md)

**Agent Skill de investigación multifuente en chino** — un comando para investigar lo que Zhihu, Bilibili, SSPAI y la web china en general dicen sobre cualquier tema en los últimos 30 días, y generar un informe estructurado en chino.

![demo](media/demo.gif)

> Inspirado en [last30days-skill](https://github.com/mvanhorn/last30days-skill), enfocado en fuentes de datos de internet china.

## Inicio rápido

### 1. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 2. Ejecutar el motor

```bash
python skills/research30days-cn/scripts/research30days_cn.py "herramientas AI Agent" --emit compact
```

### 3. Usar en Cursor

Instala el skill en Cursor:

```bash
# Windows PowerShell
Copy-Item -Recurse skills/research30days-cn "$env:USERPROFILE\.cursor\skills\research30days-cn"

# macOS / Linux
cp -r skills/research30days-cn ~/.cursor/skills/research30days-cn
```

Luego en Cursor, di:

```
/research30days-cn herramientas de programación Cursor AI
```

O en lenguaje natural:

```
Investiga lo que la web china ha dicho sobre "indie hackers y expansión global" en los últimos 30 días
```

## Ejemplo de salida

El motor devuelve clusters de evidencia; el Agent los sintetiza en un informe como:

```
🇨🇳 research30days-cn v0.1.0 · synced 2026-06-19

## 调研摘要
近 30 天中文社区对 AI Agent 工具的讨论集中在...

## 社区共识
1. **Cursor + MCP 成为默认组合** - ...
```

> Los informes se escriben en **chino** por diseño — este skill apunta a fuentes y audiencias en idioma chino.

## Fuentes de datos

| Fuente | Clave | Descripción |
|--------|-------|-------------|
| Web | `web` | Búsqueda DuckDuckGo (región china) |
| Zhihu (知乎) | `zhihu` | `site:zhihu.com` |
| Bilibili | `bilibili` | API + respaldo `site:bilibili.com` |
| SSPAI (少数派) | `sspai` | `site:sspai.com` |

## Opciones CLI

```bash
python skills/research30days-cn/scripts/research30days_cn.py "tema" [opciones]

  --days 30              Ventana de búsqueda en días
  --sources web,zhihu,bilibili   Limitar fuentes
  --max-results 8        Máximo por fuente
  --emit compact|json|md Formato de salida
  --save ~/.research30days       Guardar informe en disco
```

## Estructura del proyecto

```
skills/research30days-cn/
├── SKILL.md                 # Contrato del skill Agent
├── references/
│   └── output-template.md   # Plantilla de informe
└── scripts/
    ├── research30days_cn.py # Punto de entrada CLI
    └── lib/
        ├── sources.py       # Búsqueda multifuente
        ├── render.py        # Renderizado de salida
        └── schema.py        # Modelos de datos
```

## Plataformas compatibles

Sigue el formato abierto [Agent Skills](https://agentskills.io):

- Cursor
- Claude Code
- Codex CLI
- GitHub Copilot

## Desarrollo

```bash
pip install -e ".[dev]"
pytest tests/
```

## License

MIT
