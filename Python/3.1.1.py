class Employee:
    pass
    raise_amount = 1.04
    num_of_employees = 0
    def __init__(self,first,last,pay,yoj):
        self.first = first
        self.last = last
        self.pay = pay
        self.yoj = yoj
        self.email =  yoj + '.' + first + '.' + last + '@ves.ac.in'

        Employee.num_of_employees += 1

    def fullname(self):
        return '{} {} '.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay*Employee.raise_amount)

emp1 = Employee('Milan','Hazra',5000,'2016')

print(Employee.fullname(emp1))
emp1.raise_amount = 1.05

print(Employee.num_of_employees)

print(Employee.raise_amount)
print(emp1.raise_amount)
