# 📊 Above Average — Relatório de Pagamentos Acima da Média

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Sakila-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-2ea043?style=for-the-badge)
![Tipo](https://img.shields.io/badge/Tipo-SubQuery-8b5cf6?style=for-the-badge)

<br/>

> *"Comparar com a média é o ponto de partida de qualquer análise de desempenho real."*

</div>

---

## ✦ Visão Geral

Script que identifica os pagamentos acima da média geral da locadora, utilizando **subquery** como filtro dinâmico — o valor de corte não é fixo no código, mas calculado automaticamente pelo banco a cada execução. Em Python, os resultados são classificados entre pagamentos **Alto** e **Médio** e entregues em relatório formatado.

---

## 🧠 Conceitos aplicados

| Conceito | Onde aparece |
|---|---|
| **Subquery no `WHERE`** | `WHERE amount > (SELECT AVG(amount) FROM payment)` — filtro dinâmico baseado na média calculada em tempo real |
| **`JOIN USING`** | Combinação de `payment` e `customer` pela coluna `customer_id` em comum |
| **`ORDER BY` + `LIMIT`** | Top 20 pagamentos acima da média, ordenados do maior pro menor |
| **Parâmetro seguro via `%s`** | O `LIMIT` é passado como parâmetro, não concatenado |
| **`enumerate()` com desempacotamento interno** | Numeração + 4 campos desempacotados diretamente no `for` |
| **Classificação em Python** | `if/else` segmentando Alto (>R$8) e Médio (<=R$8) |
| **`:.2f` na f-string** | Formatação monetária diretamente na interpolação |

---

## 🏗️ Fluxo do pipeline

```
┌─────────────────────────────────────────┐
│  Subquery: calcula AVG(amount)            │
│  SELECT AVG(amount) FROM payment          │
└──────────────────┬──────────────────────┘
                   │ resultado vira o valor de corte
                   ▼
┌─────────────────────────────────────────┐
│  Query principal                          │
│  payment JOIN customer USING(customer_id) │
│  WHERE amount > [média calculada]         │
│  ORDER BY amount DESC LIMIT 20            │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│  Python: classificação                    │
│  amount > 8  → Alto                       │
│  amount <= 8 → Médio                      │
└──────────────────┬──────────────────────┘
                   ▼
┌─────────────────────────────────────────┐
│       pagamentos_acima_media.txt          │
└─────────────────────────────────────────┘
```

---

## 💻 Exemplo de saída

```
1. Karen Jackson | R$11.99 | Alto
2. Clara Shaw    | R$11.99 | Alto
3. Tim Cary      | R$9.99  | Alto
...

Total de pagamentos altos: 17
Total de pagamentos médios: 3
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
- [ ] Usar subquery com `MAX` pra identificar o maior pagamento de cada cliente
- [ ] Criar uma terceira categoria `'PREMIUM'` para pagamentos acima de R$10

---

<div align="center">

**Projeto desenvolvado como parte de uma trilha de estudos em Engenharia de Dados.** 🛤️

</div>