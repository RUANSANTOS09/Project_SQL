import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Ruan81527733",
    database="sakila"
)

cursor = connection.cursor()
query = """
SELECT *
FROM desempenho_funcionarios
ORDER BY total DESC
"""
cursor.execute(query)
employees = cursor.fetchall()
report = []
for position, (id, Nome, Sobrenome, Loja, total_alugueis, total) in enumerate(employees, start=1):
    full_name = f'{Nome} {Sobrenome}'.title()
    bonus = "Bônus aprovado" if total > 33000 else "Bonus reprovado"
    report.append(f'{position}. '
                        f'Nome: {full_name} | '
                        f'Identificação da Loja: {Loja} | '
                        f'Total de filmes alugados: {total_alugueis} | '
                        f'Total arrecadado: R${total} | '
                        f'{bonus}\n')

with open('desempenho_funcionarios.txt', 'w', encoding='utf-8') as file:
    file.writelines(report)

cursor.close()
connection.close()