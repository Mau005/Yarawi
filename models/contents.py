

class Contents:
    """Class orientated for  contents in books for app
    """

    def __init__(self, **kargs):
        self.IdContents = kargs.get("IdContents")
        self.IdsBooks = kargs.get("IdsBooks")
        self.Content = kargs.get("Content")