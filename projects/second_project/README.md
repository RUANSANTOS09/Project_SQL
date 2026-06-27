# 💲 Classificador de Filmes por Faixa de Preço

> Script que conecta a um banco de dados MySQL, classifica filmes em categorias de preço (caros e baratos) e aplica uma operação matemática sobre o volume total de dados processados.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-7FB069?style=flat-square)
![Licença](https://img.shields.io/badge/Licença-MIT-4A5550?style=flat-square)

---

## 📖 Sobre o projeto

Este projeto simula uma tarefa comum de classificação de dados: separar registros em categorias com base em uma regra de negócio simples — neste caso, **filmes acima ou abaixo de um valor de aluguel de referência**.

Diferente do projeto anterior, que apenas exibia os dados retornados pelo banco, aqui o foco está em **processar e segmentar** os resultados em Python, aplicando lógica condicional sobre cada registro e consolidando contagens por categoria.

O projeto também introduz o uso do módulo `math`, aplicando uma operação estatística simples sobre o volume total de dados processados.

---

## 🧠 Conceitos aplicados

| Conceito | Onde aparece no projeto |
|---|---|
| **Conexão e consulta SQL** | `mysql.connector`, `cursor.execute()`, `fetchall()` |
| **Acesso a tupla por índice** | `movie[0]`, `movie[1]` — extração de título e preço de cada registro |
| **Estrutura condicional** | `if/else`, classificando cada filme como caro ou barato |
| **Listas como acumuladores** | `caros.append()` e `baratos.append()`, segmentando os dados por categoria |
| **Módulo `math`** | `math.sqrt()`, calculando a raiz quadrada do total de registros processados |
| **Formatação de números** | `:.2f`, exibindo o resultado com duas casas decimais |

---

## 💻 Exemplo de uso

```python
cursor.execute("SELECT title, rental_rate FROM film")
movies = cursor.fetchall()

# Classificação:
# rental_rate > 2.99  →  filme caro
# rental_rate <= 2.99 →  filme barato

# Saída:
# Filmes caros: 325
# Filmes baratos: 675
# Raiz do total: : 31.62
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

- [ ] Tornar o valor de referência (`2.99`) configurável, em vez de fixo no código
- [ ] Calcular o valor médio de aluguel por categoria
- [ ] Exportar a classificação completa para um arquivo de relatório

---

## 👤 Autor

Projeto desenvolvido como parte de estudos pessoais em **SQL, Python e Engenharia de Dados**.