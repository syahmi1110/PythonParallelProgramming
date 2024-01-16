import socket
import threading
import random

quotes = [
    "Hustle:The only Uncontrollable Pillar of Success",
    "An Apple A Day, Keep The Doctor Away",
    "Always Push Yourself to the Limit",
    "Open Up Yourself"
]

def handle_client(client_socket):
    while True:
        try:
            client_socket.settimeout(5.0)
            quote = random.choice(quotes)
            client_socket.sendall(f"{quote}\n".encode("utf-8"))
        except socket.timeout:
            break
        except Exception as e:
            print(e)
            break
    client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("0.0.0.0", 8484))
server_socket.listen(5)

while True:
    client_socket, addr = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
