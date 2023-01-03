
class User:
    def __init__(self, **kargs):
        self.IdUser = kargs.get("IdUser")
        self.Name = kargs.get("Name")
        self.LastName = kargs.get("LastName")
        self.Age = kargs.get("Age")