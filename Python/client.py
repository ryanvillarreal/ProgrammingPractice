import socket
import sys

HOST, PORT = "http://localhost", 4444
data = " ".join(sys.argv[1:])

# Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try: 
	#connect to server and send data
	sock.connect((HOST,PORT))
	sock.sendall(data + "\n")

	# now recieve data from the server and shutdown 
	recieved = sock.recv(1024)
finally: 
		sock.close()

print "Sent:	{}".format(data)
print "recieved    {}".format(recieved)
