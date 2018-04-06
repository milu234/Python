import pickle
class Student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def display(self):
        print(self.name,"\t",self.rollno,"\t",self.marks)
with open("student.dat",'wb') as f:
    n=int(input("How many students?"))
    for i in range(n):
        name=input("Enter name of student")
        rollno=int(input("Enter rollno of student"))
        marks=int(input("Enter marks of student"))
        s=Student(name,rollno,marks)
        #pickle operation
        pickle.dump(s,f)


#Unpickle operation
f1=open('student.dat','rb')
print("Student Details:")
while True:
    try:
        obj = pickle.load(f1)
        obj.display()
    except EOFError:
        print("All students details displayed.....")
        break
f1.close()
