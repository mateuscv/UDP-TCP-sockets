from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("localhost", serverPort))
serverSocket.listen(1)

print("The server is ready to receive")

while True:
    connectionSocket, addre = serverSocket.accept() #socket especif. p cada iteração
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()