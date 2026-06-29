# 👔 Auditoria de Desempenho de Funcionários

> Script que identifica os pagamentos de maior valor processados em uma locadora, segmentando os resultados por funcionário responsável — simulando uma análise gerencial real de desempenho operacional.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-7FB069?style=flat-square)
![Licença](https://img.shields.io/badge/Licença-MIT-4A5550?style=flat-square)

---

## 📖 Sobre o projeto

Este projeto simula uma demanda gerencial comum: identificar quais transações de maior valor estão sendo processadas, e por **qual funcionário** — informação útil para avaliação de desempenho, distribuição de carga de trabalho ou identificação de quem lida com os clientes de maior ticket médio.

O diferencial deste projeto em relação aos anteriores é a combinação de **filtragem por valor**, **paginação de resultados** e **segmentação por categoria** (funcionário) em múltiplos acumuladores simultâneos — uma estrutura mais próxima de relatórios analíticos reais, que normalmente apresentam tanto o total geral quanto quebras por dimensão.

---

## 🧠 Conceitos aplicados

| Conceito | Onde aparece no projeto |
|---|---|
| **Filtro por valor (`WHERE`)** | Seleção apenas de pagamentos acima de um valor de referência |
| **Ordenação (`ORDER BY ... DESC`)** | Priorização dos pagamentos de maior valor |
| **Paginação (`LIMIT`)** | Restrição aos 15 pagamentos mais relevantes |
| **Múltiplos parâmetros via `%s`** | Dois valores diferentes (limite de valor e quantidade de linhas) passados de forma segura na mesma tupla |
| **Desempacotamento de tupla com três valores** | `for staff_id, customer_id, amount in payments:` |
| **Múltiplos acumuladores simultâneos** | Contagem geral de pagamentos e contagem segmentada por funcionário, processadas no mesmo laço |
| **Lógica condicional (`if/else`)** | Classificação de cada pagamento de acordo com o funcionário responsável |

---

## 💻 Exemplo de uso

```python
command_sql = "SELECT staff_id, customer_id, amount FROM payment WHERE amount > %s ORDER BY amount DESC LIMIT %s"
values = (7, 15)
cursor.execute(command_sql, values)

# Saída em auditoria_funcionarios.txt:
# Funcionário 1 | Cliente 318 | R$ 11.99
# Funcionário 2 | Cliente 197 | R$ 10.99
# ...
#
# Total de Pagamentos: 15
# Total de Pagamentos, pertencentes ao funcionario 1: 8
# Total de Pagamentos, pertencentes ao funcionario 2: 7
```

---

## ▶️ Como executar

```bash
python main.py
```

**Pré-requisitos:**
- Python 3.10 ou superior
- Biblioteca `mysql-connector-python`
- Servidor MySQL local com o banco de dados `sakila`

---

## 🚀 Próximos passos

- [ ] Tornar o valor mínimo e a quantidade de resultados configuráveis via `input()`
- [ ] Calcular o valor médio dos pagamentos por funcionário, além da contagem
- [ ] Incluir o nome do funcionário no relatório (quando `JOIN` for incorporado ao repositório)

---

## 👤 Autor

Projeto desenvolvido como parte de estudos pessoais em **SQL, Python e Engenharia de Dados**.