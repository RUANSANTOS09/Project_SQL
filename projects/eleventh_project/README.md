# 🏪 Inventário de Filmes por Loja

> Script que cruza o acervo de filmes com o estoque físico de cada loja da rede, identificando quais títulos estão disponíveis em cada unidade — uma tarefa comum em operações de logística e reposição de estoque.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-7FB069?style=flat-square)
![Licença](https://img.shields.io/badge/Licença-MIT-4A5550?style=flat-square)

---

## 📖 Sobre o projeto

Este projeto simula uma demanda operacional real: saber exatamente quais cópias físicas de filmes estão disponíveis em cada loja da rede, cruzando o catálogo de filmes com o inventário e as lojas. É o tipo de consulta que alimenta sistemas de gestão de estoque e planejamento de reposição.

---

## 🧠 Conceitos aplicados

| Conceito | Onde aparece no projeto |
|---|---|
| **`JOIN` triplo com alias** | Combinação de `film`, `inventory` e `store` numa única consulta |
| **Filtro pós-junção (`WHERE`)** | Restrição ao `store_id` específico |
| **`ORDER BY` + `LIMIT`** | Ordenação por título e paginação dos resultados |
| **Parâmetros seguros via `%s`** | Valores passados como tupla, sem concatenação direta |
| **Acumulador de registros** | Contagem total de itens processados |

---

## 💻 Exemplo de saída

```
1 | ACADEMY DINOSAUR — Loja 1
2 | ACE GOLDFINGER — Loja 1
...

Total Registros: 20
```

---

## ▶️ Como executar

```bash
python main.py
```

**Pré-requisitos:** Python 3.10+, `mysql-connector-python`, banco `sakila` configurado localmente.

---

## 🚀 Próximos passos

- [ ] Comparar estoque entre as duas lojas da rede
- [ ] Identificar filmes sem nenhuma cópia disponível em estoque
- [ ] Exportar relatório em `.csv` para uso em planilhas

---

## 👤 Autor

Projeto desenvolvido como parte de estudos pessoais em **SQL, Python e Engenharia de Dados**.