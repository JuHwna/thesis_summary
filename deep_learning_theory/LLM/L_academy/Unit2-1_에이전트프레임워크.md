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

