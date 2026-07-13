import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Ruan81527733",
    database="mechanic",
    charset="utf8mb4"
)

cursor = connection.cursor()
query = """
SELECT *
FROM high_revenue_mechanics
"""
cursor.execute(query)
mechanics = cursor.fetchall()
report = []
total_register = len(mechanics)
for position, (_, name, total) in enumerate(mechanics, start=1):
    report.append(f'{position}. Nome: {name} | Faturamento R${total:.2f}\n')
report.append(f'\nTotal registro: {total_register}')

with open('high_revenue_mechanics.txt', 'w', encoding = 'utf-8') as file:
    file.writelines(report)

cursor.close()
connection.close()