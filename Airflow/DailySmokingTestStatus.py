###############################
### 코드작성자 : 이  동  우 ###
### 작 성 일자 : 2023.05.02 ###
### 스케줄반복 : 매      일 ###
###############################
import subprocess
import sys
try:
    import tableauserverclient as TSC
    from fileinput import filename
    import os
    import pendulum
    from slack_sdk import WebClient
    from slack_sdk.errors import SlackApiError
    from airflow import DAG
    from airflow.operators.python import PythonOperator
    from datetime import datetime, timedelta
except ImportError:
    subprocess.check_call([sys.executable,"-m","pip","install",'slack_sdk'])
    subprocess.check_call([sys.executable,"-m","pip","install",'tableauserverclient'])
finally:
    import tableauserverclient as TSC
    from fileinput import filename
    import os
    import pendulum
    from slack_sdk import WebClient
    from slack_sdk.errors import SlackApiError
    from airflow import DAG
    from airflow.operators.python import PythonOperator
    from datetime import datetime,timedelta

# 입력값
login_id      = '' # 로그인 계정
login_pw      = '' # 로그인 비밀번호
token_name    = ''      # Default는 공백
sever_adress  = '' # 서버 주소
view_name     = ''   # 뷰 이름
savefile_name = 'temp.png' # 저장 파일 이름
channel_name  = '황'
path          = ''
loadfile_list = ['temp.png'] # 여러 이미지를 한번에 올릴 수 있으니 리스트형태

slack_token = '' ## da bot

####################################### 고정 코드 #######################################

# 태블로 접근

def tableau_api():
    tableau_auth = TSC.TableauAuth(login_id, login_pw, token_name)
    server = TSC.Server(sever_adress, use_server_version=True)

    # 태블로 이미지 id 추출
    with server.auth.sign_in(tableau_auth):
        for view in TSC.Pager(server.views):
            if view_name in view.name:
                view_id = view.id
                view_data_by_id = server.views.get_by_id(view_id)

    # 태블로 이미지 저장
    with server.auth.sign_in(tableau_auth):
        server.views.populate_image(view_data_by_id)
        with open(f'{path}/{savefile_name}','wb') as f:
            f.write(view_data_by_id.image)

    # 슬랙 접근
    client = WebClient(token=slack_token)

    # 슬랙 파일 업로드
    for value in loadfile_list:
        try:
            response = client.files_upload(
                channels=channel_name, 
                file=f'{path}/{value}',
                filename=f'{value}',
                filetype='png')
            print(response['ok'])

        except SlackApiError as e:
            assert e.response["ok"] is False
            assert e.response["error"]
            print(f"Got an error: {e.response['error']}")
local_tz=pendulum.timezone("Asia/Seoul")            
            
default_args = {
    'owner': 'airdeep'
}            
with DAG(
    dag_id='DailySmokingTestStatus',
    default_args=default_args,
    start_date=datetime(2023,5,11,tzinfo=local_tz),
    schedule='0 9 * * *'
) as dag:
    task=PythonOperator(
        task_id='DailySmoking',
        python_callable=tableau_api)
    
task
