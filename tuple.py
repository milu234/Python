my_tuple=("Cat",[2,4,6],4,5)
print(my_tuple) 
my_tuple="Lion",3,5	#tuple can be created without preferences
print(my_tuple)			#also called tuple packing
x,y,z=my_tuple
print(x)
print(y)
print(z)
my_tuple=('m','i','l','a','n','l')
print(my_tuple[2])
print(my_tuple[-1])
print(my_tuple[-3])
n_tuple=("Hen",[2,4,6],(1,5,7))
print(n_tuple)
print(n_tuple[0][1])
print(my_tuple[1:4])
print(my_tuple[:-4])
print(my_tuple[:-1])
print(my_tuple[-5:])
print(my_tuple[:])

						#WE Cannot change element in the tuple ,we cannot update the tuple
						#We cannot even delete the elements in the tuple,we cannot add the elelments
print(my_tuple.count('l'))	#number of the elements in the whole world
print(my_tuple.index('n'))	#tells about the index about whwere the elemnts is present
print('a' in my_tuple)
print('b' in my_tuple)
print('b' not in my_tuple)
print('a' not in my_tuple);
 
							#for name in ('Milan','Abhishek'):
 							#print("Hello",name)
print(all(my_tuple))
print(any(my_tuple))
print(enumerate(my_tuple))
print(len(my_tuple))
print(max(my_tuple))
print(min(my_tuple))
print(sorted(my_tuple))
						#print(sum(int(my_tuple)))  valid only if the elements in the tuple





