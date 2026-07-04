# 📊 Staff Performance — Relatório de Desempenho por Funcionário

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Sakila-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-2ea043?style=for-the-badge)
![Tipo](https://img.shields.io/badge/Tipo-Agregação%20de%20Dados-8b5cf6?style=for-the-badge)

<br/>

> *"Agregar dados é transformar ruído em decisão."*

</div>

---

## ✦ Visão Geral

Script que consolida métricas de desempenho de cada funcionário da locadora — maior venda, menor venda, média e total arrecadado — utilizando funções de agregação SQL com `GROUP BY`, entregando um relatório formatado em arquivo de texto.

---

## 🧠 Conceitos aplicados

| Conceito | Onde aparece |
|---|---|
| **`MAX`, `MIN`, `AVG`, `SUM`** | Cálculo de métricas por funcionário numa única query |
| **`GROUP BY`** | Agregação dos resultados por `staff_id` |
| **`WHERE` antes da agregação** | Filtro de pagamentos acima de R$2 antes do cálculo |
| **`round()`** | Arredondamento da média para 2 casas decimais |
| **`len(resultado)`** | Contagem direta do total de funcionários processados |

---

## 💻 Exemplo de saída

```
Funcionário 1 | Maior: R$11.99 | Menor R$0.99 | Média: 4.21 | Total: 36920.98
Funcionário 2 | Maior: R$11.99 | Menor R$0.99 | Média: 4.19 | Total: 33927.04

Total de funcionários: 2
```

---

## ▶️ Como executar

```bash
python main.py
```

**Pré-requisitos:** Python 3.10+, `mysql-connector-python`, banco `sakila` configurado localmente.

---

## 🚀 Próximos passos

- [ ] Incluir o nome do funcionário combinando com a tabela `staff` via `JOIN`
- [ ] Adicionar a data do primeiro e último pagamento processado por cada funcionário
- [ ] Exportar em `.csv` para uso em planilhas

---

<div align="center">

**Projeto desenvolvido como parte de uma trilha de estudos em Engenharia de Dados.** 🛤️

</div>