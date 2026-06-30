import mysql.connector
message = []
count_register = 0
connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Ruan81527733',
    database = 'sakila'
)
cursor = connection.cursor()
command_sql = "SELECT cus.first_name, cus.last_name, pay.amount, adr.address FROM customer cus JOIN payment pay ON cus.customer_id = pay.customer_id JOIN address adr ON cus.address_id = adr.address_id WHERE amount > %s"
values = (7,)
cursor.execute(command_sql, values)
reports = cursor.fetchall()

for first_name,last_name, amount, address in reports:
    full_name = f'{first_name} {last_name}'
    message.append(f'{full_name} - R$ {amount} - {address}\n')
    count_register += 1
message.append(f'\n{count_register} customers registered')

with open('relatorio_receita_clientes.txt', 'w', encoding='utf-8') as r:
    r.writelines(message)

connection.close()
cursor.close()