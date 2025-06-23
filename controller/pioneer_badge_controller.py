import json

from model.bigquery_model import connection
from google.cloud import bigquery
import uuid

client = bigquery.Client()
pioneer_item_id = uuid.uuid4()

# Função para INSERT
def insert_item(pioneer_item_json):

    if isinstance(pioneer_item_json, dict):
        pioneer_item_json = [pioneer_item_json]

    for item in pioneer_item_json:
        item['pioneer_item_id'] = str(uuid.uuid4())

    errors = client.insert_rows_json(connection(), pioneer_item_json)

    if not errors:
        print(f"Dado(s) inserido(s) com sucesso.")
    else:
        print(f"Erro ao inserir o item", errors)

def list_all():
    query = f"SELECT * FROM `{connection()}`"
    query_job = client.query(query)

    results = query_job.result()

    rows = [dict(row) for row in results]
    json_data = json.dumps(rows, ensure_ascii=False,indent=2)

    return json_data

def select_by_id(id):
    query = f"SELECT * FROM {connection()} WHERE pioneer_item_id=@id"

    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter("id", "STRING", id)
        ]
    )
    query_job = client.query(query, job_config=job_config)

    results = query_job.result()

    rows = [dict(row) for row in results]
    json_data = json.dumps(rows, ensure_ascii=False,indent=2)

    return json_data
