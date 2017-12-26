import json
import math
import random
from socket import *

"""
serverPort = int(input("Masukkan port : "))
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
"""
print('The server is ready to receive')
"""
data=[{"a":1,"b":2,"c":3,"d":4},{"a":1,"b":2,"c":3,"d":4},{"a":1,"b":2,"c":3,"d":4}]
with open('data.json', 'w') as outfile:
	json.dump(data, outfile)
"""
data=[{"a":1,"b":2,"c":3,"d":4}]
counter = 0;
while 1:
	if len(data) == 10:
		data.pop(0)
	data.append({"a":1,"b":2,"c":3,"d":4})
	if counter==1000000:
		with open('data.json', 'w') as outfile:
			json.dump(data, outfile)
		counter = 0
	counter+=1
	"""
	if counter==1000000:
		with open('data.json', 'w') as outfile:
			json.dump(data, outfile)
		counter = 0
	data.append({"a":1,"b":2,"c":3,"d":4})
	counter+=1
	print(counter)
	"""
	"""
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
	"""
