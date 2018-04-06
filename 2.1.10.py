#To check whether the given number is armstrong number or not
num =int(input("Enter the numberyou want to check for armstrong or not : "))

sum=0

temp=num
while temp>0:
	digit = temp%10
	sum+=digit**3
	temp//=10


if num==sum:
	print(num,"is an armstrong number")
else:
	print(num,"is not an armstrong number")

	