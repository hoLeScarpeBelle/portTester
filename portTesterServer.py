import socket

#port selection
type = int(input("type of port; 0 = UDP or 1 = TCP:"))
ip = "0.0.0.0" #non so perche ma per poter accedere al socket anche da l'esterno si deve mettere l'ip 0.0.0.0 il quale equivale a tutte le interfaccie
port = int(input("port:"))
bufferSize = 1024


if (type == 1 ):
    #TCP socket
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("--tcp server started--")
    sock.bind((ip,port))
    sock.listen()
    while True:
        conSock,addr = sock.accept()
        print("connection from " + str(addr))
        msg = conSock.recv(bufferSize)
        print("message recived = " + str(msg))
        conSock.sendall(b'thanks for the service')#ci vuole la b per dire che deve mandare la v come un insieme di byte
        conSock.close()

else:
    #UDP socket
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    print("--UDP server started--")
    sock.bind((ip,port))
    while(True):
        msgPair = sock.recvfrom(bufferSize)
        msg = msgPair[0]
        address = msgPair[1]
        print("msg = " + str(msg) + "; address = " + str(address))
        #sock.sendto(b"thanks for the service", ("127.0.0.1",port))
        sock.sendto(b"thanks for the service",address) 

sock.close()
input("--to close press enter--\n")