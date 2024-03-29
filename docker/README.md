# Docker
## 0. docker 설치
1. 우분투 시스템 패키지 업데이트
- sudo apt-get update

2. 필요한 패키지 설치
- sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common

3. Docker의 공식 GPG키를 추가
- curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

4. Docker의 공식 apt 저장소를 추가
- sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

5. 시스템 패키지 업데이트
- sudo apt-get update

6. Docker 설치
- sudo apt-get install docker-ce docker-ce-cli containerd.io

7. Docker가 설치 확인
- 도커 실행상태 확인 : sudo systemctl status docker
  - failed로 뜬다면 재부팅
- 도커 실행 : sudo docker run hello-world

## 1. docker 기초 코드
- docker 버전 확인
  - docker version
  - 계정에 docker version 다 나오게 하기 : sudo chmod 666 /var/run/docker.sock
- docker 컨테이너 확인
  - docker ps
  - docker ps -a

- docker 이미지 확인
  - docker images

- docker 이미지 다운로드
  - docker pull <설치하고 싶은 거>
  - docker pull <설치하고 싶은 거>:버전

- docker 실행하는데 자주 사용하는 옵션들
  
|옵션|설명|
|---|----|
|-d|detached mode 흔히 말하는 백그라운드 모드|
|-p|호스트와 컨테이너와 포트를 연겨(포워딩)|
|-v|호스트와 컨테이너의 디렉토리를 연겨(마운트)|
|-e|컨테이너 내에서 사용할 환경변수 설정|
|-name|컨테이너 이름 설정|
|-rm|프로세스 종료시 컨테이너 자동 제거|
|-it|-i와 -t를 동시에 사용한 것으로 터미널 입력을 위한 옵션|
|-link|컨테이너 연결[컨테이너명:별칭]|

- docker 컨테이너 생성
  - docker run -it -d --name 이름 정하기, 설치하고 싶은 거
    
- docker 컨테이너 중지
  - docker stop 이름

- docker 컨테이너 재실행
  - docker start 이름

- docker 컨테이너 삭제
  - docker rm 이름
  - 컨테이너 삭제 전에 컨테이너 중지를 해야 함. 안하면 삭제가
  
- docker 컨테이너 접속
  - docker exec -it 이름 /bin/bash
  - 초기 접속 시 업데이트 필요 : apt update -y & apt-get install wget(wget으로 깔기 위해)
    - 계정 생성 : useradd 이름
    - 폴더 생성 : mkdir 위치 생성
    - chown 이름:이름 아까 폴더 생성한 위치 -> 이건 뭔지 확인 필요
    - 생성한 계정으로 들어가기 su - 이름
      - 생성한 계정 들어갔을 때 앞에 위치와 계정 키는 것 : exec bash 
- docker 컨테이너 나가기
  - exit

- docker 아나콘다 설치
  - 리눅스처럼 설치하면 됨 wget써서 다운 받고 sh 써서 

- docker 컨테이너 복제
  - docker commit [복제할 컨테이너 이름] [복제했을 때 생성 되는 이미지] 


- docker vscode 접속 방법
  - vscode 확장 프로그램에서 remote development 설치
  - ssh에 컨테이너 영역이 생겨 서버 연결하면 자동적으로 컨테이너 목록 생성
    - 오른쪽 버튼으로 attach 하면 열림

- docker 컨테이너 내 jupyter notebook 들어가는 방법
  - 평소처럼 jupyter notebook 치면 안 들어가짐
  - jupyter notebook  --ip='*' --port=8888 --allow-root
  
- 로컬에서 docker 컨테이너로 파일 옮기는 법
  - docker ps (옮기려는 로컬 파일 위치) (컨테이터 이름):(컨테이너에서 저장시키고 싶은 위치) 

- docker log 확인
  - docker log [container name]

- docker 작동 여부 확인 방법
  - sudo systemctl status docker

### docker error
- docker ps 입력 시 해당 오류 발생
  - permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/containers/json": dial unix /var/run/docker.sock: connect: permission denied
- 해결 방법 : sudo chmod 666 /var/run/docker.sock

### docker error
- Error response from daemon: Get "https://index.docker.io/v1/search?q=miniconda&n=25": proxyconnect tcp: dial tcp: lookup proxy.example.com: no such host
  - docker image, pull 다 사용 안됨
  - 해결 방법
    ![image](https://user-images.githubusercontent.com/49123169/217153295-41ada63a-25cb-497e-9a59-47bd79147a9e.png)


## 2. jupyterhub 설치
- docker run -p 8000:8000 -d --name jupyterhub jupyterhub/jupyterhub jupyterhub --ip 0.0.0.0 --port 8000
- 이후 jupyterhub에 들어가
  - pip install notebook
  - pip install jupyterlab
