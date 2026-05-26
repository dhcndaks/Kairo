# 📋 기능별 자료조사 보고서

> Kairo 프로젝트 — 오픈소스소프트웨어 (2026-05-29 마감)
> 작성: 데이터/발표 담당

---

## 📖 개요

이 문서는 Kairo 프로젝트에서 사용 중인 **8개 오픈소스 라이브러리**와  
**발표를 위해 추가로 조사한 내용**을 정리한 보고서입니다.

---

## 🔬 오픈소스 라이브러리 상세 조사

### 1️⃣ Streamlit

| 항목 | 내용 |
|:-----|:------|
| **공식명** | Streamlit |
| **GitHub** | https://github.com/streamlit/streamlit |
| **⭐ Stars** | **44,161** |
| **라이선스** | Apache License 2.0 ✅ (상업 사용/수정/배포 자유) |
| **용도** | Kairo의 웹 UI 프레임워크 전체 |
| **선정 이유** | Python 코드만으로 웹앱 제작 가능. 복잡한 HTML/CSS/JS 불필요. |
| **사용 기업** | Snowflake(인수), Google, Tesla, PayPal, Fortune 50의 90% |
| **대안** | Gradio(단순한 데모용), Dash(기업용, 복잡함), Flask(수동 UI) |
| **선택한 이유** | Gradio보다 UI 자유도 높음, Dash보다 설정 간단, 채팅 UI 컴포넌트 내장 |
| **🔗 발표 키워드** | _Snowflake가 인수한 오픈소스, 44K⭐, Fortune 50 기업들이 사용_ |

---

### 2️⃣ NetworkX

| 항목 | 내용 |
|:-----|:------|
| **공식명** | NetworkX |
| **GitHub** | https://github.com/networkx/networkx |
| **⭐ Stars** | **16,913** |
| **라이선스** | BSD 3-Clause ✅ (가장 자유로운 라이선스 중 하나) |
| **용도** | Knowledge Graph의 노드-엣지 데이터 구조 생성 |
| **선정 이유** | Python 그래프 분석의 표준. 20년 이상 유지보수. |
| **개발 주체** | Los Alamos National Laboratory (Aric Hagberg, Dan Schult, Pieter Swart) |
| **대안** | igraph(R, C 기반, Python 연동 가능), Graph-tool(C++ 기반, 설치 어려움) |
| **선택한 이유** | Python 생태계와 가장 잘 맞음. pyvis와 직접 연동 가능. 설치 간편. |
| **🔗 발표 키워드** | _미국 로스앨러모스 국립연구소 출신, 그래프 분석의 표준, 17K⭐_ |

---

### 3️⃣ Pyvis

| 항목 | 내용 |
|:-----|:------|
| **공식명** | Pyvis |
| **GitHub** | https://github.com/WestHealth/pyvis |
| **⭐ Stars** | **1,183** |
| **라이선스** | BSD 3-Clause ✅ |
| **용도** | Knowledge Graph를 인터랙티브한 HTML 그래프로 시각화 |
| **핵심 기술** | vis.js (JavaScript 시각화 라이브러리)를 Python에서 사용 |
| **주요 기능** | 노드 드래그, 확대/축소, 마우스 호버 시 정보 표시, 필터링 |
| **대안** | Plotly(정적인 그래프), Matplotlib(정적), D3.js(JS 필요) |
| **선택한 이유** | **유일하게 인터랙티브한 네트워크 그래프를 Python으로 생성**. 발표 시청각 효과 극대화. |
| **🔗 발표 키워드** | _vis.js 기반, 인터랙티브 그래프로 발표 효과 UP, 주간 56만회 다운로드_ |

---

### 4️⃣ stvis

| 항목 | 내용 |
|:-----|:------|
| **공식명** | stvis |
| **GitHub** | https://github.com/napoles-uach/stvis |
| **⭐ Stars** | **12** (작지만 필요한 기능 정확히 수행) |
| **라이선스** | MIT ✅ |
| **용도** | Pyvis 그래프를 Streamlit 페이지에 렌더링 |
| **핵심 코드** | 단 38줄의 Python 래퍼 — `pv_static(g)` 한 줄로 끝 |
| **대안** | `streamlit.components.v1.html()` 로 직접 HTML 삽입 |
| **선택한 이유** | 3줄 → 1줄로 코드 단축. 유지보수 쉬움. 발표 코드 시연에 깔끔함. |
| **🔗 발표 키워드** | _작지만 강력한 오픈소스, Pyvis+Streamlit 연결 다리 역할_ |

---

### 5️⃣ APScheduler

| 항목 | 내용 |
|:-----|:------|
| **공식명** | APScheduler |
| **GitHub** | https://github.com/agronholm/apscheduler |
| **⭐ Stars** | **7,410** |
| **라이선스** | MIT ✅ |
| **용도** | 크론 잡 스케줄링 (정기적 작업 실행) |
| **핵심 기능** | CronTrigger(리눅스 cron과 동일), IntervalTrigger(일정 간격), DateTrigger(특정 시간) |
| **대안** | schedule(간단하지만 영구 실행 불안정), Celery(무거움, 메시지 큐 필요) |
| **선택한 이유** | 설정이 가장 간단하고, Python 프로세스 내에서 바로 실행됨. |
| **🔗 발표 키워드** | _경량 스케줄러, Celery 대비 설정 1/10, 7.4K⭐_ |

---

### 6️⃣ Kiwipiepy (Kiwi)

| 항목 | 내용 |
|:-----|:------|
| **공식명** | Kiwipiepy |
| **GitHub** | https://github.com/bab2min/kiwipiepy |
| **⭐ Stars** | **371** |
| **라이선스** | **LGPL v3** ⚠️ (GPL 계열, 주의 필요) |
| **용도** | 한글 형태소 분석 (한국어 자연어 처리) |
| **핵심 기능** | 형태소 분석, 문장 분리, 띄어쓰기 교정 |
| **대안** | KoNLPy(Java 의존성, 설치 복잡), Mecab-ko(설치 어려움), OpenAI API(유료) |
| **선택한 이유** | 순수 C++ 구현으로 설치 간편, 한국어 분석 성능 최상급, 정기 업데이트 |
| **⚡ 라이선스 주의** | LGPL v3는 BSD/MIT보다 제한적. **상업용은 코드 공개 필요할 수 있음.** 학술 프로젝트는 문제 없음. 발표에서 "LGPL v3 라이선스"라고 명시해야 함. |
| **🔗 발표 키워드** | _한국어 특화 형태소 분석기, C++ 기반 고성능, LGPL v3 라이선스_ |

---

### 7️⃣ RapidFuzz

| 항목 | 내용 |
|:-----|:------|
| **공식명** | RapidFuzz |
| **GitHub** | https://github.com/rapidfuzz/RapidFuzz |
| **⭐ Stars** | **3,856** |
| **라이선스** | MIT ✅ |
| **용도** | 문자열 유사도 비교 (스킬 트리거 매칭) |
| **선정 이유** | FuzzyWuzzy(GPL)의 MIT 라이선스 대체제. C++ 구현으로 10배 빠름. |
| **대안** | FuzzyWuzzy(GPL ⚠️, 라이선스 문제), difflib(Python 내장, 느림) |
| **선택한 이유** | FuzzyWuzzy는 GPL이라 학술 프로젝트라도 충돌 가능성 있음. RapidFuzz는 MIT로 자유로움. |
| **🔗 발표 키워드**** | _FuzzyWuzzy의 MIT 라이선스 대체제, C++ 기반 초고속, 3.9K⭐_ |

---

### 8️⃣ Requests

| 항목 | 내용 |
|:-----|:------|
| **공식명** | Requests |
| **GitHub** | https://github.com/psf/requests |
| **⭐ Stars** | 52K+ |
| **라이선스** | Apache 2.0 ✅ |
| **용도** | LLM API(DeepSeek) HTTP 통신 |
| **🔗 발표 키워드** | _Python HTTP 통신의 표준, PSF(Python Software Foundation) 관리_ |

---

## 📊 라이선스 호환성 요약

| 라이브러리 | 라이선스 | 상업 사용 | 수정 | 배포 | 특허 |
|:----------|:--------:|:---------:|:----:|:----:|:----:|
| Streamlit | Apache 2.0 | ✅ | ✅ | ✅ | ✅ |
| NetworkX | BSD 3-Clause | ✅ | ✅ | ✅ | ❌ |
| Pyvis | BSD 3-Clause | ✅ | ✅ | ✅ | ❌ |
| stvis | MIT | ✅ | ✅ | ✅ | ❌ |
| APScheduler | MIT | ✅ | ✅ | ✅ | ❌ |
| Kiwipiepy | **LGPL v3** | ⚠️ 조건부 | ✅ | ✅ | ❌ |
| RapidFuzz | MIT | ✅ | ✅ | ✅ | ❌ |
| Requests | Apache 2.0 | ✅ | ✅ | ✅ | ✅ |

> ✅ = 완전 자유, ⚠️ = 조건 필요 (LGPL: 수정 시 소스 공개), ❌ = 불가

---

## 🧩 기능별 구현 상태 분석

### 현재 작동하는 기능 (PRD 기준)

| 기능 | PRD 약속 | 실제 구현 | 비고 |
|:-----|:--------:|:---------:|:-----|
| KB.md 읽기/쓰기 | ✅ | ✅ 완료 | 팀원 구현 |
| LLM 채팅 (DeepSeek) | ✅ | ✅ 완료 | 팀원 구현 |
| 스킬 시스템 (트리거 매칭) | ✅ | ✅ 완료 | 팀원 구현 |
| 스킬 CRUD (Agent 페이지) | ❌ (명시되지 않음) | ✅ 완료 | 팀원이 추가 구현 |
| 크론 잡 스케줄링 | ✅ | ⚠️ 기본만 | 실제 작업 실행은 미완성 |
| 지식 그래프 시각화 | ❌ (자동 발견만 언급) | ✅ 완료 | **내가 구현** |
| 세션 관리 | ❌ | ✅ 완료 | 팀원 구현 |
| 레벨 시스템 | ✅ | ✅ 완료 | 팀원 구현 |
| 툴 시스템 (안전 명령어) | ✅ | ✅ 완료 | 팀원 구현 |
| API 설정 페이지 | ❌ | ✅ 완료 | 팀원 구현 |

### PRD에 약속됐지만 미구현

| 기능 | 난이도 | 영향 | 추천 |
|:-----|:------:|:----:|:----:|
| **동적 크론 자동 추천 → 실제 자동 실행** | 중 | 발표 시연 | ⭐⭐⭐ |
| **레벨별 기능 차등 적용** (Lv.1=크론추천, Lv.2=의도예측) | 중 | 발표 스토리 | ⭐⭐⭐⭐ |
| **Growth Log 자동 기록** (상호작용 로그) | 쉬움 | 부가 자료 | ⭐⭐ |
| **KB.md 압축 기능** (토큰 한계 도달 시) | 중 | 안정성 | ⭐⭐ |

---

## 🎯 발표 자료 제작을 위한 추천 구성

### PPT 슬라이드 구성案

| 슬라이드 | 내용 | 핵심 메시지 |
|:--------|:------|:-----------|
| 1 | **프로젝트 개요** | Kairo = 하나의 KB.md로 동작하는 개인 AI 비서 |
| 2 | **아키텍처** | KB.md ↔ DeepSeek V4 Flash(1M context) ↔ 사용자 |
| 3 | **사용 오픈소스 (4종)** | Streamlit(Apache 2.0) + NetworkX(BSD) + Pyvis(BSD) + RapidFuzz(MIT) |
| 4 | **Knowledge Graph 시연** | **라이브 데모** — KB.md 관계를 그래프로 시각화 |
| 5 | **협업 과정** | GitHub Issues + PR + Branch 전략 |
| 6 | **소감 및 회고** | Vibe Coding 경험, 팀 협업, 오픈소스 활용 |

---

## 📚 참고 자료 링크

- Streamlit 공식 문서: https://docs.streamlit.io
- NetworkX 공식 문서: https://networkx.org/documentation/stable/
- Pyvis + Streamlit 연동 가이드: https://github.com/kennethleungty/Pyvis-Network-Graph-Streamlit
- stvis 패키지: https://github.com/napoles-uach/stvis
- APScheduler 문서: https://apscheduler.readthedocs.io/
- Kiwi 형태소 분석기: https://github.com/bab2min/kiwipiepy
- RapidFuzz 문서: https://rapidfuzz.github.io/RapidFuzz/
- Kairo 저장소: https://github.com/dhcndaks/Kairo
