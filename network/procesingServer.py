from core.tools import unpack, package


class ProcesingServer:
    def __init__(self, **kargs):
        self.client = kargs.get("client")
        self.addr = kargs.get("addr")
        self.motd = kargs.get("motd")
        self.status = True
        
    def send(self,pack):
        self.client.send(package(pack))
        
    def receive(self):
        return unpack(self.client.recv(1024))

    def run(self):
        while self.status:
            print("Cliente iniciado")
            obj = self.receive()
            print(obj)