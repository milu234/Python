
#Inheritance
class Car:  #parent class
    def print_car_name(self):
        print("This is a  Car")
        return "Nothing"

class Sedan(Car):   #Child class
    def print_model_name(self):
        print("This is the  Brand")
        return "Nothing"

    def print_car_name(self): #method override
        print("Well , i am trying to override the car....")
        return "Something which is not polluted..."

buy = Sedan()
print(buy.print_car_name())
print(buy.print_model_name())

#polymorphism

class Car:
    def drive(self):
        print("ok,so i am still driving a car ")
        return "CNG"

    def accident(self):
        print("i got crashed")
        return "Hospital bills"

class Truck:
    def drive(self):                #Overloading
        print("I am driving too")
        return "Smoke"
    def accident(self):             #Overloading
        print("i am kinda crashing others")


car = Car()
truck = Truck()

print(car.drive)
print(car.accident)
print(truck.drive)
print(truck.accident)
