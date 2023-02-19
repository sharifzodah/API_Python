from BackEndAutomation.utils.configurations import *

conn = establish_DB_Connection()
cursor = conn.cursor()
cursor.execute('select * from ecmf_deal')
data = dict(zip(cursor.column_names, cursor.fetchone()))
columns = list(cursor.column_names)

