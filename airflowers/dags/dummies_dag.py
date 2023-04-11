from datetime import timedelta, datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'lorem',
    'start_date': datetime(2022, 3, 4),
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}

dummies_dag = DAG('dummies_dag',
                  default_args=default_args,
                  description='Dummies DAG',
                  schedule='* * * * *',
                  catchup=False,
                  tags=['example, dummies'])


def dummies_func():
    return 'This is dummy'


# Creating first task
start_task = EmptyOperator(task_id='start_task', dag=dummies_dag)

# Creating second task
dummies_task = PythonOperator(task_id='dummies_task', python_callable=dummies_func, dag=dummies_dag)

# Creating third task
end_task = EmptyOperator(task_id='end_task', dag=dummies_dag)

start_task >> dummies_task >> end_task
