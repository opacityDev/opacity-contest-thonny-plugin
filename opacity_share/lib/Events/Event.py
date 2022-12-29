from Exceptions import unimplementedAbstractFunction
from Iterable import Iterable
from Observers.Observer import Observer

class Event(Iterable):

    def __init__(self):
        super().__init__(Observer)
 
    def __fireObservers(self,e):
        with self._lock:
            for observer in self.items:
                observer.fire(self,e)

    def happened(self,e):
        self.__fireObservers(e)
