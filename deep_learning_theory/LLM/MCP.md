# MCP(Model Context Protocol)
## 1. MCP 소개
### 1. 정의와 목적
- MPC란?
  - LLM 애플리케이션과 외부 데이터 소스 및 도구들 간의 원활한 통합을 가능하게 하는 개방형 프로토콜
  - AI 기반 IDE를 구축하든 채팅 인터페이스를 개선하든, 커스텀 AI 워크플로우를 만들든 관계없이 MCP는 LLM이 필요로 하는 컨텍스트와 연결하기 위한 표준화된 방법을 제공함
- 핵심 목적
  - (1) 컨텍스트 공유 표준화
    - LLM 애플리케이션과 데이터 소스 간의 상호 작용을 위한 표준 프로토콜 제공
    - 구조화된 방식으로 컨텍스트 정보를 전달하고 관리
    - 일관된 인터페이스를 통한 데이터 접근 보장
  - (2) 도구와 기능 노출
    - AI 시스템에 로컬 또는 원격 도구들을 안전하게 노출
    - 표준화된 방식으로 기능을 정의하고 호출
    - 도구의 능력을 명확하게 기술하고 제어
  - (3) 통합 워크플로우 구축

### 2. 기본 아키텍처
- 아키텍처 개요
  - 호스트 애플리케이션, 클라이언트, 서버 간의 표준화된 통신을 위한 프로토콜
  - 구조 : JSON - RPC 기반
    - 안전하고 효율적인 데이터 및 기능 교환을 가능하게 함

![image](https://github.com/user-attachments/assets/61a17aff-1322-4fd6-b1c9-af5032dd73ed)

- (1) MCP 호스트
  - LLM 기반 애플리케이션(Claude Desktop, IDE 등)
  - 여러 MCP 서버와 동시 연결 가능
  - 사용자 인터페이스 제공
  - 보안 및 권한 관리
- (2) MCP 클라이언트
  - 호스트 애플리케이션 낸 프로토콜 구현체
  - 서버와 1:1 연결 유지
  - 메시지 직렬화/역직렬화 처리
  - 상태 관리 및 에러 핸들링
- (3) MCP 서버
  - 특정 기능이나 리소스 제공
  - JSON-RPC 기반 API 구현
  - 보안 및 접근 제어 관리
  - 상태 및 리소스 관리

- 통신 프로토콜
- (1) 메시지 구조
~~~
// 기본 JSON-RPC 2.0 메시지 형식
interface JSONRPCMessage {
    jsonrpc: "2.0";
    id?: string | number;  // 요청/응답 식별자
    method?: string;       // 메서드 이름
    params?: object;       // 매개변수
    result?: object;       // 응답 결과
    error?: {
        code: number;
        message: string;
        data?: unknown;
    };
}
~~~  

- (2) 통신흐름
  - 초기화
    - 능력 협상 (Capability Negotiation)
    - 버전 확인
    - 서버 정보 교환
  - 일반 통신
    - 요청/ 응답
    - 알림
    - 에러 처리
  - 종료
    - 정상 종료
    - 에러 복구
    - 리소스 정리

- (3) 기능 컴포넌트
- 리소스 관리

~~~
interface Resource {
    uri: string;           // 리소스 식별자
    name: string;          // 표시 이름
    description?: string;  // 설명
    mimeType?: string;    // 미디어 타입
}
~~~

### 3. 호스트 클라이언트 서버구조
- MCP의 3-티어 아키텍처
  - 호스트, 클라이언트, 서버로 구성된 3티어 아키텍처를 채택하고 있음
  - 각 계층은 명확한 역할과 책임을 가지며 이를 통해 유연하고 확장 가능한 시스템을 구현함

- (1) 호스트
  - MCP 시스템의 최상위 계층
  - 사용자와 직접 상호작용하는 애플리케이션
  - 주요 역할
    - 사용자 인터페이스 제공
    - LLM과의 통합
    - 여러 MCP 클라이언트 관리
    - 보안 정책 실행

- 대표적인 호스트 애플리케이션
- (1) Claude Desktop
  - 완전한 MCP 지원
  - 리소스, 프롬프트, 도구 통합
  - 로컬 서버 연결 관리
- (2) Zed Editor
  - 코드 에디터 통합
  - 프롬프트 기반 기능
  - 개발자 중심 인터페이스
- (3) Sourcegraph Cody

### 4. 보안 및 신뢰 모델
- MCP는 강력한 기능을 제공하는 만큼, 보안과 신뢰성이 매우 중요
- 핵심 보안 원칙
- (1) 사용자 동의 및 제어
  - 명시적 동의 : 모든 데이터 접근과 작업은 사용자의 명시적 동의 필요
  - 이해 가능한 권한 : 사용자가 이해하기 쉬운 방식으로 권한 설명
  - 세분화된 제어 : 세부적인 수준에서 권한 관리 가능
  - 권한 취소 : 언제든지 권한을 취소할 수 있는 기능
- (2) 데이터 프라이버시

~~~
interface PrivacyControl {
    // 데이터 접근 제어
    dataAccess: {
        requireConsent: boolean;
        allowedScopes: string[];
        retentionPolicy: string;
    };

    // 데이터 보호
    dataProtection: {
        encryption: boolean;
        anonymization: boolean;
        minimization: boolean;
    };
}
~~~
