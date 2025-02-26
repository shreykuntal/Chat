from tkinter import *
import tkinter.messagebox
from Client import Client
import threading

if __name__ == "__main__":
    root = Tk()
    root.geometry("800x600")
    client = Client(root)
    # root.mainloop()