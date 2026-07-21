# 🧹 Relatório de Pedidos — Tratamento de Nulos

> "Dado sujo não é falta de sorte, é falta de tratamento." — princípio de Engenharia de Dados

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

## 📋 Sobre o projeto

Mini projeto de limpeza de dados sobre a tabela `orders` do banco `ecommerce`. O objetivo era gerar um relatório de pedidos sem nenhum valor nulo visível, pronto pra apresentação ao time comercial — sem mascarar erro de dado real com tratamento superficial.

## 🗂️ Fluxo aplicado

```
MySQL (orders)
     │
     ├── 1. Correção na fonte (UPDATE)
     │      order_date nulo nos pedidos "Em andamento"
     │      e "Cancelada" → preenchido com data real
     │
     ▼
Pandas (pd.read_sql)
     │
     ├── 2. fillna() com dicionário
     │      coupon_code            → "Sem cupom"
     │      delivery_date          → "Pedido ainda não entregue"
     │      reason_for_cancellation → "Pedido não cancelado"
     │
     ▼
relatorio_pedidos_final
     (isnull().sum() = 0 em todas as colunas)
```

## 🧠 Conceitos aplicados

- `fillna()` com dicionário para tratar múltiplas colunas em uma única chamada
- `replace()` para substituição de valores específicos (incluindo mapeamento via dicionário)
- Diferença entre nulo como **regra de negócio** (delivery_date, coupon_code) e nulo como **erro de dado** (order_date) — o segundo se corrige na fonte, não se mascara com fillna
- Risco de misturar tipos ao usar `fillna` com string em coluna numérica/data (contaminação de tipo → `dtype('O')`)
- `dtype('O')` não é sinônimo automático de dado sujo — precisa checar o conteúdo real da célula (`type()`) antes de concluir
- `.isnull().sum()` como validação final de limpeza
- Imutabilidade da camada raw: transformação no Pandas nunca altera a fonte MySQL

## 👤 Autor

**Ruan Santos** — [github.com/RUANSANTOS09](https://github.com/RUANSANTOS09)