import MySQLdb

conn  = MySQLdb.Connect(host='localhost', database= 'world', user= 'root', password= 'Asdf12345#@')

cursor = conn.cursor()
cursor.execute("select * from student")

row = cursor.fetchone()
while row is not None:
    print(row)
    row = cursor.fetchone()

cursor.close()
conn.close()