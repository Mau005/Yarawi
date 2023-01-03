

class Direction:
    def __init__(self, **kargs):
        self.Street = kargs.get("Street")
        self.Country = kargs.get("Country")
        self.City = kargs.get("City")
        self.StreetNumber = kargs.get("StreetNumber")
        self.PastCode = kargs.get("PastCode")