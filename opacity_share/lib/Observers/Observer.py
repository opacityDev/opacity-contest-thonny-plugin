from Exceptions import unimplementedAbstractFunction

class Observer:
    _ids = 0
    
    def __init__(self):
        self.id = Observer._ids 
        Observer._ids+=1
    
    def fired(self,action):
        raise unimplementedAbstractFunction

    def onFired(self):
        raise unimplementedAbstractFunction

    def sendPacket(self):
        raise unimplementedAbstractFunction