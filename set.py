my_set={1,2,3}
print(my_set)
my_set={1.0,"Hello",(1,2,3)}
print(my_set)
my_set={1,2,3,43,2}
print(my_set)
a={}
print(type(a))
a=set(a)
print(type(a))
#print(my_set[0]) #set does not supports indexing
my_set.add(12)
print(my_set)
my_set.update([56,45,89])
print(my_set)
my_set.discard(12)
print(my_set)
my_set.remove(45)
print(my_set)
my_set=set("Hello Milan")
print(my_set)
my_set.pop()
print(my_set)
A={1,2,3,4,5,}
B={4,5,6,7,8,9}
print(A^B)
print(A.symmetric_difference(B))
print(B.symmetric_difference(A))
my_set=set("MILAN")
print('a' in my_set)
print('A' in my_set)
for letter in set("Milan"):
	print(letter)
	



