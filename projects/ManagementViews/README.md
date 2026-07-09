<div align="center">

# 🎬 Painel de Views Gerenciais — Sakila Rental

> "A dado sem contexto é ruído. View bem feita é a diferença entre dado e decisão."

![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-success?style=for-the-badge)

</div>

---

## 📌 Sobre o projeto

Conjunto de **Views** (visões — consultas SQL salvas como se fossem tabelas) criadas para simular um pedido real de gestão da locadora **Sakila**: relatórios fixos, prontos para consulta, sem que o time precise escrever SQL toda vez.

Cada view é consumida por um script Python independente, que gera um relatório `.txt` formatado.

---

## 🗂️ Estrutura

```
┌─────────────────────────────┐
│         MySQL (sakila)       │
│                               │
│  ┌─────────────────────────┐ │
│  │ filmes_mais_alugados     │ │
│  │ faturamento_loja         │ │
│  │ clientes_vip             │ │
│  └───────────┬─────────────┘ │
└──────────────┼───────────────┘
               │
               ▼
   ┌───────────────────────┐
   │   Scripts Python       │
   │  (mysql.connector)     │
   └───────────┬───────────┘
               │
               ▼
   ┌───────────────────────┐
   │   Relatórios .txt      │
   │  - filmes_mais_alugados│
   │  - faturamento_loja    │
   │  - clientes_vip        │
   └───────────────────────┘
```

---

## 🧠 Views criadas

### 1. `filmes_mais_alugados`
Ranking de filmes por quantidade de aluguéis (rentals), do mais para o menos alugado.

```sql
create or replace view filmes_mais_alugados as
select
    film_id as id,
    title as titulo,
    count(ren.rental_id) as mais_alugados
from film
join inventory inv using(film_id)
join rental ren using(inventory_id)
group by id
order by mais_alugados desc
```

### 2. `faturamento_loja`
Total arrecadado (revenue) por loja, via relação `staff → store`.

```sql
create or replace view faturamento_loja as
select
   store_id as id,
   sum(pay.amount) as total
from staff
join payment pay using(staff_id)
group by store_id
```

### 3. `clientes_vip`
Clientes com gasto total acima de R$150 — filtro aplicado **após** a agregação, com `HAVING`.

```sql
create or replace view clientes_vip as
select
    cus.customer_id as id,
    cus.first_name as name,
    cus.last_name as sobrenome,
    sum(amount) as total
from payment
join customer cus using(customer_id)
group by cus.customer_id
having total > 150
```

---

## 🐍 Scripts Python

Cada script segue o mesmo padrão:
- Uma única conexão (connection) por execução
- `cursor.execute()` com parâmetros seguros (`%s`, quando aplicável)
- Geração de relatório `.txt` numerado
- Contagem de registros via `len()`
- Fechamento de `cursor` e `connection` no final

| Script | View consultada | Saída |
|---|---|---|
| `report_filmes_mais_alugados.py` | `filmes_mais_alugados` | `management_views.txt` |
| `report_faturamento_loja.py` | `faturamento_loja` | `faturamento_loja.txt` |
| `report_clientes_vip.py` | `clientes_vip` | `clientes_vip.txt` |

---

## 💡 Conceitos praticados

- `CREATE OR REPLACE VIEW`
- `JOIN ... USING` (encadeamento de múltiplos JOINs)
- `GROUP BY` + `HAVING` (filtro pós-agregação)
- `ORDER BY` em resultado agregado
- Consumo de views via `mysql.connector`

---

<div align="center">

**Ruan Santos** · [GitHub](https://github.com/RUANSANTOS09)

</div>