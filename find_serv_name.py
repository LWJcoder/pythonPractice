import socket

def find_service_name():
	protocolname ='tcp'
	for port in [80, 25]:
		print "port: %s -> service name : %s" %(port, socket.getservbyport(port,protocolname))
	print "port: %s -> service name : %s" %(50, socket.getservbyport(50,'udp'))

if __name__ == '__main__':
	find_service_name()
