from sqlite3 import *

con = None
try:
	con = connect("employee.db")
	print("database created/opened")
	cursor = con.cursor()
	sql = "create table employee(id int primary key, name text, salary int)"
	cursor.execute(sql)
	print("table created")
except Exception as e:
	print("issue", e)
finally:
	if con is not None:
		con.close()
		print("closed")