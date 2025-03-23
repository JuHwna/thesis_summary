# 1. LLM과 Agents
## (1) Agent
### 에이전트 이해
- 에이전트의 개념과 다양한 응용
  - step 1: Understand what are Agents
  - step 2: Learn what are LLMs and Messages System
  - step 3: Study Tools and Actions
  - step 4: Learn the Agent workflow
  - step 5: Code your first Agent

- 에이전트 순서를 통한 예시
  - 명령 받기
  - 명령 이해하기(Reason and plan)
    - 자연어 이해 : 자연어를 이해하기 때문에 우리의 요청을 빠르게 파악
    - 추론과 계획 : 주문을 이행하기 전에 추론과 계획을 통해 필요한 단계와 툴을 파악함
    - 행동 계획
  - 실행하기
    - 행동 실행 : 계획을 실행하기 위해 자신이 알고 있는 도구 박스에서 툴을 사용
    - 커피 만들기 : 커피를 내리기 위해 커피 머신을 작동
    - 커피 제공
   
- 에이전트의 개념
  - 추론, 계획, 플랫폼과 상호작용할 수 있는 AI모델
  - 능동성, 즉 플랫폼과 상호작용할 수 있는 능력이 있음
  - User Request -> Step 1: Think and Plan -> Step 2: Act using Tools
 
### 에이전트의 정의
- 에이전트란
  - 사용자가 정의한 목표를 달성하기 위해 플랫폼과 상호작용하는 AI모델을 활용하는 시스템
  - 작업을 수행하기 위해 추론, 계획, 그리고 액션(외부 툴을 통해) 실행을 결합
- 에이전트의 구성 요소
  - 두뇌(AI모델)
    - 모든 사고가 일어나는 곳
    - 추론과 계획을 처리
    - 상황에 기반하여 어떤 액션을 취할지 결정
  - 몸 (기능과 툴)
    - 에이전트가 할 수 있는 모든 것
    - 에이전트에 사전 구성된 툴과 능력에 따라 액션의 범위가 결정됨

- 에이전트에 사용되는 AI모델
  - LLM(대규모 전이 모델)
    - 입력 : 텍스트
    - 출력 : 텍스트
    - 예시 : OpenAI의 GPT4, Meta의 Llama, Google의 Gemini
  - 그 외
    - 입력 : 텍스트 외 다른 입력 (이미지 등)
    - 예시 : VLM
      - LLM과 유사
      - 입력으로 이미지도 가능


- 에이전트의 툴
