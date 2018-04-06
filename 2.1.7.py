#To find the factorial of a given number
num=int(input("Enter the number to find the facorial : "))
factorial=1
if(num<0):
 print("You need to enter a positive number!!")
elif(num==0):
 print("Out of your curiousity the factorial is 1 ")
else:
 for i in range(1,num+1):
 	factorial=factorial*i

print("Well The factorial of ",num,"is",factorial)