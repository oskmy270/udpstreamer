import socket
import time
import testData

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
lastTime = time.time()
atr = testData.dataParameters()
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
print 'Expecting:'
print atr.printParameters()

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "message\t", len(data), '\t', time.time()-lastTime, data[:20]
    lastTime = time.time()

    if data.find('<sync>') == 0:
        print 'Sync message found'
        try:
            temp = data.find('<intensity=')
            temp2 = int(data[temp+11:temp+12])
            print 'Intensity detected:', temp2
            atr.intensity = temp2
            atr.printParameters()
        except:
            print ''