<div align="center">

# 🏋️ Modelagem de Banco — Academia (Gym)

> "Relacionamento bem modelado hoje é query simples amanhã."

![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-success?style=for-the-badge)

</div>

---

## 📌 Sobre o projeto

Modelagem de banco de dados para uma academia, com quatro entidades relacionadas: instrutores, aulas, alunos e matrículas. Destaque para a tabela `enrollments`, que conecta duas outras tabelas através de **duas Foreign Keys simultâneas**.

---

## 🗂️ Estrutura do banco

```
┌───────────────┐        ┌──────────────┐
│  instructors    │───────▶│   classes     │
│ (instrutores)   │  1:N   │  (aulas)      │
└───────────────┘        └──────┬───────┘
                                  │
                                  │ N:N (via enrollments)
                                  ▼
┌───────────────┐        ┌──────────────────┐
│    members      │───────▶│   enrollments      │
│  (alunos)       │  1:N   │  (matrículas)       │
└───────────────┘        └──────────────────┘
```

---

## 🧠 Tabelas

### `instructors`
```sql
create table instructors (
    instructors_id int not null auto_increment,
    name varchar(255) not null,
    specialty varchar(255) not null,
    primary key (instructors_id)
);
```

### `classes`
```sql
create table classes (
    class_id int not null auto_increment,
    class_name varchar(255) not null,
    duration_minutes int not null,
    instructor_id int not null,
    primary key (class_id),
    foreign key (instructor_id) references instructors (instructors_id)
);
```

### `members`
```sql
create table members (
    member_id int not null auto_increment,
    name varchar(255) not null,
    email varchar(255) not null,
    primary key (member_id)
);

alter table members
add constraint unique_email
unique(email);
```

### `enrollments`
```sql
create table enrollments(
    enrollments_id int not null auto_increment,
    member_id int not null,
    class_id int not null,
    enrollment_date date not null,
    primary key (enrollments_id),
    foreign key (member_id) references members(member_id),
    foreign key (class_id) references classes(class_id)
);
```

---

## 💡 Conceitos praticados

- `CREATE TABLE` com múltiplas `FOREIGN KEY` numa única tabela
- Modelagem de relacionamento N:N via tabela intermediária (`enrollments`)
- `ADD CONSTRAINT ... UNIQUE` para evitar duplicidade de e-mail
- `INSERT INTO` respeitando ordem de dependência entre quatro tabelas encadeadas

---

<div align="center">

**Ruan Santos** · [GitHub](https://github.com/RUANSANTOS09)

</div>