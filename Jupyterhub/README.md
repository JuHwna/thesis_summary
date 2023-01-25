# 1. 설치 방법
> https://waspro.tistory.com/567
- 해당 방법은 github에 올려져 있는 the-littlelest-jupyterhub을 사용하여 설치한 방법이다.


(1) git repository clone
- git clone https://github.com/jupyterhub/the-littlest-jupyterhub.git

(2) dokcer build
- cd the-littlest-jupyterhub
- docker build -t tljh-systemd . -f integration-tests/Dockerfile

(3) docker run
- docker run --privileged --detach --name=tljh-dev --publish 12000:80 --mount type=bind,source=$(pwd),target=/srv/src tljh-systemd

|코드|설명|
|----|---|
|privileged|host compute의 kernel 환경을 사용할 수 있으며, Docker Container 내부에서 systemctl 또는 도커 컨테이너를 기동할 수 있도록 하는 옵션|
|--detach or -d|컨테이너를 백그라운드로 기동하기 위한 옵션|
|name|컨테이너의 이름 정하는 옵션|
|--publish or -p|컨테이너 내부와 통신하기 위한 port 지정(EX) 12000:80 : 앞쪽은 외부에서 접속할 때 사용하는 port, 뒤쪽은 내부에서 접속할 때 사용하는 port |
|--mount|compute node의 파티션을 컨테이너 내부에서 공유하기 위한 옵션|

(4) jupyterhub run
- 설치한 도커 접속 : docker exec -it tljh-dev /bin/bash
- 해당 코드로 설치 : python3 /srv/src/bootstrap/bootstrap.py --admin admin
  - 파일이 없다고 뜰 수 있음 -> 이럴 때는 해당 코드로 사용하여 설치 : python3 /srv/src/the-littlest-jupyterhub/bootstrap/bootstrap.py --admin admin


(5) jupyterhub connect
- 정상적으로 설치되면 맨 끝에 Done! 메시지가 출력된다. 이제부터 jupyterhub를 쓸 수 있다.
  - jupyterhub에 들어가기 위해서는 내부와 외부 접속 방법이 존재한다.
    - 내부는 http://localhost:(설정한 내부포트)를 jupyterhub 도커 내에 입력하면 들어갈 수 있다.
    - 외부는 http://(도커 설치한 컴퓨터의 ip):(설정한 외부포트)를 인터넷 창에 입력하면 들어갈 수 있다.
- 창이 뜨면 sigin in이 존재하는데 당황하지 말고 Username에 admin을 입력한다. 비밀번호는 이 창에서 설정하면 된다. 7자리 이상으로 비밀번호를 구성해야 하며 비밀번호를 입력해서 sign in을 하게 되면 해당 비밀번호가 admin 계정의 비밀번호가 되므로 잘 정해야 한다.


(6) 기타 외
- Jupyterhub를 docker로 설치 시 cpu는 너프되지 않지만 메모리나 cpu를 사용하는 다른 외적인 부분이 너프를 당한다(최소 4% 최대 40%)
  - 이 때문에 cpu가 안 좋을 경우, 로컬 환경에서 사용하는 것보다 안 좋을 수도 있다
- Jupyterhub를 이 방법이 아닌 image로 설치할 시, admin 계정이어도 아이디를 생성할 수 있는 메뉴가 안 생긴다. 따로 설정을 통해 해당 메뉴와 권한을 넣어주어야 가능하다.
- Jupyterhub 도커 버전에서 mlflow 등 다른 것들을 사용하기 위해선 미리 포트를 뚫어놓는 편이 좋다.
  - 예를 들어 mlflow의 경우, 내부 포트가 8000인데 그대로 놔두었다간 내부 포트로만 접속 가능하며 아예 접속이 불가능한 경우도 존재한다.
  - 따라서 외부 내부 포트 둘다 미리 뚫어서 사용하기 유용하게 만들어 놓자
    - ex) docker run --privileged --detach --name=tljh-dev --publish 16000:8000 --publish 12000:80 --mount type=bind,source=$(pwd),target=/srv/src tljh-systemd

