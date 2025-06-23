#   $env:GOOGLE_APPLICATION_CREDENTIALS="D:\nc-key.json"
#   Write-Host "✅ Variável de ambiente configurada com sucesso!"

#   python.exe D:\Coisas\Projetos\Python\BigQuery\Nightcrows\test.py


from google.cloud import bigquery

client = bigquery.Client()
print("✅ Autenticação bem-sucedida com o projeto:", client.project)


