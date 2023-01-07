import mysql.connector
from BackEndAutomation.utils.configurations import *
# host, database, user, password
conn = establish_DB_Connection()
print(conn.is_connected())
cursor = conn.cursor()
cursor.execute('select * from CustomerInfo')
row = cursor.fetchone()     # returns tuple data type
print(row)
print(row[3])

allRows = cursor.fetchall()     # returns list of tuples
print(allRows)

conn.close()

# Terminal command to install mysql connector: pip install mysql-connector-python
