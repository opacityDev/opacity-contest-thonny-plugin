from Observers import Observer
from lib import Dict
from Events import Event

class MultiObserver(Observer,Dict):
    
    def __init__(self):
        super(Dict,self).__init__(Event,int)
    
    def addEvent(self,event):
        self.add(event,0)
    
    def removeEvent(self,event):
        self.remove(event)

    def fired(self,event,e):
        with self._lock:
            if event not in self.items:
                return
            self.items[event] += 1
        if (all(v > 0 for v in self.items.values())):
            for k,v in self.items:
                self.items[k]-=1
            self.onFired(event,e)

    def __onFired(self, event, e):
        self.handler.analyze(event,e)
            
            