import socket
from core.tools import unpack, package

class ProcesingClient:
    
    def __init__(self, **kargs):
        self.socket = socket.socket()
        self.socket.connect(("127.0.0.1", 7171))
        
        test = {"Hola": "Adios"}
        test = package(test)
        self.socket.send(test)
        packageReceive = unpack(self.socket.recv(1024))
        print(packageReceive)
        
        