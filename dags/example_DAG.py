from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

default_args={
    'owner':'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=3),
}

def print_hello():
    print("Hello World Python")

# Instantiate the DAG with an ID and assign to a variable
dag = DAG(dag_id='Example_DAG', 
                default_args=default_args,
                description='Example Test DAG',
                schedule="1 18 * * *",
                start_date=days_ago(1),
                catchup=False,
                tags=['example'],
    )

task = EmptyOperator(task_id="empty_task",
                      dag=dag
)

task_2 = PythonOperator(
    task_id='python_task',
    python_callable = print_hello,
    dag=dag,
)

task_3 = BashOperator(task_id="bash_task",
                      bash_command="echo 'Hello World Bash'",
                      dag=dag
)



task >> task_2 >> task_3
