#To print all prime numbers in a given range
lower = int(input("Enter the starting Point : "))
upper=int(input("Enter the Ending point : "))

print("So the Prime numbers between ",lower, "and",upper, "is : ")

for num in range(lower,upper+1):
	if num>1:
		for i in range(2,num):
			if(num % i)==0:
				break
		else:
			print(num)