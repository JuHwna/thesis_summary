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



