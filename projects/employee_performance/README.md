<div align="center">

# 👔 Auditoria de Desempenho de Funcionários — Sakila Rental

> "Todo JOIN mal feito é uma pergunta certa recebendo uma resposta errada."

![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-success?style=for-the-badge)

</div>

---

## 📌 Sobre o projeto

View + script Python para auditar a performance individual de funcionários da locadora Sakila: quantos aluguéis cada um processou, quanto arrecadou, e se bate a meta de bônus (R$33.000).

O desafio central deste projeto foi evitar **fan-out** (multiplicação indevida de linhas) ao juntar três tabelas — `staff`, `rental` e `payment` — sem uma cadeia de JOIN corretamente amarrada.

---

## 🗂️ Estrutura

```
┌─────────────────────────────────┐
│           MySQL (sakila)          │
│                                    │
│   staff ──▶ rental ──▶ payment    │
│   (staff_id)   (rental_id)        │
│                                    │
│  ┌──────────────────────────────┐ │
│  │ desempenho_funcionarios       │ │
│  └──────────────┬───────────────┘ │
└─────────────────┼─────────────────┘
                   │
                   ▼
      ┌─────────────────────────┐
      │      Script Python        │
      │    (mysql.connector)      │
      └──────────────┬───────────┘
                      │
                      ▼
      ┌─────────────────────────┐
      │ desempenho_funcionarios.txt│
      └─────────────────────────┘
```

---

## 🧠 View criada

### `desempenho_funcionarios`

```sql
create or replace view desempenho_funcionarios as
select
    stf.staff_id as id,
    stf.first_name as Nome,
    stf.last_name as Sobrenome,
    stf.store_id as Loja,
    count(ren.rental_id) as total_alugueis,
    sum(pay.amount) as total
from staff stf
join rental ren using(staff_id)
join payment pay using(rental_id)
group by id
having total_alugueis > 100
```

**Ponto-chave:** `payment` se conecta com `rental` via `rental_id` (não via `staff_id`), garantindo que cada pagamento fique amarrado ao aluguel exato que o originou — evitando produto cartesiano entre rentals e payments do mesmo funcionário.

---

## 🐍 Script Python

`report_desempenho_funcionarios.py` consulta a view ordenada por total arrecadado e gera um relatório com aprovação/reprovação de bônus (meta: R$33.000).

- Conexão única (connection)
- Leitura via `fetchall()`
- Regra de negócio (bônus) aplicada em Python, não em SQL
- Fechamento de `cursor` e `connection` no final

**Saída:** `desempenho_funcionarios.txt`

---

## 💡 Conceitos praticados

- `JOIN` encadeado com 3 tabelas (`staff → rental → payment`)
- Prevenção de **fan-out** ao escolher a chave de JOIN correta
- Qualificação de colunas ambíguas (`stf.staff_id`) quando múltiplas tabelas compartilham nome de coluna
- `GROUP BY` + `HAVING` para filtro pós-agregação
- Regra de negócio condicional em Python (`if/else` inline)

---

<div align="center">

**Ruan Santos** · [GitHub](https://github.com/RUANSANTOS09)

</div>