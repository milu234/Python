# To print sum of all natural  numbers
num=int(input("Enter the number till where you want to find the sum of all natural numbers: "))

if num<0:
	print("Yeah of course natural numbers only no integers please!!!")
else:
	sum=0

	while(num>0):
		sum+=num
		num-=1

print("The Sum of the given natural  numbers are:",sum)