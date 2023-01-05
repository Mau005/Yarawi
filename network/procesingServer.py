from core.tools import unpack, package


class ProcesingServer:
    def __init__(self, **kargs):
        self.client = kargs.get("client")
        self.addr = kargs.get("addr")
        self.motd = kargs.get("motd")
        self.cifrated = 0
        self.status = True

    @property
    def cifrated(self):
        return self._cifrated

    @cifrated.getter
    def cifrated(self):
        return self._cifrated
    @cifrated.setter
    def cifrated(self, value):
        self._cifrated = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @status.getter
    def status(self):
        return self._status

    def send(self, pack):
        self.client.send(package(pack))

    def receive(self):
        return unpack(self.client.recv(1024))

    def run(self, *args):
        while self.status:
            data = self.receive()
            if data is not None:
                self.procesing(data)

    def procesing(self, data):
        if data.get("status") == "init":
            self.send({"status":True})
