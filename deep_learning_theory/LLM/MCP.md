# MCP(Model Context Protocol)
## 1장. MCP 소개
### 1. 정의와 목적
#### MPC란?
- LLM 애플리케이션과 외부 데이터 소스 및 도구들 간의 원활한 통합을 가능하게 하는 개방형 프로토콜
- AI 기반 IDE를 구축하든 채팅 인터페이스를 개선하든, 커스텀 AI 워크플로우를 만들든 관계없이 MCP는 LLM이 필요로 하는 컨텍스트와 연결하기 위한 표준화된 방법을 제공함
#### 핵심 목적
- (1) 컨텍스트 공유 표준화
  - LLM 애플리케이션과 데이터 소스 간의 상호 작용을 위한 표준 프로토콜 제공
  - 구조화된 방식으로 컨텍스트 정보를 전달하고 관리
  - 일관된 인터페이스를 통한 데이터 접근 보장
- (2) 도구와 기능 노출
  - AI 시스템에 로컬 또는 원격 도구들을 안전하게 노출
  - 표준화된 방식으로 기능을 정의하고 호출
  - 도구의 능력을 명확하게 기술하고 제어
- (3) 통합 워크플로우 구축
  - 여러 데이터 소스와 도구를 조합한 워크플로우 생성
  - 재사용 가능한 프롬프트 템플릿 제공
  - 모듈식 구성을 통한 유연한 확장

#### 주요 특징
- (1) JSON-RPC 기반 통신
  - 표준 JSON-RPC 2.0 메시지 포맷 사용
  - 상태 기반 연결 관리
  - 서버와 클라이언트 간 능력 협상
- (2) 보안 중심 설계
  - 사용자 동의와 제어를 최우선으로 고려
  - 데이터 프라이버시 보호
  - 도구 사용에 대한 명시적 승인 필요
- (3) 유연한 확장성
  - 다양한 리소스 타입 지원
  - 커스텀 도구 및 프롬프트 정의 기능
  - 표준화된 방식의 기능 확장

#### 적용 분야
- (1) 개발 도구
  - AI 기반 코드 에디터 및 IDE
  - 코드 분석 및 리뷰 도구
  - 개발 워크플로우 자동화
- (2) 데이터 분석
  - 로컬 데이터베이스 연동
  - 데이터 시각화 및 분석
  - 보안된 데이터 접근 및 처리
- (3) 대화형 인터페이스
  - AI 챗봇 및 어시스턴트
  - 지식 기반 질의응답 시스템
- (4) 맞춤형 워크플로우 자동화

#### 개발 철학
- (1) 개방성
  - 오픈 프로토콜로 제공
  - 커뮤니티 주도 발전
  - 표준화된 확장 방식
- (2) 안전성
  - 사용자 중심의 보안 모델
  - 명시적 권한 관리
  - 데이터 보호 우선
- (3) 실용성
  - 실제 사용 사례 중심 설계
  - 구현 용이성 고려
  - 효율적인 통신 구


### 2. 기본 아키텍처
#### 아키텍처 개요
  - 호스트 애플리케이션, 클라이언트, 서버 간의 표준화된 통신을 위한 프로토콜
  - 구조 : JSON - RPC 기반
    - 안전하고 효율적인 데이터 및 기능 교환을 가능하게 함
   

#### 핵심 컴포넌트

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

#### 통신 프로토콜
##### (1) 메시지 구조
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

##### (2) 통신흐름
- (1) 초기화
  - 능력 협상 (Capability Negotiation)
  - 버전 확인
  - 서버 정보 교환
- (2) 일반 통신
  - 요청/ 응답
  - 알림
  - 에러 처리
- (3) 종료
  - 정상 종료
  - 에러 복구
  - 리소스 정리

#### 기능 컴포넌트
##### (1) 리소스 관리

~~~
interface Resource {
    uri: string;           // 리소스 식별자
    name: string;          // 표시 이름
    description?: string;  // 설명
    mimeType?: string;    // 미디어 타입
}
~~~

##### (2) 프롬프트 시스템
~~~
interface Prompt {
    name: string;          // 프롬프트 이름
    description?: string;  // 설명
    arguments?: PromptArgument[];  // 매개변수
}
~~~

##### (3) 도구 시스템
~~~
interface Tool {
    name: string;          // 도구 이름
    description?: string;  // 설명
    inputSchema: object;   // 입력 스키마
}
~~~

#### 보안 아키텍처
##### (1) 사용자 동의 체계
- 명시적 권한 요청
- 작업별 승인 프로세스
- 권한 범위 제한

##### (2) 데이터 보안
- 로컬 리소스 보호
- 데이터 접근 제어
- 암호화 통신

##### (3) 도구 보안
- 도구 실행 제한
- 리소스 사용 제어
- 오류 격리

#### 확장성 설계
##### (1) 플러그인 구조
- 새로운 서버 타입 추가
- 커스텀 프로토콜 확장
- 기능 모듈화

##### (2) 버전 관리
- 프로토콜 버전 협상
- 하위 호환성 유지
- 점진적 기능 개선

##### (3) 표준화
- 인터페이스 정의
- 메시지 포맷 표준화
- 에러 코드 체계화



### 3. 호스트 클라이언트 서버구조
#### MCP의 3-티어 아키텍처
- 호스트, 클라이언트, 서버로 구성된 3티어 아키텍처를 채택하고 있음
- 각 계층은 명확한 역할과 책임을 가지며 이를 통해 유연하고 확장 가능한 시스템을 구현함

#### (1) 호스트
- MCP 시스템의 최상위 계층
- 사용자와 직접 상호작용하는 애플리케이션

##### 주요 역할
- 사용자 인터페이스 제공
- LLM과의 통합
- 여러 MCP 클라이언트 관리
- 보안 정책 실행

##### 대표적인 호스트 애플리케이션
- (1) Claude Desktop
  - 완전한 MCP 지원
  - 리소스, 프롬프트, 도구 통합
  - 로컬 서버 연결 관리
- (2) Zed Editor
  - 코드 에디터 통합
  - 프롬프트 기반 기능
  - 개발자 중심 인터페이스
- (3) Sourcegraph Cody
  - 코드 인텔리전스 통합
  - OpenCTX를 통한 리소스 지원
  - 확장 가능한 구조

##### 호스트의 책임
~~~
interface HostResponsibilities {
    // 사용자 인터페이스 관리
    userInterface: {
        displayResults: () => void;
        collectUserInput: () => Promise<UserInput>;
        showProgress: () => void;
    };

    // 클라이언트 관리
    clientManagement: {
        initializeClients: () => void;
        manageConnections: () => void;
        handleErrors: () => void;
    };

    // 보안 관리
    security: {
        authenticateUser: () => Promise<boolean>;
        authorizeOperations: () => Promise<boolean>;
        managePermissions: () => void;
    };
}
~~~

#### (2) 클라이언트(Client)
- 클라이언트는 호스트와 서버 사이의 중개자 역할을 수행함

##### 주요 역할
- 서버와의 통신 관리
- 메시지 변환 및 처리
- 연결 상태 관리
- 에러 핸들링

##### 클라이언트 기능
~~~
interface ClientCapabilities {
    // 기본 기능
    roots?: {
        listChanged?: boolean;
    };
    // 샘플링 지원
    sampling?: object;
    // 실험적 기능
    experimental?: {
        [key: string]: object;
    };
}
~~~

- (1) 연결 관리
  - 연결 수립 및 유지
  - 재연결 로직
  - 타임아웃 처리
- (2) 메시지 처리
  - 직렬화/역직렬화
  - 메시지 큐잉
  - 응답 매칭
- (3) 오류 처리
  - 네트워크 오류
  - 프로토콜 오류
  - 비즈니스 로직 오류

#### (3) 서버
- 서버는 실제 기능과 리소스를 제공하는 계층

##### 주요 역할
- 리소스 제공
- 도구 실행
- 프롬프트 처리
- 보안 구현

##### 서버 기능
~~~
interface ServerCapabilities {
    // 로깅 지원
    logging?: object;
    // 프롬프트 지원
    prompts?: {
        listChanged?: boolean;
    };
    // 리소스 지원
    resources?: {
        subscribe?: boolean;
        listChanged?: boolean;
    };
    // 도구 지원
    tools?: {
        listChanged?: boolean;
    };
}
~~~

##### 서버 구현 유형
- (1) 파일 시스템 서버
~~~
   interface FileSystemServer {
       readFile: (path: string) => Promise<string>;
       writeFile: (path: string, content: string) => Promise<void>;
       listDirectory: (path: string) => Promise<string[]>;
   }
~~~

- (2) 데이터베이스 서버
~~~
   interface DatabaseServer {
       query: (sql: string) => Promise<any>;
       connect: () => Promise<void>;
       disconnect: () => Promise<void>;
   }
~~~

- (3) 도구 서버
~~~
   interface ToolServer {
       listTools: () => Promise<Tool[]>;
       executeTool: (name: string, args: any) => Promise<any>;
   }
~~~

##### 통신 흐름
- (1) 초기화 과정

![image](https://github.com/user-attachments/assets/01a63007-6b44-4fc2-a1f7-da225e52182b)

- (2) 작업 실행

![image](https://github.com/user-attachments/assets/f8652feb-0894-4e48-9cb4-21f25688150f)




### 4. 보안 및 신뢰 모델
- MCP는 강력한 기능을 제공하는 만큼, 보안과 신뢰성이 매우 중요

##### 핵심 보안 원칙
- (1) 사용자 동의 및 제어
  - 명시적 동의 : 모든 데이터 접근과 작업은 사용자의 명시적 동의 필요
  - 이해 가능한 권한 : 사용자가 이해하기 쉬운 방식으로 권한 설명
  - 세분화된 제어 : 세부적인 수준에서 권한 관리 가능
  - 권한 취소 : 언제든지 권한을 취소할 수 있는 기능
  - 
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

  - 동의 기반 접근 : 사용자 데이터는 명시적 동의 하에서만 접근
  - 최소 권한 : 필요한 최소한의 데이터만 접근
  - 데이터 보호 : 적절한 암호화와 보안 조치 적용
- (3) 도구 안전성
~~~
interface ToolSafety {
    // 실행 제어
    executionControl: {
        sandboxed: boolean;
        resourceLimits: ResourceLimits;
        timeoutSettings: TimeoutConfig;
    };

    // 권한 관리
    permissions: {
        requiredPermissions: string[];
        scopeRestrictions: string[];
        auditLog: boolean;
    };
}
~~~

  - 샌드박스 실행 : 도구는 격리된 환경에서 실행
  - 리소스 제한 : CPU, 메모리 등 리소스 사용 제한
  - 권한 분리 : 최소 권한 원칙에 따른 접근 제어

##### 구현 메커니즘
- (1) 인증 및 권한 부여

![image](https://github.com/user-attachments/assets/fb8be397-90a1-42da-9a99-76c5a3f71e83)

- (2) 데이터 보호 계층

~~~
interface DataProtection {
    // 전송 보안
    transport: {
        encryption: 'TLS' | 'Custom';
        version: string;
        cipherSuite: string[];
    };

    // 저장 보안
    storage: {
        encryption: boolean;
        keyManagement: string;
        secureDelete: boolean;
    };
}
~~~

- (3) 감사 및 모니터링

~~~
interface AuditLog {
    timestamp: string;
    actor: string;
    action: string;
    resource: string;
    result: 'success' | 'failure';
    details: object;
}
~~~

##### 신뢰 모델
- (1) 호스트 신뢰
  - 인증된 호스트 : 신뢰할 수 있는 호스트 애플리케이션
  - 버전 관리 : 호스트 버전 검증
  - 보안 업데이트 : 정기적인 보안 패치

- (2) 서버 신뢰
![image](https://github.com/user-attachments/assets/73ac81d2-8bc0-410d-8c15-a97d7041314c)

  - 서버 검증 : 서버의 신뢰성 확인
  - 능력 협상 : 지원 기능 확인
  - 결과 검증 : 반환된 결과의 유효성 검사
- (3) 데이터 신뢰
  - 무결성 검사 : 데이터 변조 방지
  - 출처 확인 : 데이터 소스 검증
  - 버전 관리 : 데이터 버전 추적

##### 보안 모범 사례
- (1) 구현 가이드라인

~~~
interface SecurityGuidelines {
    // 통신 보안
    communication: {
        useTLS: boolean;
        validateCertificates: boolean;
        useSecureProtocols: boolean;
    };

    // 인증
    authentication: {
        requireAuth: boolean;
        useStrongAuth: boolean;
        sessionManagement: boolean;
    };

    // 로깅
    logging: {
        auditLogging: boolean;
        secureStorage: boolean;
        retentionPolicy: string;
    };
}
~~~

- (2) 보안 체크리스트
  - 통신 보안
  - TLS 1.3 이상 사용
  - 인증서 유효성 검사
  - 안전한 암호화 suite 사용
  - 인증 및 권한
  - 강력한 인증 메커니즘 구현
  - 세션 관리 구현
  - 권한 검증 로직 구현
  - 데이터 보호
  - 민감 데이터 암호화
  - 안전한 키 관리
  - 데이터 백업 및 복구
 
## 2장. MCP 핵심기능
### 1. Resources
#### 리소스 개요
- MCP 핵심 기능 중 하나
- LLM 애플리케이션이 외부 데이터와 컨텍스트에 안전하게 접근하게 접근할 수 있게 해주는 메커니즘

#### 리소스 구조
##### 기본 리소스 정의

~~~
interface Resource {
    // 리소스의 고유 식별자 (URI 형식)
    uri: string;

    // 사용자에게 표시될 이름
    name: string;

    // 리소스에 대한 설명
    description?: string;

    // 리소스의 MIME 타입
    mimeType?: string;
}
~~~

##### 리소스 내용 형식
~~~
interface ResourceContents {
    // 리소스의 URI
    uri: string;

    // MIME 타입
    mimeType?: string;
}

interface TextResourceContents extends ResourceContents {
    // 텍스트 내용
    text: string;
}

interface BlobResourceContents extends ResourceContents {
    // base64로 인코딩된 바이너리 데이터
    blob: string;
}
~~~

#### 리소스 작업
##### (1) 리소스 목록 조회

~~~
interface ListResourcesRequest {
    method: "resources/list";
    params?: {
        cursor?: string;  // 페이지네이션을 위한 커서
    };
}

interface ListResourcesResult {
    resources: Resource[];
    nextCursor?: string;  // 다음 페이지 커서
}
~~~

##### (2) 리소스 읽기

~~~
interface ReadResourceRequest {
    method: "resources/read";
    params: {
        uri: string;  // 읽을 리소스의 URI
    };
}

interface ReadResourceResult {
    contents: (TextResourceContents | BlobResourceContents)[];
}
~~~

##### (3) 리소스 구독
~~~
interface SubscribeRequest {
    method: "resources/subscribe";
    params: {
        uri: string;  // 구독할 리소스의 URI
    };
}

interface ResourceUpdatedNotification {
    method: "notifications/resources/updated";
    params: {
        uri: string;  // 업데이트된 리소스의 URI
    };
}
~~~

#### 리소스 URI 체계
- (1) 기본 URI 구조
  - 스키마 : 리소스 유형 식별
  - 경로 : 리소스의 실제 위치
  - 쿼리 : 선택적 매개변수

~~~
(예시)
file:///path/to/document.txt
db://localhost/table/record
note:///123
~~~

- (2) URI 템플릿

~~~
interface ResourceTemplate {
    // URI 템플릿 (RFC 6570 기준)
    uriTemplate: string;

    // 템플릿 이름
    name: string;

    // 설명
    description?: string;

    // MIME 타입
    mimeType?: string;
}
~~~

#### 리소스 관리 고려사항
- (1) 성능 최적화
  - 페이지네이션 : 대량의 리소스 처리
  - 캐싱 : 자주 접근하는 리소스 캐싱
  - 지연 로딩 : 필요할 때만 데이터 로드
- (2) 오류 처리

~~~
interface ResourceError {
    code: number;      // 오류 코드
    message: string;   // 오류 메시지
    details?: object;  // 추가 정보
}

// 주요 오류 코드
const RESOURCE_NOT_FOUND = 404;
const RESOURCE_ACCESS_DENIED = 403;
const RESOURCE_UNAVAILABLE = 503;
~~~

### 2. Prompts
#### 프롬프트 시스템 개요
- MCP의 핵심기능 중 하나
- LLM 애플리케이션에서 사용할 수 있는 재사용 가능한 메시지 템플릿과 워크플로우를 정의
  - 일관된 형식의 프롬프트를 생성, 컨텍스트를 효과적으로 관리할 수 있음.
