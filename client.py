
import socket
host='localhost'

port=12345
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
str=input("Enter data:")

while str!='exit':
    s.send(str.encode())
    data=s.recv(1024)
    data=data.decode()
    print("From server:"+data)
    str=input("Enter data: ")
s.close()
