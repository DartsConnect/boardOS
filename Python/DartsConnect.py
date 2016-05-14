#!/usr/bin/python

__author__ = 'JordanLewis'

from DartsConnectServer import *
from DartsConnectBonjour import *
from thread import *

class DartsConnect(DartsConnectServerDelegate):
    def consoleMainLoop(self):
        self.breadcrumbs = []
        while self.shouldRunConsole:

            command = raw_input("~> ").lower().replace(" ", "")
            if command == "help":
                print """
        Register user cards: card -p(xxx,xxx,xxx)
        Simulate game: game -t<gametype> -s<total score to hit (if count down)> -p<number of players> -c<conditions in (open,close)>
        Manually Enter Throws: throw
                                Each entry should be in the format <area>,<multiplier>*<number of times to repeat 1~3>
                                Note that the *<number of times> part is optional
        Game types: 0: 01
                    1: Cricket
                    2: Free
                    3: 20 to 1
                    4: World
        Condition Codes:    a: Any
                            s: Single
                            d: Double
                            t: Triple
                            b: Bull
                            db: Double Bull
                            """
            else:
                parts = command.split("-")
                function = parts[0]
                if function == "card":
                    self.handleCardCommand(parts)
                elif function == "game":
                    pass
                elif function == "throw":
                    self.handleManualThrows()
        print "Terminate Console"

    def handleManualThrows(self):
        shouldExit = False
        while not shouldExit:
            throw = raw_input("Throw ~> ").lower()
            if throw == "b":
                shouldExit = True
            elif len(throw.split("*")) > 1:
                parts = throw.split("*")
                value = parts[0]
                for _ in range(0, int(parts[1])):
                    print value
                    self.dcs.sendMessage("DartHit", value)
                    sleep(1)
            else:
                self.dcs.sendMessage("DartHit", throw)  # should be in the format area, multiplier

    def splitFlagsAndData(self, message):
        flag = message[0]
        data = message[1:]
        return (flag, data)

    def handleCardCommand(self, parts):
        message = parts[1]
        (flag, data) = self.splitFlagsAndData(message)
        names = data[1:][:-1].split(",")
        for name in names:
            print "Sending " + name + " in:"
            countDownDuration = 3
            for i in range(0, countDownDuration):
                print countDownDuration - i
                sleep(1)
        self.dcs.sendMessage('Card', self.cardIDs[name])

    def dcsInitialised(self, hostName):
        self.bonjour = DartsConnectBonjour(self.dcs.getHostIP(), self.dcs.port)
        self.bonjour.startBonjour()
        #print self.dcs.getSelfIP('en0')
        self.cardIDs = {
            'jordan':'00000000',
            'jack':'00000001',
            'will':'00000002',
            'sam':'00000003'
        }

    def dcsDidReceiveData(self, senderTag, data):
        pass

    def dcsDidReceiveError(self, errorMessage):
        pass

    def dcsAppleTVConnected(self):
        self.shouldRunConsole = True
        start_new_thread(self.consoleMainLoop, ())


    def dcsAppleTVDisconnected(self):
        self.shouldRunConsole = False

    def dcsWillShutdown(self):
        self.bonjour.stopBonjour()

    def __init__(self):
        self.dcs = DartsConnectServer(4006, self, 1) # under 1024 is privelidged, reserved for OS 0 for auto port assignment
        self.dcs.startServer()

if __name__ == '__main__':
    DartsConnect()