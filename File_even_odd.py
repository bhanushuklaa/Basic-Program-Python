# Print all the even odd number using FIle handling and function

def  getvalue():
    a = int(input("Enter a value...."))
    return a

def putvalue(a):
    file1 = open("even.py","w")
    file2 = open("odd.py","w")
    for x in range(1,a+1):
        if x%2==0:
            file1.write(x)
        else:
            file2.write(x)
    file1.close()
    file2.close()
    
def readFile():
    file1 = open("even.py","r")
    file2 = open("odd.py","r")
    print("Reading even number....")
    for x in file1:
        print(x)
    print("Reading Odd number....")
    for y in file2:
        print(y)
    file1.close()
    file2.close()
    
result = getvalue()
putvalue(result)
readFile()
    