from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

## Define the task1
def preprocess_data():
    print('Data preprocessing step')

## Define the task2
def train_model():
    print('Model training step')

## Define the task3
def evaluate_model():
    print('Model evaluation step')

## Define the DAG

with DAG(
    'ml_pipeline', ## DAG name
    start_date = datetime(2025,1,1), ## DAG start date
    schedule_interval = '@daily', ## DAG schedule interval

)as dag:
    
    ## Define the task1
    preprocess_data = PythonOperator(
        task_id = 'preprocess_data',
        python_callable = preprocess_data
    )

    ## Define the task2
    train_model = PythonOperator(
        task_id = 'train_model',
        python_callable = train_model
    )

    ## Define the task3
    evaluate_model = PythonOperator(
        task_id = 'evaluate_model',
        python_callable = evaluate_model
    )

    ## Define the task sequence
    preprocess_data >> train_model >> evaluate_model

