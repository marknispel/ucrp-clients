import socket

UDP_IP = "172.20.20.2"
UDP_PORT = 49153

sd = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sd.bind((UDP_IP, UDP_PORT))

print("[ ] Listening on port: %s" % (sd.getsockname(),))
while True:
    data, addr = sd.recvfrom(1024) # buffer size is 1024 bytes
    print("received message: %s" % data)