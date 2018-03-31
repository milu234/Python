#To find Hcf of the given number
def computeHCF(x,y):


    while (y):
        x,y=y,x % y
    pass
    return x


num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))

print("The Hcf of ",num1,"and" ,num2, "is ",computeHCF(num1,num2))
