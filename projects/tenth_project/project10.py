import mysql.connector

data_cleanup_valid_clients = []
valid_clients = 0 # Variavél acumuladora responsável por totalizar o numero de clientes validos

data_cleanup_invalid_clients = []
invalid_clients = 0  # Variavél acumuladora responsável por totalizar o numero de clientes invalidos

message_payment_segmentation = []
# Variavéis acumuladoras responsáveis por totalizar o numero de categorias de pagamentos, baixas, médias e altas
category_low = 0
category_medium = 0
category_high = 0

message_report = []

total_register = 0 # Variavél acumuladora responsável por totalizar o numero de Registros

connection = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    passwd = 'Ruan81527733',
    database = 'sakila'
)
cursor = connection.cursor()
# Extração e limpeza de clientes ativos

clean_data = """
SELECT first_name,last_name, email FROM customer
WHERE active = %s and email IS NOT NULL
ORDER BY last_name
"""
values = (1,)
cursor.execute(clean_data,values)
customers = cursor.fetchall()

for first_name, last_name, email in customers:
    full_name = f'{first_name} {last_name}'
    if '@' in email and '.' in email:
       valid_clients += 1
       data_cleanup_valid_clients.append(f'{full_name.strip().title()} - @{email.strip()}\n')
    else:
       invalid_clients += 1
       data_cleanup_invalid_clients.append(f'{full_name.strip().title()}\n')

data_cleanup_valid_clients.append(f'\nTotal de clientes válidos: {valid_clients} ')
data_cleanup_invalid_clients.append(f'\nTotal de clientes inválidos: {invalid_clients} ')

with open('clientes_validos.txt', 'w', encoding='utf-8') as f_valid:
    f_valid.writelines(data_cleanup_valid_clients)

with open('clientes_invalidos.txt', 'w', encoding='utf-8') as f_invalid:
    f_invalid.writelines(data_cleanup_invalid_clients)

# Segmentação de pagamentos por faixa de valor

command_sql_payment_segmentation = """
SELECT customer_id, staff_id, amount FROM payment
WHERE amount BETWEEN %s and %s
ORDER BY amount DESC
LIMIT %s 
"""
values_payment = (5,11,50,)
cursor.execute(command_sql_payment_segmentation, values_payment)
payments = cursor.fetchall()

for customer_id, staff_id, amount in payments:
    if amount >= 5 and amount <= 7:
        category = 'Baixo'
        category_low += 1
    elif amount >= 7.01 and amount <= 9:
        category = 'Médio'
        category_medium += 1
    else:
        category = 'Alto'
        category_high += 1
    message_payment_segmentation.append(f'Cliente {customer_id} | Funcionário  {staff_id} | R$ {amount} | Faixa: {category}\n')
message_payment_segmentation.append(f'\nTotal de vendas baixas: {category_low}\nTotal de vendas médias: {category_medium}\nTotal de vendas altas: {category_high}')

with open('segmentacao_pagamentos.txt', 'w', encoding='utf-8') as f_segmentation:
    f_segmentation.writelines(message_payment_segmentation)

# Relatório cruzado com JOIN
report = """
SELECT
    cus.first_name,
    cus.last_name,
    pay.amount,
    adr.address
FROM customer cus
JOIN payment pay
     ON cus.customer_id = pay.customer_id
JOIN address adr
     ON cus.address_id = adr.address_id
WHERE amount > %s and address IS NOT NULL
ORDER BY amount DESC
LIMIT %s
"""
values_report = (8,20)
cursor.execute(report, values_report)
cross_report = cursor.fetchall()

for position, (first_name, last_name, amount, address) in enumerate(cross_report, start = 1):
    full_name = f'{first_name} {last_name}'
    message_report.append(f'{position}. {full_name.strip().title()} - R$ {amount} - {address}\n')
    total_register += 1
message_report.append(f'\nTotal de registros: {total_register} ')

with open('report.txt', 'w', encoding='utf-8') as f_report:
    f_report.writelines(message_report)

cursor.close()
connection.close()