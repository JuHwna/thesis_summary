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
  - 
