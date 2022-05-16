import socket

host = str(input("server ip: "))
type = int(input("port type, 0=UDP and 1=TCP: "))
port = int(input("port number: "))
bufferSize = 1024
if (type==1):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((host,port))
    sock.sendall(b'client ok')
    string = str(sock.recv(bufferSize))
    print("server msg:" + string)
else:
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.sendto(b'client msg' , (host,port))
    msgPair = sock.recvfrom(bufferSize)
    clientMsg = msgPair[0]
    address = msgPair[1]
    print("msg = " + str(clientMsg) + "; address = " + str(address))

sock.close()
print("--programm ended--")