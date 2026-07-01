import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Ruan81527733",
    database= 'sakila'
)
cursor = connection.cursor()
query = """
SELECT
     stf.first_name,
     stf.last_name,
     str.store_id,
     address
FROM staff stf
JOIN store str
     ON stf.store_id = str.store_id
JOIN address adr
     ON str.address_id = adr.address_id
ORDER BY stf.first_name
"""
cursor.execute(query)
result_staff = cursor.fetchall()
report_staff = []
total_staff = len(result_staff)
for first_name,last_name, store_id, address in result_staff:
    full_name = f'{first_name} {last_name}'.strip().title()
    report_staff.append(f'{full_name} - Loja {store_id} - {address}\n')
report_staff.append(f'\nTotal: {total_staff}')
with open("funcionarios_lojas.txt", "w", encoding = 'utf-8') as f:
    f.writelines(report_staff)

cursor.close()
connection.close()