import socket, sys
import threading

from network.procesingServer import ProcesingServer


class Server:
    
    def __init__(self, **kargs):
        self.ip = kargs.get("ip")
        self.port = kargs.get("port")
        self.motd = kargs.get("motd")
        self.socket = None
        self.listUser = []
        
    def generate_socket(self) -> socket:
        try:
            sock = socket.socket()
            sock.bind((self.ip, self.port))
            sock.listen(0)
            return sock
        except TypeError as error:
            input("Error IP or Port is None, press key to continue")
            sys.exit(1)
        
    def run(self):
        self.socket = self.generate_socket()
        print("Servidor iniciado")
        while self.socket is not None:
            clt, addr = self.socket.accept()
            obj = ProcesingServer(client = clt, addr = addr, motd = self.motd)
            self.listUser.append(obj)
            th = threading.Thread(target = obj.run)
            th.start()
            
        self.socket.close()
        print("Servidor Cerrado")
            
        
        
if __name__ == "__main__":
    server = Server(ip="127.0.0.1", port=7171, motd="Bienvenidos a la app")
    server.run()