# 2. LlamaIndex
## 1. LlamaIndex
### LlamaIndex란?
- 데이터에 대한 LLM 기반의 에이전트를 생성하기 위한 툴킷
  - 대규모 언어 모델(LLM)을 사용하는 애플리케이션을 만들기 위한 프레임워크
  - 컨텍스트 증강을 통해 데이터를 더 잘 활용할 수 있게 도와주는 역할
  - 비개발자도 쉽게 설계 가능

### LlamaIndex 주요 구성 요소
- 컴포넌트 : LlamaIndex에서 사용하는 기본 빌딩 블록(프롬프트, 모델 등)
- 툴 : 검색, 계산 또는 외부 서비스에 접근하는 특정 기능을 제공하는 컴포넌트
  - 에이전트가 작업을 수행할 수 있도록 하는 빌딩 블록
- 에이전트 : 툴을 사용하고 결정을 내릴 수 있는 컴포넌트
  - 복잡한 목표 달성을 위해 툴 사용을 조정
- 워크플로우 : 논리를 함께 처리하는 단계별 프로세스

### LlamaIndex 장점
- 명확한 워크플로우 
  - 이벤트 기반으로 작동
  - 비동기 방식 사용
    - 로직을 쉽게 구성하고 정리 가능
- LlamaParse
  - LlamaParse를 사용해 정확하고 효율적으로 문서 파싱 가능(유료 기능)
- 호환성
  - 다양한 프레임워크와 호환성이 좋음
    - LLM, retriever, 인덱스 등 사용 가능
- Llama Hub
  - LlamaIndex에서 사용할 수 있는 컴포넌트, 에이전트 및 툴이 등록된 허브

### LlamaHub
- LlamaIndex에서 사용할 수 있는 컴포넌트, 에이전트 및 툴이 등록된 허브

<img width="673" height="427" alt="image" src="https://github.com/user-attachments/assets/465033d9-99c1-4157-877a-4be11d94d25d" />

- 예시
  - LLM 컴포넌트를 위한 Hugging Face 추론 API 사용
  - LlamaIndex와 Hugging Face API를 활용하여 특정 LLM을 설정
  - 설정한 LLM을 통해 사용자 질문에 대한 응답을 생성

## 2. LlamaIndex 컴포넌트
### LlamaIndex 주요 컴포넌트
- QueryEngine
  - 데이터에 대한 질문 처리
  - 자연어 쿼리를 입력받아 응답 변환
  - RAG 툴로 활용 가능
- Retriever
  - 정보 검색
  - 요청한 데이터와 관련된 내용을 검색하여 반환
- Index
  - 데이터 저장 및 구조화
  - LLM의 경우 벡터 임베딩을 생성
  - 다양한 메타데이터 활용
- Response Synthesizers
  - 검색 결과로 응답 생성
  - 전략을 통해 응답 품질을 개선하고 맞춤화

### RAG(Retrieval Augmented Generation)
- LLM의 훈련 데이터에 최신 정보와 관련 데이터를 추가하는 기법
<img width="636" height="368" alt="image" src="https://github.com/user-attachments/assets/e80d40a9-3675-43cf-abf7-1eaeaf21e3d7" />

### RAG 파이프라인
#### 데이터 로드
- 데이터 로드 : 다양한 소스에서 데이터 가져오기
- (1) SimpleDirectoryReader : 로컬 파일 로드
- (2) LlamaParse : PDF 및 기타 형식 파싱
- (3) LlamaHub : 다양한 데이터 소스 통
- 
<img width="706" height="297" alt="image" src="https://github.com/user-attachments/assets/f1f7938d-946f-4890-8a5a-dea382c4b7dd" />

- 노드 객체 생성
  - 원본 문서를 작은 조각으로 쪼개기
  - AI가 쉽게 작업할 수 있도록 변환

<img width="701" height="539" alt="image" src="https://github.com/user-attachments/assets/04aabbbb-986f-4cc8-a51c-d87a2fe430fc" />

#### 인덱싱 및 저장
- 인덱싱 : 검색 가능하도록 데이터 구조화
- 저장 : 반복 사용 가능하도록 인덱스 저장
- 벡터 저장소
  - Chroma 및 기타 저장소 활용하여 인덱스 생성
- 예시 코드
  - (1) ChromaDB 클라이언트 생성
  - (2) "alfred"라는 Chroma 컬렉션 생성/가져오기
  - (3) 벡터 저장소 설정
  - (4) 데이터 Ingestion 파이프라인 설정

<img width="700" height="518" alt="image" src="https://github.com/user-attachments/assets/90886848-56ea-4ee2-a5e5-6d0c1a453ba3" />

- 벡터 임베딩 활용
  - 쿼리와 노드를 동일한 벡터 공간에 임베딩하여 사용자가 입력한 쿼리에 대해 유사한 정보를 찾음
  - VectorStoreIndex로 자동 처리하여 일관성을 보장
  - 모든 정보는 자동으로 ChromeVectorStore 객체와 전달된 디렉토리 경로 내에 유지

<img width="702" height="311" alt="image" src="https://github.com/user-attachments/assets/8ba72f2c-ac10-43b7-9654-1d708a67f542" />

#### 검색 요청
- 검색 요청 : 사용자가 요청한 정보를 검색
- 쿼리 인덱스 변환
  - as_retriever
    - 기본 문서 검색
    - 유사성 점수가 포함된 NodeWithScore 객체 목록 반환
  - as_chat_engine
    - 여러 메시지에 걸쳐 기억을 유지하는 대화형 상호작용
    - 각 메시지의 맥락을 이해하고 이전 대화 내용을 바탕으로 응답을 생성
  - as_query_engine
    - 단일 질문-답변 상호작용
    - 사용자로부터 받은 질문에 대한 직접적인 답변을 제공

<img width="700" height="444" alt="image" src="https://github.com/user-attachments/assets/a94b3879-fa7f-4c30-948a-2eb498c02ce5" />

#### 평가
- 평가 : 응답의 정확성과 품질을 분석

### 응답 처리 전략
- compact(default)
  - 여러 텍스트 조각을 미리 연결하고 요약하여 LLM을 호출하는 횟수를 줄임
- refine
  - 검색된 각 텍스트 조각을 순서대로 살펴보고 이를 기반으로 답변을 생성하고 개선
- tree_summarize
  - 검색된 각 텍스트 조각을 통해 답변 생성
  - 응답의 구조를 트리 형태로 설
 
### RAG-평가
- Faithfulness Evaluator
  - 충실도 : 사용자가 요청한 정보와 얼마나 잘 일치하는지를 분석
- AnswerRelevancy Evaluator
  - 관련성 : 질문과 응답 간의 관련성을 판단
- Correctness Evaluator
  - 정확성 : 사용자가 얻는 정보가 오류가 없고 사실에 기반하여 제공되도록 평가

<img width="660" height="529" alt="image" src="https://github.com/user-attachments/assets/c97a0272-14b5-4625-83c8-fa17fb8531b5" />

- 쿼리 결과의 충실도를 평가
  - FaithfulnessEvaluator 사용
  - 쿼리 엔진이 질문에 대한 응답을 반환
  - evaluate_response를 사용하여 쿼리의 응답을 평가
  - 평가 결과의 passing 속성을 호출하여 응답이 충실한지 여부를 확인(True/False)

## 3. LlamaIndex 툴
### 툴의 중요성
- 명확하게 툴을 정의하여 성능을 향상시킬 수 있음
  - 명확한 툴 인터페이스는 LLM이 쉽게 사용할 수 있도록 도와줌
  - 소프트웨어 API처럼 도구의 작동 방식을 이해하는 것이 효과적
- 툴 생성 시 반드시 포함해야 하는 정보
  - 함수만 필요
  - 이름과 설명은 제공된 함수의 이름과 문서 문자열로 기본값이 설정

### LlamaIndex 툴의 주요 유형
- FunctionTool
  - Python 함수를 툴로 변환
- QueryEngine Tool
  - 에이전트가 쿼리 엔진을 사용할 수 있도록 도와줌
  - 다른 에이전트를 툴로 사용할 수 있음
- Toolspecs
  - 특정 서비스 및 커뮤니티에서 생성된 툴
  - 특정 서비스와 통합 가능
- Utility Tools
  - 다른 툴로부터 대량의 데이터 처리 가능

### FunctionTool
- Python 함수를 툴로 변환
- 지원하는 함수 유형 : 동기식 및 비동기식 함수
- 선택적 매개변수 : name, description

- 코드 예시
  - get_weather : location의 날씨 정보(sunny) 변환
  - FunctionTool.from_defaults
    - 툴에 이름(my_weather_tool)과 설명을 추가
    - 에이전트가 툴의 기능을 이해
  - 출력 : Getting weather for New York
  - 반환 : The weather in New York is sunny

<img width="660" height="533" alt="image" src="https://github.com/user-attachments/assets/71789efb-8d19-4889-9188-7e725277a474" />

### QueryEngineTool
- 에이전트가 쿼리 엔진을 사용할 수 있도록 지원
- 쿼리 엔진을 기반으로 구축
- 다른 에이전트를 툴로 사용할 수 있는 기능 포함
- 코드 예시
  - 임베딩 모델과 벡터 저장소를 사용하여 쿼리 엔진 생성
  - 생성한 쿼리 엔진을 툴로 변환

<img width="659" height="537" alt="image" src="https://github.com/user-attachments/assets/454e0d3e-7e6e-4fed-b35b-a8effade4ab2" />

### Toolspecs
- 특정 목적을 위해 함께 작동하는 툴의 조합
  - 에이전트 기능을 확장하는 커뮤니티 생성 툴 조합
  - 커뮤니티가 툴을 공유하고 재사용할 수 있게 
- 코드 예시
  - GmailToolSpec을 사용하여 Gmail 관련 툴을 로드
  - 각 툴의 메타데이터(name, descriptio)를 추출하여 리스트 형식으로 저장
<img width="655" height="539" alt="image" src="https://github.com/user-attachments/assets/104d210f-ed1d-4da7-8651-b3d81de88ce1" />

### Utility Tools
- 다른 툴로부터 대량의 데이터를 처리할 수 있도록 지원
- API를 직접 쿼리하면 대량의 데이터가 반환될 수 있음
- 반환된 데이터 중 일부는 무관할 수 있으며 LLM의 컨텍스트 창을 초과하거나 불필요한 토큰 수를 증가시킬 수 있음
  - Utility Tool을 사용해서 개선 가능
- A. OnDemand ToolLoader
  - 데이터를 필요에 따라 로드하고 인덱싱하여 쿼리할 수 있는 툴
  - 자연어 쿼리로 호출하면 데이터를 가져오고 처리하는 모든 단계가 자동으로 수행됨
- B. LoadAndSearch ToolSpec
  - 로드 툴과 검색 툴을 결합한 툴
  - 데이터를 로드하고 인덱싱한 후, 쿼리를 통해 정보를 검색할 수 있도록 함

## 4. LlamaIndex 에이전트
### LlamaIndex 주요 추론 에이전트
- Function Calling
  - 특정 함수를 호출하여 결과를 반환하는 에이전트
- ReAct
  - 텍스트 엔드포인트와 함께 작동하며 복잡한 추론 처리
- Advanced
  - 더 복잡한 작업과 워크플로를 처리하기 위한 방법

### 에이전트 초기화
- 에이전트 생성 시 기능을 정의하는 함수 및 툴 제공
- 코드 예시
  - multiply : 두 수의 곱을 반환
  - LLM을 초기화
  - multiply를 FunctionTool로 변환하여 에이전트 초기화

<img width="654" height="430" alt="image" src="https://github.com/user-attachments/assets/ca41c530-ce8a-45c2-8771-e33d1c233886" />

- Context 객체
  - 에이전트는 기본적으로 이전의 대화를 기억하지 못함
  - Context 객체를 사용해서 에이전트는 사용자가 이전에 한 말이나 요청을 기억할 수 있음
  - 에이전트가 여러 메시지에 걸쳐 맥락을 유지할 수 있어, 자연스러운 대화 가능
  - 워크플로 상태를 추적하는 데 사용되는 올바른 객체
  - 코드 : run(query_str,ctx=ctx)

<img width="658" height="441" alt="image" src="https://github.com/user-attachments/assets/c263d219-ecde-4d15-a21a-d08dcc48bbd8" />

### QueryEngineTool로 RAG 에이전트 만들기
- RAG 에이전트
  - 데이터를 기반으로 한 정보 검색 및 응답 생성을 위해 에이전트를 활용하는 효과적인 접근 방식
  - QueryEngineTools를 통해 에이전트가 질문에 효과적으로 답변하도록 설정 가능
  - RAG 도구를 포함하여 질문에 답하기 위해 어떤 툴이든지 사용할 수 있도록 결정할 수 있음.

<img width="1247" height="395" alt="image" src="https://github.com/user-attachments/assets/68e03646-0a11-474f-b99e-81a2e243be33" />

### 다중 에이전트 시스템
- 하나의 시스템에서 여러 에이전트가 협력하여 복잡한 작업을 수행
- 다중 에이전트 시스템에서 에이전트의 역할
  - 각 에이전트에 name과 discription을 부여
  - 각 에이전트는 특정한 기능이나 역할을 갖고 있음
    - 사용자의 요청에 대해 더 정확하고 관련성 높은 응답을 제공
- 시스템의 활성 발화자 유지
  - 하나의 에이전트가 사용자와의 주된 상호작용을 담당
    - 일관된 대화 흐름을 유지

## 5. LlamaIndex 워크플로우
### 에이전틱 워크플로우
- 여러 단계로 구성된 프로세스를 정의하여 작업을 체계적으로 수행

- 명확한 코드 구성
  - 코드가 명확하게 구성되어 유지 관리가 용이함
- 유연한 제어 흐름
  - 다양한 상황에 따라 유연하게 대응할 수 있는 구조
- 시스템의 신뢰성
  - 각 단계가 서로 안전하게 정보를 주고받을 수 있음.
- 상태 관리
  - 상태 관리 가능
 
### 워크플로우
- 기본 워크플로우 생성 : 단일 단계 워크플로우 생성
- 단계 연결 : 단계 간에 데이터를 전달하는 사용자 정의 이벤트 생성
- 루프 및 분기 생성 : 타입 헌팅을 통해 단계 간에 분기나 반복적인 작업을 쉽게 처리
- 상태 관리 : 각 단계에서 작업을 수행할 때 현재 상태를 기억하고 계속 추적할 수 있도록 상태 관리 추가

### 다중 에이전트 워크플로우
- 여러 에이전트로 구성된 워크플로우를 자동으로 생성
  - AgentWorkflow 클래스를 사용
  - 각 에이전트는 특정한 기능에 특화되어 있음
  - 서로 다른 에이전트가 협력하여 복잡한 작업을 나누어 처리 -> 시스템의 전체 효율성 향상
  - 루트 에이전트를 지정하여 이 루트 에이전트가 첫 번째 요청을 처리하도록 설계 -> 일관된 흐름을 유지

- 에이전트의 역할
  - 요청 처리 : 툴을 사용하여 사용자의 요청을 직접 처리
  - 작업 재배치 : 자신이 처리하기에 어려운 작업은 다른 더 적합한 에이전트에게 할당
  - 응답 반환 : 사용자의 질문에 대한 응답을 작성해 사용자에게 제공
