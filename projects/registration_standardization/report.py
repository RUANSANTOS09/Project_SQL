import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Ruan81527733",
    database="sakila",
    charset="utf8mb4"
)

cursor = connection.cursor()
query = """
SELECT
    id,
    nome,
    sobrenome,
    email,
    dominio_email,
    status_cadastro
FROM padronização_cadastro
"""
cursor.execute(query)
customers = cursor.fetchall()
report = []
total_register = len(customers)
for (id, nome, sobrenome, email, dominio_email, status_cadastro) in customers:
    full_name = f'{nome} {sobrenome}'
    report.append(f'ID: {id} | '
                  f'Nome: {full_name} | '
                  f'Email: {email} | '
                  f'Domínio: {dominio_email} | '
                  f'Status do cadastro: {status_cadastro}\n')
report.append(f'\nTotal de registros: {total_register}')
with open('registration_standardization.txt', 'w', encoding='utf-8') as f:
    f.writelines(report)

cursor.close()
connection.close()