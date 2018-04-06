#To Find Factors of Numbers
def Factors(x):

    print("The Factors of ", x ,"are : ")
    for i in range(1,x+1):
        if x % i == 0:
            print(i)


num=int(input("Enter the number of those whose factors you want to remove : "))
print(Factors(num))
