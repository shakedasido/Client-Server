from threading import Thread
import socket
import sys

"Author: Shaked Asido"

"""Description: Client 5's side: Client 5 sends her\his name and an address of the server, and the server inserts 
them into a names&addresses dictionary. Then the client sends another message with the name of the other client s\he 
wants to send a message to and the message, superheated with spaces. if the other client appears in the names at the 
dictionary, the server sends the message client 5 sent to the other client. else: client 5 will get a message say's: 
"no such user"."""

SERVER_ADDR = ('127.0.0.1', 9999)
BUFFER_SIZE = 1024

client5_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
my_name = input('Enter your name: ')
client5_sock.sendto(my_name.encode(), SERVER_ADDR)
print("Enter the name of the person you wants to send a message to, and the message suppurated with spaces, Please:")


def output_recvfrom(sock):
    while True:
        data, _ = sock.recvfrom(BUFFER_SIZE)
        if not data: break
        print(data.decode())


x = Thread(target=output_recvfrom, args=(client5_sock,))
x.start()
for line in sys.stdin:
    client5_sock.sendto(line.strip().encode(), SERVER_ADDR)
client5_sock.close()
x.join()