FROM apache/airflow:2.8.0

ENV AIRFLOW_HOME=/opt/airflow

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR $AIRFLOW_HOME