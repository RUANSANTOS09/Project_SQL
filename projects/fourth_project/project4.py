message = []
count_movies = 0
import mysql.connector
connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Ruan81527733",
    database = "sakila"
)
cursor = connection.cursor()
command_sql = "SELECT title, rental_rate FROM film WHERE rental_rate BETWEEN %s and %s"
values = 2.99, 4.99
cursor.execute(command_sql, values)
movies = cursor.fetchall()

for title, rental_rate in movies:
    message.append(f'{title} - R$ {round(rental_rate,2)}\n')
    count_movies += 1
message.append(f'\nQuantidade de filmes: {count_movies} ')

with open ('filmes_faixa_preco.txt', 'w', encoding='utf-8') as price_range_movies:
    price_range_movies.writelines(message)

    for m in message:
        print(m, end='')

cursor.close()
connection.close()