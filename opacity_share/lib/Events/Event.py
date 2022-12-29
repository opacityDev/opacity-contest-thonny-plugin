from Exceptions import unimplementedAbstractFunction
from Iterable import Iterable
from Observers.Observer import Observer

class Event(Iterable):

    def __init__(self):
        super().__init__(Observer)
 
    def __fireObservers(self):
        with self._lock:
            for observer in self.items:
                observer.fire()

    def happened():
        raise unimplementedAbstractFunction
