# 💰 Relatório de Receita por Cliente

> Script que cruza dados de identificação de cliente, histórico de pagamentos e endereço de cobrança, combinando três tabelas relacionadas em uma única consulta — simulando um relatório financeiro real que integra diferentes domínios de dados.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-7FB069?style=flat-square)
![Licença](https://img.shields.io/badge/Licença-MIT-4A5550?style=flat-square)

---

## 📖 Sobre o projeto

Este projeto simula uma demanda comum de times financeiros: consolidar, em um único relatório, informações que vivem em **tabelas diferentes** do banco de dados — neste caso, dados cadastrais do cliente, histórico de pagamentos e endereço de cobrança.

É o primeiro projeto deste repositório a utilizar `JOIN` combinando **três tabelas simultaneamente**, refletindo um cenário realista onde uma única consulta de negócio raramente se resolve com dados de uma tabela isolada.

---

## 🧠 Conceitos aplicados

| Conceito | Onde aparece no projeto |
|---|---|
| **`JOIN` com múltiplas tabelas** | Combinação de `customer`, `payment` e `address` em uma única consulta |
| **Alias de tabela** | Uso de `cus`, `pay` e `adr` para tornar a consulta mais legível |
| **Filtro pós-junção (`WHERE`)** | Restrição aos pagamentos acima de um valor de referência, aplicada sobre o resultado já combinado |
| **Parâmetro seguro via `%s`** | O valor de corte é passado como parâmetro, não concatenado na string |
| **Desempacotamento de tupla com quatro valores** | `for first_name, last_name, amount, address in reports:` |
| **Acumulador e geração de relatório** | Contagem de registros processados, com escrita em arquivo via `with` |

---

## 🏗️ Fluxo do processamento

```
┌────────────┐     ┌────────────┐     ┌────────────┐
│  customer    │ ──▶ │  payment     │     │  address     │
└─────┬──────┘     └─────┬──────┘     └─────┬──────┘
      │   customer_id = customer_id   │
      │                                │
      └────────────┬───────────────────┘
                    │ customer_id = address_id
                    ▼
         ┌──────────────────────┐
         │  Resultado combinado    │
         │  (nome, valor, endereço) │
         └──────────┬─────────────┘
                    │ WHERE amount > 7
                    ▼
         ┌──────────────────────┐
         │relatorio_receita        │
         │  _clientes.txt           │
         └────────────────────────┘
```

---

## 💻 Exemplo de uso

```python
command_sql = """
    SELECT cus.first_name, cus.last_name, pay.amount, adr.address
    FROM customer cus
    JOIN payment pay ON cus.customer_id = pay.customer_id
    JOIN address adr ON cus.address_id = adr.address_id
    WHERE amount > %s
"""
values = (7,)
cursor.execute(command_sql, values)

# Saída em relatorio_receita_clientes.txt:
# Maria Santos R$ 8.99 - 1913 Hanoi Way
# Joao Pereira R$ 9.99 - 1121 Loja Way
#
# 287 customers registered
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

- [ ] Calcular a receita total acumulada por cliente, em vez de listar pagamento por pagamento
- [ ] Agrupar o relatório por cidade, utilizando a tabela `city`
- [ ] Permitir que o valor de corte seja informado pelo usuário via `input()`

---

## 👤 Autor

Projeto desenvolvido como parte de estudos pessoais em **SQL, Python e Engenharia de Dados**.