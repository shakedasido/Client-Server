from threading import Thread
import socket
import sys

SERVER_ADDR = ('127.0.0.1', 9999)
BUFFER_SIZE = 1024

client1_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
my_name = input('Enter your name: ')
client1_sock.sendto(my_name.encode(), SERVER_ADDR)
print("Enter the name of the person you wants to send a message to, and the message suppurated with spaces, Please:")


def output_recvfrom(sock):
    while True:
        data, _ = sock.recvfrom(BUFFER_SIZE)
        if not data: break
        print(data.decode())


x = Thread(target=output_recvfrom, args=(client1_sock,))
x.start()
for line in sys.stdin:
    client1_sock.sendto(line.strip().encode(), SERVER_ADDR)
client1_sock.close()
x.join()
