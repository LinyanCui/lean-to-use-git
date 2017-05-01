import socket
import base64
from PIL import Image
from array import array
import io
import os
import select

HOST, PORT = "115.156.164.250",5085
savepath='/home/lycui/back_end/testIm.jpg'

#def run_detect(path,):
rece_size=1024
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
#inputs=[listen_socket]
request=''

print 'Serving HTTP on port %s ...' % PORT
while True:

	client_connection, client_address = listen_socket.accept()
	#received_size=0
	#while received_size
	#rs,ws,es = select.select([listen_socket],[],[])
	#print 'rs:',rs
	#for r in rs:
	#	if r is listen_socket:
	#		client_connection, client_address = listen_socket.accept()
	#		inputs.append(client_connection)

	#request=inputs[0]
	data = client_connection.recv(rece_size)
	#request2 = client_connection.recv(rece_size)
	#request3 = client_connection.recv(rece_size)
	#request4 = client_connection.recv(rece_size)
	while data:
		request +=data
		data = client_connection.recv(rece_size)
		#request = request1+request2+request3+request4

		#anz_paddings = (len(request) % 3)+1
		#if anz_paddings > 1:
		#	request += b'=' * anz_paddings
		#lens = len(request)  
		#lenx = lens - (lens % 4 if lens % 4 else 4)
		#request += "=" * ((4 - len(request) % 4) % 4)
		#request=request+'='

		
	print 'request:',request
	print 'length:',len(request)

	with open(savepath, "wb") as fh:
		#fh.write(base64.decodestring(request[:lenx]))
		fh.write(base64.decodestring(request))
	request=''

	count=100

	while count>0:
		count=count-1

	#request=request.strip('GET /')
	#request=request.strip(' ')
	#request=request.split(' HTTP/1.1')
	#print 'request2:\n',request[0]
	#image=Image.open(io.BytesIO(request[0]))
	#image.save(savepath)

	#image=open('test_im.jpg','wb').writre(''.decode(''))
	http_response = """\
	HTTP/1.1 200 OK

	Hello, World!
	"""
	ht

	client_connection.sendall(http_response)
	client_connection.close()