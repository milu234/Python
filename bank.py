#Write a mneu driven Program for banking system

class AccountP(object):
    def __init__(self, name, account_number, initial_amount, pack):
        self._name = name
        self._no = account_number
        self._balance = initial_amount
        self._p = pack

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def get_balance(self):
        return self._balance

    def compute_interest(self,amount,t,r):
        self._p = self._balance
        self._p = ((self._p*t*r)/100)
        return self._p
#Main program

import random
ch=1
p=0
p=random.randint(101,999)
while ch!=7:
    print("\n\n****************************************************")
    print("Welcome to the Bank of Wadiya")
    print("****************************************************")

    print("\n1 : Create Account")
    print("2 : Deposit")
    print("3 : Withdraw")
    print("4 : Rate of interest")
    print("5 : Display Balance")
    print("6 : Display Account Details")
    print("7 : Exit")
    ch=int(input("\nEnter Your Choice :"))
    if(ch==1):
        a1 = AccountP(input("Enter name : "),int(p),int(input("Enter the initial amount :")),print())
        print("Account created Successfuly")

    elif(ch==2):
        a1.deposit(int(input("Enter the amount you want to deposit : ")))
        print("The total balance of the customer is : ",a1._balance)
    elif(ch==3):
        a1.withdraw(int(input("Enter the amount to be withdrawn : ")))
        print("The available balance is : ",a1._balance)
    elif(ch==4):
        a1.compute_interest(a1._p,int(input("Enter the rate of no 0f years : ")),int(input("Enter the rate of interest : ")))
        print("The rate of interestis : " ,a1._p)

    elif(ch==5):
        print("The balance in the account is : Rs.",a1.get_balance())
    elif(ch==6):
        print("Name      : ",a1._name)
        print("Account No: ",p)
    elif(ch==7):
        print("LOGGING OUT......")
    else:
        print("Wrong Choice!!!!")
