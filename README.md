<h2>Dashboard - MRR</h2>

<h4>Dashboard de exemplo de apresentação de métricas SaaS</h4>

<h3>1. ETL</h3>

<p>Para ETL foi utilizado o package Pandas(1.0.5) do Python (v3.8) e sequências de scripts em SQL. O Data warehouse foi criado utilizando PostgreSQL (v9.6.19). Para conexão com o SGBD foi utilizado SQLAlchemy (v1.3.20) e psycopg2-binary (v2.8.6). Foram ainda utilizados notebooks Jupyter para auxiliar na visualização e na análise exploratória dos dados. Os scripts gerados pode ser encontrados na pasta <strong>etl</strong>.</p>
<p>O Data warehouse foi criado utilizando Star Schema. Foram definidos dois fatos: <strong>MRR</strong> e <strong>Segmento</strong>.
A granularidade da dimensão tempo foi definida por dia, apesar de os gráficos apresentarem dados por mês.</p>

<h3>2. Dashboards</h3>

<p>Para criação do gráficos foi utilizado Plotly (v4.8.1) e para criação da ferramenta Web de visualização utilizado Django (v3.0.7). O framework CSS utilizado foi Bootstrap (v4.3).</p>