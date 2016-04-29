import SocketServer
'''
class DartsConnectServer(SocketServer.StreamRequestHandler):

    def handle(self):
        self.data = self.rfile.readline().strip()
        print self.client_address[0] + " wrote:"
        print self.data
        self.wfile.write("testing")
'''

class DartsConnectServer(SocketServer.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024)
        print "{} wrote:".format(self.client_address[0])
        print self.data
        print self.data.strip()
        print self.data.decode('utf-8')