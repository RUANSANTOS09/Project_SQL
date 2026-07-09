import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Ruan81527733",
    database="sakila"
)

cursor = connection.cursor()
query_report_rental = """
SELECT *
FROM filmes_mais_alugados
LIMIT %s
"""
cursor.execute(query_report_rental, (20,))
report_rental = cursor.fetchall()
final_report = []
for position, (id, titulo, mais_alugados) in enumerate(report_rental):
    final_report.append(f'Titulo: {titulo} | Total alugados: {mais_alugados}\n')
final_report.append(f'\nTotal de filmes: {len(final_report)}')

with open('management_views.txt', 'w', encoding='utf-8') as f:
    f.writelines(final_report)

cursor.close()
connection.close()