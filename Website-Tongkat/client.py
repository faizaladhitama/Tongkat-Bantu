from socket import *

serverIP = '127.0.0.1'
serverPort = 12345
clientSocket = socket(AF_INET, SOCK_STREAM)
connected = False
while not connected :
    try:
        clientSocket.connect((serverIP, serverPort))
        connected = True
    except:
        pass
sentence = input('Masukkan perintah:')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('From Server:', modifiedSentence.decode())
clientSocket.close()
