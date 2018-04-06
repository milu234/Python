#Dictionary contains both key and value
my_dict={}	#Empty Dictionary
my_dict={1:'Potato',2:'Onion'}
print(my_dict)
my_dict={'Name':'Milan','Middlename':'Loknath','Lastname':'Hazra'}
print(my_dict)
my_dict={1:[12,13],2:(5,6)}
print(my_dict)
#my_dict={[(1,'apple'),(2,'Adam')]}		#You will get an error of unhashable list
my_dict={'Name':'Milan','Middlename':'Loknath','Lastname':'Hazra'}
print(my_dict['Name'])
print(my_dict['Lastname'])
my_dict={'Name':'Milan','Middlename':'Loknath','Lastname':'Hazra','Age':26}

print(my_dict)

a={'Name':'Milan','Middlename':'Loknath','Lastname':'Hazra','Age':26}
b=a.copy()
print(b)
print(a.get('Name'))
print(a.fromkeys('Name'))
print(a.items())
print(a.keys())
print(a.pop('Name'))
print(a)
print(a.popitem())
print(a.setdefault('Lastname'))
#print(a.update('Middlename'))

marks={}.fromkeys(['Maths','English','Science'],0)
print(marks)
print(marks)
squares={1:1,2:4,3:9,4:16,5:25,6:36,7:49,9:81}
print(squares)
print(1 in squares)
print(2 in squares)
for i in squares:
	print(squares[i])
	print(all(squares))

print(any(squares))
print(len(squares))
#print(cmp(squares,my_dict))
print(sorted(squares))

