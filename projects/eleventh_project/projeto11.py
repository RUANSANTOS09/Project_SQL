import mysql.connector
connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Ruan81527733',
    database = 'sakila'
)
cursor = connection.cursor()
query_film = """
SELECT
    fil.film_id,
    fil.title,
    s.store_id,
    inv.inventory_id
FROM film fil
JOIN inventory inv
     ON fil.film_id = inv.film_id
JOIN store s
     ON inv.store_id = s.store_id
WHERE s.store_id = %s
ORDER BY fil.title
LIMIT %s
"""
values = (1,20)
cursor.execute(query_film, values)
inv_film = cursor.fetchall()
inventory_movies = []
register_count = 0
for film_id, title ,store_id, inventory_id in inv_film:
    inventory_movies.append(f'{inventory_id} | {title} - Loja {store_id}\n')
    register_count += 1
inventory_movies.append(f'\nTotal Registros: {register_count}')

with open('inventario_loja.txt', 'w', encoding = 'utf-8') as f:
    f.writelines(inventory_movies)

cursor.close()
connection.close()