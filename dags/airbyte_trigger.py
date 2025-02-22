import os
from dotenv import main
from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator
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

trigger_airbyte_sync