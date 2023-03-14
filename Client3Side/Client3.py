from threading import Thread
import socket
import sys

"Author: Shaked Asido"
"""Description: Client 1's side: Client 1 sends her\his name and an address of the server, and the server inserts 
them into a names&addresses dictionary. Then the client sends another message with the name of the other client 
(client 2) s\he wants to send a message to and the message, superheated with spaces. if client 2 appears in the names 
at the dictionary, the server sends the message client 1 sent to client 2. else: client 1 will get a message say's: 
"no such user"."""

SERVER_ADDR = ('127.0.0.1', 9999)
BUFFER_SIZE = 1024

client3_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
my_name = input('Enter your name: ')
client3_sock.sendto(my_name.encode(), SERVER_ADDR)
print("Enter the name of the person you wants to send a message to, and the message suppurated with spaces, Please:")


def output_recvfrom(sock):
    while True:
        data, _ = sock.recvfrom(BUFFER_SIZE)
        if not data: break
        print(data.decode())


x = Thread(target=output_recvfrom, args=(client3_sock,))
x.start()
for line in sys.stdin:
    client3_sock.sendto(line.strip().encode(), SERVER_ADDR)
client3_sock.close()
x.join()
