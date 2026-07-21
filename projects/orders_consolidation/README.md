# 📦 Consolidação e Exportação de Pedidos

> "Dado consolidado é dado que alguém pode confiar." — princípio de Engenharia de Dados

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

## 📋 Sobre o projeto

Consolida os pedidos da tabela `orders` (banco `ecommerce`), lidos separadamente por status, em um único relatório e exporta o resultado como CSV — simulando a entrega mensal do time de operações.

## 🗂️ Fluxo aplicado

```
MySQL (orders)
     │
     ├── SELECT status = 'Finalizada'    → df_finished
     ├── SELECT status = 'Em andamento'  → df_in_progress
     ├── SELECT status = 'Cancelada'     → df_canceled
     │
     ▼
pd.concat([...], ignore_index=True)
     │
     ▼
consolidated_orders_report
     │
     ▼
orders.csv
(pasta de destino separada da pasta de origem,
 evita releitura acidental em execuções futuras)
```

## 🧠 Conceitos aplicados

- `pd.concat()` para empilhar DataFrames com a mesma estrutura
- `ignore_index=True` para evitar índice duplicado após concatenação
- Separação entre pasta de origem e pasta de destino como prática de segurança contra reprocessamento duplicado em pipelines com loop
- `os.path.join()` para montar caminhos de arquivo de forma segura, evitando erro manual de barra em string
- Diagnóstico de `PermissionError` no Windows (pasta inexistente ou arquivo aberto em outro processo)
- Validação de integridade pós-exportação, relendo o CSV salvo e comparando número de linhas

## 👤 Autor

**Ruan Santos** — [github.com/RUANSANTOS09](https://github.com/RUANSANTOS09)