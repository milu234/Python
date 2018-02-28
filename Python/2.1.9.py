#To print the fibonnacci series
num=int(input("Enter the number of the terms you want to print : "))

n1=0
n2=1
count=0

if(num<0):
	print("You Gotaa be kidding me !! thats a negative!!")
elif num==1:
	print("Fibonacci sequence upto",num,":")
	print(n1)
else:
	print("Fibonacci sequence upto",num,":")
	while count<num:
		print(n1,end=' , ')
		nth=n1+n2
		n1=n2
		n2=nth
		count+=1
		