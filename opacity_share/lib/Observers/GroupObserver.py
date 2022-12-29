from Observers import Observer
from lib import UniqueList

class GroupObserver(Observer,UniqueList):
    
    def __init__(self):
        super(UniqueList,self).__init__(Observer)
    
    def addObserver(self,observer):
        self.add(observer)
    
    def removeEvent(self,observer):
        self.remove(observer)

    def fired(self,event,e):
        with self._lock:
            for observer in self.items:
                observer.fired(event,e)
    




    
