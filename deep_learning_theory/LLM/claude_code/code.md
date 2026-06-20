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
   
    - 
