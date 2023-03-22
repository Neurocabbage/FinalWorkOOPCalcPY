import socket

def client_program():
    try:
        host = socket.gethostname()  # as both code is running on same pc
        port = 5000  # socket server port number

        client_socket = socket.socket()  # instantiate
        client_socket.connect((host, port))  # connect to the server

        message = input("Enter an expression: ")  # take input

        while message.lower().strip() != 'end':
            client_socket.send(message.encode())  # send message
            data = client_socket.recv(1024).decode()  # receive response

            print('Message from server: ' + data)  # show in terminal

            message = input("Enter an expression: ")  # again take input

        client_socket.close()  # close the connection
    except Exception as e:
        print("Unknown client error")


if __name__ == '__main__':
    client_program()