# 1. Smolagents
## 1. AI 에이전트 프레임워크
### 에이전트 프레임워크란
- 에이전트 애플리케이션 구축 시 자동화된 작업을 수행하고 상호작용을 통해 문제 해결 및 의사 결정을 지원하는 소프트웨어
  - 특정 작업을 효율적으로 해결하기 위한 워크플로우의 유연성 제공
  - 워크플로우가 복잡한 경우 주로 사용
    - 여러 단계의 작업이 연속적으로 진행
    - LLM이 함수를 호출
    - 여러 에이전트를 함께 사용
  - 예시 : crewai, LangGraph

### 에이전트 프레임워크 예시
- smolagents
  - 다양한 작업을 수행할 수 있도록 설계된 경량화 에이전트 프레임워크
- LlamaIndex
  - 대규모 언어 모델과 외부 데이터 소스 간의 연결을 강화하여 정보를 효율적으로 검색하고 관리
- LangGraph
  - LLM의 아키텍처를 시각적으로 표현하여 복잡한 프롬프트 설계를 효율적으로 지

<img width="777" height="390" alt="image" src="https://github.com/user-attachments/assets/89328619-71fa-40e5-965b-212f38e026de" />

## 2. smolagents
### smolagents란
- AI 에이전트를 간단하게 만들 수 있는 경량 프레임워크
  - Hugging Face에서 제공하는 라이브러리
  - LLM이 상호작용할 수 있또록 에이전시를 부여
  - smolagents의 에이전트
    - Code Agents : 소프트웨어 개발
    - Tool Calling Agents : 모듈화된 기능 중심 워크플로우 구축
    - Retrieval Agents : 정보를 검색하고 종합

### smolagents 장점

<img width="1064" height="356" alt="image" src="https://github.com/user-attachments/assets/8eefe980-3726-4855-a47d-07699af3dda2" />
