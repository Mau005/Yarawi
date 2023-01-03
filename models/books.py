

class Books:
    """Class orientated title for books 
    """

    def __init__(self, **kargs):
        self.IdsBooks = kargs.get("IdsBooks")
        self.Title = kargs.get("Title")
        self.Description = kargs.get("Description")
        self.CountPages = kargs.get("CountPages")
        self.Starts = kargs.get("Starts")