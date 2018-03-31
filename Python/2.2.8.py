# To Make a simple Calculator
def add(x,y):
    return x+y


def subtract(x,y):
    return x-y


def multiply(x,y):
    return x*y



def division(x,y):
    return x/y


print("Select a Operation")
print("1. ADD")
print("2. Subtract")
print("2. Multiply")
print("2. Divide")


choice = input("Enter your choice(1/1/3/4):")

num1=int(input("Enter the first number : "))
num2=int(input("Enter your Second Numer:"))

if choice == '1':
    print("The Addition od"num1,"+",num2,"=",add(num1,num2))

elif choice == '2':
    print(num1,"-",num2,"=",subtract(num1,num2))

elif choice == '3':
    print(num1,"x",num2,"=",multiply(num1,num2))

else:
    print(num1,"/",num2,"=",division(num1,num2))
