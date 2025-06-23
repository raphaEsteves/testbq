from model.bigquery_model import connection
from google.cloud import bigquery
import uuid

client = bigquery.Client()
pioneer_item_id = uuid.uuid4()

# Função para INSERT
def insert_item(pioneer_item_name, pioneer_item_cost, pioneer_item_pre_requisits):
    rows = [{
        'pioneer_item_id': str(pioneer_item_id),
        'pioneer_item_name': pioneer_item_name,
        'pioneer_item_cost': pioneer_item_cost,
        'pioneer_item_pre_requisits': pioneer_item_pre_requisits
    }]
    errors = client.insert_rows_json(connection(), rows)
    if not errors:
        print(f"O item {pioneer_item_name}, com valor de {pioneer_item_cost} foi inserido com sucesso.")
    else:
        print(f"Erro ao inserir o item", errors)

def list_all():
    query = f"SELECT * FROM `{connection()}`"
    query_job = client.query(query)

    # for row in query_job:
    #     print(dict(row))

    results = query_job.result()

    return results



