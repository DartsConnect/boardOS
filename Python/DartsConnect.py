#!/usr/bin/python

__author__ = 'JordanLewis'

import logging
from DartsConnectServer import *
from DartsConnectBonjour import *

class DartsConnect():#(DartsConnectServerDelegate):

    def dcsInitialised(self, hostName):
        self.bonjour = DartsConnectBonjour(self.dcs.getHostIP(), self.dcs.port)
        self.bonjour.startBonjour()
        #print self.dcs.getSelfIP('en0')

    def dcsDidReceiveData(self, senderTag, data):
        pass

    def dcsDidReceiveError(self, errorMessage):
        pass

    def dcsAppleTVConnected(self):
        pass

    def dcsAppleTVDisconnected(self):
        pass

    def dcsWillShutdown(self):
        pass

    def __init__(self):
        self.dcs = DartsConnectServer(4004, self, 1) # under 1024 is privelidged, reserved for OS 0 for auto port assignment
        self.dcs.startServer()

if __name__ == '__main__':
    DartsConnect()