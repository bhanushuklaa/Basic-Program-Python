#import _Database
#from sqlite3 import Cursor, connect
import MySQLdb
conn = MySQLdb.connect(host='localhost', database='bhanudb', user='root', password='Qwert12345#@')
cursor = conn.cursor()
cursor.execute("select * from student")
row = cursor.fetchone()
while row is not None:
    print(row)
    row = cursor.fetchone()
cursor.close()
conn.close() 