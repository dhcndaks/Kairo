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

## 2. GraphRAG: Knowledge Graph + LLM 통합 (핵심 기술)

**Authors:** Darren Edge, Ha Trinh, Newman Cheng, Joshua Bradley, Alex Chao, Apurva Mody, Steven Truitt, Dasha Metropolitansky, Robert Osazuwa Ness, Jonathan Larson
**Publication:** Microsoft Research (April 2024)
**arXiv:** https://arxiv.org/abs/2404.16130
**DOI:** arXiv:2404.16130

### 핵심 개념
> "We propose GraphRAG, a graph-based approach to question answering over private text corpora that scales with both the generality of user questions and the quantity of source text. Our approach uses an LLM to build a graph-based text index in two stages: first to derive an entity knowledge graph from the source documents, then to pre-generate community summaries for all groups of closely-related entities."

### Kairo에 적용된 부분
- Knowledge Graph를 활용한 LLM 추론 보강
- 엔티티 간 관계를 그래프로 구조화하여 LLM이 문맥을 파악
- Community detection 기반 지식 그룹화 → Kairo의 Edge 분류 시스템과 유사

### 기술적 의의
- Microsoft Research가 개발한 오픈소스 Graph RAG 시스템
- 전통적 RAG의 한계(전역적 질문 처리 불가)를 Knowledge Graph로 극복
- Map-Reduce 방식으로 대규모 텍스트 처리 (100만 토큰 이상)

---

## 3. ReAct: LLM 추론 + 행동 통합 (에이전트 아키텍처)

**Authors:** Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao
**Publication:** ICLR 2023 (International Conference on Learning Representations)
**arXiv:** https://arxiv.org/abs/2210.03629

### 핵심 개념
> "We explore the use of LLMs to generate both reasoning traces and task-specific actions in an interleaved manner, allowing for greater synergy between the two: reasoning traces help the model induce, track, and update action plans as well as handle exceptions, while actions allow it to interface with external sources."

### Kairo에 적용된 부분
- Kairo 에이전트의 추론-행동 루프 (KB 읽기 → 분석 → 쓰기)
- `cron_manager`의 정기적 작업 실행이 ReAct 패턴을 따름
- LLM이 도구(KB Manager, Knowledge Graph)를 호출하며 추론하는 구조

### 기술적 의의
- LLM 에이전트 설계의 기반이 되는 논문
- Chain-of-Thought(추론) + Tool Use(행동)의 결합 최초 제안
- ICLR 2023 발표, 3,000+ 인용

---

## 4. MemGPT: LLM을 운영체제처럼 (메모리 관리)

**Authors:** Charles Packer, Vivian Fang, Shishir G. Patil, Kevin Lin, Sarah Wooders, Joseph Gonzalez
**Publication:** ICLR 2024
**arXiv:** https://arxiv.org/abs/2310.08560

### 핵심 개념
> "We propose virtual context management, a technique drawing inspiration from hierarchical memory systems in traditional operating systems which provide the illusion of an extended virtual memory via paging between physical memory and disk."

### Kairo에 적용된 부분
- KB.md가 LLM의 "외부 메모리(디스크)" 역할
- 컨텍스트 윈도우 제한을 지속적 파일 저장으로 극복
- `kb_manager`의 읽기/쓰기가 MemGPT의 페이징과 유사한 패턴

### 기술적 의의
- UC Berkeley 연구, ICLR 2024 발표
- OS의 가상 메모리 개념을 LLM에 적용
- 대화형 에이전트가 장기 기억을 유지하는 방법론 제시

---

## 5. Toolformer: LLM의 자율적 도구 사용 (Function Calling)

**Authors:** Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Luke Zettlemoyer, Nicola Cancedda, Thomas Scialom (Meta AI)
**Publication:** NeurIPS 2023 (Oral Presentation)
**arXiv:** https://arxiv.org/abs/2302.04761

### 핵심 개념
> "We introduce Toolformer, a model trained to decide which APIs to call, when to call them, what arguments to pass, and how to best incorporate the results into future token prediction. This is done in a self-supervised way."

### Kairo에 적용된 부분
- Kairo LLM이 KB Manager, Knowledge Graph 등의 도구를 자율적으로 호출
- Function calling 패턴: 언제 읽고, 언제 쓸지 LLM이 스스로 결정
- Self-supervised 방식의 도구 학습 → Kairo의 지식 축적 루프와 유사

### 기술적 의의
- Meta AI 연구, NeurIPS 2023 Oral (전체 논문의 2%만 선정)
- LLM이 스스로 도구 사용법을 학습하는 최초의 연구
- 검색 엔진, 계산기, 번역 등 5개 도구 통합

---

## 6. Generative Agents: LLM 기반 자율 에이전트 (에이전트 시스템)

**Authors:** Joon Sung Park, Joseph C. O'Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, Michael S. Bernstein
**Publication:** UIST 2023 (ACM User Interface Software and Technology Symposium)
**arXiv:** https://arxiv.org/abs/2304.03442

### 핵심 개념
> "We introduce generative agents — computational software agents that simulate believable human behavior. Generative agents wake up, cook breakfast, and head to work; artists paint, while authors write; they form opinions, notice each other, and initiate conversations; they remember and reflect on days past as they plan the next day."

### Kairo에 적용된 부분
- Kairo의 `cron_manager`가 주기적으로 작업을 수행하는 자율 에이전트 패턴
- 지식의 지속적 축적과 반영(Reflect) → Growth Log 시스템
- 에이전트가 환경을 관찰하고 행동하는 아키텍처

### 기술적 의의
- Stanford University 연구, UIST 2023 발표
- "AI Town"으로 알려진 시뮬레이션, 25개 자율 에이전트 구현
- Memory → Reflection → Planning의 3단계 에이전트 아키텍처 제안
- 2,800+ 인용

---

## 7. HuggingGPT: LLM 기반 멀티모달 에이전트 (시스템 아키텍처)

**Authors:** Yongliang Shen, Kaitao Song, Xu Tan, Dongsheng Li, Weiming Lu, Yueting Zhuang
**Publication:** NeurIPS 2023
**arXiv:** https://arxiv.org/abs/2303.17580

### 핵심 개념
> "We present HuggingGPT, an LLM-powered agent that leverages LLMs to connect various AI models in machine learning communities to solve AI tasks. Specifically, we use ChatGPT to conduct task planning, select models according to their function descriptions, execute each subtask with the selected AI model, and summarize the response."

### Kairo에 적용된 부분
- Task Planning → Model Selection → Execution → Response Generation 워크플로우
- LLM이 컨트롤러 역할을 하며 전문 모듈(KB Manager, Graph Builder)을 조율
- Kairo의 모듈형 아키텍처와 유사한 패턴

### 기술적 의의
- Zhejiang University & Microsoft 연구, NeurIPS 2023 발표
- LLM을 "두뇌"로, 전문 AI 모델을 "실행자"로 사용하는 아키텍처 최초 제안
- 4단계 파이프라인: Task Planning → Model Selection → Task Execution → Response Generation

---

## 8. Fruchterman-Reingold: Force-Directed 그래프 레이아웃 (시각화 알고리즘)

**Authors:** Thomas M. J. Fruchterman, Edward M. Reingold
**Publication:** Software: Practice and Experience, Vol. 21(11), pp. 1129-1164 (November 1991)
**DOI:** https://doi.org/10.1002/spe.4380211102

### 핵심 개념
> "We present a modification of the spring-embedder model for drawing undirected graphs with straight edges. Our heuristic strives for uniform edge lengths, and we develop it in analogy to forces in natural systems, for a simple, elegant, conceptually-intuitive, and efficient algorithm."

### Kairo에 적용된 부분
- `pages/5_🧩_Graph.py`의 노드 배치 알고리즘
- PyVis/VisJS의 Physics Engine이 이 알고리즘의 변형을 사용
- Knowledge Graph의 엣지를 "스프링"으로 모델링하여 자연스러운 배치

### 기술적 의의
- Force-directed layout 알고리즘의 고전 (1,900+ 인용)
- 물리적 힘(인력/척력)을 그래프 배치에 적용
- 이 알고리즘의 변형이 VisJS, D3.js, Gephi 등에 사용됨

---

## 9. Network Visualizations with Pyvis and VisJS (시각화 도구)

**Authors:** WestHealth Group
**Publication:** SciPy Proceedings 2020 (학술 논문)
**Link:** https://proceedings.scipy.org/articles/Majora-342d178e-008

### 핵심 개념
> "Pyvis is built on top of VisJS JavaScript library... declarative approach makes it easy to quickly explore graph visualizations."

### Kairo에 적용된 부분
- `pages/5_🧩_Graph.py` — Knowledge Graph 인터랙티브 시각화
- Physics engine 기반 노드 배치 (Barnes-Hut 알고리즘)
- 마우스 드래그, 확대/축소, 호버 툴팁

### 기술적 근거
- VisJS는 Force-directed layout 알고리즘 사용
- 1,000개 노드 이상에서도 WebGL 기반 고성능 렌더링
- 과학 컴퓨팅 학회(SciPy)에서 인정받은 오픈소스 시각화 도구

---

## 10. Interactive Knowledge Graph Visualization + LLM Agents (최신 트렌드)

**Authors:** Jamie P. McCusker et al.
**Publication:** CEUR Workshop Proceedings (2025)
**Link:** https://ceur-ws.org/Vol-3773/paper2.pdf

### 핵심 개념
> "Interactive visualization over large knowledge graphs combined with LLM reasoning shows promise."

### Kairo에 적용 가능한 개선 방향
- 현재 Kairo는 정적 그래프만 표시 → LLM이 그래프를 해석/설명하는 기능 추가 가능
- 노드 클릭 시 LLM이 해당 노드의 관계를 자연어로 설명
- Knowledge Graph → 자연어 생성 (Graph-to-Text)

---

## 11. Personal Knowledge Management (PKM) 시스템 (지식 관리 이론)

**Authors:** Max Völkel, et al.
**Publication:** International Journal of Knowledge Management (IJKM)
**Link:** https://pdfs.semanticscholar.org/fc01/d8db4f15533f475c02ba1cf29d49fa7b5f90.pdf

### 핵심 개념
> "Personal knowledge management (PKM) is a crucial element as well as complement of enterprise knowledge management (EKM) which has been largely neglected by Enterprise Information Systems. This paper collects requirements for a specific class of PKM software, which supports personal note taking and the idea of extending the human memory by information management."

### Kairo에 적용된 부분
- KB.md가 개인 지식 관리(PKM) 도구로서의 역할
- 지식의 생성(Creation) → 저장(Storage) → 검색(Retrieval) → 공유(Sharing) 라이프사이클
- Knowledge-cue life cycle 모델과 Kairo의 Growth Log 대응

### 기술적 의의
- PKM 시스템의 요구사항을 체계적으로 정리한 기초 연구
- 개인 지식 모델링 도구의 설계 가이드라인 제시
- 링킹(Linking), 계층(Hierarchy), 주석(Annotation) 등 핵심 기능 정의

---

## 12. Streamlit in Academic & Enterprise Settings (UI 프레임워크)

**Authors:** Kyle Kearns (Wharton AI & Analytics Initiative)
**Publication:** Wharton School, University of Pennsylvania (2025)
**Link:** https://ai-analytics.wharton.upenn.edu/build-interactive-dashboards-with-chatgpt-and-streamlit/

### 핵심 개념
> "Streamlit is an open-source Python framework that makes it easy to build web-based data apps — no front-end experience required."

### Kairo에 적용된 부분
- 전체 UI 프레임워크로 Streamlit 채택
- ChatGPT + Streamlit 결합 → LLM 대시보드 구축
- 순수 Python만으로 웹 인터페이스 구현

### 기술적 의의
- Apache 2.0 라이선스, 44,000+ GitHub Stars
- Python 스크립트를 인터랙티브 웹앱으로 변환하는 프레임워크
- 과학 컴퓨팅, 데이터 분석, ML 데모에 널리 사용

---

## 종합: Kairo의 학술적 위치

Kairo는 위 12개 학술 자료의 핵심 철학과 기술을 융합한 프로젝트입니다:

### 철학적 기반
1. **Karpathy LLM Wiki** → 단일 파일(KB.md) 지식 축적 철학
2. **PKM 시스템** → 개인 지식 관리의 이론적 토대

### 핵심 기술
3. **GraphRAG (Microsoft)** → Knowledge Graph + LLM 통합
4. **ReAct (ICLR 2023)** → 추론-행동 결합 에이전트
5. **MemGPT (ICLR 2024)** → LLM 메모리 계층 관리
6. **Toolformer (NeurIPS 2023)** → 자율적 도구 사용
7. **Generative Agents (UIST 2023)** → 자율 에이전트 아키텍처
8. **HuggingGPT (NeurIPS 2023)** → 모듈형 에이전트 시스템

### 시각화 기술
9. **Fruchterman-Reingold (1991)** → Force-directed 그래프 레이아웃
10. **Pyvis/VisJS (SciPy 2020)** → 인터랙티브 지식 그래프 시각화
11. **CM4AI KG + LLM (CEUR 2025)** → 지식 그래프와 LLM의 시너지

### UI 프레임워크
12. **Streamlit / Wharton** → 데이터 + LLM + 웹앱 통합 프레임워크

> 참고: 위 논문/기사는 모두 오픈소스 프로젝트 또는 공개 논문으로, 학술/상업 목적으로 자유롭게 인용 가능합니다.
> arXiv 논문은 CC-BY 라이선스, PyVis는 BSD-3, Streamlit은 Apache 2.0 라이선스를 따릅니다.
