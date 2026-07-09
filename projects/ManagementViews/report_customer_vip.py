import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Ruan81527733",
    database="sakila"
)

cursor = connection.cursor()
query_report_vip = """
select *
from clientes_vip
"""
cursor.execute(query_report_vip)
report_vip = cursor.fetchall()
final_report_vip = []
for position, (id, name, sobrenome, total) in enumerate(report_vip, start=1):
    full_name = f'{name} {sobrenome}'.title()
    final_report_vip.append(f'{position}. Nome: {full_name} | total em compras: R${total}\n')
final_report_vip.append(f'\nTotal de registros: {len(report_vip)}')

with open('clientes_vip.txt', 'w', encoding='utf-8') as file:
    file.writelines(final_report_vip)

cursor.close()
connection.close()