from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2015, 6, 1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('skype_bot_2', default_args=default_args, schedule_interval=timedelta(days=1))

t1 = BashOperator(
    task_id='run_test',
    bash_command='python ~/skype_bot_message_processing/hivebatch.py',
    dag=dag)
