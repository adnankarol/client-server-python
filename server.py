import socket

# IPV4, TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Since server is held on same laptop as code
# 1234 is custom port that we create
s.bind((socket.gethostname(), 1234))
s.listen(5)


# Listen forever
while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established !! ")
    msg = "Welcome to the server !!"
    clientsocket.send(bytes(msg.encode("utf-8")))
    
