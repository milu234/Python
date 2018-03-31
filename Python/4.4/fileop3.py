import os
reclen=20
size=os.path.getsize('cities.bin')
n=int(size/reclen)
f1=open('cities.bin','rb')
f2=open('file2.bin','wb')
city=input("Enter city name to delete")
ln=len(city)
city=city+(reclen-ln)*''
city=city.encode()
for i in range(n):
	str=f1.read(reclen)
	if(str!=city):
		f2.write(str)
print("Record deleted")
f1.close()
f2.close()
os.remove("cities.bin")
os.rename("files2.bin","cities.bin")
