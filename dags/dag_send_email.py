from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.email_operator import EmailOperator
from datetime import datetime
from random import randint

def _training_model():
    return randint(1,10)

with DAG("dag_send_email", start_date=datetime(2022,1,1), 
        schedule_interval="@daily", catchup=False) as dag:

        training_model_A = PythonOperator(
            task_id="training_model_A",
            python_callable=_training_model
        )

        email = EmailOperator(
            task_id='send_email',
            to='yourmail@whatever.com', 
            subject='Airflow Alert',
            html_content=""" <h3> Email Test Airflow </h3>""",
            dag=dag
        )

        training_model_A >> email



