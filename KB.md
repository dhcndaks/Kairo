# Kairo Knowledge Base

## 👤 User Profile
- name: (당신 이름)
- major: 컴퓨터공학
- preferences: AI, 웹 개발, 트렌드 분석

## 📚 Projects
### project: Kairo
- role: 데이터 및 발표 담당
- description: 하나의 KB.md로 동작하는 개인 에이전트 시스템
- tech: Streamlit, DeepSeek V4 Flash, Python

## 🔧 Skills
### skill: web-research
- trigger: "검색", "찾아봐", "search"
- action: web_search(query)
- description: 웹 검색 결과 요약

### skill: planner
- trigger: "계획", "일정", "schedule"
- action: generate_plan(tasks)
- description: 작업 계획 수립

### skill: coding-helper
- trigger: "코드", "프로그래밍", "code", "디버그"
- action: help_coding(problem)
- description: 코딩 문제 해결 도움

### skill: trend-analysis
- trigger: "트렌드", "뉴스", "키워드", "trend"
- action: web_search(query)
- description: 뉴스 트렌드 분석 및 요약

## 🧩 Knowledge Graph (자동 발견)

### Edge: 사용자 → 프로젝트
- source: 사용자 (컴퓨터공학)
- target: Kairo 프로젝트
- type: 참여
- discovered: 2026-05-22

### Edge: 프로젝트 → 기술
- source: Kairo 프로젝트
- target: DeepSeek V4 Flash
- type: 사용
- discovered: 2026-05-22

### Edge: 프로젝트 → 기술
- source: Kairo 프로젝트
- target: Streamlit
- type: 사용
- discovered: 2026-05-22

### Edge: 기술 → 기술
- source: Streamlit
- target: Python
- type: 기반
- discovered: 2026-05-22

### Edge: 기술 → 기술
- source: DeepSeek V4 Flash
- target: LLM
- type: 분류
- discovered: 2026-05-22

### Edge: 기술 → 기술
- source: LLM
- target: AI
- type: 분류
- discovered: 2026-05-22

### Edge: 기술 → 기술
- source: Python
- target: AI
- type: 분야
- discovered: 2026-05-22

## 📊 Growth Log

<!-- 상호작용 기록이 자동으로 추가됩니다 -->
