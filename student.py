class Student:
    cnt = 0
    def __init__(self, rollno, name, course,sem,address):
        self.rollno = rollno
        self.name = name
        self.course = course
        self.sem = sem
        self.address = address
        print("The objects are....",Student.cnt)
        Student.cnt += 1
    def getdata(self):
        rollno = input("Enter a rol no...")
        