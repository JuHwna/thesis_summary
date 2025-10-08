# 01. 에이전트 RAG 구현
## 1. 에이전트 구현 시나리오
### 파티 준비를 위한 에이전트, 알프레드
#### 최신 정보를 반영하기 위해 RAG 사용, 손님 리스트와 같은 특정 데이터에 대한 접근성 향상
- **RAG(Retrieval Augmented Generation)**
  - LLM의 제한된 지식 문제를 해결하기 위해 실시간으로 외부 데이터에서 정보를 검색한 뒤 그 정보로 응답을 생성하는 방식
- 에이전틱 RAG
  - 에이전트가 필요한 툴을 스스로 선택하여 RAG 워크플로우를 조립하고 실행하는 구조
  - 단순히 문서 위에서 답변하는 것이 아니라 툴 간 전환과 판단을 수행
 
- 시나리오
  - 호화로운 파티 개최
  - 손님, 일정, 메뉴 등 다양한 정보 필요
  - 실시간 질의 응답 및 이벤트 대응 필요
- 요구 사항
  - 파티 기획 보조
  - 손님 응대
  - 정보 수집, 검색, 업데이트 실행

### 고려해야 할 조건
- 르네상스적 교양 : 스포츠, 문화, 과학 지식
- 금기 주제 : 정치, 종교
- 예절 : 손님의 관심사 이해
- 날씨 정보 : 실시간 확인으로 불꽃놀이 타이밍 조절

### 툴 구성
- 아래의 툴을 에이전트 내에서 조합하여 실행
- 손님 정보 검색 : 손님의 이름, 배경, 취향 등 저장된 정보를 빠르게 조회
- 웹 검색 : 외부 인터넷에서 최신 뉴스나 정보들을 실시간으로 수집
- 날씨 업데이트 API : 기상 정보를 가져와 불꽃놀이 타이밍 등 행사 계획에 반영
- 모델 다운로드 통계 : 인기 있는 AI 모델의 다운로드 수나 트렌드를 확인해 기술적 참고자료로 활용

### 프로젝트 구조
- tools.py : 에이전트의 보조 도구 제공
- retriever.py : 검색 기능 구현
- app.py : 모든 구성 요소를 통합하여 완전한 에이전트 구축

### 데이터셋

||설명|예시|
|-|---|----|
|name|손님의 이름|Ada Lovelace|
|relation|게스트와 호스트의 관계|best friend|
|description|게스트에 대한 설명|Lady Ada Lovelace is my best friend <br> She is an esteemed mathematician and friend|
|email|초대장을 보내기 위한 연락처|ada.lovelace@example.com|

## 2. 손님 정보 검색 툴
### 예시 상호작용 - 손님에 대한 정보를 실시간으로 제공
- 사용자 : "알프레드, 저 엠버서더와 대화하고 있는 신사는 누구인가요?"
- 알프레드
  - 데이터베이스 검색
  - 손님의 배경, 최근 업적, 이메일 주소 등 상세 정보 제공

### Smolagents
#### [STEP 1] 데이터셋 로드 및 준비
- (1) 데이터셋 로드 및 준비
- (2) 각 항목을 Document 객체로 변환
  - langchain.docstore.document 모듈 사용
- (3) Document 객체를 리스트로 저장
<img width="649" height="529" alt="image" src="https://github.com/user-attachments/assets/be94cbda-c1cd-494f-8c67-d307e40536e2" />

#### [STEP 2] 검색 툴 생성
- name, description
  - 에이전트가 툴을 이해할 수 있도록 이름과 설명 설정
- inputs : 툴이 필요로 하는 파라미터 정의
- output_type : 반환 결과의 자료형은 문자열

<img width="661" height="476" alt="image" src="https://github.com/user-attachments/assets/214862fb-6ab7-46cb-8dc7-c033b42d6b75" />

- \_\_init\_\_ 메서드
  - 미리 준비된 손님 정보 문서들(docs)을 받음
  - BM25Retriever 생성
    - langchain_community.retrievers 모듈 사용
    - 텍스트 검색 알고리즘 활용
    - 임베딩 없이도 강력한 성능을 발휘
- forward 메서드
  - 사용자의 쿼리를 처리해 가장 관련성 높은 손님 정보 3개를 반환

<img width="653" height="467" alt="image" src="https://github.com/user-attachments/assets/b11f9a1f-5cb0-4fc2-8cd0-ce79b9730806" />

#### [STEP 3] 에이전트와 툴 통합
- 에이전트 생성
  - 모델 초기화
    - Hugging Face에서 제공하는 모델 사용
  - 에이전트 생성
    - CodeAgent 사용
    - 앞서 정의한 guest_info_tool을 사용할 수 있도록 연결
- 에이전트 실행
  - 쿼리의 의미 파악 => 손님 정보 요청임을 인식
  - 연결된 툴 중 guest_info_tool이 적합하다고 판단
  - 해당 툴을 호출하며 BM25 기반으로 손님 정보를 검색
  - 검색 결과를 종합하여 자연스럽게 응답 생성

<img width="706" height="464" alt="image" src="https://github.com/user-attachments/assets/2d492292-e52a-4b13-a847-6f34e7364dd2" />

### LlamaIndex
#### [STEP 1] 데이터셋 로드 및 준비
- 데이터셋 로드 및 준비
- 각 항목을 Document 객체로 변환
  - llama_index.core.schema 모듈 사용
- Document 객체를 리스트로 저장

<img width="664" height="527" alt="image" src="https://github.com/user-attachments/assets/dec3da4e-d91d-4f87-a533-d978654dc5c0" />

#### [STEP 2] 검색 툴 생성
- BM25Retriever 생성
