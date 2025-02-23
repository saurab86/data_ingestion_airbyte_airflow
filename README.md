# Airflow DAG: Trigger Airbyte Sync and Transform Data in Postgres

## Overview

This Airflow DAG triggers an Airbyte sync operation and then performs a SQL transformation in PostgreSQL. The DAG runs daily and ensures data is extracted, loaded, and transformed efficiently.

The Airbyte connection in this DAG has:
- **Data Source**: Google Analytics
- **Destination**: PostgreSQL

This DAG consists of triggering the Airbyte connection (Google Analytics to Postgres), and after that, it triggers a PostgreSQL query for data transformation. However, we can also trigger other tools for transformation, such as AWS Glue jobs using PySpark. This Airflow DAG is just an example of triggering an Airbyte connection.

## Prerequisites

Ensure the following are installed and configured:
- Docker (for containerized deployment) [https://docs.docker.com/engine/install/](https://docs.docker.com/engine/install/)
- Apache Airflow (running in Docker)    [https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)
- Airbyte (running in Docker) [https://docs.airbyte.com/using-airbyte/getting-started/oss-quickstart](https://docs.airbyte.com/using-airbyte/getting-started/oss-quickstart)
- PostgreSQL (running in Docker)        [https://www.docker.com/blog/how-to-use-the-postgres-docker-official-image/](https://www.docker.com/blog/how-to-use-the-postgres-docker-official-image/)
- Python `dotenv` package for managing environment variables

**Note**: All components (Airbyte, Airflow, and PostgreSQL) are installed and running in Docker containers.
**how-to-use-airflow-and-airbyte-together** : [https://airbyte.com/tutorials/how-to-use-airflow-and-airbyte-together](https://airbyte.com/tutorials/how-to-use-airflow-and-airbyte-together)

## DAG Structure
1. **Trigger Airbyte Sync**: Initiates the data sync process via Airbyte.
2. **Transform Data in PostgreSQL**: Executes a SQL query to count the total number of customers in the database.

## Screenshots
**Airbyte Connection**:
![Screenshot from 2025-02-20 00-42-47](https://github.com/user-attachments/assets/6b312c99-9104-4776-a65b-86ce3aa36d37)

**Airflow DAG Graph**:
![Screenshot from 2025-02-23 13-54-56](https://github.com/user-attachments/assets/723b7ada-5436-42cf-bbcf-2bd7a7bd7753)
