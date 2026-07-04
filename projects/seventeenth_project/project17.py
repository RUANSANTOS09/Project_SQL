import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Ruan81527733",
    database="sakila"
)

cursor = connection.cursor()
query_report = """
SELECT
    cus.customer_id as ID,
    cus.first_name as first_name,
    cus.last_name as last_name,
    sum(amount) as total_paid,
    count(amount) as quantity_of_purchases
FROM payment pay
JOIN customer cus using(customer_id)
WHERE amount > %s
GROUP BY ID
ORDER BY total_paid DESC
LIMIT %s
"""
values = (1,20)
cursor.execute(query_report, values)
report = cursor.fetchall()
final_report = []
vip_clients = 0
regular_customers = 0
for position, (ID, first_name, last_name, total_paid, quantity_of_purchases) in enumerate(report, start=1):
    if total_paid > 150:
        classification = 'VIP'
        vip_clients += 1
    else:
        classification = 'REGULAR'
        regular_customers += 1

    full_name = f'{first_name} {last_name}'
    final_report.append(
        f'{position}. {full_name} | Total: R${total_paid:.2f} | Pagamentos: {quantity_of_purchases} | {classification}\n')
final_report.append(f'\nTotal de Clientes VIPs: {vip_clients}\nTotal de Clientes REGULAR: {regular_customers}')

with open('top_clientes.txt', 'w', encoding='utf-8') as top_clientes:
    top_clientes.writelines(final_report)

cursor.close()
connection.close()