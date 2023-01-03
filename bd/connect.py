

class Connect:
    
    def __init__(self, **kargs):
        self.ipBd = kargs.get("ip")
        self.port = kargs.get("port")
        self.bdName = kargs.get("bdname")
        self.user = kargs.get("user")
        self.passuser = kargs.get("passuser")
        
        