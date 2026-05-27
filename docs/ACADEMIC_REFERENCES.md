# 📚 학술 자료 목록 (Academic References)

> Kairo 프로젝트의 기술적 선택과 철학에 대한 학술 근거

---

## 1. Karpathy's LLM Wiki Pattern (핵심 철학)

**Author:** Andrej Karpathy (OpenAI Co-founder, former Tesla Director of AI)  
**Publication:** GitHub Gist (April 2026) — Viral with 16M+ views  
**Link:** https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

### 핵심 개념
> "Instead of retrieving from raw documents at query time (RAG), the LLM incrementally builds and maintains a persistent wiki — a structured, interlinked collection of markdown files."

### Kairo에 적용된 부분
- KB.md 단일 파일 아키텍처
- LLM이 직접 지식을 읽고/쓰고/관계를 발견
- Growth Log를 통한 지식 축적 기록

### 관련 기사
- Towards AI (April 2026): "Compounding Knowledge With LLMs"  
  https://pub.towardsai.net/compounding-knowledge-with-llms-karpathys-wiki-pattern-in-action-d01db84d5b8b
- Particula Tech (April 2026): "When Compiled Knowledge Beats RAG"  
  https://particula.tech/blog/karpathy-llm-wiki-compiled-knowledge-vs-rag

---

## 2. Network Visualizations with Pyvis and VisJS (시각화 기술)

**Authors:** WestHealth Group  
**Publication:** **SciPy Proceedings 2020** (학술 논문)  
**Link:** https://proceedings.scipy.org/articles/Majora-342d178e-008

### 핵심 개념
> "Pyvis is built on top of VisJS JavaScript library... declarative approach makes it easy to quickly explore graph visualizations."

### Kairo에 적용된 부분
- `pages/5_🧩_Graph.py` — Knowledge Graph 인터랙티브 시각화
- Physics engine 기반 노드 배치 (Barnes-Hut 알고리즘)
- 마우스 드래그, 확대/축소, 호버 툴팁

### 기술적 근거
- VisJS는 **Force-directed layout** 알고리즘 사용
- 1,000개 노드 이상에서도 WebGL 기반 고성능 렌더링
- 과학 컴퓨팅 학회(SciPy)에서 인정받은 오픈소스 시각화 도구

---

## 3. Interactive Knowledge Graph Visualization + LLM Agents (최신 트렌드)

**Authors:** Jamie P. McCusker et al.  
**Publication:** CEUR Workshop Proceedings (2025)  
**Link:** https://ceur-ws.org/Vol-3773/paper2.pdf

### 핵심 개념
> "Interactive visualization over large knowledge graphs combined with LLM reasoning shows promise."

### Kairo에 적용 가능한 개선 방향
- 현재 Kairo는 정적 그래프만 표시 → **LLM이 그래프를 해석/설명**하는 기능 추가 가능
- 노드 클릭 시 LLM이 해당 노드의 관계를 자연어로 설명
- Knowledge Graph → 자연어 생성 (Graph-to-Text)

---

## 4. Streamlit in Academic & Enterprise Settings (UI 프레임워크)

**Authors:** Kyle Kearns (Wharton AI & Analytics Initiative)  
**Publication:** Wharton School, University of Pennsylvania (2025)  
**Link:** https://ai-analytics.wharton.upenn.edu/build-interactive-dashboards-with-chatgpt-and-streamlit/

### 핵심 개념
> "Streamlit is an open-source Python framework that makes it easy to build web-based data apps — no front-end experience required."

### Kairo에 적용된 부분
- 전체 UI 프레임워크로 Streamlit 채택
- ChatGPT + Streamlit 결합 → LLM 대시보드 구축

---

## 종합

Kairo는 위 4개 학술 자료의 핵심 철학과 기술을 융합한 프로젝트입니다:

1. **Karpathy LLM Wiki** → 단일 파일(KB.md) 지식 축적 철학
2. **Pyvis/VisJS (SciPy)** → 인터랙티브 지식 그래프 시각화
3. **CM4AI KG + LLM** → 지식 그래프와 LLM의 시너지
4. **Wharton/Streamlit** → 데이터 + LLM + 웹악 통합 프레임워크

> 참고: 위 논문/기사는 모두 오픈소스 프로젝트로, MIT/Apache/BSD 라이선스 하에 학술/상업 목적으로 자유롭게 사용 가능합니다.
