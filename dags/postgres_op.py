from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='postgres_trigger_dag',
    default_args=default_args,
    schedule_interval='@once',  # Change to your desired schedule
    start_date=datetime(2025, 2, 22),
    catchup=False,
) as dag:
    # # Create a table
    # create_table = PostgresOperator(
    #     task_id='create_table',
    #     conn_id='postgres_default',  # Replace with your connection ID
    #     sql="""
    #         CREATE TABLE IF NOT EXISTS test_table (
    #             id SERIAL PRIMARY KEY,
    #             name VARCHAR(100),
    #             created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    #         );
    #     """
    # )

    # # Insert data
    # insert_data = PostgresOperator(
    #     task_id='insert_data',
    #     conn_id='postgres_default',
    #     sql="""
    #         INSERT INTO test_table (name)
    #         VALUES ('Test Record');
    #     """
    # )

    # Query data
    query_data = SQLExecuteQueryOperator(
        task_id='query_data',
        conn_id='postgres_default',
        sql='''SELECT * FROM customers;'''
    )

    # Set dependencies
    query_data