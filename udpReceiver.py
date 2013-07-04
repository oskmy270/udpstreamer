import socket
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
 
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))


while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    if len(data) > 20:
        print time.time(), "received message, length:", len(data)
    else:
        print time.time(), "received message:", data
    if data.find('OSKAR:') == 0:
        print 'Sync message found'
        try:
            data[6:]
        except:
            print ''