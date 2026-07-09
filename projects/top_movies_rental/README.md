<div align="center">

# 🎥 Top Filmes por Disponibilidade de Aluguel — Sakila Rental

> "Não é sobre ter todos os dados. É sobre saber qual pergunta fazer a eles."

![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-success?style=for-the-badge)

</div>

---

## 📌 Sobre o projeto

View + script Python para identificar quais filmes têm mais **cópias físicas** (copies) disponíveis no estoque da locadora Sakila — um indicador indireto de quais títulos a rede aposta mais.

---

## 🗂️ Estrutura

```
┌───────────────────────────────┐
│         MySQL (sakila)         │
│                                 │
│  ┌───────────────────────────┐ │
│  │  top_filmes_aluguel        │ │
│  │  (film + inventory)        │ │
│  └─────────────┬─────────────┘ │
└────────────────┼───────────────┘
                  │
                  ▼
      ┌───────────────────────┐
      │   Script Python         │
      │  (mysql.connector)      │
      └─────────────┬─────────┘
                     │
                     ▼
      ┌───────────────────────┐
      │ top_filmes_aluguel.txt │
      └───────────────────────┘
```

---

## 🧠 View criada

### `top_filmes_aluguel`
Ranking de filmes por número de cópias disponíveis em estoque (inventory), do maior para o menor.

```sql
create view top_filmes_aluguel as
select
    fil.film_id as Id,
    fil.title as title,
    fil.rental_rate as rental_rate,
    count(inventory_id) as copias
from inventory
join film fil using(film_id)
group by fil.film_id
order by copias desc
```

---

## 🐍 Script Python

`report_top_filmes_aluguel.py` consulta a view, limita o resultado aos **20 primeiros** (via parâmetro `%s`), e gera um relatório `.txt` numerado com título, preço de aluguel e quantidade de cópias.

- Conexão única (connection)
- Query parametrizada com `%s` e tupla (`(20,)`)
- Contagem de registros via `len()`
- Fechamento de `cursor` e `connection` no final

**Saída:** `top_filmes_aluguel.txt`

---

## 💡 Conceitos praticados

- `CREATE VIEW`
- `JOIN ... USING`
- `GROUP BY` + `COUNT()`
- `ORDER BY` em view e em query consumidora
- `LIMIT` parametrizado em Python

---

<div align="center">

**Ruan Santos** · [GitHub](https://github.com/RUANSANTOS09)

</div>