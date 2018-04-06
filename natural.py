#Find the sum of natural number susing Recurssion
def Rec(n):
    if (n<=1):
        return n
    else:
        return (n+Rec(n-1))

a=int(input("Enter the no. of naturalnumbers you want to find the sum : "))
print(Rec(a))
