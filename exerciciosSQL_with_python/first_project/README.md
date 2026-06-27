# 🎭 Listagem de Atores — Primeira Integração Python + SQL

> Script introdutório que estabelece a conexão entre Python e um banco de dados MySQL, executando a primeira consulta e percorrendo os resultados — o ponto de partida da integração entre as duas tecnologias.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-7FB069?style=flat-square)
![Licença](https://img.shields.io/badge/Licença-MIT-4A5550?style=flat-square)

---

## 📖 Sobre o projeto

Este é o primeiro script de integração entre Python e SQL deste repositório. O objetivo é simples e fundamental: estabelecer uma **conexão real** com um banco de dados MySQL, executar uma consulta `SELECT` e processar o retorno utilizando uma estrutura básica de repetição.

Apesar da simplicidade, este projeto representa a base de tudo que vem a seguir — sem essa conexão funcionando corretamente, nenhuma automação ou relatório mais complexo seria possível.

---

## 🧠 Conceitos aplicados

| Conceito | Onde aparece no projeto |
|---|---|
| **Conexão com banco de dados** | `mysql.connector.connect()`, estabelecendo a sessão com o MySQL |
| **Cursor** | `conexao.cursor()`, intermediário utilizado para executar comandos SQL |
| **Execução de consulta** | `cursor.execute()`, rodando um `SELECT` simples |
| **Recuperação de resultados** | `cursor.fetchall()`, trazendo todas as linhas retornadas como lista de tuplas |
| **Laço de repetição** | `for actor in actors:`, percorrendo cada registro retornado |
| **Encerramento de conexão** | `conexao.close()`, liberando o recurso ao final da execução |

---

## 💻 Exemplo de uso

```python
cursor.execute("SELECT first_name, last_name FROM actor")
actors = cursor.fetchall()

for actor in actors:
    print(actor)

# Saída:
# ('PENELOPE', 'GUINESS')
# ('NICK', 'WAHLBERG')
# ...
```

---

## ▶️ Como executar

```bash
python main.py
```

**Pré-requisitos:**
- Python 3.10 ou superior
- Biblioteca `mysql-connector-python` (`pip install mysql-connector-python`)
- Servidor MySQL local com o banco de dados de exemplo `sakila` configurado

---

## 🚀 Próximos passos

- [ ] Selecionar colunas adicionais para enriquecer a listagem
- [ ] Aplicar filtros com `WHERE` para refinar os resultados
- [ ] Formatar a saída em arquivo de texto, em vez de apenas exibir no console

---

## 👤 Autor

Projeto desenvolvido como parte de estudos pessoais em **SQL, Python e Engenharia de Dados**.