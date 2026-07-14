<div align="center">

# 🍔 Sistema de Delivery de Comida

> "A tabela do meio sempre aponta pras duas pontas, nunca o contrário."

![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-success?style=for-the-badge)

</div>

---

## 📌 Sobre o projeto

Modelagem completa de um app de delivery, do zero: restaurantes, cardápio, clientes, endereços e pedidos — com o desafio central de resolver corretamente um relacionamento **muitos-para-muitos (N:N)** entre pedidos e pratos, já que um pedido pode conter múltiplos itens do cardápio.

Projeto guiado por descoberta, com decisões de modelagem tomadas de forma independente e revisadas em várias iterações até fixar o padrão correto.

---

## 🗂️ Estrutura do banco

```
┌──────────────┐        ┌──────────────┐
│  restaurant   │───────▶│    dishes     │
│ (restaurantes)│  1:N   │  (cardápio)   │
└──────┬───────┘        └──────┬───────┘
       │                        │
       │ 1:N                    │ N:N (via order_items)
       ▼                        ▼
┌──────────────┐        ┌──────────────────┐
│    orders     │───────▶│   order_items      │
│  (pedidos)    │  1:N   │ (itens do pedido)   │
└──────┬───────┘        └──────────────────┘
       │
       │ N:1
       ▼
┌──────────────┐        ┌──────────────┐
│   customer    │        │   address     │
│  (clientes)   │        │ (endereços)   │
└──────────────┘        └──────────────┘
```

**Decisão de design central:** `order_items` é a tabela que resolve o N:N entre `orders` e `dishes` — cada linha representa um item específico de um pedido, permitindo múltiplos pratos por pedido sem duplicar dados de cliente/endereço/restaurante.

**Preço congelado (price snapshot):** `order_items.price_at_order` guarda o valor já calculado (preço unitário × quantidade) no momento da compra, independente de mudanças futuras no preço do prato em `dishes.price`.

---

## 🧠 Tabelas

- **`restaurant`** — restaurantes cadastrados
- **`dishes`** — cardápio, ligado ao restaurante via FK
- **`customer`** — clientes, com `email` único (constraint)
- **`address`** — endereços de entrega
- **`orders`** — pedido em si: cliente, restaurante e endereço (sem referência a pratos)
- **`order_items`** — itens de cada pedido: prato, quantidade e preço congelado, resolvendo o relacionamento N:N

---

## 🧠 View de negócio: `high_revenue_restaurants`

```sql
select
    res.restaurant_id,
    res.name,
    sum(ordt.price_at_order) as total,
    count(distinct order_id) as Quantidade_total
from restaurant res
join orders ordr using(restaurant_id)
join order_items ordt using(order_id)
group by res.restaurant_id, res.name
having total > 100
```

Faturamento total e quantidade de **pedidos únicos** (via `COUNT(DISTINCT order_id)`, não contagem de itens) por restaurante, filtrando quem faturou acima do valor de referência.

---

## 🐍 Script Python

`report_high_revenue_restaurants.py` consulta a view e gera relatório `.txt` numerado com nome do restaurante, faturamento e quantidade de pedidos.

- Conexão única com `charset="utf8mb4"`
- `_` para ignorar `restaurant_id` no unpacking
- Formatação de moeda com `:.2f`
- Contagem de registros via `len()`

**Saída:** `high_revenue_restaurants.txt`

---

## 💡 Conceitos praticados

- Modelagem de relacionamento N:N via tabela intermediária (`order_items`)
- Padrão de preço congelado (price snapshot) para histórico imutável
- `JOIN` encadeado (3 tabelas) para acessar dado indiretamente relacionado
- `COUNT(DISTINCT coluna)` para evitar contagem inflada em relação N:N
- `GROUP BY` + `SUM` + `HAVING` para regra de negócio agregada

---

<div align="center">

**Ruan Santos** · [GitHub](https://github.com/RUANSANTOS09)

</div>