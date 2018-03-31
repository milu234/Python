#Python Program to dispaly fibonacci sequence using reccursive function
def rec(n):


    if n<=1:
        return n
    else:
        return(rec(n-1)+rec(n-2))


nterms=int(input("Enter the Number of terms : "))

if nterms <= 0:
    print("Please enter a positive number !!")
else:
    print("Fibonacci sequence :")
    for i in range(nterms):
        print(rec(i))
