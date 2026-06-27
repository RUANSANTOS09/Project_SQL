import mysql.connector
message = []
count_customers = 0
connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Ruan81527733',
    database = 'sakila'
 )
cursor = connection.cursor()
value_entered_by_user = str(input('Digite uma letra: '))

command_sql = "SELECT first_name, last_name, email FROM customer WHERE first_name LIKE %s "
values = (value_entered_by_user + '%',)
cursor.execute(command_sql,values)
customers = cursor.fetchall()
for first_name, last_name, email in customers:
    full_name = f'{first_name} {last_name}'
    count_customers += 1
    message.append(f'{full_name} - {email}\n')
message.append(f'\n{count_customers} clientes cadastrados')

with open('clientes_por_letra.txt', 'w', encoding='utf-8') as c:
    c.writelines(message)

cursor.close()
connection.close()