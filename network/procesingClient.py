import socket
from core.tools import unpack, package

class ProcesingClient:
    """
    Procesing class for client, send big data for acocunt,
    procesing package distance for default in 1024
    or modified.
    """
    
    def __init__(self, **kargs):
        self.ip = kargs.get("ip")
        self.port = kargs.get("port")
        self.packagesend = kargs.get("packagesend")
        self.socket = self.ConnectionServer()

    def send(self, data) -> bool:
        """
        method procesing send package,
        or return bool if correct send or not
        """
        if isinstance(data, dict):
            self.socket.send(package(data))
            return True
        return False

    def receive(self):
        """
        Methodo receive package for server and procrsing packate size
        default mode or others
        """
        if self.packagesend is not None:
            return unpack(self.socket.receive(self.packagesend))
        return unpack(self.socket.receive(1024))

    def connectionServer(self) -> socket:
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
        
        