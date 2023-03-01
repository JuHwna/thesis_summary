# 설치방법
(1) miniconda 이미지를 다운받아서 설치한다
- docker pull continuumio/miniconda3
- docker run -d -it -p 2222:8888 -p 19000:8080 --name airflow continuumio/miniconda3
- **airflow 이미지가 아닌 miniconda 이미지로 설치한 이유?**
  - airflow 이미지로 설치 시 내외부에서 문제없이 airflow 웹페이지에 접속할 수 있으나 airflow를 돌리기 위해 필요한 파이썬 파일을 만드는데 필요한 권한이라던가 필요한 패키지를 설치할 수가 없다.


(2) miniconda 이미지로 설치한 컨테이너에 접속한다.
- docker exec -it airflow /bin/bash

(3) airflow 공식 문서에 따라 설치한다.
- 설치전 airflow라는 폴더를 만들어서 설치하는 것이 문제 없이 설치된다고 하여 편한 곳에 airflow 폴더를 만들고 설치하면 된다.
  - export AIRFLOW_HOME=~/airflow
  - AIRFLOW_VERSION=2.5.0
  - PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
  - CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
  - pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
- airflow standalone
  - 해당 코드 입력 시 airflow 웹페이지가 실행된다.
  - airflow 웹페이지에 들어가는 방법은 설정해놓은 포트를 통해 들어가면 되며 내부의 경우, 전체적으로 관리할 수 있는 페이지로 들어가지고 외부는 admin이라는 계정이지만 사이트 형태가 다르게 켜진다.

→ 이후 접속 시 docker exec -it airflow airflow standalone치면 web ui 켜짐

# 사용 방법
- DAGs라는 곳에서 배치를 돌릴 수 있는데 해당 부분에 등록하는 방법은 좀 복잡하다.
1. airflow 배치에 사용할 DB를 등록한다. 등록하는 방법은 Admin 메뉴에 Connections을 클릭한다. 
- 클릭하면 예시로 되어 있는 db 정보들이 뜨는데 무시하고 + 버튼을 누른다.

2. 여러 정보들을 입력하는 창이 뜨는데 connection type을 우선적으로 맞추어준다. 드롭박스를 누르면 연결하려는 DB에 맞는 것을 클릭해야 하는데 Oracle, MySQL, JDBC Connection이 초기에는 없어서 설치해줘야 나타난다. 설치하는 방법은 찾아서 잘 설치하면 된다!

### mysql connection 설치
(1) apt-get update
(2) apt-get install libmysqlclient-dev -y
(3) pip install mysqlclinet
(4) pip install **apache-airflow-providers-mysql**


## 참고자료
> https://www.slideshare.net/YoungHeonKim1/airflow-workflow
