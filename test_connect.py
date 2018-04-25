import socket

def test_connection(ip_address, port_number):
	sock = socket.socket()
	sock.settimeout(10)
	try:
		sock.connect((ip_address, int(port_number)))
		print("Connection to " + ip_address + ", port " + port_number + " successful!")
	except Exception as e:
		print("Unable to connect to " + ip_address + ", port " + port_number + " : " + str(e))
	finally:
		sock.close()

#Test connection to Google
test_connection("172.217.13.228", "445")
