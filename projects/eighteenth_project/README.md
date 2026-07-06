# 🌍 Premium Clients — Relatório de Clientes Premium por Região

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Sakila-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-2ea043?style=for-the-badge)
![Tipo](https://img.shields.io/badge/Tipo-Segmentação%20Regional-8b5cf6?style=for-the-badge)

<br/>

> *"Filtrar pelo comportamento agregado é o que separa análise de dado bruto de inteligência de negócio."*

</div>

---

## ✦ Visão Geral

Script que identifica clientes de alto valor por região, cruzando pagamentos, cadastro e endereço em uma única consulta com `JOIN` triplo, `GROUP BY` e `HAVING`. Em Python, os clientes são segmentados em categorias **Ouro** e **Prata** com base no total gasto — simulando uma análise real de expansão comercial.

---

## 🧠 Conceitos aplicados

| Conceito | Onde aparece |
|---|---|
| **`JOIN USING` + `JOIN ON`** | Combinação de `payment`/`customer` via `USING`, e `customer`/`address` via `ON` |
| **`SUM` + `COUNT` com `GROUP BY`** | Total gasto e quantidade de compras por cliente |
| **`HAVING` com dois parâmetros** | Filtro de grupos por total e quantidade, ambos via `%s` |
| **`ORDER BY` no resultado agregado** | Ordenação pelo total do maior pro menor |
| **`enumerate()` com desempacotamento de 6 valores** | Numeração + 5 campos do banco desempacotados diretamente |
| **Classificação em Python (`if/elif`)** | Segmentação Ouro (>R$180) e Prata (R$130–R$180) |
| **Dois acumuladores simultâneos** | Contagem independente de clientes Ouro e Prata |
| **`:.2f` na f-string** | Formatação monetária do total diretamente na interpolação |

---

## 🏗️ Fluxo do pipeline

```
┌─────────────────────────────────────┐
│  payment                             │
│  JOIN customer USING(customer_id)    │
│  JOIN address ON address_id          │
└──────────────────┬──────────────────┘
                   │ GROUP BY customer_id
                   │ HAVING Total > 130
                   │        AND Qtd > 30
                   │ ORDER BY Total DESC
                   ▼
┌─────────────────────────────────────┐
│  Python: classificação               │
│  Total > 180  → OURO                 │
│  Total >= 130 → PRATA                │
└──────────────────┬──────────────────┘
                   ▼
┌─────────────────────────────────────┐
│      clientes_premium_regiao.txt     │
└─────────────────────────────────────┘
```

---

## 💻 Exemplo de saída

```
1. Ouro Eleanor Hunt | Região: Southern Georgia | Total: R$211.55 | Compras: 46
2. Ouro Karl Seal    | Região: Gansu            | Total: R$208.58 | Compras: 45
...

Total de clientes Ouro: 12
Total de clientes Prata: 8
```

---

## ▶️ Como executar

```bash
python main.py
```

**Pré-requisitos:** Python 3.10+, `mysql-connector-python`, banco `sakila` configurado localmente.

---

## 🚀 Próximos passos

- [ ] Adicionar uma terceira categoria `'BRONZE'` para clientes entre R$100 e R$130
- [ ] Agrupar o relatório por distrito, mostrando quantos clientes premium existem em cada região
- [ ] Exportar em `.csv` para uso em ferramentas de visualização

---

<div align="center">

**Projeto desenvolvido como parte de uma trilha de estudos em Engenharia de Dados.** 🛤️

</div>