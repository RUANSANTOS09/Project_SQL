import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Ruan81527733",
    database="sakila"
)

cursor = connection.cursor()
query_report = """
SELECT *
FROM top_filmes_aluguel
ORDER BY copias DESC
LIMIT %s
"""
cursor.execute(query_report, (20,))
report = cursor.fetchall()
final_report = []
for position, (Id, title, rental_rate, copias) in enumerate(report, start=1):
    final_report.append(f'Titulo: {title} | Rental: {rental_rate} | Copias: {copias}\n')
final_report.append(f'\nTotal de filmes: {len(report)}')

with open('top_filmes_aluguel.txt', 'w', encoding='utf-8') as f:
    f.writelines(final_report)

cursor.close()
connection.close()

