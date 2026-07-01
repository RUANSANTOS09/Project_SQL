import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Ruan81527733",
    database="sakila"
)
cursor = connection.cursor()
query_customer = """
SELECT
    cus.first_name,
    cus.last_name,
    fil.title,
    ren.rental_date
FROM customer cus
JOIN rental ren
    ON cus.customer_id = ren.customer_id
JOIN inventory inv
    ON inv.inventory_id = ren.inventory_id 
JOIN film fil
    On inv.film_id = fil.film_id
WHERE cus.customer_id = %s
ORDER BY ren.rental_date DESC
LIMIT %s
"""
values = (1,10)
cursor.execute(query_customer, values)
history_customer = cursor.fetchall()
list_history = []
history_total = 0
for position, (first_name, last_name, title, rental_date) in enumerate(history_customer, start = 1):
    full_name = f'{first_name} {last_name}'.strip()
    list_history.append(f'{position}. {full_name} - {title} - {rental_date}\n')
    history_total += 1
list_history.append(f'\nQuantidade total: {history_total}')

with open('historico_alugueis.txt', 'w', encoding='utf-8') as f:
    f.writelines(list_history)

cursor.close()
connection.close()