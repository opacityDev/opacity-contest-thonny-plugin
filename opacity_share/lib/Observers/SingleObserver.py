from Observers import Observer

class SingleObserver(Observer):

    def fired(self,event,e):
        self.onFired(event,e)