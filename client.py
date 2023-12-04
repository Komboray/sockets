import socket


client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

client.connect(("34-13-E8-2E-D9-6B", 1))

try:
    while True:
        message = input("Enter message:")
        client.send(message.encode('utf-8'))
except OSError as o:
    pass

client.close()