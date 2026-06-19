# research30days-cn

[简体中文](./README.md) | [English](./README.en.md) | [繁體中文](./README.zh-TW.md) | [日本語](./README.ja.md) | **한국어** | [Español](./README.es.md) | [Français](./README.fr.md) | [Deutsch](./README.de.md) | [Português](./README.pt.md) | [Русский](./README.ru.md)

**중국어 멀티소스 리서치 Agent Skill** — 한 번의 명령으로 Zhihu, Bilibili, SSPAI 및 중국어 웹 전체에서 지난 30일간의 주제별 논의를 조사하고, 구조화된 중국어 보고서를 출력합니다.

![demo](media/demo.gif)

> [last30days-skill](https://github.com/mvanhorn/last30days-skill)에서 영감을 받아, 중국어 인터넷 데이터 소스에 특화했습니다.

## 빠른 시작

### 1. 의존성 설치

```bash
pip install -r requirements.txt
```

### 2. 엔진 실행

```bash
python skills/research30days-cn/scripts/research30days_cn.py "AI Agent 도구" --emit compact
```

### 3. Cursor에서 사용

Skill을 Cursor에 설치:

```bash
# Windows PowerShell
Copy-Item -Recurse skills/research30days-cn "$env:USERPROFILE\.cursor\skills\research30days-cn"

# macOS / Linux
cp -r skills/research30days-cn ~/.cursor/skills/research30days-cn
```

Cursor에서 다음과 같이 입력:

```
/research30days-cn Cursor AI 코딩 도구
```

또는 자연어로:

```
지난 30일간 중국어 커뮤니티에서 '인디 해커 해외 진출'에 대해 어떤 논의가 있었는지 조사해줘
```

## 출력 예시

엔진이 증거 클러스터를 반환하고, Agent가 다음과 같은 보고서로 종합합니다:

```
🇨🇳 research30days-cn v0.1.0 · synced 2026-06-19

## 调研摘要
近 30 天中文社区对 AI Agent 工具的讨论集中在...

## 社区共识
1. **Cursor + MCP 成为默认组合** - ...
```

> 보고서는 **중국어**로 출력됩니다 — 본 Skill은 중국어 소스와 독자를 대상으로 설계되었습니다.

## 데이터 소스

| 소스 | 키 | 설명 |
|------|-----|------|
| 웹 전체 | `web` | DuckDuckGo (중국어 리전) |
| Zhihu (知乎) | `zhihu` | `site:zhihu.com` |
| Bilibili | `bilibili` | API + `site:bilibili.com` 폴백 |
| SSPAI (少数派) | `sspai` | `site:sspai.com` |

## CLI 옵션

```bash
python skills/research30days-cn/scripts/research30days_cn.py "주제" [옵션]

  --days 30              조회 기간(일)
  --sources web,zhihu,bilibili   소스 제한
  --max-results 8        소스당 최대 결과 수
  --emit compact|json|md 출력 형식
  --save ~/.research30days       원본 보고서 저장
```

## 프로젝트 구조

```
skills/research30days-cn/
├── SKILL.md                 # Agent 스킬 계약
├── references/
│   └── output-template.md   # 보고서 출력 템플릿
└── scripts/
    ├── research30days_cn.py # CLI 진입점
    └── lib/
        ├── sources.py       # 멀티소스 검색
        ├── render.py        # 출력 렌더링
        └── schema.py        # 데이터 모델
```

## 호환 플랫폼

오픈 [Agent Skills](https://agentskills.io) 형식 준수:

- Cursor
- Claude Code
- Codex CLI
- GitHub Copilot

## 개발

```bash
pip install -e ".[dev]"
pytest tests/
```

## License

MIT
