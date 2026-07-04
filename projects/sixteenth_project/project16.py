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
    staff_id,
    MAX(amount) as max_payment,
    MIN(amount) as min_payment,
    AVG(amount) as average_payment,
    SUM(amount) as total_collected
FROM payment
WHERE amount > %s
group by staff_id
"""
values = (2,)
cursor.execute(query_report, values)
report = cursor.fetchall()
total_staff = len(report)
final_report = []
for staff_id, max_payment, min_payment, average_payment, total_collected in report:
    clean_data = round(average_payment,2)
    final_report.append(
        f'Funcionário {staff_id} | Maior: R${max_payment} | Menor R${min_payment} |'
        f' Média: {clean_data} | Total: {total_collected}\n'
    )
final_report.append(f'\nTotal de funcionários: {total_staff}')

with open('desempenho_funcionarios.txt', 'w', encoding='utf-8') as file:
    file.writelines(final_report)

cursor.close()
connection.close()