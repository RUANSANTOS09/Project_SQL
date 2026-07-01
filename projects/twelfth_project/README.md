# 📋 Histórico de Aluguéis por Cliente

> Script que reconstrói o histórico de filmes alugados por um cliente específico, cruzando quatro tabelas relacionadas — simulando uma consulta de relacionamento com o cliente usada em sistemas de CRM e recomendação.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-7FB069?style=flat-square)
![Licença](https://img.shields.io/badge/Licença-MIT-4A5550?style=flat-square)

---

## 📖 Sobre o projeto

Este projeto simula uma funcionalidade comum em plataformas de streaming e locadoras digitais: recuperar o histórico de consumo de um cliente específico, com título do conteúdo e data do aluguel. O caminho entre cliente e filme passa por três tabelas intermediárias, exigindo um `JOIN` encadeado de quatro tabelas.

---

## 🧠 Conceitos aplicados

| Conceito | Onde aparece no projeto |
|---|---|
| **`JOIN` com quatro tabelas** | `customer` → `rental` → `inventory` → `film`, encadeados em sequência lógica |
| **Ordenação por data decrescente** | Resultado ordenado do aluguel mais recente pro mais antigo |
| **`enumerate()` com desempacotamento interno** | `for position, (first_name, last_name, title, rental_date) in enumerate(...)` |
| **Filtro por cliente específico** | `WHERE customer_id = %s`, tornando a consulta reutilizável para qualquer cliente |

---

## 🏗️ Caminho do JOIN

```
customer
   └── rental          (customer_id = customer_id)
         └── inventory  (inventory_id = inventory_id)
               └── film  (film_id = film_id)
```

---

## 💻 Exemplo de saída

```
1. Mary Smith - BEAST HUNCHBACK - 2005-08-23 20:03:39
2. Mary Smith - GRADUATE LORD - 2005-08-22 01:27:57
...

Quantidade total: 10
```

---

## ▶️ Como executar

```bash
python main.py
```

**Pré-requisitos:** Python 3.10+, `mysql-connector-python`, banco `sakila` configurado localmente.

---

## 🚀 Próximos passos

- [ ] Tornar o `customer_id` configurável via `input()`
- [ ] Adicionar o valor pago por cada aluguel ao relatório
- [ ] Identificar o gênero favorito do cliente com base no histórico

---

## 👤 Autor

Projeto desenvolvido como parte de estudos pessoais em **SQL, Python e Engenharia de Dados**.