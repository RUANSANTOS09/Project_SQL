import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Ruan81527733",
    database="sakila"
)

cursor = connection.cursor()
query_dashboard = """
SELECT *
FROM clientes_premium
ORDER BY Total DESC
LIMIT %s
"""
cursor.execute(query_dashboard, (15,))
report = cursor.fetchall()
total_customers = len(report)
final_report = []
for position, (Id, Name, Sobrenome, Total) in enumerate(report):
    full_name = f'{Name} {Sobrenome}'.title()
    final_report.append(f'{position}. {full_name} | R${Total:.2f}\n')
final_report.append(f'\nTotal de clientes: {total_customers}')

with open('dashboard_vendas.txt', 'w', encoding='utf-8') as f:
    f.writelines(final_report)

cursor.close()
connection.close()