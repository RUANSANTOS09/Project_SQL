# 📋 Relatório de Clientes Ativos

> Script que consulta clientes ativos em um banco de dados MySQL, formata e organiza os resultados, e gera um relatório em arquivo de texto com contagem total — simulando uma tarefa real de extração e documentação de dados.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-7FB069?style=flat-square)
![Licença](https://img.shields.io/badge/Licença-MIT-4A5550?style=flat-square)

---

## 📖 Sobre o projeto

Este projeto simula uma tarefa comum em ambientes corporativos: gerar um **relatório de clientes ativos**, combinando uma consulta SQL filtrada e ordenada com processamento em Python para formatação e persistência em arquivo.

Diferente dos projetos anteriores, que apenas exibiam ou classificavam dados em memória, este projeto avança para a etapa de **entrega**: os dados processados são organizados em um relatório final, salvo em disco, pronto para ser consultado, compartilhado ou consumido por outro processo.

---

## 🧠 Conceitos aplicados

| Conceito | Onde aparece no projeto |
|---|---|
| **Consulta SQL filtrada e ordenada** | `WHERE active = %s` combinado com `ORDER BY last_name` |
| **Parâmetros seguros (prevenção de SQL Injection)** | Uso de `%s` e tupla de valores, em vez de concatenação direta na query |
| **Desempacotamento de tupla** | `for first_name, last_name, email in customers:` |
| **Manipulação de strings** | `.title()`, padronizando a capitalização dos nomes |
| **Acumulador** | Contagem total de clientes processados |
| **Gerenciamento de contexto (`with`)** | Escrita do relatório final em arquivo, com fechamento automático |

---

## 🏗️ Fluxo do processamento

```
┌──────────────────────┐
│   Conexão MySQL         │
└──────────┬─────────────┘
           │ SELECT ... WHERE active = 1
           │ ORDER BY last_name
           ▼
┌──────────────────────┐
│   Resultados (tuplas)   │
└──────────┬─────────────┘
           │ for first_name, last_name, email in customers:
           ▼
┌──────────────────────┐
│  Formatação e contagem  │
└──────────┬─────────────┘
           ▼
┌──────────────────────┐
│relatorio_clientes      │
│   _ativos.txt            │
└────────────────────────┘
```

---

## 💻 Exemplo de uso

```python
# Saída em relatorio_clientes_ativos.txt:
# Maria Santos - maria.santos@email.com
# Joao Pereira - joao.pereira@email.com
#
# Total de clientes: 584
```

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

- [ ] Adicionar filtro por loja (`store_id`) como parâmetro opcional
- [ ] Exportar o relatório também em formato `.csv`
- [ ] Adicionar tratamento de exceções para falhas de conexão

---

## 👤 Autor

Projeto desenvolvido como parte de estudos pessoais em **SQL, Python e Engenharia de Dados**.