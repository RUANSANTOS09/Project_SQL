message = []
count_movies = 0
import mysql.connector
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Ruan81527733',
    database='sakila'
)
cursor = connection.cursor()
command_sql = "SELECT title, rental_rate from film WHERE title REGEXP '^A|^B|^C' ORDER BY rental_rate DESC LIMIT %s "
values = (8,)
cursor.execute(command_sql, values)
movies = cursor.fetchall()
for title, rental_rate in movies:
    message.append(f'{title} - R$ {round(rental_rate,2)}\n')
    count_movies += 1
message.append(f'\nTOTAL: {count_movies}')

with open('catalogo_premium.txt', 'w', encoding='utf-8') as c:
    c.writelines(message)

connection.close()
cursor.close()