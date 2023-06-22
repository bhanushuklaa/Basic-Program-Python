#WAP to find prime number using file_handling and Function

def getvalue():
    a = int(input("Enter a value :"))
    print("="*40)
    return a

def putvalue(a):
    flag = 0
    newfile = open("newprogram.py","w")
    print("Reading Prime Number....")
    print("="*40)
    for i in range(2,a+1):
        for j in range(2,i):
            if i%j==0:
                flag = 1
                break
            if flag==0:
                print(i)
            flag = 0
    newfile.close()

def readFile():
    file = open("newprogram.py","r")
    for x in file:
        print(x)
    file.close()

z = getvalue()
putvalue(z)
readFile()
