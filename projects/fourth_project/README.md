# 🎬 Filtro de Filmes por Faixa de Preço

> Script que utiliza o operador SQL `BETWEEN` para filtrar filmes dentro de uma faixa específica de valor de aluguel, processando e exportando os resultados para um relatório em arquivo.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-7FB069?style=flat-square)
![Licença](https://img.shields.io/badge/Licença-MIT-4A5550?style=flat-square)

---

## 📖 Sobre o projeto

Este projeto demonstra o uso do operador `BETWEEN` do SQL para filtrar registros dentro de um intervalo de valores — uma alternativa mais legível do que combinar `>=` e `<=` manualmente.

A consulta filtrada é combinada com processamento em Python para gerar um relatório legível, seguindo o mesmo padrão de extração e documentação de dados já estabelecido nos projetos anteriores deste repositório.

---

## 🧠 Conceitos aplicados

| Conceito | Onde aparece no projeto |
|---|---|
| **Operador `BETWEEN`** | Filtragem de `rental_rate` dentro de uma faixa de valores |
| **Parâmetros múltiplos via `%s`** | Dois placeholders na mesma query, preenchidos por uma tupla de dois valores |
| **Desempacotamento de tupla** | `for title, rental_rate in movies:` |
| **Arredondamento de valores** | `round(rental_rate, 2)`, padronizando a exibição de valores monetários |
| **Acumulador** | Contagem total de filmes encontrados na faixa de preço |
| **Gerenciamento de contexto (`with`)** | Escrita do relatório em arquivo |

---

## 💻 Exemplo de uso

```python
command_sql = "SELECT title, rental_rate FROM film WHERE rental_rate BETWEEN %s and %s"
values = 2.99, 4.99
cursor.execute(command_sql, values)

# Saída em filmes_faixa_preco.txt:
# ACADEMY DINOSAUR - R$ 2.99
# ACE GOLDFINGER - R$ 4.99
#
# Quantidade de filmes: 538
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

- [ ] Permitir que a faixa de preço seja informada pelo usuário via `input()`
- [ ] Ordenar os resultados por valor de aluguel
- [ ] Calcular o valor médio dos filmes dentro da faixa filtrada

---

## 👤 Autor

Projeto desenvolvido como parte de estudos pessoais em **SQL, Python e Engenharia de Dados**.