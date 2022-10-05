from datetime import datetime

from airflow import DAG
from airflow.operators.dummy import DummyOperator

with DAG(
        dag_id='dummy-dag-2',
        start_date=datetime(2022, 10, 5),
        schedule_interval=None,
) as dag:
    DummyOperator(task_id='one') >> [DummyOperator(task_id='two'), DummyOperator(task_id='three')] >> DummyOperator(task_id='four')
