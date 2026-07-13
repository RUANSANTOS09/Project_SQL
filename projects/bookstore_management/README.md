<div align="center">

# 📚 Modelagem de Banco — Livraria (Bookstore)

> "Dado bem modelado é a diferença entre consultar e adivinhar."

![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-success?style=for-the-badge)

</div>

---

## 📌 Sobre o projeto

Modelagem de banco de dados para uma livraria, cobrindo relacionamento entre autores e livros via Foreign Key, tipos de dado apropriados para dinheiro e datas, e evolução de schema com `ALTER TABLE`.

---

## 🗂️ Estrutura do banco

```
┌──────────────┐        ┌──────────────┐
│   authors     │───────▶│    books      │
│ (autores)     │  1:N   │  (livros)     │
└──────────────┘        └──────────────┘
```

---

## 🧠 Tabelas

### `authors`
```sql
create table authors(
    author_id int not null auto_increment,
    name varchar(255) not null,
    nationality varchar(255) not null,
    primary key (author_id)
);

alter table authors add birth_date date;
```

### `books`
```sql
create table books(
    book_id int not null auto_increment,
    title varchar(255) not null,
    price decimal(10,2) not null,
    authors_id int not null,
    primary key (book_id),
    foreign key (authors_id) references authors(author_id)
);

alter table books add stock int;
```

---

## 🔍 Decisões de tipo de dado

| Coluna | Tipo | Motivo |
|---|---|---|
| `price` | `DECIMAL(10,2)` | Dinheiro exige precisão exata — `FLOAT` introduz erros de arredondamento em cálculos |
| `birth_date` | `DATE` | Só o dia importa (nascimento não precisa de hora) — evitado `DATETIME` por ser dado desnecessário |
| `stock` | `INT` | Quantidade inteira de exemplares em estoque |

---

## 💡 Conceitos praticados

- `CREATE TABLE` com `PRIMARY KEY` e `FOREIGN KEY`
- `ALTER TABLE ADD` para evoluir schema após criação
- Escolha correta de tipo de dado (`DECIMAL` vs `FLOAT`, `DATE` vs `DATETIME`)
- `INSERT INTO` respeitando ordem de dependência de Foreign Key
- `UPDATE ... SET ... WHERE` para popular colunas adicionadas posteriormente

---

<div align="center">

**Ruan Santos** · [GitHub](https://github.com/RUANSANTOS09)

</div>