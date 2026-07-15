import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Ruan81527733",
    database="animal_adoption_center",
    charset="utf8mb4"
)

cursor = connection.cursor()
query = """
SELECT * FROM animals_available
"""
cursor.execute(query)
animals_available = cursor.fetchall()
report = []
total_register = len(animals_available)
for position, (_, Nome, especie, situation) in enumerate(animals_available, start=1):
    report.append(f'{position}. Espécie: {especie} | Nome : {Nome} | Situação : {situation}\n')
report.append(f'\nTotal de registros: {total_register}')

with open('animals_available.txt', 'w', encoding='utf-8') as file:
    file.writelines(report)

cursor.close()
connection.close()