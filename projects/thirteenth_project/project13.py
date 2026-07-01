import mysql.connector
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Ruan81527733',
    database = 'sakila'
)
cursor = connection.cursor()
query_category = """
SELECT
    cat.name,
    fil.title,
    pay.amount
FROM payment pay
JOIN rental ren
     ON pay.rental_id = ren.rental_id
JOIN inventory inv
     ON ren.inventory_id = inv.inventory_id
JOIN film fil
     ON inv.film_id = fil.film_id
JOIN film_category fca
     ON fil.film_id = fca.film_id
JOIN category cat
     ON fca.category_id = cat.category_id
WHERE pay.amount > %s
ORDER BY pay.amount DESC
LIMIT %s
"""
values = (3,15)
cursor.execute(query_category, values)
report = cursor.fetchall()
list_report = []
total_report = len(report)
for position, (category_name, title, amount) in enumerate(report):
    list_report.append(f'{position}. {category_name} | {title} | R$ {amount}\n')
list_report.append(f'\nTotal: {total_report}')

with open('receita_por_categoria.txt', 'w', encoding = 'utf-8') as f:
    f.writelines(list_report)

cursor.close()
connection.close()