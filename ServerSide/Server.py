import socket
"""Author: Shaked Asido"""

"""Description: This is the server's side: The server gets a name and an address of the sender (first client), 
which he inserts into a names&addresses dictionary. Then he gets another message with the name of the anf a massage 
designated to the other client. if the other client appears in the names at the dictionary, the server sends the 
message the first client sent to the other client."""

UDP_IP = '0.0.0.0'
UDP_PORT = 9999
BUFFER_SIZE = 1024

try:
    # this server use UDP, So we will use: SOCK_DGRAM
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

    # binds between the socket and the configuration (port etc..) & checks that we connected properly
    server_sock.bind((UDP_IP, UDP_PORT))

    # dictionary of the names and addresses of each sender
    name_and_addr_dict = {}
    while True:
        # The client sends her\his name
        data, addr = server_sock.recvfrom(BUFFER_SIZE)
        # We add its name and address into the dictionary
        name_and_addr_dict[data.decode()] = addr
        # The client sends a message and the name of the person s\he wants to send in to
        data, _ = server_sock.recvfrom(BUFFER_SIZE)
        name_and_message = data.decode().split()
        if name_and_message[0] in name_and_addr_dict:
            # Save the name of client 2 that client 1 wants to send message to.
            name = name_and_message[0]
            # Remove name
            name_and_message.remove(name_and_message[0])
            # Take the message out of the string
            message = " ".join(name_and_message)
            # Send the encoded message with the address to the client
            server_sock.sendto(message.encode(), name_and_addr_dict[name])
        else:
            server_sock.sendto("No such user".encode(), addr)

except socket.timeout as e:
    print(f"Socket timeout: {e}")
except socket.herror as e:
    print(f"Socket hostname error: {e}")
except socket.gaierror as e:
    print(f"Socket address error: {e}")
except socket.error as e:
    print(f"Socket error: {e}")
finally:
    # close the socket
    server_sock.close()
