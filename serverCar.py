import socket

HOST = "127.0.0.1"
PORT = 1234


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    print(f"Server Carre listening on {HOST}:{PORT}")

    client_socket, client_address = server_socket.accept()
    print(f"Client connected: {client_address}")

    while True:
        data = client_socket.recv(1024)



        try:
            number = int(data.decode("utf-8"))
            result = number ** 2

            response = f"Square of {number} = {result}"

        except ValueError:
            response = "Error"

        client_socket.send(response.encode("utf-8"))

    client_socket.close()
    server_socket.close()


if __name__ == "__main__":
    start_server()