import socket

# IPV4, TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Since client is held on same laptop as code
s.connect((socket.gethostname(), 1234))

# How much data you want to recieve i.e. buffer size
msg = s.recv(1024)
print(msg.decode("utf-8"))

msg = "Real-Time-Video-Output.png"
s.send(msg.encode("utf-8"))

