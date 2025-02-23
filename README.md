# Airflow DAG: Trigger Airbyte Sync and Transform Data in Postgres

## Overview

This Airflow DAG triggers an Airbyte sync operation and then performs a SQL transformation in PostgreSQL. The DAG runs daily and ensures data is extracted, loaded, and transformed efficiently.

The Airbyte connection in this DAG has:
- **Data Source**: Google Analytics
- **Destination**: PostgreSQL

This DAG consists of triggering the Airbyte connection (Google Analytics to Postgres), and after that, it triggers a PostgreSQL query for data transformation. However, we can also trigger other tools for transformation, such as AWS Glue jobs using PySpark. This Airflow DAG is just an example of triggering an Airbyte connection.

## Prerequisites

Ensure the following are installed and configured:
- Docker (for containerized deployment)
- Apache Airflow (running in Docker)
- Airbyte (running in Docker)
- PostgreSQL (running in Docker)
- Python `dotenv` package for managing environment variables

**Note**: All components (Airbyte, Airflow, and PostgreSQL) are installed and running in Docker containers.

## DAG Structure

1. **Trigger Airbyte Sync**: Initiates the data sync process via Airbyte.
2. **Transform Data in PostgreSQL**: Executes a SQL query to count the total number of customers in the database.