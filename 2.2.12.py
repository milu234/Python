#To find Sum of all Natural numbers using reccursion
def sum(n):


    if n <= 1:
        return n;
    else:
        return n +sum(n-1)


num=int(input("Enter the number of terms to be added : "))

if num < 0:
    print("Enter a positive Number : ")
else:
    print("The Sum is ",sum(num))
