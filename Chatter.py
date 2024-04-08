import socket
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
username = input("Whats your Username? \n")
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
socketconnecter = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketconnecter.connect((ip, 123))
socketconnecter.send(bytes("Chatter connected successfully!", "utf-8"))



def Send(connection):
    while True:
        msg = input("Enter Message: ")
        connection.send(bytes("Message from {}: {}".format(username, msg), "utf-8"))
        data = connection.recv(2048)
        if data != None:
            print(connection.recv(2048).decode("utf-8"))
        else: continue



while True:
    print(socketconnecter.recv(2048).decode("utf-8"))
    msg = input("Enter Message: ")
    socketconnecter.send(bytes("Message from {}: {}".format(username, msg), "utf-8"))


