

class ControlServer:

    def __init__(self, **kargs):
        self._listUser = {}
        self._listBand = []
        self._listActive = []
        self._listDesconection = []

    def addUser(self, user):
        self._listUser.update({user.cifrated:user})

    def addDesconection(self, user):
        self._listDesconection.append(user.cifrated)

    def update(self, *args):
        if len(self._listDesconection) >= 1:
            for user in self._listDesconection:
                self._listUser.pop(user.cifrated)
            self._listDesconection.clear()




