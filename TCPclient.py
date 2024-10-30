# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 21:53:57 2024

@author: calik
"""
from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = bytes(input('Input lowercase sentence:'),'utf-8')
clientSocket.send(sentence)
modifiedSentence = clientSocket.recv(1024)
print('From Server:', modifiedSentence)
clientSocket.close()