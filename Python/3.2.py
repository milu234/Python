# write a program to demonstrate the constructors

#constructors
class ComplexNumber:
    def __init__(self,r=0,i=0):
        self.real= r
        self.imag= i
    def getData(self):
        print("{0}+{1}j".format(self.real,self.imag))

c1 = ComplexNumber(5,6)
print(c1.getData())

#Python non-parameterized constructor
class Student:
    def __init__(self):
        print("This is non-parametrized Constructors")
    def show(self,name):
        print("Hello",name)

student = Student()
student.show("Milan")

#parametrized Constructors

class Student:
    def __init__(self,name):
        print("This is the parametrized Constructors")
        self.name = name
    def show(self):
        print("Hello",self.name)

student = Student("Milan")
print(student.show())
