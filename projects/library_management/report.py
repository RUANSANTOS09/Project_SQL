import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Ruan81527733",
    database="library_management",
    charset="utf8mb4"
)

cursor = connection.cursor()
query = """
SELECT *
FROM overdue_book
"""
cursor.execute(query)
overdues_books = cursor.fetchall()
report = []
total_register = len(overdues_books)

for position, (_, name, due_date) in enumerate(overdues_books, start=1):
    report.append(f'{position}. Nome: {name} | Data prevista de entrega: {due_date}\n')
report.append(f'\nTotal de registros: {total_register}')

with open('overdues_report.txt', 'w', encoding='utf-8') as f:
    f.writelines(report)

cursor.close()
connection.close()