#!/usr/bin/python

__author__ = 'JordanLewis'

import socket
import time
from thread import *

import fcntl
import struct

class DartsConnectServerDelegate:
    def dcsInitialised(self, hostName):
        pass
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

class DartsConnectServer:

    endFlag = "\\e"
    messageSplitter = "|"

    '''
    Called by the messageReceived function when it receives a new message from the client
    Args:
        message: The raw message received by this server
    Function:
        This function parses the message received by this server and converts the data's data types into the correct one for each of the tiles.
    '''
    def parseMessage(self, message):
        parts = message.split(self.messageSplitter)
        if len(parts) != 3:
            return None
        tag = parts[0]
        type = parts[1]
        value = parts[2]

        if type == "s":
            pass # Value received is already text, don't need to do anything
        if type == "i":
            value = int(value)
        if type == "f":
            value = float(value)
        if type == "b":
            if value == '0':
                value = False
            else:
                value = True

        return {self.tagKey: tag, self.valueKey: value}



    '''
    Called by the user when wanting to send data to the client.
    Args:
        tag: The tag of the target tile
        value: The data to send to the tile
    Function:
        1. Create message
        2. Send it to the client
    '''
    def sendMessage(self, type, value):
        try:
            message = str(type + self.messageSplitter + str(value) + self.endFlag)
            self.client.sendall(message)
        except:
            print "Failed to send message (" + type + ":" + str(value) + ")"


    '''
    Called when a device connects and sends in the tag CONNECT
    Args:
        connection: A variable containing the connection variable that the message was received on
    Function:
        1. Sets the variable containing the connection instance (self.client) to the connection
        2. Calls the delegate function for handling the connection for the front end developer
    '''
    def addClient(self, connection):
        if self.client != None:
            print "--> Denied access, Apple TV already connected."
            self.sendMessage("DISCONNECT", "Leave:Same name connected.")
        else:
            self.client = connection
            self.delegate.dcsAppleTVConnected()
            print "--> CONNECTED: Apple TV"
            self.printLine()
            self.sendMessage("CONNECT", "Welcome")



    '''
    Called when a device connects and sends in the tag DISCONNECT
    Function:
        1. Sets the self.client to None
        2. Notifies the delegate about the disconnect
    '''
    def removeClient(self):
        try:
            self.sendMessage("DISCONNECT", "Bye")
            self.client = None
            self.delegate.appleTVDisconnected()
            self.printLine()
            print '--> Disconnected from Apple TV'
        except:
            print "Failed to remove Apple TV connection."

    def kickClient(self, reason):
        try:
            self.sendMessage("DISCONNECT", "Leave:" + reason)
            self.client = None
            self.delegate.dcsAppleTVDisconnected()
            self.printLine()
            print '--> Disconnected from Apple TV'
        except:
            print "Failed to kick Apple TV"

    '''
    Called when the threaded_server receives a message from the client device
    Args:
        message: The raw message which was received
        sendingConnection: Self explanatory, the connection which the message was received on
    Function:
        1. Checks if the message is valid or not empty
        2. Parses the message to a dictionary
        3. Decides what to do depending on the tag received and calls the appropriate function
            Notable tags are:
                1. ERROR
                2. CONNECT
                3. DISCONNECT
    '''
    def messageReceived(self, message, sendingConnection):
        if message != "" and message != None:
            result = self.parseMessage(message)
            if result == None:
                return
            if result[self.tagKey] == "ERROR":
                self.delegate.dcsDidReceiveError(result[self.valueKey])
            elif result[self.tagKey] == "CONNECT":
                self.addClient(sendingConnection)
            elif result[self.tagKey] == "DISCONNECT":
                self.removeClient(result[self.valueKey])
            else:
                if result[self.tagKey] != None and result[self.valueKey] != None:
                    self.delegate.dcsDidReceiveData(result[self.tagKey], result[self.valueKey])


    '''
    Called when a device connects to the server
    There will be several instances of this running in the background as more and more devices connect
    The number of instances of this is equal to the amount of devices connected to the server
    Args:
        conn: The connection which the device is connected to this server on
    Function:
        Infinite loop running in the background always listening for data from the clients
        Connection is closed if something goes wrong or the server is closing down.
    '''
    def threaded_server(self, conn):
        fullMessage = ""
        while self.serverAlive:
            data = conn.recv(2048)
            fullMessage += data.decode('utf-8')
            if self.endFlag in fullMessage:
                self.messageReceived(fullMessage.replace(self.endFlag, ""), conn)
                fullMessage = ""
            if not data:
                break

        self.printLine()
        print "--> Apple TV unexpectedly disconnected"
        self.client = None

        conn.close()

        print "--> Disconnected from Apple TV"
        self.printLine()


    '''
    Called when the server is being shut down
    '''
    def killServer(self):
        print ""
        self.printLine()
        print "Darts Connect Server will begin shutting down."
        self.printLine()

        if self.client != None:
            self.kickClient("Server Shutting Down")

        time.sleep(self.shutDownKickTimeout)

        self.serverAlive = False

        self.delegate.dcsWillShutdown()
        print "Darts Connect Server has shut down."
        self.printLine()

    def getHostIP(self):
        return socket.gethostbyname(socket.gethostname())

    '''
    Called when this class is initiated
    Args:
        N/A
    Function:
        Single infinite loop running to accept incoming connections up to the number stated above
        When a device connects, it creates a new thread for the device
        Listens for a keyboard interrupt to close connections and shut down the server
    '''
    def startServer(self):
        print "--> Binding Data Socket"
        try:
            self.s.bind((self.host, self.port))
        except socket.error as e:
            print (str(e))

        self.s.listen(self.maxClients)
        print "--> Data Socket Bound"
        hostName = self.getHostIP()
        #port = socket.getsockname()[1]

        self.printLine()
        print "--> Server Host is: " + hostName + ":" + str(self.port)
        self.printLine()

        self.delegate.dcsInitialised(hostName)

        while self.serverAlive:
            try:
                conn, addr = self.s.accept()

                #if len(self.clients.keys()) > 0:
                self.printLine()

                print ('--> CONNECTING: ' + addr[0] + ':' + str(addr[1]))

                start_new_thread(self.threaded_server, (conn,))

            except KeyboardInterrupt:
                self.killServer()
                break

    def getSelfIP(self, interfaceName):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915, #SIOCGIFADDR
            struct.pack('256s', interfaceName[:15])
        ))

    def printLine(self):
        print "--------------------------------------------------"

    '''
    Init function called when an instance of this class is created
    Args:
        _port: The port to open for listening to connection on
        _delegate: The instance of a class which will conform to the delegate functions, most likely the calling class
    Function:
        Sets the passed values to global values
        Calls the main loop for accepting connections on
    '''
    def __init__(self, _port, _delegate, _maxClients):
        self.printLine()
        print "Initiating the Darts Connect Server: By Jordan Lewis"

        self.port = _port
        self.delegate = _delegate
        self.maxClients = _maxClients
        self.client = None
        self.serverAlive = True
        self.tagKey = 'Tag'
        self.valueKey = 'Value'
        self.host = ''
        self.shutDownKickTimeout = 3
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.printLine()
        print ">>> Darts Connect Server Class Initialised"
        print "->>     Don't forget to call the start server function!"
        self.printLine()