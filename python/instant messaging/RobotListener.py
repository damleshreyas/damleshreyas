'''
Author : 		Shreyas Damle
Desription :	This is sample robotfframework listener to send messagesg to skype service(SkypeServer.py) after completion of each test case and test suite.
'''

import socket               # Import socket module
import os
import sys
import time

class RobotListener():
	ROBOT_LISTENER_API_VERSION = 2

	def __init__(self,host,sendMessageToUserOrGroup,userOrGroupTopic):
		print sendMessageToUserOrGroup
		print userOrGroupTopic
		self.s = socket.socket()         # Create a socket object
		self.host = socket.gethostname() # Get local machine name
		self.port = 12346                # Reserve a port for your service.
		self.host=host
		self.sendMessageToUserOrGroup=sendMessageToUserOrGroup
		self.userOrGroupTopic=userOrGroupTopic
		self.testCaseName=""
		self.status=""
		self.message=""
		self.suitName=""
		self.statistics=""

	def end_test(self,name,attributes):
		self.s.connect((self.host, self.port))

		self.testCaseName=str(attributes['longname'])
		self.status=str(attributes['status'])
		self.message=self.testCaseName+" : "+self.status
		self.s.send(self.message)

		self.s.close()

	def end_suite(self,name,attributes):
		self.s.connect((self.host, self.port))
		message=""
		message="sendMessageToUserOrGroup="+self.sendMessageToUserOrGroup+";userOrGroupTopic="+self.userOrGroupTopic+";"
		self.suitName=str(attributes['longname'])
		self.statistics=str(attributes['statistics'])
		self.message=message+self.suitName+" : "+self.statistics
		self.s.send(self.message)

		self.s.close()

if __name__ == '__main__':
	i = 10
    print i