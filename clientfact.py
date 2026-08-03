import socket

HOST = "127.0.0.1"
PORT = 1235


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((HOST, PORT))

    print("Connected to Server Factorielle")

    while True:
        number = input("Enter a number  ")


        client_socket.send(number.encode("utf-8"))

        response = client_socket.recv(1024)
        print(response.decode("utf-8"))

    client_socket.close()


if __name__ == "__main__":
    start_client()