import mysql.connector
count_customer = 0
message = []
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ruan81527733",
    database= "sakila"
)
cursor = connection.cursor()
command_sql = "SELECT first_name, last_name, email FROM customer WHERE active = %s ORDER BY last_name;"
values = (1,)
cursor.execute(command_sql,values)
customers = cursor.fetchall()
for first_name, last_name, email in customers:
    count_customer += 1
    full_name = first_name + ' ' + last_name
    message.append(f'{full_name.title()} - {email}\n')
message.append(f'\nTotal de costumers: {count_customer}')

with open('relatorio_clientes_ativos.txt', 'w', encoding='utf-8') as report:
    report.writelines(message)
    for v in message:
        print(v, end='')

cursor.close()
connection.close()
