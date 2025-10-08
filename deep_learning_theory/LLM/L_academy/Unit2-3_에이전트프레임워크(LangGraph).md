# 03. LangGraph
## 1. LangGraph
### LangGraph란
- 복잡한 LLM 워크플로를 구성하고 조율하는 데 도움을 주는 프레임워크
  - LangChain에서 개발한 프레임워크
  - LLM을 통합한 애플리케이션의 제어 흐름을 관리하는 데 사용

### LangChain VS LangGraph
- LangChain
  - 표준 인터페이스 제공(검색, LLM 호출, 툴 호출)
  - LLM을 사용한 대화형 애플리케이션 또는 정보 검색 시스템을 쉽게 만들 수 있도록 툴과 기능 제공
- LangGraph
  - LLM의 작동 흐름을 조정하고 관리
  - 사용자가 작업의 흐름을 쉽게 시각화하고 조정할 수 있도록 지원

### LangChain과 LangGraph는 독립적으로 사용할 수 있으나 실제 사용 사례에서는 함께 사용하는 경우가 많음

### LangGraph는 언제 사용해야 할까?
- 자유 : 창의적 문제 해결(ex. Code Agents)
- 제어 : 예측 가능한 동작(ex. LangGraph)

### LangGraph는 애플리케이션에 대한 제어가 필요할 때 사용


### LangGraph의 장점
- 명확한 제어 흐름 구성
  - 복잡한 분기와 다단계 절차를 시각적으로 설계할 수 있는 구조 제공
- 지속 가능한 상태 관리
  - 단계 간 데이터를 유지하며 흐름 전체에서 일관된 처리 가능
- AI 기능과 로직의 결합
  - LLM 기반의 유연성과 조건 기반의 결정성을 동시에 활용
- 복잡한 워크플로우 통합
  - 사용자의 개입이나 다중 구성 요소가 포함된 시스템에도 적용 가능

- LLM의 할루시네이션 문제 다루는 방법
  - LangGraph는 LLM의 출력을 검증하고 확인할 수 있는 구조화된 워크플로우를 제공함
    - 검증단계, 오류 처리 경로 등을 포함한 구조적 접근을 통해 환각의 영향을 줄이는데 도움이 됨.

### 예시 : 문서 질의 응답
- 문서에 대한 질문에 답변하는 LLM 어시스턴트
- 워크플로우
  - 문서 형태에 따라 분기
  - 일부는 텍스트화, 일부는 툴 호출
  - 결정 지점이 존재함
<img width="432" height="522" alt="image" src="https://github.com/user-attachments/assets/75b4d32e-517d-4e09-8fe1-13bdd279e127" />

- 문서 형태에 따라 분기
<img width="428" height="523" alt="image" src="https://github.com/user-attachments/assets/91d9740f-c75d-4aa6-b886-a8d28d4285ff" />

- 일부는 텍스트화
<img width="676" height="550" alt="image" src="https://github.com/user-attachments/assets/796002b6-13fa-454e-9d74-0e4a7c5a7f33" />

- 일부는 툴 호출
<img width="495" height="518" alt="image" src="https://github.com/user-attachments/assets/131dbe67-8a86-4391-8cf8-bf2d719d5ad6" />

### LangGraph의 구성 요소
- 노드(Node) : 애플리케이션의 개별 처리 단계 => LLM 호출, 툴 실행, 판단 로직
- 엣지(Edge) : 한 노드에서 다음 노드로 이동하는 경로 => 질문 유형이 "표"일 경우 변환 노드로 이동
- 상태(State) : 노드 간에 공유되는 데이터 흐름 제어에 사용 => 현재까지 수집된 입력값, 이전 응답 결과 등

### "일반 Python 코드로도 모든 흐름을 처리할 수 있지 않나요?"
- Python만으로도 흐름 제어는 가능하지만 LangGraph는 더 쉽고 체계적인 방식으로 복잡한 LLM 기반 애플리케이션을 설계할 수 있도록 지원

||일반 Python 코드|LangGraph|
|-|--------------|----------|
|제어 흐름 설계|수동 구현(if, for, 함수 등으로 직접 작성)|유도 그래프 기반 구조 제공|
|상태 관리|별도 전역 변수, 클래스 등으로 처리|내장된 상태 객체를 통한 간결한 관리|
|시각화 및 로깅|외부 라이브러리 필요|기본 제공|
|툴 추상화|직접 설계 필요|노드 단위로 추상화 가능|
|인간 개입 처리|별도 로직 구성 필요|내장 기능으로 쉽게 구현 가능|

## 2. LangGraph 구성 요소
### 기본 빌딩 블록
<img width="670" height="292" alt="image" src="https://github.com/user-attachments/assets/85a5aea9-1da5-47e9-ad94-fa04461e7d2e" />

- LangGraph의 애플리케이션은 진입점(entrypoint)에서 시작
- 실행에 따라 흐름이 하나의 함수나 다른 함수로 이동하여 END에 도달

### 노드(Node)
- 하나의 동작 단위
  - 입력 : 상태
  - 출력 : 상태 반환
- 워크플로우에서 특정 작업을 수행
  - LLM 호출 : 텍스트 생성 또는 의사 결정
  - 툴 호출 : 외부 시스템과 상호 작용
  - 조건부 논리 : 다음 단계를 결정
  - 상호작용 : 사용자로부터 입력 받기
- Edge를 통해 노드 간의 호름 연결

<img width="676" height="451" alt="image" src="https://github.com/user-attachments/assets/45d5b619-5f84-482a-95ea-bdca41e58734" />

### 엣지(Edge)
- 노드 간의 흐름
- 기본 엣지 : 항상 다음 노드로 이동
- 조건부 엣지 : 한 노드의 실행 결과에 따라 어떤 노드로 이동할지를 결정하는 조건부 연결

<img width="676" height="455" alt="image" src="https://github.com/user-attachments/assets/fa73198f-ce3a-446b-8ef7-0273684c7bd5" />

### 상태(State)
- 현재 워크플로우의 정보를 담고 있는 구조체
- 노드가 실행될 때마다 state 업데이트 => 업데이트된 state를 다음 노드로 전달
- 예시 : 채팅 봇에서 사용자의 입력이나 이전 응답 같은 정보를 담은 상태

<img width="693" height="245" alt="image" src="https://github.com/user-attachments/assets/ba3c4277-b700-473d-a7d1-64ce00e6ef3f" />

### 상태 그래프(StateGraph)
- 전체 에이전트 워크플로우를 담고 있는 컨테이너
<img width="694" height="381" alt="image" src="https://github.com/user-attachments/assets/8c7989f4-e888-4eb5-8e62-62246b0ceb3f" />

<img width="338" height="497" alt="image" src="https://github.com/user-attachments/assets/59c4ade2-7eda-45c4-966d-d40dc4649d6b" />

- get_graph()를 통해 raw graph 구조를 가져옴
- invoke를 통해 graph 실행




