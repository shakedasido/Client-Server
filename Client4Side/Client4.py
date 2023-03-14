from threading import Thread
import socket
import sys

SERVER_ADDR = ('127.0.0.1', 9999)
BUFFER_SIZE = 1024

client4_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
my_name = input('Enter your name: ')
client4_sock.sendto(my_name.encode(), SERVER_ADDR)


def output_recvfrom(sock):
    while True:
        data, _ = sock.recvfrom(BUFFER_SIZE)
        if not data: break
        print(data.decode())


x = Thread(target=output_recvfrom, args=(client4_sock,))
x.start()
for line in sys.stdin:
    print("Enter the name of the person you wants to send a message to, and the message suppurated with spaces, Please:")
    client4_sock.sendto(line.strip().encode(), SERVER_ADDR)
client4_sock.close()
x.join()
