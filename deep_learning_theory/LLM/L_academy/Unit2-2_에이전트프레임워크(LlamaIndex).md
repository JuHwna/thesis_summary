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
  
