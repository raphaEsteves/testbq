<H1> Utilizar Acesso ao BigQuery. </H1>
<hr>

<H3> Instalar as bibliotecas necessárias: </H3>

<code>pip install google-cloud-bigquery</code>

<H3> Permissão para acessar o BigQuery </H3>
<ol>
    <li> Criar uma conta de Serviço </li>
    <li> Gerar Chave JSON </li>
    <li> Definir variável de ambiente no sistema </li>
</ol>

<H5> Criando conta de Serviço: </H5>
<ol> 
    <li> Criar uma conta de serviço</li> 
    <li> Acesse o console do Google Cloud. </li>
    <li> Selecione ou crie um projeto. </li>
    <li> Vá para <b>IAM e administrador > Contas de serviço.</b> </li>
    <li> Clique em <b> "Criar conta de serviço" </b>. </li>
    <li> Dê um nome (ex: python-bigquery). </li>
    <li> Clique em Criar e continuar.</li>
    <li> Dê à conta o papel: BigQuery Admin (ou outro mais restritivo se desejar). </li>
    <li> Clique em Concluir.</li>
</ol>

<H5> Gerar chave JSON </H5>
<ol>
    <li> Na lista de <b> contas de serviço</b>, clique na que foi criada  </li>
    <li> Vá até a aba <b> Chaves </b></li>
    <li> Clique em <b> Adicionar Chave > Criar nova </b></li>
    <li> Selecione <b> JSON </b></li>
    <li> O arquivo será baixado, guarde-o com segurança. </li>
</ol>

<H5> Definindo Variável de ambiente no Windows </H5>
<ul> 
    <li> No CMD</li><code>set GOOGLE_APPLICATION_CREDENTIALS=C:\caminho\para\chave-bigquery.json</code>
    <li> No PowerShell</li><code>$env:GOOGLE_APPLICATION_CREDENTIALS="C:\caminho\para\chave-bigquery.json"</code>
</ul>

 <h4>Após realizar esses passos, pode usar o seguinte código para testar a conexão: </h4> 
<pre><code>from google.cloud import bigquery

client = bigquery.Client()
print("✅ Autenticação bem-sucedida com o projeto:", client.project)
</code></pre>
