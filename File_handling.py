"""fo = open("database_connection.py","r+")
str = fo.read(10)
print(str)
fo.close"""

fo = open("module.py","r+")
str = fo.read(10)

print("read the string : ",str)
position = fo.tell

print("Current position",position)
position = fo.seek(0,0)
str = fo.read(10)

print("Again read string ",str)
fo.close()