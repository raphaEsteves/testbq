import json

from controller.pioneer_badge_controller import (
	insert_item,
	list_all,
)

if __name__ == "__main__":

# 	INSERT
#   Função para inserir dados na tabela.
#   insert_item()_item(
#       'Bau de Seleção de Pergaminho Secreto Raro (Vinculado)',
#       5000,
#       "0"
#   )

# 	SELECT
  list_all() #Função que retorna o conteúdo da tabela

  rows = [dict(row) for row in list_all()]    # Transforma o conteúdo para um dicionário antes de converter pra JSON
  json_data = json.dumps(rows, ensure_ascii=False, indent=2)    #Converte para JSON

  print(json_data)
