import mysql.connector
# ============================================================
# PIPELINE DE DADOS — LOCADORA SAKILA
# Extração, validação, segmentação e cruzamento de dados
# ============================================================



# ── Conexão com o banco de dados ──────────────────────────
connection = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    passwd = 'Ruan81527733',
    database = 'sakila'
)
cursor = connection.cursor()


# ============================================================
# PARTE 1 — Extração e limpeza de clientes ativos
# ============================================================
query_clean_data = """
SELECT first_name,last_name, email 
FROM customer
WHERE active = %s 
  AND email IS NOT NULL
ORDER BY last_name
"""
values = (1,)
cursor.execute(query_clean_data,values)
customers = cursor.fetchall()

data_cleanup_valid_clients = []
data_cleanup_invalid_clients = []
valid_clients = 0
invalid_clients = 0

for first_name, last_name, email in customers:
    full_name = f'{first_name} {last_name}'.strip().title()
    clean_email = email.strip()
    if '@' in email and '.' in email:
       valid_clients += 1
       data_cleanup_valid_clients.append(f'{full_name} - @{clean_email}\n')
    else:
       invalid_clients += 1
       data_cleanup_invalid_clients.append(f'{full_name}\n')

data_cleanup_valid_clients.append(f'\nTotal de clientes válidos: {valid_clients} ')
data_cleanup_invalid_clients.append(f'\nTotal de clientes inválidos: {invalid_clients} ')

with open('clientes_validos.txt', 'w', encoding='utf-8') as f_valid:
    f_valid.writelines(data_cleanup_valid_clients)

with open('clientes_invalidos.txt', 'w', encoding='utf-8') as f_invalid:
    f_invalid.writelines(data_cleanup_invalid_clients)

# ============================================================
# PARTE 2 — Segmentação de pagamentos por faixa de valor
# ============================================================

query_payment = """
SELECT customer_id, staff_id, amount 
FROM payment
WHERE amount BETWEEN %s and %s
ORDER BY amount DESC
LIMIT %s 
"""
values_payment = (5,11,50,)
cursor.execute(query_payment, values_payment)
payments = cursor.fetchall()

message_payment_segmentation = []
category_low = 0
category_medium = 0
category_high = 0

for customer_id, staff_id, amount in payments:
    if amount <= 7:
        category = 'Baixo'
        category_low += 1
    elif amount <= 9:
        category = 'Médio'
        category_medium += 1
    else:
        category = 'Alto'
        category_high += 1
    message_payment_segmentation.append(
        f'Cliente {customer_id} | Funcionário  {staff_id} '
        f'| R$ {amount} | Faixa: {category}\n'
)
message_payment_segmentation.append(
    f'\nTotal de vendas baixas: {category_low}'
    f'\nTotal de vendas médias: {category_medium}'
    f'\nTotal de vendas altas: {category_high}'
)

with open('segmentacao_pagamentos.txt', 'w', encoding='utf-8') as f_segmentation:
    f_segmentation.writelines(message_payment_segmentation)

# ============================================================
# PARTE 3 — Relatório cruzado com JOIN triplo
# ============================================================

query_report = """
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
cursor.execute(query_report, values_report)
cross_report = cursor.fetchall()

message_report = []
total_register = 0

for position, (first_name, last_name, amount, address) in enumerate(cross_report, start = 1):
    full_name = f'{first_name} {last_name}'.strip().title()
    message_report.append(f'{position}. {full_name} - R$ {amount} - {address}\n')
    total_register += 1
message_report.append(f'\nTotal de registros: {total_register} ')

with open('report.txt', 'w', encoding='utf-8') as f_report:
    f_report.writelines(message_report)

# ── Encerramento da conexão ────────────────────────────────
cursor.close()
connection.close()