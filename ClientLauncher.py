from tkinter import *
import tkinter.messagebox
from Client import Client

def getInput():
    global client
    try:
        client = Client(serverAddrVar.get(), int(serverPortVar.get()))
        root.destroy()
    except:
        tkinter.messagebox.showwarning("Connection Failed", "Cannot connect to the specified server. Please re-enter.")
def createWidgetsInit(root):
    serverPortLabel = Label(root, text = "Server Port")
    serverPortEntry = Entry(root, textvariable = serverPortVar)
    serverAddrLabel = Label(root, text = "Server Address")
    serverAddrEntry = Entry(root, textvariable = serverAddrVar)
    submitButton = Button(root, text = "Submit", command = getInput)

    serverAddrLabel.grid(row = 0, column = 0)
    serverAddrEntry.grid(row = 0, column = 1)
    serverPortLabel.grid(row = 1, column = 0)
    serverPortEntry.grid(row = 1, column = 1)
    submitButton.grid(row = 2, column = 1)

if __name__ == "__main__":
    root = Tk()
    root.geometry("800x600")
    serverPortVar = StringVar()
    serverAddrVar = StringVar()
    createWidgetsInit(root)
    client = None
    root.mainloop()
    client.root.mainloop()