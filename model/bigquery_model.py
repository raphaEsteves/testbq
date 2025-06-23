# Configurações da conexão
# Uma boa ideia também é definir a conexão com parâmetros para a tabela
# assim, basta importar o método e utilizá-lo na tabela que desejar.
# O que não deve sofrer alteração, possivelmente, é o PROJECT_ID e o DATABASE_ID
import os
from dotenv import load_dotenv

load_dotenv()


def connection():
	PROJECT_ID = os.environ['PROJECT_ID']
	DATABASE_ID = os.environ['DATABASE_ID']
	TABLE_ID = os.environ['TABLE_ID']
	TABLE_REF = f"{PROJECT_ID}.{DATABASE_ID}.{TABLE_ID}"

	return TABLE_REF
