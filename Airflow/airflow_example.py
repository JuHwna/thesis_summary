#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import os
from datetime import datetime, timedelta


from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.mysql.operators.mysql import MySqlOperator
from airflow.providers.mysql.hooks.mysql import MySqlHook

default_args = {
    'owner': 'hsjoo'
}

now=datetime.now()
yester=now-timedelta(days=1)
yester_ymd=yester.strftime('%Y%m%d')
yester_=yester.strftime('%Y-%m-%d')

three=now-timedelta(days=3)
three_ymd=three.strftime('%Y%m%d')

four=now-timedelta(days=4)
four_ymd=four.strftime('%Y%m%d')
now_ymd=now.strftime('%Y%m%d')

if not os.path.exists('/root/report/'+now_ymd):
    os.makedirs('/root/report/'+now_ymd)

def mysql_hook1(four_ymd,three_ymd,yester_ymd):
    # hook 내용 작성
    if now.weekday()==0:
        hook = MySqlHook.get_hook(conn_id="db_airproxy") # 미리 정의한 mysql connection 적용
        conn = hook.get_conn() # connection 하기
        cursor = conn.cursor() # cursor객체 만들기
        cursor.execute("""SELECT	ROW_NUMBER() OVER(ORDER BY B.CAR_NUMBER, A.TS ASC) AS No
        ,		B.CAR_NUMBER							AS car_num
        ,		concat('SN',NOTE) 								AS device_sn
        ,		B.CAR_MODEL								AS car_name
        ,		DATE(FROM_UNIXTIME(A.TS / 1000)) 		AS check_date
        ,		MIN(FROM_UNIXTIME(A.TS / 1000, '%H:%i:%s' ))	AS start_time
        ,		MAX(FROM_UNIXTIME(A.TS / 1000, '%H:%i:%s' ))	AS end_time
        FROM	td_air_quality A
        LEFT JOIN
                ti_device B
        ON		1=1
        AND		A.DEVICE_ID = B.DEVICE_ID
        WHERE	1=1
        AND		COMPANY_CODE = 'SOCAR'
        AND		DATE(FROM_UNIXTIME(A.TS / 1000)) BETWEEN {0} AND {1} 
        GROUP BY	B.CAR_NUMBER
        ,			DATE(FROM_UNIXTIME(A.TS / 1000))
        ORDER BY No ASC""".format(four_ymd,yester_ymd))
        result = cursor.fetchall()
        df1=pd.DataFrame(result,columns=[i[0] for i in cursor.description])
        df1.to_csv('/root/report/{0}/AirDeep_SOCAR센서점검_작동점검_{0}.csv'.format(now_ymd),
                   index=False,encoding='cp949')
    else:
        hook = MySqlHook.get_hook(conn_id="db_airproxy") # 미리 정의한 mysql connection 적용
        conn = hook.get_conn() # connection 하기
        cursor = conn.cursor() # cursor객체 만들기
        cursor.execute("""SELECT	ROW_NUMBER() OVER(ORDER BY B.CAR_NUMBER, A.TS ASC) AS No
	,		B.CAR_NUMBER							AS car_num
	,		concat('SN',NOTE) 								AS device_sn
	,		B.CAR_MODEL								AS car_name
	,		DATE(FROM_UNIXTIME(A.TS / 1000)) 		AS check_date
	,		MIN(FROM_UNIXTIME(A.TS / 1000, '%H:%i:%s' ))	AS start_time
	,		MAX(FROM_UNIXTIME(A.TS / 1000, '%H:%i:%s' ))	AS end_time
            FROM	td_air_quality A
            LEFT JOIN
                    ti_device B
            ON		1=1
            AND		A.DEVICE_ID = B.DEVICE_ID
            WHERE	1=1
            AND		COMPANY_CODE = 'SOCAR'
            AND		DATE(FROM_UNIXTIME(A.TS / 1000)) BETWEEN {0} AND {1} 
            GROUP BY	B.CAR_NUMBER
            ,			DATE(FROM_UNIXTIME(A.TS / 1000))
            ORDER BY No ASC""".format(three_ymd,yester_ymd))
        result = cursor.fetchall()
        df1=pd.DataFrame(result,columns=[i[0] for i in cursor.description])
        df1.to_csv('/root/report/{0}/AirDeep_SOCAR센서점검_작동점검_{0}.csv'.format(now_ymd),
                   index=False,encoding='cp949')
        
def mysql_hook2(four_ymd,three_ymd,yester_ymd):

 
    if now.weekday()==0:
        hook = MySqlHook.get_hook(conn_id="db_airproxy") # 미리 정의한 mysql connection 적용
        conn = hook.get_conn() # connection 하기
        cursor = conn.cursor() # cursor객체 만들기
        cursor.execute("""
	SELECT	ROW_NUMBER() OVER(ORDER BY B.CAR_NUMBER, A.TS ASC) AS No
	,		B.CAR_NUMBER							AS car_num
	,		concat('SN',NOTE) 								AS device_sn
	,		B.CAR_MODEL								AS car_name
	,		DATE(FROM_UNIXTIME(A.TS / 1000)) 		AS created_date
	,		FROM_UNIXTIME(A.TS / 1000, '%%H:%%i:%%s' )	AS created_at
	,		CASE AQS_RESULT_CODE WHEN 'C110' THEN '01'
								WHEN 'C120' THEN '02' END AS smoking_type
	FROM	td_air_quality A
	LEFT JOIN
			ti_device B
	ON		1=1
	AND		A.DEVICE_ID = B.DEVICE_ID
	WHERE	1=1
	AND		COMPANY_CODE = 'SOCAR'
	AND		A.AQS_RESULT_CODE IN ('C110', 'C120')
	AND		DATE(FROM_UNIXTIME(A.TS / 1000)) BETWEEN {0} AND {1} 
	ORDER BY No ASC
	""".format(four_ymd,yester_ymd))
        result = cursor.fetchall()
        df2=pd.DataFrame(result,columns=[i[0] for i in cursor.description])
        df2['smoking_type']=df2['smoking_type'].replace(['01','02'],['연초','전자담배'])
        df2.to_csv('/root/report/{0}/AirDeep_SOCAR센서점검_흡연탐지이력_{0}.csv'.format(now_ymd),
                   index=False,encoding='cp949')
    else:
        hook = MySqlHook.get_hook(conn_id="db_airproxy") # 미리 정의한 mysql connection 적용
        conn = hook.get_conn() # connection 하기
        cursor = conn.cursor() # cursor객체 만들기
        cursor.execute("""
	SELECT	ROW_NUMBER() OVER(ORDER BY B.CAR_NUMBER, A.TS ASC) AS No
	,		B.CAR_NUMBER							AS car_num
	,		concat('SN',NOTE) 								AS device_sn
	,		B.CAR_MODEL								AS car_name
	,		DATE(FROM_UNIXTIME(A.TS / 1000)) 		AS created_date
	,		FROM_UNIXTIME(A.TS / 1000, '%%H:%%i:%%s' )	AS created_at
	,		CASE AQS_RESULT_CODE WHEN 'C110' THEN '01'
								WHEN 'C120' THEN '02' END AS smoking_type
	FROM	td_air_quality A
	LEFT JOIN
			ti_device B
	ON		1=1
	AND		A.DEVICE_ID = B.DEVICE_ID
	WHERE	1=1
	AND		COMPANY_CODE = 'SOCAR'
	AND		A.AQS_RESULT_CODE IN ('C110', 'C120')
	AND		DATE(FROM_UNIXTIME(A.TS / 1000)) BETWEEN {0} AND {1}
	ORDER BY No ASC
	""".format(three_ymd,yester_ymd))
        result = cursor.fetchall()
        df2=pd.DataFrame(result,columns=[i[0] for i in cursor.description])
        df2['smoking_type']=df2['smoking_type'].replace(['01','02'],['연초','전자담배'])
        df2.to_csv('/root/report/{0}/AirDeep_SOCAR센서점검_흡연탐지이력_{0}.csv'.format(now_ymd),
                   index=False,encoding='cp949')


def mysql_hook3(four_ymd,three_ymd,yester_ymd):
    # hook 내용 작성
    if now.weekday()==0:
        hook = MySqlHook.get_hook(conn_id="db_airproxy") # 미리 정의한 mysql connection 적용
        conn = hook.get_conn() # connection 하기
        cursor = conn.cursor() # cursor객체 만들기
        cursor.execute("""
	SELECT  ROW_NUMBER() OVER(ORDER BY CREATE_TIME ASC) AS No
	,		CAR_NUMBER AS car_num
	,		concat('SN',NOTE) AS device_sn
	,		CAR_MODEL AS car_name
	,		SUBSTR(CREATE_TIME,1,10) AS installation_date	
	FROM	ti_device B
	WHERE	1=1
	AND		COMPANY_CODE = 'SOCAR'
	AND		DATE(SUBSTR(CREATE_TIME,1,10))<={0}
	""".format(yester_ymd))
        result = cursor.fetchall()
        df3=pd.DataFrame(result,columns=[i[0] for i in cursor.description])
        df3.to_csv('/root/report/{0}/AirDeep_SOCAR센서점검_설치정보_{0}.csv'.format(now_ymd),
                   index=False,encoding='cp949')
    else:
        hook = MySqlHook.get_hook(conn_id="db_airproxy") # 미리 정의한 mysql connection 적용
        conn = hook.get_conn() # connection 하기
        cursor = conn.cursor() # cursor객체 만들기
        cursor.execute("""
	SELECT  ROW_NUMBER() OVER(ORDER BY CREATE_TIME ASC) AS No
	,		CAR_NUMBER AS car_num
	,		concat('SN',NOTE) AS device_sn
	,		CAR_MODEL AS car_name
	,		SUBSTR(CREATE_TIME,1,10) AS installation_date	
	FROM	ti_device B
	WHERE	1=1
	AND		COMPANY_CODE = 'SOCAR'
	AND		DATE(SUBSTR(CREATE_TIME,1,10))<={0}
	""".format(yester_ymd))
        result = cursor.fetchall()
        df3=pd.DataFrame(result,columns=[i[0] for i in cursor.description])
        df3.to_csv('/root/report/{0}/AirDeep_SOCAR센서점검_설치정보_{0}.csv'.format(now_ymd),
                   index=False,encoding='cp949')

    
        
with DAG(
    dag_id="socar_report",
    default_args=default_args,
    start_date=datetime(2023,1, 18),
    schedule='* * * * *'
) as dag:
    # 
    task1 = PythonOperator(
        task_id="socar_operation",
        python_callable=mysql_hook1,
        op_args=[four_ymd,three_ymd,yester_ymd] 
    )
    task2 = PythonOperator(
        task_id="socar_smoking",
        python_callable=mysql_hook2,
        op_args=[four_ymd,three_ymd,yester_ymd] 
    )
    task3 = PythonOperator(
        task_id="socar_install",
        python_callable=mysql_hook3,
        op_args=[four_ymd,three_ymd,yester_ymd] 
    )
    
task1 >> task2 >> task3

