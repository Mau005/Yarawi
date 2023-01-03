import socket
from core.tools import unpack, package

class ProcesingClient:
    
    def __init__(self, **kargs):
        self.ip = kargs.get("ip")
        self.port = kargs.get("port")
        self.socket = self.ConnectionServer()
        
    def ConnectionServer(self) -> socket:
        try:
            sock = socket.socket()
            sock.connect(("127.0.0.1", 7171))
            return sock
        except TypeError as error:
            print(error)
            return None
        except ConnectionRefusedError as error:
            print(error)
            return None
        
        