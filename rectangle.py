class rectangle():
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):
        return self.breadth*self.length
#a=int(input("Enter length of rectangle: "))
#b=int(input("Enter breadth of rectangle: "))
obj=rectangle(10,5)
print("Area of rectangle:",obj.area())
 
print()