import mysql.connector
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ruan81527733",
    database="sakila"
)
cursor = conexao.cursor()
cursor.execute("SELECT title, rental_rate FROM film")
movies = cursor.fetchall()

import math
caros = []
baratos = []
for movie in movies:
    titulo = movie[0]
    price = movie[1]

    if price > 2.99:
        caros.append(titulo)
    else:
        baratos.append(titulo)

print(f'Filmes caros: {len(caros)}')
print(f'Filmes baratos: {len(baratos)}')
print(f'Raiz do total: : {math.sqrt(len(movies)):.2f}')