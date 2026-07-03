import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ruan81527733",
    database="sakila"
)
cursor = connection.cursor()
query_backup = """ 
CREATE TABLE language_backup AS
SELECT * FROM language
"""


query_update_language = """
UPDATE language
SET name = 'South Korean'
WHERE language_id = %s
"""
connection.commit()
values = (20,)
cursor.execute(query_update_language, values)

query_report = """
SELECT * FROM language
"""
cursor.execute(query_report)
report = cursor.fetchall()
final_report = []
final_total = len(report)
for language_id, name, last_update in report:
    final_report.append(f'{language_id} | {name}\n')
final_report.append(f'\nTotal de linguas: {final_total}\n')

with open('relatorio_idiomas.txt', 'w', encoding='utf-8') as f:
    f.writelines(final_report)