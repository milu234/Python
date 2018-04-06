#Python Program to find the Lcm of two Numbers
def gcd(x,y):

    while(y):
        x, y = y, x % y

    return x

def lcm(x,y):


    lcm = (x*y)//gcd(x,y)
    return lcm

num1 = int(input("Enter the First Numer : "))
num2 = int(input("Enter the second Number: "))

print("The L.C.M of",num1,"and",num2,"is",lcm(num1, num2))
