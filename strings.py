print("Hi Milan");
my_string="Milanhazra"
print(my_string[0]) 
print(my_string[-1])
print(my_string[-2])
print(my_string[1:3])
print(my_string[:3])
print(my_string[4:])
print(my_string[3:5])
print(my_string[:])
print(len(my_string)) #Find the length of the string
print(my_string*10) 	#will printthe statement 10times
print("Milan" in my_string) #find a substring in string
print("Nalim" in my_string)	
print(my_string.find("M"))	#Find the partricular word in the string
print(my_string.find("h"))
print(my_string.find("Milan"))	#Find the index in the particular string
print(my_string.count("a"))		#Find the word in the particular string and find the index
print(my_string.lower())		#Convert the string in lowwer case
print(my_string.upper())		#Convert the strin the in the upper case
print(my_string.replace("M","N")) #It will replace the M with the N
print(my_string.replace("lanhaz","****")) #It will get replace 
print(my_string.startswith("M"))
print(my_string.endswith("a"))
s="Merle"
s=s[:3]+"C"+s[4:]
print(s)
s=s.replace("M","P")
print(s)
