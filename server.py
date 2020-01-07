import socket

TCP_PORT = 4003
BUFFER_SIZE = 1024  # Apparently, 1024 is standard.


def server_socket(tcp_ip, tcp_port):
    # Create socket object.
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Bind socket to tcp address and port then listen.
		sock.bind((tcp_ip, tcp_port))
		sock.listen()
		print("The server is listening.")

		# If client connects.
		conn, addr = sock.accept()
		print(f"Client on: {addr} has connected.")

        # Read incoming data
		while True:
			data = conn.recv(BUFFER_SIZE)
			if data:
				conn.sendall("Recieved all.".encode())
			else:
				break

		conn.close()
		print("The data is: " + str(data))


def main():
    tcp_ip = socket.gethostbyname("localhost")
    server_socket(tcp_ip, TCP_PORT)


if __name__ == "__main__":
    main()
