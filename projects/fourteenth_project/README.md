# 🏪 Staff & Stores — Mapeamento de Funcionários por Unidade

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Sakila-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-2ea043?style=for-the-badge)
![Tipo](https://img.shields.io/badge/Tipo-Engenharia%20de%20Dados-8b5cf6?style=for-the-badge)

<br/>

> *"Dados bem cruzados respondem perguntas que planilhas nunca conseguiriam."*

<br/>

</div>

---

## ✦ Visão Geral

Este script responde a uma pergunta simples de RH, mas que exige cruzar três tabelas diferentes: **quem trabalha onde?** Combinando funcionários, lojas e endereços num único pipeline Python + SQL, o resultado é um relatório limpo e direto — pronto para ser consumido por qualquer time operacional.

---

## ⚙️ Como funciona

```
┌─────────────┐      store_id       ┌─────────────┐     address_id    ┌─────────────┐
│    staff      │ ────────────────▶ │    store      │ ────────────────▶ │   address    │
│  (funcionário)│                   │    (loja)     │                   │  (endereço)  │
└─────────────┘                    └─────────────┘                    └─────────────┘
       │                                  │                                   │
  first_name                          store_id                            address
  last_name                                                      
```

O caminho percorre três tabelas em sequência — do **funcionário** até o **endereço físico** da loja onde ele trabalha.

---

## 🧠 Conceitos aplicados

```
SQL ──────────────────────────────────────────────────────────────
  JOIN triplo          →  staff + store + address
  Alias de tabela      →  stf, str (clareza nas condições ON)
  ORDER BY             →  ordenação alfabética por nome

Python ───────────────────────────────────────────────────────────
  mysql.connector      →  conexão com banco de dados local
  fetchall()           →  recuperação de todos os registros
  len()                →  contagem direta sem acumulador manual
  .strip().title()     →  normalização do nome completo
  with open()          →  escrita segura em arquivo de saída
```

---

## 📄 Saída gerada

```
📁 funcionarios_lojas.txt
─────────────────────────────────────────────────
  Mike Hillyer — Loja 1 — 23 Workhaven Lane
  Jon Stephens — Loja 2 — 47 MySakila Drive

  Total: 2
─────────────────────────────────────────────────
```

---

## ▶️ Execução

```bash
# Clone o repositório
git clone https://github.com/RUANSANTOS09/Projeto_SQL.git

# Acesse a pasta do projeto
cd projects/staff_stores

# Execute o script
python main.py
```

**Dependências:**

| Dependência | Versão mínima |
|---|---|
| Python | 3.10+ |
| mysql-connector-python | qualquer versão estável |
| MySQL + banco sakila | configurado localmente |

---

## 🗂️ Estrutura

```
staff_stores/
├── main.py                   # Script principal
├── funcionarios_lojas.txt     # Relatório gerado (criado na execução)
└── README.md                  # Este arquivo
```

---

## 🚀 Evoluções futuras

| # | Melhoria |
|---|---|
| 01 | Adicionar o e-mail do funcionário ao relatório |
| 02 | Comparar número de funcionários por loja |
| 03 | Exportar relatório em `.csv` para uso em planilhas |
| 04 | Incluir foto do funcionário (campo `picture` da tabela `staff`) |

---

<div align="center">

**Projeto desenvolvido como parte de uma trilha de estudos em Engenharia de Dados.**

*Construído consulta por consulta, JOIN por JOIN.* 🛤️

</div>