import mysql.connector
from utils.configurations import *

conn = establish_DB_Connection()
# print(conn.is_connected())
cursor = conn.cursor()
query = "select CourseName , Location from CustomerInfo where Location like \'Asia\'"
cursor.execute(query)
rows = cursor.fetchall()
print(rows)
conn.commit()

cursor.execute('select * from CustomerInfo')
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.commit()

conn.close()
