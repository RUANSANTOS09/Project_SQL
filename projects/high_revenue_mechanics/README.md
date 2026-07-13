<div align="center">

# 🔧 Sistema de Gestão de Oficina Mecânica

> "Toda tabela que não é dona de nada é, na verdade, o ponto de encontro entre outras."

![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-success?style=for-the-badge)

</div>

---

## 📌 Sobre o projeto

Modelagem completa de banco de dados para uma oficina mecânica de carros de luxo, do zero: definição de entidades, relacionamentos via Foreign Key, população de dados, view com regra de negócio (agregação + filtro), e script Python para geração de relatório de faturamento por mecânico.

Projeto guiado por descoberta — sem passo a passo pronto, com decisões de modelagem (quais tabelas, onde colocar as FKs, como evitar redundância) tomadas de forma independente.

---

## 🗂️ Estrutura do banco

```
┌─────────────┐        ┌─────────────┐
│  customer    │───────▶│  vehicles    │
│ (1 cliente)  │  1:N   │ (N veículos) │
└─────────────┘        └──────┬──────┘
                               │
                               │ N:1
                               ▼
┌─────────────┐        ┌──────────────────┐
│  mechanic    │───────▶│ services_performed│
│ (mecânicos)  │  1:N   │ (serviços feitos)  │
└─────────────┘        └──────────────────┘
```

**Decisão de design:** `services_performed` não guarda `customer_id` diretamente — o cliente é alcançável indiretamente via `vehicles`, evitando redundância de dado.

---

## 🧠 Tabelas

- **`customer`** — clientes da oficina, com `email` único (constraint)
- **`vehicles`** — veículos, com `plate` única (constraint), ligados ao cliente dono
- **`mechanic`** — mecânicos da oficina, sem dependência de outras tabelas
- **`services_performed`** — serviços realizados, com FK para `mechanic` e `vehicles`, `price` em `DECIMAL(10,2)` e `service_date` em `DATE`

---

## 🧠 View de negócio: `high_revenue_mechanics`

```sql
create view high_revenue_mechanics as
select
    mec.mechanic_id as ID,
    mec.name as name,
    sum(price) as total
from services_performed
join mechanic as mec using (mechanic_id)
group by mec.mechanic_id
having total > 15000
order by total desc
```

Agrupa faturamento por mecânico, filtrando apenas quem ultrapassou R$15.000 em serviços — filtro pós-agregação com `HAVING`, ordenado do maior pro menor faturamento.

---

## 🐍 Script Python

`report_high_revenue_mechanics.py` consulta a view e gera um relatório `.txt` numerado com nome do mecânico e faturamento formatado em duas casas decimais.

- Conexão única com `charset="utf8mb4"`
- Uso de `_` para ignorar explicitamente valores não utilizados no unpacking da tupla
- Formatação de moeda com `:.2f`
- Contagem de registros via `len()`

**Saída:** `high_revenue_mechanics.txt`

---

## 💡 Conceitos praticados

- Modelagem de banco do zero (decisão independente de entidades e relacionamentos)
- Prevenção de redundância de dado (FK indireta via tabela intermediária)
- `GROUP BY` + `SUM` + `HAVING` para regra de negócio agregada
- `DECIMAL` para dinheiro, `DATE` para datas
- Boas práticas de Python: `_` para valores ignorados, f-string com format spec

---

<div align="center">

**Ruan Santos** · [GitHub](https://github.com/RUANSANTOS09)

</div>