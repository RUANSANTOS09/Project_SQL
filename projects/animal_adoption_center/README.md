<div align="center">

# 🐾 Centro de Adoção de Animais

> "Ausência de correspondência também é informação — se você souber perguntar do jeito certo."

![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-success?style=for-the-badge)

</div>

---

## 📌 Sobre o projeto

Modelagem de banco para um centro de adoção de animais, com o desafio central de identificar registros **sem correspondência** em outra tabela — introduzindo `LEFT JOIN` pela primeira vez no repertório de projetos.

---

## 🗂️ Estrutura do banco

```
┌──────────────┐        ┌──────────────────┐        ┌──────────────┐
│   animals      │◀───────│    adoptions       │───────▶│   adopters     │
│  (animais)     │  1:N   │ (registro de adoção) │  N:1   │  (adotantes)   │
└──────────────┘        └──────────────────┘        └──────────────┘
```

**Decisão de design:** nem todo animal tem uma linha correspondente em `adoptions` — só quem já foi adotado. Isso exige `LEFT JOIN` (em vez do `INNER JOIN` padrão) para não perder os animais ainda disponíveis na consulta.

---

## 🧠 Tabelas

- **`animals`** — animais cadastrados (nome, espécie, idade, sexo)
- **`adopters`** — adotantes, com `email` único
- **`adoptions`** — registro de adoção realizada; `adoption_date` é `NOT NULL`, já que toda linha aqui representa uma adoção que de fato aconteceu

---

## 🧠 View de negócio: `animals_available`

```sql
create or replace view animals_available as
select
    anm.animals_id as Id,
    anm.name as Nome,
    anm.species as Especie,
    case
    	when adoption_date is null then 'Disponível'
    else
       'Adotado'
    end as situation
from animals anm
left join adoptions using(animals_id)
where adoption_date is null;
```

**Conceito central: `LEFT JOIN`**

Diferente do `INNER JOIN` (que só traz linhas com correspondência nas duas tabelas), o `LEFT JOIN` traz **todas** as linhas da tabela à esquerda (`animals`), preenchendo com `NULL` os campos de `adoptions` quando não existe adoção correspondente. É esse `NULL` que o `WHERE adoption_date IS NULL` usa para filtrar apenas os animais disponíveis.

---

## 🐍 Script Python

`report.py` consulta a view e gera relatório `.txt` numerado com espécie, nome e situação de cada animal disponível.

- Conexão única com `charset="utf8mb4"`
- `_` para ignorar o `Id` no unpacking da tupla
- Contagem de registros via `len()`

**Saída:** `animals_available.txt`

---

## 💡 Conceitos praticados

- `LEFT JOIN` para capturar registros sem correspondência
- `IS NULL` aplicado sobre resultado de `LEFT JOIN` (padrão comum para "encontrar o que falta")
- `CASE WHEN` para classificação condicional
- Modelagem de relacionamento opcional (nem todo animal tem uma adoção)

---

<div align="center">

**Ruan Santos** · [GitHub](https://github.com/RUANSANTOS09)

</div>