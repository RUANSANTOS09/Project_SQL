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
    cus.customer_id as ID,
    cus.first_name as FirstName,
    cus.last_name as LastName,
    adr.district as District,
    SUM(amount) as Total,
    COUNT(amount) as Quantidade
FROM payment pay
JOIN customer cus using(customer_id)
JOIN address adr
    ON cus.address_id = adr.address_id
GROUP BY cus.customer_id
HAVING Total > %s and Quantidade > %s
ORDER BY Total DESC
"""
values = (130,30)
cursor.execute(query_report,values)
report = cursor.fetchall()
final_report = []
classification_ouro = 0
classification_prata = 0
for position, (ID, FirstName, LastName, District, Total, Quantidade) in enumerate(report, start=1):
    full_name = f'{FirstName} {LastName}'.title()
    if Total > 180:
        classification = 'Ouro'
        classification_ouro += 1
    elif Total >= 130:
        classification = 'Prata'
        classification_prata += 1

    final_report.append(f'{position}. {classification} {full_name} | Região: {District} | Total: {Total} | Compras: {Quantidade}\n')
final_report.append(f'\nTotal de clientes Ouro: {classification_ouro}\nTotal de clientes Prata: {classification_prata}')

with open('clientes_premium_regiao.txt', 'w', encoding='utf-8') as f:
    f.writelines(final_report)

cursor.close()
connection.close()