#WAP to convert the number from decimal to binary using Reccursion
def Convert(n):
    if n > 1:
        Convert(n//2)
    print(n%2,end = ' ')

a=int(input("Enter the decimal number to conver into Binary : "))
Convert(a)
