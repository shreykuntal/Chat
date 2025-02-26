from tkinter import *
import tkinter.messagebox
import socket, threading

class Client:
    INIT = 0
    CHAT_READY = 1
    state = INIT

    def __init__(self, serverAddr, serverPort):
        self.serverAddr = serverAddr
        self.serverPort = serverPort
        self.connectToServer()
        self.root = Tk()
        self.sendChatVar = StringVar()
        self.createWidgetsChatReady()
        self.userName = None
        self.receiveThread = None

    def connectToServer(self):
        self.clientPort = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientPort.connect((self.serverAddr, self.serverPort))

    def createWidgetsChatReady(self):
        self.seeChat = Text(self.root, height = 25, width = 50)
        self.sendChat = Entry(self.root, textvariable = self.sendChatVar, width = 40)
        self.submitButton = Button(self.root, text = "Submit", command = self.sendMessage)
        self.seeChat.grid(row = 0, column = 0)
        self.sendChat.grid(row = 1, column = 0)
        self.submitButton.grid(row = 1, column = 1)
        self.seeChat.insert(END, "Connection Successful!\nEnter user-name")
    
    def sendMessage(self):
        message = self.sendChat.get()
        self.sendChatVar.set("")
        self.clientPort.send(message.encode())
        if (self.state == self.INIT):
            self.seeChat.insert(END, '\n'+reply)
            if (reply == "!OKAY"):
                self.userName = message
                self.receiveThread = threading.Thread(target = self.receiveMessage)
                self.receiveThread.daemon = True
                self.receiveThread.start()
                self.state = self.CHAT_READY
    
    def receiveMessage(self):
        message = self.clientPort.recv(2048).decode()
        self.seeChat.insert(END, '\n'+message)