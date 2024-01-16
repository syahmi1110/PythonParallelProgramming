import socket

server_address = ("192.168.37.128", 8484)

client_socket = socket.create_connection(server_address)
quote = client_socket.recv(4096)

print(quote.decode("utf-8"))
client_socket.close()
