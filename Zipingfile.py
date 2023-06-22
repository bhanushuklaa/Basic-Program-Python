#A python program to compress the contents of files.
"""from zipfile import*

f = ZipFile("code.zip", "w", ZIP_DEFLATED)

f.write("calendar.py")
f.write("File_handling.py")
f.write("student.py")

print("code.zip file created....")
f.close()

#z = ZipFile("code.zip","r")       to unzip files
#z.extractall("d:")"""
"""
list = [1,2,3,4,5,6,7]
z = [x**3 for x in list]
a = (x**3 for x in list)

print(a)
print(z)"""

"""list = [1,2,3,4,5,6]
z = (x**3 for x in list)
for k in range(6):              # for k in range(len(list)):
    print(next(z))"""
    
def table(n):
    for i in range(1,11):
        yield n*i
        i = i+1
for j in table(7):
    print(j)