import socket

server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server.bind(("48-5F-99-92-4B-FB", 7))
server.listen(1)

#this is our client that is talking to the other side
client, addr = server.accept()

try:
    while True:
        #we are telling the client to receive
        data = client.recv(1024)
        if not data:
            break
        print(f"Message: {data.decode('utf-8')}")
        message = int("Enter message")
        client.send(message.encode("utf-8"))
except OSError as o:
    pass

client.close()
server.close()