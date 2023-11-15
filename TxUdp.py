import socket

#UDP_IP = "143.198.42.213" #mnispel.work
UDP_IP = "172.20.20.55" #rpi
UDP_PORT = 49153

#MESSAGE = b"Hello, World!"
#MESSAGE = bytearray([1,2,3,4,5,6])

#CONSTRUCT A IONetworkControlMessage
MESSAGE = bytearray([0x55,0xAA,0x00,0xff,0xaa,0x55,0xff,0x00])  # sync pattern
MESSAGE += bytearray([0xff,0xff]) # msgCommand
MESSAGE += bytearray([14]) # number of data bytes in this message after the header
MESSAGE += bytearray([1]) #message format version
MESSAGE += bytearray([0x00,0x00,]) # message security number
MESSAGE += bytearray([0x00,0x00]) # reserved 1
MESSAGE += bytearray([0x00,0x00]) # msg verification value (CRC)
MESSAGE += bytearray([0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, 0x00]) # msg data

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)

sd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sd.sendto(MESSAGE, (UDP_IP, UDP_PORT))

#CONSTRUCT a second IONetworkControlMessage
MESSAGE = bytearray([0x55,0xAA,0x00,0xff,0xaa,0x55,0xff,0x00])  # sync pattern
MESSAGE += bytearray([0xff,0xff]) # msgCommand
MESSAGE += bytearray([14]) # number of data bytes in this message after the header
MESSAGE += bytearray([1]) #message format version
MESSAGE += bytearray([0x00,0x00,]) # message security number
MESSAGE += bytearray([0x00,0x00]) # reserved 1
MESSAGE += bytearray([0x00,0x00]) # msg verification value (CRC)
MESSAGE += bytearray([0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, 0x00]) # msg data

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)

#sd.sendto(MESSAGE, (UDP_IP, UDP_PORT))

sd.close()
