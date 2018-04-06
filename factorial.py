#WAP to find the factorial of the number using Reccursion
def factorial(n):
    if(n==0):
        return 1
    else:
        return(n*factorial(n-1))

a=int(input("Enter the number to find the factorial of the number: "))
print("The factorial of the number is : ",factorial(a))
