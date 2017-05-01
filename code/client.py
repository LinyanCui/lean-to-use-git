import socket
from base64 import b64encode

HOST, PORT = "115.156.164.250",5087
im="/home/lycui/back_end/1.jpg"

BUFFER_SIZE=1024
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)

with open(im,'rb') as imF:
	data=imF.read()
	imInfo=b64encode(data)

print "Start connect"
sock.connect(server_address)
sent_size=0
tmp=0

#sock.send(str(len(imInfo)))
if False:	
	while sent_size<len(imInfo):
		remained_size=len(imInfo)-sent_size
		send_size = BUFFER_SIZE if remained_size > BUFFER_SIZE else remained_size	
		send_file=imInfo[tmp:send_size]
		tmp=send_size
		sent_size += send_size
		sock.send(send_file)

sock.sendall(imInfo)

sock.close()
print "Closing connect"


