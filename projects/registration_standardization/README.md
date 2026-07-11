<div align="center">

# 📤 Consumo Python — Padronização de Cadastro (Sakila Rental)

> "Encoding errado é bug invisível: os textos parecem iguais até o banco discordar."

![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-success?style=for-the-badge)

</div>

---

## 📌 Sobre o projeto

Script Python que consome a view `padronização_cadastro` (criada no projeto de Funções de String) e gera um relatório `.txt` com os dados de clientes já tratados: nome em formato próprio, domínio de e-mail extraído e status de validação do cadastro.

---

## 🐛 Bug corrigido: encoding de conexão

O nome da view usa acentuação (`padronização_cadastro`). Ao consultar do Python, a conexão padrão do `mysql.connector` não força UTF-8, então os bytes enviados para o nome da view podiam divergir do que o MySQL tinha registrado — gerando erro de "tabela não encontrada" mesmo com o nome digitado corretamente.

**Correção:** parâmetro `charset="utf8mb4"` explícito na conexão.

```python
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Ruan81527733",
    database="sakila",
    charset="utf8mb4"
)
```

> **Nota técnica:** nomes de objetos de banco com acento são fonte recorrente desse tipo de problema. Recomendado usar apenas `a-z0-9_` em nomes de tabelas/views daqui pra frente, reservando acentuação só para o conteúdo dos dados.

---

## 🐍 Script

`report_padronizacao_cadastro.py` consulta a view, monta uma linha formatada por cliente (usando `' | '.join()` para separador consistente entre campos) e grava tudo em `.txt`.

- Conexão única (connection) com `charset="utf8mb4"`
- Contagem de registros via `len()`
- Separador de campos padronizado com `join()` em vez de concatenação manual
- Fechamento de `cursor` e `connection` no final

**Saída:** `padronização_cadastro.txt`

---

## 💡 Conceitos praticados

- Encoding de conexão MySQL (`charset`)
- Consumo de view via `mysql.connector`
- `str.join()` para concatenação limpa de múltiplos campos

---

<div align="center">

**Ruan Santos** · [GitHub](https://github.com/RUANSANTOS09)

</div>