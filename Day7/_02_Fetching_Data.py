import mysql.connector
from BackEndAutomation.utils.configurations import *

conn = establish_DB_Connection()
print(conn.is_connected())
cursor = conn.cursor()
cursor.execute('select * from CustomerInfo')
rows = cursor.fetchall()
print(type(rows))
print(rows)

sum_total = 0
for row in rows:
    sum_total += row[2]

print(sum_total)

# Updating data in Table
query = "update CustomerInfo set Location = %s where CourseName = %s"
data = ("CA", "Jmeter")
cursor.execute(query, data)
conn.commit()

# Deleting data from Table
query = "delete from CustomerInfo where CourseName = 'WebServices'"
cursor.execute(query)
conn.commit()

# Inserting new data into Table
query = "insert into CustomerInfo values(\"WebServices\", current_date(), 65, 'Africa');"
cursor.execute(query)
conn.commit()

conn.close()
