# 🌐 Language Manager — Gestão de Idiomas da Locadora

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Sakila-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-2ea043?style=for-the-badge)
![Tipo](https://img.shields.io/badge/Tipo-Manipulação%20de%20Dados-8b5cf6?style=for-the-badge)

<br/>

> *"Antes de modificar, faça backup. Antes de deletar, pense duas vezes."*

<br/>

</div>

---

## ✦ Visão Geral

Este projeto demonstra o ciclo completo de **manipulação de dados** em um banco relacional, integrando Python e SQL para executar operações de `INSERT`, `UPDATE`, `DELETE` e geração de relatório — tudo com segurança e rastreabilidade.

---

## ⚙️ Fluxo do Pipeline

```
┌─────────────────────────────────────────────────┐
│                   INÍCIO                          │
└───────────────────┬─────────────────────────────┘
                    │
        ┌───────────▼───────────┐
        │  1. BACKUP              │
        │  CREATE TABLE AS SELECT │  ← cópia de segurança antes de tudo
        └───────────┬───────────┘
                    │
        ┌───────────▼───────────┐
        │  2. INSERT              │
        │  Novos idiomas          │  ← Korean, Russian
        └───────────┬───────────┘
                    │
        ┌───────────▼───────────┐
        │  3. UPDATE              │
        │  Korean → South Korean  │  ← correção via Python + WHERE
        └───────────┬───────────┘
                    │
        ┌───────────▼───────────┐
        │  4. DELETE              │
        │  Remove Russian         │  ← limpeza de dado desnecessário
        └───────────┬───────────┘
                    │
        ┌───────────▼───────────┐
        │  5. RELATÓRIO           │
        │  SELECT + arquivo .txt  │  ← estado final documentado
        └────────────────────────┘
```

---

## 🧠 Conceitos aplicados

| Conceito | Onde aparece |
|---|---|
| **`CREATE TABLE ... AS SELECT`** | Backup da tabela antes de qualquer modificação |
| **`INSERT INTO` múltiplas linhas** | Inserção de dois idiomas numa única operação |
| **`UPDATE ... SET ... WHERE`** | Atualização segura de um registro específico via `customer_id` |
| **`DELETE FROM ... WHERE`** | Remoção cirúrgica de um registro pelo nome |
| **`connection.commit()`** | Confirmação explícita das alterações no banco |
| **`len(resultado)`** | Contagem direta do total sem acumulador manual |
| **`with open()`** | Escrita segura do relatório final em arquivo |

---

## 📄 Saída gerada

```
📁 relatorio_idiomas.txt
─────────────────────────────
  1 | English
  2 | Italian
  3 | Japanese
  ...
  20 | South Korean

  Total de linguas: 11
─────────────────────────────
```

---

## ▶️ Como executar

```bash
git clone https://github.com/RUANSANTOS09/Projeto_SQL.git
cd projects/language_manager
python main.py
```

**Pré-requisitos:** Python 3.10+, `mysql-connector-python`, banco `sakila` configurado localmente.

---

## ⚠️ Observação importante

Este projeto executa operações que **modificam dados reais** no banco. A etapa de backup (`CREATE TABLE language_backup`) deve ser executada antes de qualquer modificação. Caso a tabela de backup já exista de uma execução anterior, comente ou remova essa linha antes de rodar novamente.

---

## 🚀 Próximos passos

| # | Melhoria |
|---|---|
| 01 | Adicionar `try/except` para tratar erros de conexão e de tabela já existente |
| 02 | Tornar o idioma a ser atualizado/deletado configurável via `input()` |
| 03 | Registrar cada operação num arquivo de log com timestamp |

---

<div align="center">

**Projeto desenvolvido como parte de uma trilha de estudos em Engenharia de Dados.**

*Construído operação por operação, com segurança e rastreabilidade. 🛤️*

</div>