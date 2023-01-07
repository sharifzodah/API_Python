import mysql.connector
from BackEndAutomation.utils.configurations import *

conn = establish_DB_Connection()
print(conn.is_connected())
cursor = conn.cursor()
cursor.execute('select * from Books')
allRows = cursor.fetchall()
print(type(allRows))
print(allRows)


# Updating data in Table
query = "update Books set Author = 'Abduhamid'"
cursor.execute(query)
conn.commit()
cursor.execute('select * from Books')
allRows = cursor.fetchall()
print(allRows)
conn.close()
