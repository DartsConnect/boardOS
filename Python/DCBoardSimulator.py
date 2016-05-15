
from DartsConnectServer import *
from thread import *
from time import sleep

class DCBoardSimulator():

    dartHitTag = "DartHit"
    cardTag = "Card"

    def startConsole(self):
        self.shouldRunConsole = True
        start_new_thread(self.consoleMainLoop, ())

    def stopConsole(self):
        self.shouldRunConsole = False

    def consoleMainLoop(self):
        while self.shouldRunConsole:
            try:
                command = raw_input("~> ").lower().replace(" ", "")
                if command == "help":
                    print """
Register user cards: card -p xxx,xxx,xxx OR card (to enter them manually)
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
            except:
                print "Invalid Command: type help to show valid commands"
        print "Terminate Console"

    def handleManualThrows(self):
        shouldExit = False
        while not shouldExit and self.shouldRunConsole:
            throw = raw_input("Throw ~> ").lower()
            if throw == "b":
                shouldExit = True
            elif len(throw.split("*")) > 1:
                parts = throw.split("*")
                value = parts[0]
                for _ in range(0, int(parts[1])):
                    print value
                    self.sendDartHit(value)
                    sleep(1)
            else:
                self.sendDartHit(throw)

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
            while self.shouldRunConsole:
                name = raw_input("Username ~> ").replace(" ", "").lower()
                if name == "b":
                    break
                else:
                    try:
                        self.dcs.sendMessage(self.cardTag, self.cardIDs[name])
                    except:
                        print "Invalid Username"
        else:
            message = parts[1]
            (flag, data) = self.splitFlagsAndData(message)
            names = data.split(",")
            for name in names:
                print "Sending " + name + " in:"
                countDownDuration = 3
                for i in range(0, countDownDuration):
                    print countDownDuration - i
                    sleep(1)
                try:
                    self.dcs.sendMessage(self.cardTag, self.cardIDs[name])
                except:
                    print "Invalid Username"

    def __init__(self, dcs, cardIDs):
        self.dcs = dcs
        self.cardIDs = cardIDs