import socket

UDP_IP_ADDRESS="192.168.43.83"
UDP_PORT_NO=6789

Message="Eclub"
#creating a socket
clientSock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
	clientSock.sendto(Message, (UDP_IP_ADDRESS,UDP_PORT_NO))
	#print("Sending")	
clientSock.close()
