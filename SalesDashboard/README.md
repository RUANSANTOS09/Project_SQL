# Dashboard de Vendas Premium com Python e MySQL

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluido-2E7D32?style=for-the-badge)
![Relatorio](https://img.shields.io/badge/Output-TXT-111827?style=for-the-badge)

Projeto desenvolvido em **Python** para conectar a um banco de dados **MySQL**, consultar clientes premium, ordenar os resultados por valor total de compras e gerar um relatorio em arquivo `.txt`.

A aplicacao consulta uma base de dados local, busca os principais clientes da view ou tabela `clientes_premium`, formata os dados e salva um dashboard simples no arquivo `dashboard_vendas.txt`.

Este projeto foi criado para praticar integracao entre Python e banco de dados, uso de consultas SQL, parametros em query, leitura de registros, formatacao de dados e escrita de arquivos.

<p align="center">
  <img src="assets/preview.svg" alt="Preview do projeto Dashboard de Vendas Premium" width="780">
</p>

---

## Sumario

- [Sobre o Projeto](#sobre-o-projeto)
- [Objetivo](#objetivo)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Como Funciona](#como-funciona)
- [Fluxo da Aplicacao](#fluxo-da-aplicacao)
- [Exemplo de Saida](#exemplo-de-saida)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Como Executar](#como-executar)
- [Seguranca](#seguranca)
- [Conceitos Praticados](#conceitos-praticados)
- [Codigo Principal](#codigo-principal)
- [Possiveis Melhorias](#possiveis-melhorias)
- [Autor](#autor)

---

## Sobre o Projeto

O **Dashboard de Vendas Premium com Python e MySQL** e um script de automacao que gera um relatorio de clientes com maior volume de compras.

O programa se conecta ao banco de dados `sakila`, executa uma consulta SQL na tabela ou view `clientes_premium`, ordena os clientes pelo campo `Total` em ordem decrescente e limita a busca aos 15 maiores resultados.

Depois disso, os dados sao formatados e gravados em um arquivo chamado:

```text
dashboard_vendas.txt
```

Esse arquivo funciona como um relatorio simples, pronto para leitura, compartilhamento ou evolucao futura para outros formatos, como `.csv`, `.xlsx` ou dashboard web.

---

## Objetivo

O objetivo principal deste projeto e praticar uma rotina realista de consulta e exportacao de dados usando Python.

O projeto trabalha com um fluxo muito comum em aplicacoes profissionais:

- Conectar ao banco de dados.
- Executar uma query SQL.
- Buscar registros retornados pela consulta.
- Processar e formatar os dados.
- Gerar um arquivo de relatorio.
- Encerrar a conexao corretamente.

Mesmo sendo um projeto simples, ele representa uma base importante para automacoes de relatorios, dashboards internos e rotinas de analise de dados.

---

## Funcionalidades

O projeto possui as seguintes funcionalidades:

- Conecta a um banco de dados MySQL local.
- Utiliza o banco `sakila`.
- Executa uma query na tabela ou view `clientes_premium`.
- Ordena os clientes pelo campo `Total`.
- Limita o relatorio aos 15 principais clientes.
- Busca os dados com `fetchall()`.
- Calcula o total de clientes retornados.
- Formata nome e sobrenome com `.title()`.
- Gera linhas formatadas com nome completo e total em reais.
- Cria o arquivo `dashboard_vendas.txt`.
- Escreve o relatorio usando codificacao `utf-8`.
- Fecha cursor e conexao ao final da execucao.

---

## Tecnologias Utilizadas

| Tecnologia | Uso no projeto |
| --- | --- |
| Python 3 | Linguagem principal da aplicacao. |
| MySQL | Banco de dados usado para consulta dos clientes. |
| mysql-connector-python | Biblioteca usada para conectar Python ao MySQL. |
| SQL | Consulta, ordenacao e limitacao dos resultados. |
| Arquivo `.txt` | Saida final do relatorio gerado. |

---

## Como Funciona

O funcionamento do projeto pode ser dividido em etapas.

### 1. Conexao com o banco de dados

```python
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="sua_senha",
    database="sakila"
)
```

O script usa `mysql.connector.connect()` para abrir uma conexao com o banco MySQL.

Por seguranca, a senha real nao deve ser versionada no GitHub. O ideal e usar variaveis de ambiente ou um arquivo `.env` ignorado pelo Git.

### 2. Criacao do cursor

```python
cursor = connection.cursor()
```

O cursor e o objeto responsavel por executar comandos SQL e buscar os resultados retornados pelo banco.

### 3. Consulta SQL

```sql
SELECT *
FROM clientes_premium
ORDER BY Total DESC
LIMIT %s
```

A consulta seleciona os registros de `clientes_premium`, ordena pelo campo `Total` em ordem decrescente e limita a quantidade de resultados.

O uso de `%s` permite passar o limite como parametro:

```python
cursor.execute(query_dashboard, (15,))
```

Isso deixa a query mais segura e flexivel do que montar SQL diretamente com concatenacao de strings.

### 4. Busca dos dados

```python
report = cursor.fetchall()
```

O metodo `fetchall()` retorna todos os registros encontrados pela consulta.

Cada linha retornada e tratada no loop principal:

```python
for position, (Id, Name, Sobrenome, Total) in enumerate(report):
    full_name = f'{Name} {Sobrenome}'.title()
```

O codigo usa desempacotamento de tuplas para separar os campos de cada cliente.

### 5. Geracao do relatorio

```python
final_report.append(f'{position}. {full_name} | R${Total:.2f}\n')
```

Cada cliente e formatado com:

- Posicao no ranking.
- Nome completo.
- Total comprado em formato monetario.

Ao final, tambem e adicionada a quantidade total de clientes retornados:

```python
final_report.append(f'\nTotal de clientes: {total_customers}')
```

### 6. Escrita do arquivo

```python
with open('dashboard_vendas.txt', 'w', encoding='utf-8') as f:
    f.writelines(final_report)
```

O relatorio final e salvo em um arquivo `.txt` usando `with open()`, que garante o fechamento correto do arquivo apos a escrita.

---

## Fluxo da Aplicacao

```text
Banco MySQL
    |
    v
Conexao com mysql.connector
    |
    v
Execucao da query SQL
    |
    v
Busca dos clientes premium
    |
    v
Formatacao dos dados
    |
    v
Geracao do dashboard_vendas.txt
```

---

## Exemplo de Saida

O arquivo `dashboard_vendas.txt` tera uma estrutura semelhante a esta:

```text
0. Maria Silva | R$189.50
1. Joao Santos | R$175.20
2. Ana Oliveira | R$160.80
3. Pedro Souza | R$149.90

Total de clientes: 15
```

Observacao: no codigo atual, o ranking comeca em `0` porque `enumerate(report)` foi usado sem `start=1`.

Caso queira iniciar em `1`, basta usar:

```python
enumerate(report, start=1)
```

---

## Estrutura do Projeto

Estrutura recomendada para o repositorio:

```text
dashboard-vendas-mysql/
├── assets/
│   └── preview.svg
├── main.py
├── dashboard_vendas.txt
└── README.md
```

| Arquivo | Descricao |
| --- | --- |
| `main.py` | Arquivo principal com a conexao, consulta e geracao do relatorio. |
| `dashboard_vendas.txt` | Relatorio gerado apos a execucao do script. |
| `README.md` | Documentacao completa do projeto. |
| `assets/preview.svg` | Imagem de preview usada no README. |

---

## Como Executar

### 1. Clone o repositorio

```bash
git clone https://github.com/seu-usuario/dashboard-vendas-mysql.git
```

### 2. Acesse a pasta do projeto

```bash
cd dashboard-vendas-mysql
```

### 3. Crie e ative um ambiente virtual

No Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

No Linux ou macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Instale a dependencia

```bash
pip install mysql-connector-python
```

### 5. Configure o banco de dados

Antes de executar, confirme que:

- O MySQL esta rodando.
- O banco `sakila` existe.
- A tabela ou view `clientes_premium` existe.
- Os campos retornados seguem a estrutura esperada: `Id`, `Name`, `Sobrenome`, `Total`.

### 6. Execute o projeto

```bash
python main.py
```

Ao final, o arquivo `dashboard_vendas.txt` sera criado ou sobrescrito na pasta do projeto.

---

## Seguranca

Este ponto e muito importante para publicar o projeto no GitHub:

```python
passwd="sua_senha"
```

Credenciais reais de banco de dados nunca devem ser enviadas para repositorios publicos.

Uma abordagem mais segura e usar variaveis de ambiente:

```python
import os
import mysql.connector

connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    passwd=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)
```

Tambem e recomendado adicionar arquivos de configuracao local ao `.gitignore`, como:

```text
.env
dashboard_vendas.txt
```

---

## Conceitos Praticados

| Conceito | Aplicacao no projeto |
| --- | --- |
| Importacao de biblioteca | Uso de `import mysql.connector`. |
| Conexao com banco | Abertura de conexao com MySQL. |
| Cursor | Execucao de comandos SQL pelo Python. |
| SQL | Consulta com `SELECT`, `ORDER BY` e `LIMIT`. |
| Parametros em query | Uso de `%s` e tupla `(15,)` no `execute()`. |
| `fetchall()` | Busca de todos os registros retornados. |
| Listas | Armazenamento das linhas do relatorio final. |
| `len()` | Contagem total de clientes retornados. |
| `enumerate()` | Criacao do ranking de clientes. |
| Desempacotamento | Separacao de `Id`, `Name`, `Sobrenome` e `Total`. |
| F-strings | Formatacao das linhas do relatorio. |
| `.title()` | Padronizacao do nome completo. |
| Escrita de arquivos | Criacao de `dashboard_vendas.txt`. |
| Context manager | Uso de `with open()` para lidar com arquivo. |
| Encerramento de recursos | Fechamento de cursor e conexao. |

---

## Codigo Principal

Exemplo seguro do codigo principal, sem credenciais reais:

```python
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="sua_senha",
    database="sakila"
)

cursor = connection.cursor()

query_dashboard = """
SELECT *
FROM clientes_premium
ORDER BY Total DESC
LIMIT %s
"""

cursor.execute(query_dashboard, (15,))
report = cursor.fetchall()

total_customers = len(report)
final_report = []

for position, (Id, Name, Sobrenome, Total) in enumerate(report):
    full_name = f'{Name} {Sobrenome}'.title()
    final_report.append(f'{position}. {full_name} | R${Total:.2f}\n')

final_report.append(f'\nTotal de clientes: {total_customers}')

with open('dashboard_vendas.txt', 'w', encoding='utf-8') as f:
    f.writelines(final_report)

cursor.close()
connection.close()
```

---

## Possiveis Melhorias

Este projeto pode evoluir bastante com algumas melhorias:

- Remover credenciais fixas do codigo e usar variaveis de ambiente.
- Criar um arquivo `.gitignore`.
- Refatorar o script em funcoes como `connect_database()`, `fetch_customers()` e `write_report()`.
- Usar `try`, `except` e `finally` para tratar erros e fechar recursos com seguranca.
- Iniciar o ranking com `enumerate(report, start=1)`.
- Exportar o relatorio em `.csv` ou `.xlsx`.
- Permitir configurar o limite de clientes por input ou argumento de linha de comando.
- Criar logs de execucao.
- Adicionar testes para a formatacao do relatorio.
- Criar uma interface web ou dashboard visual.

---

## Aprendizados

Este projeto mostra como Python pode ser usado para automatizar tarefas de consulta e relatorio a partir de um banco de dados.

Ele tambem reforca a importancia de separar dados, consulta, processamento e saida final, que e uma base essencial para projetos maiores de backend, automacao e analise de dados.

---

## Autor

Desenvolvido por **Ruan**.

Projeto criado como parte dos estudos em Python, banco de dados MySQL e geracao de relatorios automatizados.
