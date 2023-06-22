"""class Parent:
    def mymethod(self):
        print("Calling Parent Class")
class Child:
    def mymethod(self):
        print("Calling Child Class")
c=Child()
c.mymethod()
d=Parent()
d.mymethod()"""


class Parent:
    parentattr=100
    def __init__(self):
        print("Calling parent class Constructor")
    def parent_method(self):
        print("Calling parent method")
    def setAttr(self,atr):
        Parent.parentattr=atr
    def get_attr(self):
        print("Parent Attr = ",Parent.parentattr)
class Child(Parent):
    def __init__(self):
        print("Calling Child Constructor")
    def child_method(self):
        print("calling child method")
c = Child()
c.child_method
c.parent_method()
c.setAttr(100)
c.get_attr()
