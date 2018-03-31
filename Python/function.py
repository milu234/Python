#Menu driven program to find faftorial recursion reverse and pallindrome
def factorial(n):
    if (n==0):
        return 1
    else:
        return (n*factorial(n-1))

def reverse(str):
        str=str[::-1]
        return str

def Armstrong(num):
    order = len(str(num))
    add=0
    temp=num
    while(temp>0):
        digit=temp%10
        add=add+(digit**order)
        temp=temp//10
    if(num==add):
        print("The number is armstrong")
    else:
        print("The number is not armstrong")

def Pallindrome(str):
    if(str==reverse(str)):
        print("The given string is pallindrome")
    else:
        print("The given string is not pallindrome")

def Prime(num1):
    flag=1
    for i in range(2,num1):
        if(num1%i==0):
            flag=0
            break
    if(flag==1):
        print(num1,"is Prime ")
    else:
        print(num1,"is not Prime")

def Fibo(a,b,n):
    print(a,b,end=" ")
    while(n-2):
        c=a+b
        a=b
        b=c
        print(c,end=" ")
        n=n-1



ch=0
while ch!=7:
    print("\n\n1 : Factorial")
    print("2 : Reverse")
    print("3 : Fibonacci")
    print("4 : Check Armstrong")
    print("5 : Check Pallindrome")
    print("6 : Check Prime")
    print("7 : Exit")
    ch=int(input("Enter Your choice : "))
    if (ch==1):
        a=int(input("Enter the number to find the factorial : "))
        print("The Factorial of the num is : ",factorial(a))
    elif(ch==2):
        b=input("Enter the string to reverse the : ")
        print("The reversed string is : ",reverse(b))
    elif(ch==3):
        c=int(input("Enter the number till which you want to find the Fibonacci series : "))
        Fibo(0,1,c)
    elif(ch==4):
        d=int(input("Enter the number to check the number is armstrong or not"))
        Armstrong(d)
    elif(ch==5):
        e=input("Enter the string to check whether the number is pallindrome or not")
        Pallindrome(e)
    elif(ch==6):
        f=int(input("Enter the number to check the number is Prime or not :"))
        Prime(f)
    elif(ch==7):
        print("You are Being Logged out......")
    else:
        print("You have selected a wrong choice!!!")
