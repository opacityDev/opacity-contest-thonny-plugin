from Observers import Observer
from lib import Dict
from Events import Event

class MultiObserver(Observer,Dict):
    
    def __init__(self):
        super(Dict,self).__init__()
    
    def fired(self,action):
        with self._lock:
            if action not in self.items:
                return

            
            