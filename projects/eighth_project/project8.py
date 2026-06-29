import mysql.connector
message = []
count_payments = 0
count_staff1 = 0
count_staff2 = 0
connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Ruan81527733',
    database = 'sakila'
)
cursor = connection.cursor()
command_sql = "SELECT staff_id, customer_id, amount FROM payment WHERE amount > %s ORDER BY amount desc LIMIT %s"
values = (7,15)
cursor.execute(command_sql, values)
payments = cursor.fetchall()
for staff_id, customer_id, amount in payments:
    message.append(f'Funcionário {staff_id} | Cliente {customer_id} | R$ {round(amount,2)}\n')
    count_payments += 1

    if staff_id == 1:
        count_staff1 += 1
    else:
        count_staff2 += 1

message.append(f'\nTotal de Pagamentos: {count_payments}')
message.append(f'\nTotal de Pagamentos, pertencentes ao funcionario 1: {count_staff1}')
message.append(f'\nTotal de Pagamentos, pertencentes ao funcionario 2: {count_staff2}')

with open('auditoria_funcionarios.txt', 'w', encoding='utf-8') as a:
    a.writelines(message)

connection.close()
cursor.close()