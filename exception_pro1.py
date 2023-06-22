"""x = ""hello""

if not type(x) is int:
  raise TypeError("Only integers are allowed")


try:
  f = open("demofile.txt")
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()

x=10
y=8
assert x>y, 'X too small' 

a=False
while not a:
    try:
        f_n = input("Enter file name")
        i_f = open(f_n, 'r')
    except:
        print("Input file not found")


def f(x):
    yield x+1
    g=f(8)
    print(next(g))

def a():
    try:
        f('x', 4)
    finally:
        print('after f')
        print('after f?')
a()

def foo():
    try:
        print(1)
    finally:
        print(2)"""

import itertools
l1=(1, 2, 3)
l2=[4, 5, 6]
l=itertools.chain(l1, l2)
print(next(l1))