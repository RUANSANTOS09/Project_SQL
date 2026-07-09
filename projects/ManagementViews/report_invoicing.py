import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Ruan81527733",
    database="sakila"
)

cursor = connection.cursor()
query_report_invoicing = """
SELECT *
FROM faturamento_loja
ORDER BY total DESC
"""
cursor.execute(query_report_invoicing)
report_invoicing = cursor.fetchall()
final_report_invoicing = []
for position, (id, total) in enumerate(report_invoicing, start=1):
    final_report_invoicing.append(f'{position}. Numero de identificação da loja: {id} | Total de vendas: {total}\n')
final_report_invoicing.append(f'\nTotal de registros: {len(report_invoicing)}')

with open('faturamento_loja.txt', 'w', encoding='utf-8') as file:
    file.writelines(final_report_invoicing)

cursor.close()
connection.close()