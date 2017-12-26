import json
import math
import random
from socket import *


serverPort = int(input("Masukkan port : "))
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
data={"a":1,"b":2,"c":3}
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
while 1:
	connectionSocket, addr = serverSocket.accept()
	try:
		sentence = connectionSocket.recv(1024)
		print("Connection success....")
		output=sentence.decode()
		print(output)
		dataJSON = json.dumps(data)
		output+="\r\n"
		connectionSocket.send(dataJSON.encode())
		print("Connection end....")
		connectionSocket.close()
	except:
		print("Connection was aborted by Client")
