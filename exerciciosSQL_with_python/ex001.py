import mysql.connector
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Ruan81527733",
    database="sakila"
)
cursor = conexao.cursor()
# Rodar um SELECT
cursor.execute("SELECT first_name, last_name FROM actor")

# Guardar os resultados numa lista
actors = cursor.fetchall()

#Percorrer com FOR
for actor in actors:
    print(actor)
conexao.close()