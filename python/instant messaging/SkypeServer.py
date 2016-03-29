'''
Author : 		Shreyas Damle
Desription :	This is Skype service/server. It is multithreaded service which is listening on port 12346 for incoming requests. It gets these requests and sends given message to given skype user or group.
Prerequisites : If you wish to send message to a group then it expects that group is created with some prereuisites as follows =>
'''

#!/usr/bin/python           # This is server.py file
import string
import socket               # Import socket module
import Skype4Py
import thread
import time

soc = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12346                # Reserve a port for your service.
soc.bind((host, port))        # Bind to the port

skype = Skype4Py.Skype()
skype.Attach()

soc.listen(5)                 # Now wait for client connection.
def sampleFun(threadName,delay,sendMessageToUserOrGroup,userOrGroupTopic,message):
	if sendMessageToUserOrGroup == "user":
		print "User : ", userOrGroupTopic
		skype.SendMessage(userOrGroupTopic,message)
	elif sendMessageToUserOrGroup == "group":
		print userOrGroupTopic
		for chat in skype.BookmarkedChats:
		       	if chat.Topic == userOrGroupTopic:
				print message
				chat.SendMessage(message)
	else:
		print "wrong arguments given"

while True:
	try:
		i=[]
		c, addr = soc.accept()     # Establish connection with client.
		message='Got connection from', addr
		message=c.recv(1024)
		print message

		line=message.splitlines(True)

		userOrGroupTopic=line[0].split(';')
		sendMessageToUserOrGroup=userOrGroupTopic[0].split('=')[1]
		print sendMessageToUserOrGroup

		userOrGroupTopic=userOrGroupTopic[1].split('=')[1]
		print userOrGroupTopic

		thread.start_new_thread( sampleFun, ("Thread-1", 2, sendMessageToUserOrGroup,userOrGroupTopic,message))
#		if i=="1":
#			thread.start_new_thread( sampleFun, ("Thread-1", 2, user1,message))
#		else:
#			thread.start_new_thread( sampleFun, ("Thread-2", 2, user2,message))
#			time.sleep(10)
#		thread.start_new_thread( sampleFun, ("Thread-2", 5, user2,message))

		c.send('Thank you for connecting')
		c.close()               		# Close the connection	
	except:
		print "Error: unable to start thread"
