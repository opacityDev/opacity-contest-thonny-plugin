from Exceptions import unimplementedAbstractFunction

class Observer:
    
    def fired(self,event,e):
        raise unimplementedAbstractFunction

    def __onFired(self,event,e):
        self.handler.analyze(event,e)

    def setHandler(self,handler):
        self.handler = handler