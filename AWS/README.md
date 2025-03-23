# AWS Glue
## 정의 및 특징
- AWS에서 사용할 수 있는 ETL 서비스
- Script를 Visualizing 하여 설정이 편하고 쉬움
- 다른 AWS 서비스와의 연동성도 뛰어나며 S3, RDS 등 다양한 데이터 소스를 받아 사용이 가능함
- 관리형 서비스로 사용자가 서버나 인프라를 직접 관리할 필요가 없고 Filter 과정이 정형화 되어 있는 편이라고 할 수 있음
- Apache Spark 기반으로 구축되어 있으며 메모리를 사용하여 데이터 처리 작업을 수행

## AWS Glue Studio
- Glue를 쓰는데 AWS Glue Studio가 설치 및 세팅 과정을 전부 정형화 시켜 둠

![image](https://github.com/user-attachments/assets/0932649c-52fe-4a75-9904-765508a3af1e)

- Glue Crawler는 스토리지나 DB를 탐색하면서 데이터의 스키마를 제안
  - 관련 데이터를 메타데이터로 하여 Data Catalog에 기록함

- S3와 DB 생성 -> Crawler 생성(사전에 만들어둔 s3 버킷과 DB를 지정해 줌
  -> 크롤러 생성 후 실행을 하면 S3 버킷 안에 있는 데이터 셋을 크롤링하여 메타데이터를 DB에 적재함

- Glue Studio

![image](https://github.com/user-attachments/assets/2b88a970-4ee3-4eeb-992d-da8f5acc47df)

(1) 각 노드를 사용하여 ETL을 구축
- 각 소스와 타켓이 타겟이 되는 엔드 포인트 지정
- 데이터 변환 및 ETL 작업을 위한 복잡한 코드 작성 없이도 데이터 파이프라인을 구축
(2) 지정한 노드 이름, 엔드포인트 값, 변환 작업 내용 등 기입
(3) ETL Workflow 확인 후 저장 - 실행

* 위에서 작업한 모든 과정은 apache spark script화 되어 기록이 되고 추가로 visual node에서 없는 변환 기능을 코딩으로 작업 가능
