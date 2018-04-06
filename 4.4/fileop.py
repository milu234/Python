reclen=20
with open("cities.bin",'wb') as f:
    n=int(input("Number of entries:-"))
    for i in range(n):
        city=input("Enter city name:")
        ln=len(city)
        city=city+(reclen-ln)*''
        city=city.encode()
        f.write(city)
