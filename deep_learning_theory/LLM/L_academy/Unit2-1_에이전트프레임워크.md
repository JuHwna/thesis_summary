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
  - LLM의 아키텍처를 시각적으로 표현하여 복잡한 프롬프트 설계를 효율적으로 지원

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

### smolagents를 사용하는 경우
- 최소한의 솔루션이 필요한 경우
- 애플리케이션 로직이 단순한 경우
- 복잡한 설정 없이 빠르게 테스트하고 싶은 경우

### 코드 기반 vs JSON 기반
- 일반적으로 다른 프레임워크에서는 에이전트가 JSON 형식으로 액션 작성
- smolagents는 Python 코드 기반의 툴 호출이 중심(JSON 형식도 사용할 수 있음)
- JSON을 해석하여 코드를 생성하는 과정 없이 LLM이 직접 실행 가능한 Python 코드를 출력하여 실행 가능

<img width="1063" height="376" alt="image" src="https://github.com/user-attachments/assets/22d8ba34-1c5a-4251-9536-16eae282b1f3" />

### smolagents의 주요 모델 클래스
- Transformers Model
  - transformers 라이브러리를 활용한 로컬 모델 실행 지원
- HfApiModel
  - Hugging Face Inference API 또는 서드파티 인퍼런스 제공 업체와 통합 가능
- LiteLLM Model
  - LiteLLM을 활용한 경량화된 모델 실행
- OpenAI ServerModel
  - OpenAI API와 호환되는 모든 서비스 연결 가능
- AzureOpenAI ServerModel
  - Azure OpenAI API를 활용하여 서비스 배포 가능

### 코드 에이전트 구축하기
- 실습 : 프로그래밍 작업을 도와주는 코드 에이전트(Code Agent) 를 직접 구축
  - 프롬프트를 입력하면 자동으로 파이썬 코드를 생성하고, 그 결과를 실행한 뒤 다시 피드백하는 구조로 설계
  - 내용
    - 사용자 질문을 이해하고 코드로 변환하는 LLM 구성
    - 생성된 코드를 실행하고 출력값 얻기
    - 반복적인 수정과 실행을 통한 문제 해결 구조 만들기
    - 코드 실행 결과에 따라 다음 행동을 선택하는 루프 로직 구현

### 코드 에이전트가 필요한 이유
- 다단계 에이전트 (Multi-Step Agents) 프로세스에서 LLM은 작업을 작성하고 실행하며, 일반적으로 외부 툴 호출이 포함
- 기존 방식에서는 JSON 형식으로 툴의 이름과 인수를 문자열로 지정해야 하며, 시스템이 이를 구문 분석하여 실행할 툴을 결정
- 연구에 따르면 **LLM이 코드로 직접 작업을 수행하는 방식이 더 효과적**
- JSON 대신 코드를 사용하여 작업의 이점
  - 조합성(Composability): 쉽게 작업을 결합하고 재사용 가능
  - 객체 관리(Object Management): 이미지와 같은 복잡한 구조를 직접 처리 가능
  - 범용성(Generality): 계산적으로 가능한 모든 작업을 표현 가능
  - 자연스러움(Natural for LLMs): LLM이 학습한 고품질 코드 데이터와 유사

### 코드 에이전트의 작동 방식
<img width="875" height="476" alt="image" src="https://github.com/user-attachments/assets/6302d41b-e63e-45d8-a28f-63fa0d6b3a0b" />




## 3. ToolCallingAgent
### ToolCallingAgent
- smolagents에서 제공하는 에이전트
  - LLM의 내장 툴 호출 기능을 활용해 JSON 구조로 툴 호출을 생성
  - CodeAgent와의 차이점
    - CodeAgent : Python 스니펫
    - ToolCallingAgent : JSON 구조(OpenAI, Anthropic 등 많은 회사에서 사용)
### CodeAgent vs ToolCallingAgent
- CodeAgent의 성능이 전반적으로 뛰어나기 때문에 smolagents는 주로 CodeAgent에 초점을 맞추고 있음
- ToolCallingAgent는 복잡한 툴 호출이 필요 없는 간단한 시스템에서 효과적

- CodeAgent : 실행 가능한 Python 코드 생성
- ToolCallingAgent : 툴의 이름과 인수를 저장하는 JSON 객체 생성

<img width="1175" height="424" alt="image" src="https://github.com/user-attachments/assets/cb811603-141c-432c-8829-a8a25566208a" />

<img width="1250" height="583" alt="image" src="https://github.com/user-attachments/assets/12cb4b99-6f03-4000-87a2-9ae65a1ca468" />

