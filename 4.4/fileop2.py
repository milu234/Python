import os
reclen=20
size=os.path.getsize('cities.bin')
print("Size of file={} bytes".format(size))
n=int(size/reclen)
with open("cities.bin",'r+b') as f:
    name=input("Enter city name")
    name=name.encode()
    newname=input("Enter new name")
    ln=len(newname)
    newname=newname+(20-n)*''
    newname=newname.encode()
    position=0
    found='false'
    for i in range(n):
        f.seek(position)
        str=f.read(20)
        if name in str:
            f.seek(-20,1)
            f.write(newname)
        position+=reclen

    if not found:
        print("City not found")
