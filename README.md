# Client-Server
Client Server project. implement the idea of sockets:

In this project we have two sides:

The Client side:
Client wants to send a message to anothe client, so:
Client sends her\his name and an address of the server, and the server inserts them into a names&addresses dictionary. Then the client sends another message with the name of the other client s\he wants to send a 
message to and the message, superheated with spaces. if the other client appears in the names at the dictionary, 
the server sends the message client 2 sent to the other client. else: client 2 will get a message say's: 
"no such user".

The Server's side:
Server needs to pass message fron one client to another, so:
The server gets a name and an address of the sender (first client), which he inserts into a names&addresses dictionary. Then he gets another message with the name of the anf a massage designated to the other client. 
If the other client appears in the names at the dictionary, the server sends the 
message the first client sent to the other client. Otherwise: It retures to the first client: "no such user"
