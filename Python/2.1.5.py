#To Check the number is prime or not
a=int(input("Enter the Number:"))
k=0
for i in range(2,a//2+1):
	if(a%i==0):
		k=k+1
if(k<=0):
	print(" The Number you have eneterd  is Prime")
else:
	print("The Number you kave enetered  is not prime")