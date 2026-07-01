# 🎬 Pipeline de Dados de Locadora

> Pipeline completo de extração, validação, segmentação e cruzamento de dados de uma locadora de filmes — integrando SQL e Python para gerar três relatórios distintos a partir de uma única conexão com o banco de dados.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-7FB069?style=flat-square)
![Licença](https://img.shields.io/badge/Licença-MIT-4A5550?style=flat-square)

---

## 📖 Sobre o projeto

Este é o projeto mais completo do repositório até o momento. Diferente dos projetos anteriores, que resolviam uma tarefa específica e isolada, este pipeline executa **três análises distintas em sequência**, simulando um cenário real onde um engenheiro de dados precisa extrair valor de diferentes domínios do mesmo banco — clientes, pagamentos e dados geográficos — em um único script organizado.

A proposta reflete a estrutura básica de um pipeline ETL real:
- **Extração** — dados brutos vêm do banco via SQL
- **Transformação** — Python valida, limpa, classifica e formata os dados
- **Carga** — resultados processados são entregues em arquivos de relatório

---

## 🧠 Conceitos aplicados

| Conceito | Onde aparece no projeto |
|---|---|
| **Conexão única para múltiplas queries** | Uma única instância de `connection` e `cursor` percorre as três partes do pipeline |
| **Filtro com `IS NOT NULL`** | Garantia de que apenas registros com email preenchido entram na análise de clientes |
| **Validação de dados em Python** | Verificação de integridade do email (`@` e `.`) separando registros válidos de inválidos |
| **`BETWEEN` + `ORDER BY` + `LIMIT`** | Segmentação de pagamentos dentro de faixa de valor, ordenados e paginados |
| **Variável local de categoria** | Classificação de cada pagamento em `Baixo`, `Médio` ou `Alto` usando `if/elif/else` |
| **Múltiplos acumuladores simultâneos** | Contagens independentes por categoria de pagamento, processadas no mesmo laço |
| **`JOIN` triplo com alias** | Cruzamento de `customer`, `payment` e `address` em uma única consulta |
| **`enumerate()` com desempacotamento interno** | `for position, (first_name, last_name, amount, address) in enumerate(...)` — numeração de registros sem perder o desempacotamento da tupla original |
| **Comentários de código** | Documentação inline explicando o propósito de cada seção e variável |

---

## 🏗️ Fluxo do pipeline

```
┌──────────────────────────────────────────────┐
│              Conexão MySQL (única)              │
└───────────────────┬──────────────────────────┘
                    │
        ┌───────────▼───────────┐
        │  PARTE 1               │
        │  Extração e limpeza    │
        │  de clientes ativos    │
        └───────┬───────┬───────┘
                │       │
        ┌───────▼──┐ ┌──▼──────────┐
        │clientes   │ │clientes      │
        │_validos   │ │_invalidos    │
        │.txt        │ │.txt           │
        └───────────┘ └─────────────┘
                    │
        ┌───────────▼───────────┐
        │  PARTE 2               │
        │  Segmentação de        │
        │  pagamentos por faixa  │
        └───────────┬───────────┘
                    │
        ┌───────────▼───────────┐
        │segmentacao_pagamentos  │
        │.txt                     │
        └───────────┬───────────┘
                    │
        ┌───────────▼───────────┐
        │  PARTE 3               │
        │  Relatório cruzado     │
        │  com JOIN triplo       │
        └───────────┬───────────┘
                    │
        ┌───────────▼───────────┐
        │      report.txt        │
        └────────────────────────┘
                    │
        ┌───────────▼───────────┐
        │  cursor.close()        │
        │  connection.close()    │
        └────────────────────────┘
```

---

## 📂 Arquivos gerados

| Arquivo | Conteúdo |
|---|---|
| `clientes_validos.txt` | Clientes ativos com email válido, normalizados |
| `clientes_invalidos.txt` | Clientes com email inválido ou ausente |
| `segmentacao_pagamentos.txt` | Pagamentos classificados por faixa de valor (baixo/médio/alto) |
| `report.txt` | Top 20 pagamentos acima de R$8, com nome, valor e endereço |

---

## ▶️ Como executar

```bash
python main.py
```

**Pré-requisitos:**
- Python 3.10 ou superior
- Biblioteca `mysql-connector-python`
- Servidor MySQL local com o banco de dados `sakila`

---

## 🚀 Próximos passos

- [ ] Adicionar tratamento de exceções para falhas de conexão
- [ ] Parametrizar os valores de corte via arquivo de configuração
- [ ] Exportar os relatórios também em formato `.csv`
- [ ] Adicionar log de execução registrando horário de início e fim de cada parte

---

## 👤 Autor

Projeto desenvolvido como parte de estudos pessoais em **SQL, Python e Engenharia de Dados**.