
from DartsConnectServer import *
from thread import *
from time import sleep

class DCBoardSimulator():

    dartHitTag = "DartHit"
    cardTag = "Card"

    def startConsole(self):
        self.shouldRunConsole = True
        start_new_thread(self.consoleMainLoop, ())

    def getMainInput(self):
        self.response = raw_input("~>").lower().replace(" ","")

    def getSubInput(self, title):
        self.subResponse = raw_input(title + " ~> ").lower().replace(" ","")

    def printHelp(self):
        '''
        Simulate game: game -t<gametype> -s<total score to hit (if count down)> -p<number of players> -c<conditions in (open,close)>
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
        :return:
        '''
        print """
Register user cards: card -p xxx,xxx,xxx OR card (to enter them manually)
Manually Enter Throws: throw
                        Each entry should be in the format <area>,<multiplier>*<number of times to repeat 1~3>
                        Note that the *<number of times> part is optional
                """

    def isStillConnected(self):
        return self.dcs.client != None

    def consoleMainLoop(self):
        start_new_thread(self.getMainInput,())
        while True:
            if self.response == None:
                if not self.isStillConnected():
                    break
            else:
                try:
                    command = self.response
                    self.response = None
                    #command = raw_input("~> ").lower().replace(" ", "")
                    if command == "help":
                        self.printHelp()
                    else:
                        parts = command.split("-")
                        function = parts[0]
                        if function == "card":
                            self.handleCardCommand(parts)
                        elif function == "throw":
                            self.handleManualThrows()
                        else:
                            print "Invalid Command (" + command + "): type help to show valid commands"
                    if self.isStillConnected():
                        start_new_thread(self.getMainInput, ())
                except:
                    print "Invalid Command (" + command + "): type help to show valid commands"
        print "--> Terminate Console"

    def handleManualThrows(self):
        start_new_thread(self.getSubInput, ("Throw",))
        while True:
            if self.subResponse == None:
                if not self.isStillConnected():
                    break
            else:
                throw = self.subResponse
                self.subResponse = None

                if throw == "b":
                    break
                elif len(throw.split("*")) > 1:
                    parts = throw.split("*")
                    value = parts[0]
                    for _ in range(0, int(parts[1])):
                        print value
                        self.sendDartHit(value)
                        sleep(1)
                else:
                    self.sendDartHit(throw)
                if self.isStillConnected():
                    start_new_thread(self.getSubInput, ("Throw",))

    def sendDartHit(self, value):
        if len(value.split(",")) == 1:
            self.dcs.sendMessage(self.dartHitTag, value + ",1")
        else:
            self.dcs.sendMessage(self.dartHitTag, value) # should be in the format area, multiplier

    def splitFlagsAndData(self, message):
        flag = message[0]
        data = message[1:]
        return (flag, data)

    def handleCardCommand(self, parts):
        if len(parts) == 1:
            start_new_thread(self.getSubInput, ("Username",))
            while True:
                if self.subResponse == None:
                    if not self.isStillConnected():
                        break
                else:
                    name = self.subResponse
                    self.subResponse = None
                    if name == "b":
                        break
                    else:
                        if self.isStillConnected():
                            start_new_thread(self.getSubInput, ("Username",))
                        try:
                            self.dcs.sendMessage(self.cardTag, self.cardIDs[name])
                        except:
                            print "Invalid Username"
        else:
            message = parts[1]
            (flag, data) = self.splitFlagsAndData(message)
            names = data.split(",")
            for name in names:
                sleep(1)
                try:
                    self.dcs.sendMessage(self.cardTag, self.cardIDs[name])
                    print "Semt: " + name
                except:
                    print "Invalid Username"

    def __init__(self, dcs, cardIDs):
        self.response = None
        self.subResponse = None
        self.dcs = dcs
        self.cardIDs = cardIDs