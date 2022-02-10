# import socket module
from cgi import test
from multiprocessing import connection
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  #Prepare a server socket
  serverSocket.bind(("", port))
  serverSocket.listen(1)
  while True:
    #Establish the connection
    # print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    # print("test")
    try:
      try:
        print("in first try")
        message = connectionSocket.recv(1024).decode(set)
        filename = message.split()[1]
        f = open(filename[1:])
        # print(f)
        outputdata = f.read()
        # print(outputdata)
        
        #Send one HTTP header line into socket.
        connectionSocket.send("200 OK".encode())

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
          connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
      except IOError:
        # Send response message for file not found (404)
        message_not_found = "404 not found"
        connectionSocket.send((message_not_found.upper()).encode())
        
        #Close client socket
        connectionSocket.close()

    except (ConnectionResetError, BrokenPipeError):
      pass

  serverSocket.close()
  sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)
