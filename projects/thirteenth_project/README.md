# 🎭 Receita por Categoria de Filme

> Script que rastreia a receita gerada por categoria de filme, percorrendo o caminho completo entre pagamento e classificação do conteúdo através de seis tabelas relacionadas — o JOIN mais complexo do repositório até o momento.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-7FB069?style=flat-square)
![Licença](https://img.shields.io/badge/Licença-MIT-4A5550?style=flat-square)

---

## 📖 Sobre o projeto

Este projeto responde a uma pergunta de negócio real: **qual categoria de filme gera mais receita?** Para chegar nessa resposta, é preciso percorrer um caminho longo no banco de dados — do pagamento até a categoria, passando por aluguel, inventário, filme e tabela de relacionamento entre filme e categoria.

É o projeto com maior número de tabelas combinadas do repositório, e demonstra como uma pergunta aparentemente simples pode exigir uma query complexa quando os dados estão devidamente normalizados.

---

## 🧠 Conceitos aplicados

| Conceito | Onde aparece no projeto |
|---|---|
| **`JOIN` com seis tabelas** | `payment` → `rental` → `inventory` → `film` → `film_category` → `category` |
| **Ordem correta dos JOINs** | Cada tabela deve ser declarada antes de ser referenciada numa condição `ON` |
| **`ORDER BY` + `LIMIT`** | Top 15 pagamentos de maior valor, priorizando receita |
| **`len()` como acumulador** | Contagem direta do total de resultados sem necessidade de `+= 1` no loop |
| **`enumerate()` com desempacotamento interno** | Numeração de registros combinada com desempacotamento de três valores |

---

## 🏗️ Caminho do JOIN

```
payment
   └── rental              (rental_id = rental_id)
         └── inventory      (inventory_id = inventory_id)
               └── film      (film_id = film_id)
                     └── film_category  (film_id = film_id)
                               └── category  (category_id = category_id)
```

---

## 💻 Exemplo de saída

```
1. Sports | SMOOCHY CONTROL | R$ 11.99
2. Drama  | DOGMA FAMILY    | R$ 10.99
...

Total: 15
```

---

## ▶️ Como executar

```bash
python main.py
```

**Pré-requisitos:** Python 3.10+, `mysql-connector-python`, banco `sakila` configurado localmente.

---

## 🚀 Próximos passos

- [ ] Agrupar por categoria e somar a receita total de cada uma (`GROUP BY` + `SUM`)
- [ ] Comparar receita por categoria entre as duas lojas da rede
- [ ] Visualizar o resultado em gráfico usando `matplotlib`

---

## 👤 Autor

Projeto desenvolvido como parte de estudos pessoais em **SQL, Python e Engenharia de Dados**.