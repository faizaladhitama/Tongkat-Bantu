import math
import random
from socket import *


serverPort = int(input("Masukkan port : "))
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
server_db = dict()
while 1:
	connectionSocket, addr = serverSocket.accept()
	try:
		sentence = connectionSocket.recv(1024)
		print("Connection success....")
		output=sentence.decode()
		print(output)
		output+="\r\n"
		connectionSocket.send(output.encode())
		print("Connection end....")
		connectionSocket.close()
	except:
		print("Connection was aborted by Client")
