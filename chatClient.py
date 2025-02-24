from socket import *
from threading import Thread

serverPort = 6961
serverAddress = '10.81.60.12'
socketPort = socket(AF_INET, SOCK_STREAM)
socketPort.connect((serverAddress, serverPort))

close_ack = False
def receive_message(socketPort):
	global close_ack
	while True:
		message = socketPort.recv(2048).decode()
		if (not message):
			close_ack = True
			print("Enter any key to quit: ")
			return
		print(message)
		print("TYPE: ")
def send_message(socketPort):
	while True:
		print("TYPE: ")
		message = input()
		if (not close_ack):
			socketPort.send(message.encode())
		else:
			return

while True:
	while True:
		print("Enter user-name: ")
		user_name = input()
		socketPort.send(user_name.encode())
		reply = socketPort.recv(2048).decode()
		print(reply)
		if (reply == "!CONNECTED"):
			break
	send_thread = Thread(target=send_message, args=(socketPort,))
	receive_thread = Thread(target=receive_message, args=(socketPort,))
	send_thread.start()
	receive_thread.start()
	receive_thread.join()
	send_thread.join()
	socketPort.close()
	break