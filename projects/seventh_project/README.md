# 🎬 Catálogo de Filmes Premium

> Script que combina expressões regulares e paginação de resultados para gerar um catálogo segmentado dos filmes mais caros de um conjunto específico de títulos — simulando uma demanda real de marketing por segmentação de catálogo.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-7FB069?style=flat-square)
![Licença](https://img.shields.io/badge/Licença-MIT-4A5550?style=flat-square)

---

## 📖 Sobre o projeto

Este projeto simula uma demanda comum em times de marketing e produto: gerar um **catálogo segmentado** de itens com base em um critério textual (neste caso, a letra inicial do título), priorizando os de maior valor e limitando a quantidade de resultados exibidos — como aconteceria em uma vitrine de produtos em destaque.

O projeto combina três operadores SQL distintos numa única consulta — `REGEXP` para o filtro de padrão, `ORDER BY` para priorização, e `LIMIT` para paginação — demonstrando como múltiplas cláusulas podem ser empilhadas de forma coerente em uma consulta real.

---

## 🧠 Conceitos aplicados

| Conceito | Onde aparece no projeto |
|---|---|
| **Operador `REGEXP`** | Filtro de títulos que começam com `A`, `B` ou `C`, usando alternância (`\|`) e âncora de início (`^`) |
| **Ordenação (`ORDER BY ... DESC`)** | Priorização dos filmes de maior valor de aluguel |
| **Paginação (`LIMIT`)** | Restrição do resultado aos 8 itens mais relevantes, recebido como parâmetro |
| **Ordem correta de cláusulas SQL** | `WHERE` → `ORDER BY` → `LIMIT`, sequência exigida pela sintaxe do SQL |
| **Parâmetro seguro via `%s`** | O valor do `LIMIT` é passado como parâmetro, e não concatenado na string |
| **Arredondamento de valores monetários** | `round(rental_rate, 2)` |
| **Acumulador e geração de relatório** | Contagem de itens processados, com escrita em arquivo via `with` |

---

## 💻 Exemplo de uso

```python
command_sql = "SELECT title, rental_rate FROM film WHERE title REGEXP '^A|^B|^C' ORDER BY rental_rate DESC LIMIT %s"
values = (8,)
cursor.execute(command_sql, values)

# Saída em catalogo_premium.txt:
# AFRICAN EGG - R$ 4.99
# ALABAMA DEVIL - R$ 4.99
# ...
#
# TOTAL: 8
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

- [ ] Tornar as letras iniciais do filtro configuráveis via `input()`
- [ ] Implementar paginação real, permitindo navegar entre "páginas" do catálogo
- [ ] Adicionar a categoria do filme ao relatório (quando `JOIN` for incorporado ao repositório)

---

## 👤 Autor

Projeto desenvolvido como parte de estudos pessoais em **SQL, Python e Engenharia de Dados**.