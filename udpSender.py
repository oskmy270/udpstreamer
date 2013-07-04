import socket
import time
import string
import random
import testData
import os

          
class Starter:

    def __init__(self):
        print 'Default values set'
    
    def askSize(self):
        atr.setSize(int(raw_input('Enter size for each UDP packet in Bytes: ')))
    def askIntensity(self):
        atr.setIntensity(int(raw_input('Enter intensity (packets per second): ')))
    def askTarget(self):
        atr.setTarget(raw_input('Enter target IP: '), int(raw_input('Enter target port: ')))
    def askTimePeriod(self):
        atr.setTime(int(raw_input('How long should the test occur? (seconds): ')))
        
    def printValues(self):
        print 'Target IP:\t\t\t', atr.targetIP
        print 'Target port:\t\t\t', atr.targetPort
        print 'Intensity (Msg/s)\t\t', atr.intensity
        print 'Datagram size (Bytes)\t\t', atr.size
        print 'Time for test:\t\t\t', atr.time
        print 'Stream throughput (Bytes/s)\t', int(atr.size)*int(atr.intensity)
        print 'Time between packets:', str(1./int(atr.intensity))
        
        
    def menu(self):
        #os.system('clear')
        print '------------------------'
        print '1. Set stream intensity'
        print '2. Set stream size'
        print '3. Set target'
        print '4. Set time period'
        print '5. Print values'
        print ''
        print '6. Start test'
        print '7. Send synch info to server'
        print '------------------------'
        
        return raw_input('Choice (q to quit): ')
    
    def sendUDP(self, msg):
        sock = socket.socket(socket.AF_INET, # Internet
                             socket.SOCK_DGRAM) # UDP
        sock.sendto(atr.getMessage(), (atr.targetIP, atr.targetPort))
        
    def createPayload(self, random, size):
        if random:
            atr.message = self.id_generator(atr.size, string.ascii_uppercase + string.digits)
        else:
            print 'Creating non-random payload' 
    
    def id_generator(self, size, chars):
        return ''.join(random.choice(chars) for x in range(size))
    
    def sendSynchInfo(self):
        synchInfo = '<sync>'
        synchInfo += '<intensity='+str(atr.intensity)+'>'
        sock = socket.socket(socket.AF_INET, # Internet
                             socket.SOCK_DGRAM) # UDP
        sock.sendto(synchInfo, (atr.targetIP, atr.targetPort))
    
    def startTest(self):
        print 'Starting test...'
        self.printValues()
        startTime = time.time()
        while (time.time() < startTime+atr.time):
            self.createPayload(True, int(atr.size))
            self.sendUDP(atr.message)
            print '.'
            time.sleep(1./int(atr.intensity))
        
        
atr = testData.dataParameters()
run = Starter()
inputText = ''
while (inputText != 'q'):
    inputText = run.menu()
    if inputText == '1':
        run.askIntensity()
    if inputText == '2':
        run.askSize()
    if inputText == '3':
        run.askTarget()
    if inputText == '4':
        run.askTimePeriod()
    if inputText == '5':
        run.printValues()
    if inputText == '6':
        run.startTest() 
    if inputText == '7':
        run.sendSynchInfo()




