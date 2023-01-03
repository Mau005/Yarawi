from kivymd.app import MDApp
from network.procesingClient import ProcesingClient

class Kimn(MDApp):
    def __init__(self, **kargs):
        MDApp.__init__(self, **kargs)
        test = ProcesingClient()
    
    def build(self):
        return 

if __name__=="__main__":
    Kimn().run()