# 🧾 Auditoria de Endereços Incompletos

> Script de auditoria que identifica registros de endereço com campo de complemento ausente, utilizando o operador `IS NULL` do SQL — uma tarefa comum em rotinas de verificação de qualidade de dados.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-7FB069?style=flat-square)
![Licença](https://img.shields.io/badge/Licença-MIT-4A5550?style=flat-square)

---

## 📖 Sobre o projeto

Este projeto simula uma rotina de **auditoria de qualidade de dados** — uma tarefa recorrente em equipes de dados, onde é necessário identificar registros incompletos ou inconsistentes antes que eles sigam para etapas seguintes de um pipeline.

Neste caso específico, o objetivo é localizar endereços cujo campo de complemento (`address2`) não foi preenchido, retornando, ainda assim, as informações úteis do endereço principal para referência.

---

## 🧠 Conceitos aplicados

| Conceito | Onde aparece no projeto |
|---|---|
| **Operador `IS NULL`** | Identificação de registros com campo vazio/nulo no banco de dados |
| **Seleção de múltiplas colunas com propósito** | Inclusão de `address` na consulta, mesmo filtrando por `address2`, para manter o relatório informativo |
| **Desempacotamento de tupla com três valores** | `for address_id, address, address2 in addresses:` |
| **Acumulador** | Contagem total de registros incompletos identificados |
| **Gerenciamento de contexto (`with`)** | Escrita do relatório de auditoria em arquivo |

---

## 💡 Decisão de design

Embora o filtro da consulta seja baseado na ausência de `address2`, o relatório final exibe o campo `address` (endereço principal), e não o campo nulo que originou o filtro. Essa escolha é intencional: um relatório de auditoria precisa ser **acionável** — de nada serve indicar que um campo está vazio sem fornecer contexto suficiente para localizar e corrigir o registro.

---

## 💻 Exemplo de uso

```python
command_sql = "SELECT address_id, address, address2 FROM address WHERE address2 IS NULL"
cursor.execute(command_sql)

# Saída em enderecos_incompletos.txt:
# ID 5: 1913 Hanoi Way
# ID 6: 1121 Loja Way
#
# Quantidade de endereços nulos: 4
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

- [ ] Estender a auditoria para outros campos opcionais da tabela
- [ ] Adicionar a cidade correspondente a cada endereço incompleto (quando `JOIN` for incorporado ao repositório)
- [ ] Gerar um percentual de completude dos dados, além da contagem absoluta

---

## 👤 Autor

Projeto desenvolvido como parte de estudos pessoais em **SQL, Python e Engenharia de Dados**.