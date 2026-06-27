

import mysql.connector
message = []
count_address = 0
connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Ruan81527733',
    database = 'sakila'
)
cursor = connection.cursor()
command_sql = "SELECT address_id,address , address2 FROM address WHERE address2 IS NULL"
cursor.execute(command_sql)
addresses = cursor.fetchall()
for address_id, address, address2 in addresses:
    message.append(f'ID {address_id}: {address}\n')
    count_address += 1
message.append(f'\nQuantidade de endereços nulos: {count_address}')

with open('enderecos_incompletos.txt', 'w', encoding='utf-8') as e:
    e.writelines(message)

cursor.close()
connection.close()