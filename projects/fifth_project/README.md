# 🔍 Busca de Clientes por Padrão de Nome

> Script interativo que recebe uma letra digitada pelo usuário e busca, de forma segura, todos os clientes cujo nome começa com essa letra, utilizando o operador `LIKE` do SQL combinado com parametrização dinâmica em Python.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-7FB069?style=flat-square)
![Licença](https://img.shields.io/badge/Licença-MIT-4A5550?style=flat-square)

---

## 📖 Sobre o projeto

Este projeto simula uma ferramenta de busca dinâmica, como as utilizadas em campanhas de marketing segmentado ou sistemas de CRM: o usuário informa um critério (uma letra inicial), e o sistema retorna todos os clientes que correspondem a esse padrão.

O diferencial deste projeto em relação aos anteriores é a **entrada dinâmica do usuário** sendo utilizada dentro de uma consulta SQL — o que exige atenção redobrada à forma como o valor é inserido na query, para evitar vulnerabilidades de segurança.

---

## 🧠 Conceitos aplicados

| Conceito | Onde aparece no projeto |
|---|---|
| **Operador `LIKE`** | Busca por padrão de texto (`'letra%'`), capturando nomes que começam com o valor informado |
| **Entrada dinâmica do usuário** | `input()`, capturando o critério de busca em tempo de execução |
| **Parametrização segura** | Construção do padrão de busca (`letra + '%'`) fora da string SQL, evitando concatenação direta — prevenção de SQL Injection |
| **Tupla de um único elemento** | `(valor,)`, sintaxe necessária para passar um único parâmetro ao `cursor.execute()` |
| **Desempacotamento de tupla** | `for first_name, last_name, email in customers:` |
| **Acumulador e geração de relatório** | Contagem de resultados e escrita em arquivo |

---

## ⚠️ Nota sobre segurança

Este projeto demonstra, na prática, por que valores vindos de entrada do usuário **nunca devem ser concatenados diretamente** dentro de uma string SQL. A abordagem correta — utilizada aqui — é montar o padrão de busca separadamente e passá-lo como parâmetro (`%s`), garantindo que o valor seja tratado como dado, e não como parte executável do comando SQL.

---

## 💻 Exemplo de uso

```python
letra = input('Digite uma letra: ')  # exemplo: "m"

command_sql = "SELECT first_name, last_name, email FROM customer WHERE first_name LIKE %s"
values = (letra + '%',)
cursor.execute(command_sql, values)

# Saída em clientes_por_letra.txt:
# Maria Santos - maria.santos@email.com
# Marcos Oliveira - marcos.oliveira@email.com
#
# 12 clientes cadastrados
```

---

## ▶️ Como executar

```bash
python main.py
```

Ao executar, o programa solicitará que você digite uma letra para realizar a busca.

**Pré-requisitos:**
- Python 3.10 ou superior
- Biblioteca `mysql-connector-python`
- Servidor MySQL local com o banco de dados `sakila`

---

## 🚀 Próximos passos

- [ ] Permitir busca por sobrenome além do primeiro nome
- [ ] Validar a entrada do usuário (garantir que seja uma única letra)
- [ ] Tornar a busca case-insensitive de forma explícita, independente da configuração do banco

---

## 👤 Autor

Projeto desenvolvido como parte de estudos pessoais em **SQL, Python e Engenharia de Dados**.