mylist=[] #emptylist
mylist=[1,2,3,4] #list of integers
print(mylist)
mylist=[1,"Heello",3.6]
print(mylist)
mylist=[1,[1,8,9,8,[1.89,87,],(4,5,6)]]	#nested list
print(mylist)
mylist=(1,2,5,[5,6],8)	#list inside the tuple
print(mylist)
a=["mouse",['a']];
print(a);
a=['maa','iiiiggggugg','l','a','n','h','a',['c','o']]
print(a[0])		#print first element of the list
print(a[2])		#print third element of the list
print(a[0][1])  #print the first elemnet of the zeroth element
print(a[1][4])	#print the fourth element of the first element
print(a[-1])
print(a[-5])
even=[1,2,4,6,8]   #mistake values
even[0]=0         #update the mistakes
print(even)
even.append(10)		#Append a element
print(even)
even.extend((10,12,14,16))	#extend a tuple or a list
print(even)
print(even+[17,18,20]) #other ways of appending
print(even*2);			#multiply the elemnts of the list
even.insert(1,6) 	#insrt elements in the list by giving index and value
print(even);
print(even[5:9]);  #display the eements in the middle
del even[2]; #delete one element that was 2 from the list
print(even);
del even[5:9] #delete multiple elements in the given range
print(even)
even.remove(8)
print(even)
print(even.pop(1)); #pop the given element 
print(even.pop());	#pop the last element
even.clear()  #delete all the element
print(even)
even=[1,2,4,6,8]
print(even)
even[:2]=[]			# delete the elemeentss
print(even)
print(even.index(6))  #find out the index
#print(even.sort())
even.sort()  #sort the elements in the ascending order
print(even)
even.reverse()		#reverse a string
print(even)
m=even.copy();
print(m)
pow2=[2**x for x in range(20)]
print(pow2)
pow2=[2**x for x in range(20) if x>5 and x<8]
print(pow2)
lastname=['Aswani','kulchandani','hotchandani','mulchandani']
print("%s" % lastname[1])
print("%s" % lastname[0][2])  






