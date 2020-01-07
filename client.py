import socket

BUFFER_SIZE = 1024


def client_socket(tcp_ip, tcp_port):
    # Create socket object.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((tcp_ip, tcp_port))

        message = "Hello there."
        sock.sendall(message.encode())

        # Read incoming data
        while True:
                data = sock.recv(BUFFER_SIZE)
                if data:
                        print(data)
                else: 
                        break
        sock.close()
        print("The data is: " + str(data))


def main():
    tcp_ip = "127.0.0.1"
    tcp_port = 4003
    client_socket(tcp_ip, tcp_port)


if __name__ == "__main__":
    main()
