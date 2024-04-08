import os
import sys
import socket
from cryptography.fernet import Fernet
import threading
username = input("Enter Username: ")

'''
def EncryptData(message):
    key = b'1wIZTRFxxYsIUsbm18dajfF8bj6_2FK4eX5oH7PzzLo='
    
    fernet = Fernet(key)
    
    encMessage = fernet.encrypt(message.encode())
    return encMessage
    
def DecryptData(message):
    key = b'1wIZTRFxxYsIUsbm18dajfF8bj6_2FK4eX5oH7PzzLo='
    
    fernet = Fernet(key)
    
    decMessage = fernet.decrypt(message)
    return decMessage
'''


# Create Socket for hosting
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print("IP from this Chat Room Server is {}   Port: 123".format(ip))
hostsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostsocket.bind((ip, 123))
hostsocket.listen(1)

print("Waiting for Connections")
connection, addr = hostsocket.accept()

while True:
    print(connection.recv(2048).decode("utf-8"))
    msg = input("Enter Message: ")
    connection.send(bytes("Message from {}: {}".format(username, msg), "utf-8"))
