n=int(input("Enter the number of terms : "))
result = list(map(lambda x: 2**x,range(n)))


print("The total number of terms are : ",n)
for i in range(n):
    print("2^",i,"=",result[i])
