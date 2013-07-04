def data2hex(data):
    print 'Converting data parameters to hex string.'
    return hex(data)
def hex2data(data):
    print 'Converting hex string to data parameters.'

class dataParameters():
    targetIP = '127.0.0.1'
    targetPort = 5005
    intensity = 1
    time = 10
    size = 100
    message = 'DJJHWIUHFOJEFKFJEOPJFPO'
    
    def __init__(self):
        print 'Creating class for test parameters'

    def setSize(self, size):
        self.size = size
    def setIntensity(self, intensity):
        self.intensity = intensity
    def setTarget(self, IP, port):
        self.targetIP = IP
        self.targetPort = port
    def setTimePeriod(self, time):
        self.time = time
    def setMessage(self, msg):
        self.message = msg
    
    def getMessage(self):
        return self.message
    def printParameters(self):
        print 'Target IP:\t\t\t', self.targetIP
        print 'Target port:\t\t\t', self.targetPort
        print 'Intensity (Msg/s)\t\t', self.intensity
        print 'Datagram size (Bytes)\t\t', self.size
        print 'Time for test:\t\t\t', self.time
        print 'Stream throughput (Bytes/s)\t', int(self.size)*int(self.intensity)
        print 'Time between packets:\t\t', str(1./int(self.intensity))