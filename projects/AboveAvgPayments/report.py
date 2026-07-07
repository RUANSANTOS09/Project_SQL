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
    cus.customer_id as id,
    cus.first_name as name,
    cus.last_name as lastname,
    amount
FROM payment as pay
JOIN customer cus USING(customer_id)
WHERE amount > (
      SELECT AVG(amount)
      FROM payment
)
ORDER BY amount DESC
LIMIT %s
"""
cursor.execute(query_report, (20,))
report = cursor.fetchall()
final_report = []
high_rating = 0
medium_rating = 0
for position, (id, name, lastname, amount) in enumerate(report, start=1):
    full_name = f'{name} {lastname}'.title()
    if amount > 8:
        classification = 'Alto'
        high_rating += 1
    else:
        classification = 'Médio'
        medium_rating += 1
    final_report.append(f'{position}. {full_name} | R${amount:.2f} | {classification}\n')
final_report.append(f'\nTotal de pagamentos altos: {high_rating}\nTotal de pagamentos médios: {medium_rating}')

with open('pagamentos_acima_media.txt', 'w', encoding='utf-8') as f:
    f.writelines(final_report)

cursor.close()
connection.close()