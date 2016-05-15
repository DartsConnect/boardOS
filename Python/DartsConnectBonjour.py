#!/usr/bin/env python

""" Example of announcing a service (in this case, a fake HTTP server) """

import logging
import socket
import sys
from time import sleep

from zeroconf import ServiceInfo, Zeroconf

class DartsConnectBonjour():

    def stopBonjour(self):
        print("DartsConnectBonjour --> Unregistering...")
        self.zeroconf.unregister_service(self.info)
        self.zeroconf.close()

    def startBonjour(self):
        if len(sys.argv) > 1:
            assert sys.argv[1:] == ['--debug']
            self.logging.getLogger('zeroconf').setLevel(logging.DEBUG)

        #desc = {'path': '/~paulsm/'}

        self.info = ServiceInfo("_dartsconnect._tcp.local.",
                           "Dartboard._dartsconnect._tcp.local.",
                           socket.inet_aton(self.ip), self.port, 0, 0,
                           {}, None)

        self.zeroconf = Zeroconf()
        print("DartsConnectBonjour --> DartsConnect service registered")
        self.zeroconf.register_service(self.info)

    def __init__(self, ipAddr, port):
        self.ip = ipAddr
        self.port = port
