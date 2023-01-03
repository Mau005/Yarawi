class Accounts:
    """Class orientated manager for account in procesing for login and send information
    """

    def __init__(self, **kargs):
        self.IdAccount = kargs.get("IdAccount")
        self.NameAccount = kargs.get("NameAccount")
        self.PassAccount = kargs.get("PassAccount")
        self.DateCreate = kargs.get("DateCreate")
        self.IsActive = kargs.get("IsActive")
        self.DirectionAccount = kargs.get("DirectionAccount")