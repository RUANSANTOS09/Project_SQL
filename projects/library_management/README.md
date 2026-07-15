<div align="center">

# 📖 Sistema de Biblioteca com Controle de Empréstimos

> "NULL não é um valor — é a ausência de um. E às vezes essa ausência é o dado mais importante."

![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-success?style=for-the-badge)

</div>

---

## 📌 Sobre o projeto

Modelagem de banco para controle de empréstimos de uma biblioteca, com relacionamento N:N entre livros e autores (coautoria), e uma view de inadimplência que identifica membros com empréstimo vencido — combinando `NULL` (estado pendente) com comparação de datas via `CURDATE()`.

---

## 🗂️ Estrutura do banco

```
┌──────────────┐        ┌──────────────────┐        ┌──────────────┐
│    author      │───────▶│   book_authors     │◀───────│     book      │
│  (autores)     │  N:N   │ (conecta autor+livro)│  N:N   │   (livros)    │
└──────────────┘        └──────────────────┘        └──────┬───────┘
                                                              │
                                                              │ 1:N
                                                              ▼
┌──────────────┐                                     ┌──────────────┐
│   members      │────────────────────────────────────▶│     loan       │
│  (membros)     │                1:N                  │ (empréstimos)  │
└──────────────┘                                     └──────────────┘
```

**Decisão de design:** `book_authors` resolve o N:N entre `book` e `author`, permitindo livros com múltiplos autores (coautoria) sem duplicar dados.

**Estado pendente via NULL:** `loan.return_date` aceita `NULL` (sem `NOT NULL`), representando "ainda não devolvido" — diferente de todas as outras colunas do projeto, que são obrigatórias.

---

## 🧠 Tabelas

- **`author`** — autores cadastrados
- **`book`** — livros cadastrados
- **`book_authors`** — resolve N:N entre livro e autor (coautoria)
- **`members`** — membros da biblioteca, com `email` único
- **`loan`** — empréstimos: retirada, prazo de devolução e devolução real (nullable)

---

## 🧠 View de negócio: `overdue_books`

```sql
create or replace view overdue_books as
select
    mem.members_id as ID,
    mem.name as name,
    loa.due_date
from members mem
join loan loa using (members_id)
where return_date is null and due_date < curdate()
```

Identifica membros com empréstimo em atraso: livro ainda não devolvido (`IS NULL`) **e** prazo já vencido (`due_date < CURDATE()`), combinando os dois filtros com `AND`.

---

## 🐍 Script Python

`report_overdue_books.py` consulta a view e gera relatório `.txt` numerado com nome do membro inadimplente e data prevista de devolução.

- Conexão única com `charset="utf8mb4"`
- `_` para ignorar o `ID` no unpacking da tupla
- Contagem de registros via `len()`

**Saída:** `overdues_report.txt`

---

## 💡 Conceitos praticados

- Relacionamento N:N aplicado de forma independente (sem correção necessária)
- `NULL` como representação de estado pendente/indefinido
- `IS NULL` / `IS NOT NULL` para testar ausência de valor
- `CURDATE()` para comparação com a data atual do sistema
- Combinação de múltiplas condições com `AND` no `WHERE`

---

<div align="center">

**Ruan Santos** · [GitHub](https://github.com/RUANSANTOS09)

</div>