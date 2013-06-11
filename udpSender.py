import socket
import time
import string
import random

class Starter:
    targetIP = ''
    targetPort = 0
    intensity = 0
    time = 0
    size = 0
    message = ''
    
    def __init__(self):
        self.targetIP = '127.0.0.1'
        self.targetPort = 5005
        self.intensity = 1
        self.time = 10
        self.size = 20
        self.message = 'DJJHWIUHFOJEFKFJEOPJFPO'
        
        print 'Default values set'
        
    def printValues(self):
        print 'Target IP:\t\t\t', self.targetIP
        print 'Target port:\t\t\t', self.targetPort
        print 'Intensity (Msg/s)\t\t', self.intensity
        print 'Datagram size (Bytes)\t\t', self.size
        print 'Time for test:\t\t\t', self.time
        print 'Stream throughput (Bytes/s)\t', self.size*self.intensity
        
        
    def menu(self):
        print '------------------------'
        print '1. Set stream intensity'
        print '2. Set stream size'
        print '3. Set target'
        print '4. Set time period'
        print '5. Print values'
        print ''
        print '6. Start test'
        print '------------------------'
        
        return raw_input('Choice (q to quit): ')
    
    def sendUDP(self, msg):
        sock = socket.socket(socket.AF_INET, # Internet
                             socket.SOCK_DGRAM) # UDP
        sock.sendto(msg, (self.targetIP, self.targetPort))
        
    def createPayload(self, random, size):
        if random:
            self.message = str(time.time())
            self.message += ','+self.id_generator(size-len(self.message), string.ascii_uppercase + string.digits)
        else:
            print 'Creating non-random payload' 
    
    def id_generator(self, size, chars):
        return ''.join(random.choice(chars) for x in range(size))
    
    def startTest(self):
        print 'Starting test...'
        self.printValues()
        startTime = time.time()
        while (time.time() < startTime+self.time):
            self.createPayload(True, self.size)
            self.sendUDP(self.message)
            print '.'
            time.sleep(1)
        
        

run = Starter()
inputText = ''
while (inputText != 'q'):
    inputText = run.menu()
    if inputText == '6':
        run.startTest()




