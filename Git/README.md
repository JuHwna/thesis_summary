# Git bash
- 계정 로그인
  - 현재 로그인된 계정 확인
    - git config user.name
    - git config user.email
  - 변경하고자 하는 이름과 계정 입력
    - git config --global user.name 이름
    - git config --global user.email 로그인할 이메일
 
 - 원격 저장소 연결
   - git remote add origin <깃허브주소>
     - 원격 저장소 == remote
     - 깃허브 저장 주소 == origin
   - 연결 확인
     - git remote -v
   - 원격 저장소에 파일 올리기
     - git push -u origin master(or main)
       - 지역 저장소의 브랜치를 origin, 원격 저장소의 master 브랜치로 push함
       - -u : 지역 저장소의 브랜치를 원격 저장소의 master 브랜치에 연결하기 위한 것
     - git add .
     - git commit -m "add a"
     - git push
   - 원격 저장소에서 파일 내려받기
     - git pull origin master(or main)


- 브랜치 생성
  - 로컬 브랜치 생성
    - git checkout -b <이름>
  - 원격 저장소 브랜치 생성
    - git push origin <이름>
    - 브랜치 생성하기 전에 원격 저장소에 파일이 존재한다면 pull을 한 뒤에 브랜치를 따야함
    - 
