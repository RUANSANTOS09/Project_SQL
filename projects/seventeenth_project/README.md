# 🏆 Top Clients — Ranking de Clientes por Receita e Volume

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Sakila-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-2ea043?style=for-the-badge)
![Tipo](https://img.shields.io/badge/Tipo-Segmentação%20de%20Clientes-8b5cf6?style=for-the-badge)

<br/>

> *"Conhecer o cliente pelo comportamento de compra é o primeiro passo de qualquer análise comercial."*

</div>

---

## ✦ Visão Geral

Script que identifica e classifica os 20 clientes de maior receita da locadora, combinando dados de pagamentos e cadastro via `JOIN`, agrupando por cliente com `GROUP BY`, e segmentando em Python entre clientes **VIP** e **Regular** com base no total gasto.

---

## 🧠 Conceitos aplicados

| Conceito | Onde aparece |
|---|---|
| **`JOIN ... USING(customer_id)`** | Combinação de `payment` e `customer` pela coluna em comum |
| **`SUM` + `COUNT` com `GROUP BY`** | Total gasto e quantidade de compras por cliente |
| **`ORDER BY` + `LIMIT`** | Top 20 clientes ordenados por receita decrescente |
| **`enumerate()` com desempacotamento interno** | Numeração de posição combinada com 5 variáveis por registro |
| **Classificação em Python** | `if/else` segmentando VIP (>R$150) ou Regular |
| **Dois acumuladores simultâneos** | Contagem independente de VIPs e Regulares |
| **`:.2f` na f-string** | Formatação monetária diretamente na interpolação |

---

## 🏗️ Fluxo do pipeline

```
┌──────────────────────────────┐
│  payment JOIN customer        │
│  USING(customer_id)           │
└──────────────┬───────────────┘
               │ GROUP BY customer_id
               │ ORDER BY total DESC
               │ LIMIT 20
               ▼
┌──────────────────────────────┐
│  Python: classificação        │
│  total > 150 → VIP            │
│  total <= 150 → Regular       │
└──────────────┬───────────────┘
               ▼
┌──────────────────────────────┐
│       top_clientes.txt        │
└──────────────────────────────┘
```

---

## 💻 Exemplo de saída

```
1. Eleanor Hunt | Total: R$211.55 | Pagamentos: 46 | VIP
2. Karl Seal    | Total: R$208.58 | Pagamentos: 45 | VIP
...
20. Clara Shaw  | Total: R$149.00 | Pagamentos: 38 | Regular

Total de Clientes VIPs: 14
Total de Clientes REGULAR: 6
```

---

## ▶️ Como executar

```bash
python main.py
```

**Pré-requisitos:** Python 3.10+, `mysql-connector-python`, banco `sakila` configurado localmente.

---

## 🚀 Próximos passos

- [ ] Adicionar o endereço do cliente ao relatório via segundo `JOIN`
- [ ] Calcular o ticket médio por cliente (total / quantidade de pagamentos)
- [ ] Criar uma terceira categoria `'PREMIUM'` para clientes acima de R$200

---

<div align="center">

**Projeto desenvolvido como parte de uma trilha de estudos em Engenharia de Dados.** 🛤️

</div>