import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Ruan81527733",
    database="delivery",
    charset="utf8mb4"
)

cursor = connection.cursor()
query = """
SELECT *
FROM high_revenue_restaurants
"""
cursor.execute(query)
restaurants = cursor.fetchall()
report = []
total_register = len(restaurants)
for position, (_, name, total, Quantidade_total) in enumerate(restaurants, start=1):
    report.append(f'{position}. Nome do restaurante: {name} | Faturamento total: R${total:.2f} | Quantidade de pedidos: {Quantidade_total}\n')
report.append(f'\n Total de registros: {total_register}')
with open('high_revenue_restaurants.txt', 'w', encoding='utf-8') as file:
    file.writelines(report)

cursor.close()
connection.close()
