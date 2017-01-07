#!/usr/bin/python

__author__ = 'JordanLewis'

from DartsConnectServer import *
from DartsConnectBonjour import *
from DCBoardSimulator import *

class DartsConnect(DartsConnectServerDelegate):
    def dcsInitialised(self, hostName):
        self.bonjour = DartsConnectBonjour(self.dcs.getHostIP(), self.dcs.port)
        self.bonjour.startBonjour()
        #print self.dcs.getSelfIP('en0')
        self.cardIDs = {
            'jordan':'00000000',
            'jack':'00000001',
            'will':'00000002',
            'sam':'00000003',
            'kimber':'00000004'
        }

    def dcsDidReceiveData(self, senderTag, data):
        pass

    def dcsDidReceiveError(self, errorMessage):
        pass

    def dcsAppleTVConnected(self):
        self.simulator = DCBoardSimulator(self.dcs, self.cardIDs)
        self.simulator.startConsole()

    def dcsAppleTVDisconnected(self):
        pass

    def dcsWillShutdown(self):
        self.bonjour.stopBonjour()

    def __init__(self):
        self.dcs = DartsConnectServer(4018, self, 1) # under 1024 is privileged, reserved for OS 0 for auto port assignment
        self.dcs.startServer()

if __name__ == '__main__':
    DartsConnect()
