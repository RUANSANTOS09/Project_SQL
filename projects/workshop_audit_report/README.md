# 🔧 Workshop Audit Report

> "Não se gerencia o que não se mede." — Peter Drucker

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

## 📋 Sobre o projeto

Script de auditoria para uma oficina mecânica, consumindo dados diretamente do MySQL via `mysql-connector-python` e processando com Pandas. Gera três relatórios distintos a partir de views SQL, identificando onde está concentrado o faturamento de maior valor.

## 🗂️ Estrutura de dados

```
mechanic (database)
│
├── customer ──┐
│              ├── vehicles ──┐
│              │              ├── services_performed ── mechanic
│              │
views:
├── info_problem_price   (vehicles JOIN services_performed)
└── info_price_services  (mechanic JOIN services_performed)
```

## 📊 Relatórios gerados

| Relatório | Critério | Origem |
|---|---|---|
| `expensive_services_report` | `price > 20000` | `services_performed` |
| `critical_transmission_report` | `price > 20000` AND problema contém "transmissão" | `info_problem_price` |
| `mechanics_audit_report` | Mecânico em `['Pedro', 'Leticia', 'Valdemir']` | `info_price_services` |

## ⚙️ Como rodar

```bash
pip install pandas mysql-connector-python
python report.py
```

## 🧠 Conceitos aplicados

- `pd.read_sql()` para consumir dados direto do MySQL, sem etapa intermediária de CSV
- Filtragem com `.loc[]`, `==`, `>`
- `.str.contains()` como equivalente ao `LIKE` do SQL
- `.isin()` para filtrar por múltiplos valores
- Views SQL para pré-join de dados espalhados em tabelas normalizadas

## 👤 Autor

**Ruan Santos** — [github.com/RUANSANTOS09](https://github.com/RUANSANTOS09)