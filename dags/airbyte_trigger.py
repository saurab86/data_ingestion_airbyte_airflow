import os
from dotenv import main
from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator


main.load_dotenv()
AIRBYTE_CONNECTION_ID = os.getenv('AIRBYTE_CONNECTION_ID')

with DAG(dag_id='trigger_airbyte',
        default_args={'owner': 'airflow'},
        schedule='@daily',
        start_date=datetime.today()
   ) as dag:

      trigger_airbyte_sync = AirbyteTriggerSyncOperator(
       task_id='trigger_airbyte',
       airbyte_conn_id='airbyte_default',
       connection_id=AIRBYTE_CONNECTION_ID,
       asynchronous=True
   )
      
      data_transform = SQLExecuteQueryOperator(
        task_id='transform_data_in_postgres',
        conn_id='postgres_default',
        sql='''SELECT count(CustomerID) AS total_customers FROM customers;'''
    )

trigger_airbyte_sync >> data_transform