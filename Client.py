from tkinter import *
import tkinter.messagebox
import socket, threading

class Client:
    INIT = 0
    CHAT_READY = 1
    state = INIT

    def __init__(self, root):
        self.clientPort = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.root = root
        self.sendChatVar = StringVar()
        self.serverPortVar = StringVar()
        self.serverAddrVar = StringVar()
        self.createWidgetsInit()
        self.userName = None
        self.receiveThread = threading.Thread(target = self.receiveMessage)
        self.receiveThread.daemon = True
        self.root.mainloop()

    def setup(self):
        try:
            self.clientPort.connect((self.serverAddrVar.get(), int(self.serverPortVar.get())))
            self.serverAddr = self.serverAddrVar.get()
            self.serverPort = int(self.serverPortVar.get())
        except:
            tkinter.messagebox.showwarning("Connection Failed", "Cannot connect to the specified server. Please re-enter.")
            return
        self.deleteWidgetsInit()
        self.createWidgetsChatReady()
        self.receiveThread.start()
    
    def createWidgetsInit(self):
        self.serverPortLabel = Label(self.root, text = "Server Port")
        self.serverPortEntry = Entry(self.root, textvariable = self.serverPortVar)
        self.serverAddrLabel = Label(self.root, text = "Server Address")
        self.serverAddrEntry = Entry(self.root, textvariable = self.serverAddrVar)
        self.submitButton = Button(self.root, text = "Submit", command = self.setup)

        self.serverAddrLabel.grid(row = 0, column = 0)
        self.serverAddrEntry.grid(row = 0, column = 1)
        self.serverPortLabel.grid(row = 1, column = 0)
        self.serverPortEntry.grid(row = 1, column = 1)
        self.submitButton.grid(row = 2, column = 1)

    def deleteWidgetsInit(self):
        self.serverPortLabel.destroy()
        self.serverPortEntry.destroy()
        self.serverAddrLabel.destroy()
        self.serverAddrEntry.destroy()
        self.submitButton.destroy()

    def createWidgetsChatReady(self):
        self.seeChat = Text(self.root, height = 25, width = 50)
        self.sendChat = Entry(self.root, textvariable = self.sendChatVar, width = 40)
        self.submitButton = Button(self.root, text = "Submit", command = self.sendMessage)
        self.seeChat.grid(row = 0, column = 0)
        self.sendChat.grid(row = 1, column = 0)
        self.submitButton.grid(row = 1, column = 1)
        self.seeChat.insert(END, "Connection Successful!\nEnter user-name\n")
    
    def sendMessage(self):
        message = self.sendChat.get()
        self.sendChatVar.set("")
        self.clientPort.send(message.encode())
    
    def receiveMessage(self):
        while True:
            message = self.clientPort.recv(2048).decode()
            self.seeChat.insert(END, message+'\n')