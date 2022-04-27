# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator, BranchPythonOperator

from datetime import datetime, timedelta
from random import randint

# [END import_module]


# Functions to execute:
def _trainig_model():
    return randint(1, 10)


def _choose_best_model(ti):
    accuracies = ti.xcom_pull(task_ids=[
        'training_model_A',
        'training_model_B',
        'training_model_C',
    ])
    best_accuracy = max(accuracies)
    if(best_accuracy > 8):
        return 'accurate'
    return 'inaccurate'


# [START instantiate_dag]
with DAG(
    'my_first_dag',
    # [START default_args]
    # These args will get passed on to each operator
    # You can override them on a per-task basis during operator initialization
    default_args={
        'depends_on_past': False,
        'email': ['airflow@example.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
        # 'queue': 'bash_queue',
        # 'pool': 'backfill',
        # 'priority_weight': 10,
        # 'end_date': datetime(2016, 1, 1),
        # 'wait_for_downstream': False,
        # 'sla': timedelta(hours=2),
        # 'execution_timeout': timedelta(seconds=300),
        # 'on_failure_callback': some_function,
        # 'on_success_callback': some_other_function,
        # 'on_retry_callback': another_function,
        # 'sla_miss_callback': yet_another_function,
        # 'trigger_rule': 'all_success'
    },
    # [END default_args]
    description='A simple tutorial DAG',
    schedule_interval=timedelta(minutes=60),
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=['Roberto'] ) as dag:


    training_model_A = PythonOperator(
        task_id="training_model_A",
        python_callable=_trainig_model
    )

    training_model_B = PythonOperator(
        task_id="training_model_B",
        python_callable=_trainig_model
    )

    training_model_C = PythonOperator(
        task_id="training_model_C",
        python_callable=_trainig_model
    )

    choose_best_model = BranchPythonOperator(
        task_id="choose_best_model",
        python_callable=_choose_best_model
    )

    accurate = BashOperator(
        task_id="accurate",
        bash_command="echo 'accurate'"
    )

    inaccurate = BashOperator(
        task_id="inaccurate",
        bash_command="echo 'inaccurate'"
    )
    
    [training_model_A, training_model_B, training_model_C] >> choose_best_model >> [accurate, inaccurate]

