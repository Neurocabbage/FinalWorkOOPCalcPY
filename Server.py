import socket
from math import *
import logging

def server_program():
    try:
        # get the hostname
        host = socket.gethostname()
        port = 5000  # initiate port no above 1024

        server_socket = socket.socket()  # get instance
        # look closely. The bind() function takes tuple as argument
        server_socket.bind((host, port))  # bind host address and port together
        print("Server started, waiting for connection....")

        # configure how many client the server can listen simultaneously
        server_socket.listen(2)
        conn, address = server_socket.accept()  # accept new connection
        print("Connection from: " + str(address))
        while True:
            # receive data stream. it won't accept data packet greater than 1024 bytes
            data = conn.recv(1024).decode()
            if data == "end":
                # if data is not received break
                break
            print("We got the expression: " + str(data))
            # data = input(' -> ')
            # conn.send(data.encode())  # send data to the client

            res = eval(str(data))
            print("Expression result= " + str(res))
            conn.send(str(res).encode())

        conn.close()  # close the connection
    except Exception as e:
        print("Unknown server error")


if __name__ == '__main__':
    server_program()