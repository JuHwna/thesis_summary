# window 환경에서 claude code 설치
~~~
# Windows PowerShell
irm https://claude.ai/install.ps1 | iex
~~~

- 이후에 껐다가 다시 켜서 claude를 통해 실행
- 그래도 안되면
  - [Environment]::SetEnvironmentVariable("PATH", "$env:PATH;$env:USERPROFILE\.local\bin", [EnvironmentVariableTarget]::User) 붙여넣은 후에 다시 껐다가 키기

- 연습용 폴더를 만들고 실행 진행

## 세션 이어하기
### 1. 마지막 대화 이어하기
- /exit으로 세션을 종료한 뒤, -c 플래그로 다시 시작함
  - claude -c
  - 직전 대화가 그대로 이어감

### 2. 현재 세션에 이름 붙이기
- 대화 중에 /rename으로 이름을 붙여둠
  - /rename 버그수정

### 3. 이름으로 세션 재개하기
- 종료 후, 이름으로 바로 재개할 수 있음
  - claude -r "버그수정"
 
#### 이전 세션 목록을 보고 싶으면 대화 중에 /resume을 입력

## 파일 참조(@)
- 대화 중에 특정 파일을 언급하려면 @를 입력함
  - @src/main.js 이 파일의 구조를 설명해줘
  - @를 입력하면 자동완성으로 파일 목록이 나타남
    - 경로를 일일이 외울 필요 없이 선택하면 됨
   
## 슬래시 명령어
|명령어|역할|
|-----|-----|
|/help|도움말|
|/exit|세션종료|
|/model|모델변경|
|/voice|음성입력모드|
|/resume|이전 세션 목록에서 선택하여 재개|
|/rename|현재 세션에 이름 붙이기|
|/clear|대화 이력 초기화|
|/compact|대화를 핵심만 남기고 압축|

## 여러 줄 입력
- 긴 지시를 할 때 줄바꿈
  - 모든 터미널 : \+enter

## 되돌리기(체크포인트)
- claude가 파일을 수정할 때마다 자동으로 체크포인트를 만듦
- 결과가 마음에 들지 않으면 Esc를 두 번 누르면 됨
  - Esc Esc
  - /rewind를 입력해도 같은 메뉴가 나타
- 되감기 메뉴가 나타나면 화살표 키로 되돌릴 시점을 선택함, 선택 후 복원 옵션이 표시됨
  - Restore code and conversation - 코드와 대화를 모두 해당 시점으로 되돌림
  - Restore code - 파일만 되돌리고 대화 맥락은 유지 (가장 자주 사용)
  - Restore conversation - 대화만 되돌리고 파일은 그대로
  - Summarize from here - 해당 시점부터 대화를 요약으로 압축
  - Never mind - 취소
 
## 모델 선택
- /model을 입력하면 사용 가능한 모델 목록이 나타남

|모델|특징|
|Opus 4.8 (1M context)|가장 강력. 복잡한 작업에 적합 (기본값, 권장)|
|Sonnet 4.6|일상적인 작업에 균형 잡힌 선택|
|Sonnet 4.6 (1M context)|Sonnet에 확장 컨텍스트. 모든 구독 플랜(Max 포함)에서 usage credits 필요. 200K 토큰 초과분에도 프리미엄 없이 표준 모델 요금 적용
|Haiku 4.5|가장 빠름. 간단한 질문에 적합|

- /fast를 입력하면 Fast mode를 켤 수 있음
  - Opus 모델이 더 빠른 출력 속도(최대 2.5배)로 동작하며, 토큰당 비용이 높아짐
  - 즉, 토큰이 빠르게 소진됨
 

## Effort 레벨
|레벨|적합한 작업|사고 깊이|
|low|간단한 질문, 오타 수정, 파일 이름 변경|얕고 빠름|
|medium|일반적인 코드 작성, 문서 정리|균형|
|high|복잡한 버그 분석, 아키텍처 설계, 여러 파일 리팩토링 (Opus 4.8/Opus 4.6/Sonnet 4.6 기본값)|깊고 느림|
|xhigh|요구 난이도 높은 코딩/에이전트 작업 (Opus 4.8/4.7에서 지원, Opus 4.7 기본값)|매우 깊음|
|max|가장 깊은 사고, 토큰 제한 없음 (현재 세션만 적용)|최대|

- 설정 방법
  - /effort [low|medium|high|xhigh|max|auto]
  - /model을 열면 모델 선택과 함께 하단에 effort 슬라이더가 나타남 => 방향키로 조절하고 enter로 확인함
 
## ultrathink
- 한 번만 더 깊이 생각하게 하고 싶을 때는 메시지에 ultrathink를 포함함
  - 문장 앞, 뒤, 중간 어디에 있어도 됨
  - 세션 effort 설정이 바뀌거나 API로 전송되는 effort 수준이 변경되는 것은 아님
  - claude code가 이 키워드를 인식해 그 턴에 더 깊이 추론하라는 in-context 지시를 추가함
- "think", "think hard", "think more" 같은 문구는 키워드로 인식되지 않고 일반 프롬프트 텍스트로 처리됨
- ex ) ultrathink 이 인증 로직에서 race condition이 발생할 수 있는 경로를 모두 분석해줘

## 권한 모드
|모드|CLI 플래그|설명|
|Plan|plan|코드 수정 불가, 분석과 계획만 수행|
|Default|default|파일 읽기는 자동, 수정/명령 실행은 승인 필요 (기본값)|
|Auto-accept Edits|acceptEdits|파일 수정은 자동 허용, 명령 실행은 승인 필요|
|Auto|auto|분류기가 백그라운드에서 안전 검사. 프롬프트 피로 없이 작업 (리서치 프리뷰, 모든 플랜 사용 가능. Opus 4.6 이상 또는 Sonnet 4.6. Anthropic API 전용 - Bedrock/Vertex/Foundry 불가)|
|Don't Ask|dontAs|/permissions이나 설정 파일에서 사전 승인된 것만 허용, 나머지는 자동 거부|
|Bypass Permissions|bypassPermissions|모든 작업을 자동 실행 (위험)|

~~~
# Default 모드로 시작 (기본)
claude

# 특정 모드로 시작
claude --permission-mode plan
~~~

- 어떤 모드로 시작하든, 대화 중에 Shift+Tab으로 언제든 모드를 전환할 수 있음

## 모드 전환
- CLI : Shift + Tab으로 일상적으로 쓰는 3개 모드가 순환함
  - Normal(Default) → Plan → Auto-accept 순서로 전환
  - 현재 모드는 입력창 옆에 표시됨
    - Default: 아무 표시 없음
    - Plan: plan mode on
    - Auto-accept Edits: accept edits on
    - Bypass Permissions: bypass permissions on
  - 나머지 2개는 CLI 플래그나 설정 파일로 지정함
    - claude --permission-mode dontAsk
    - claude --permission-mode bypassPermissions

## 권한 규칙 설정(/permissions)
- 매번 같은 명령에 허용을 누르는 것이 번거롭다면 /permissions로 규칙을 미리 설정할 수 있음

|탭|역할|
|Allow|허용된 도구는 승인 없이 자동 실행|
|Ask|이 도구를 쓸 때마다 항상 확인 요청|
|Deny|거부된 도구는 항상 차단|
|Workspace|Claude가 접근할 수 있는 작업 디렉토리 관리|

- 규칙은 도구명 또는 도구명(상세지정) 형식으로 작성함

|규칙 예시|의미|
