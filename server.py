import socket

host='localhost'
port=12345
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
c,addr=s.accept()
print("Connection from client: ",str(addr))
while True:
	data=c.recv(1024)
	if not data:
		break
	print("From client :"+str(data.decode()))
	data1=input("Enter response:")
	c.send(data1.encode())
c.close()
