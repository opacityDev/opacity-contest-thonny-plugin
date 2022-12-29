from Exceptions import unimplementedAbstractFunction  
from threading import Lock

class Iterable:
    def __init__(self,cls=None):
        self._lock = Lock()
        self.__cls = cls
        self.__types = {}

    def addItemType(self,itemType,itemCls):
        self.__types[itemType] = itemCls

    def canBeHandled(self,item,itemType=None):
        if itemType is not None:
            if (isinstance(item,self.__types[itemType])):
                return True
        elif self.__cls is None:
            return True
        return isinstance(item,self.__cls)

    def add(self,item):
        raise unimplementedAbstractFunction

    def remove(self,item):
        raise unimplementedAbstractFunction


class UniqueList(Iterable):
    def __init__(self,cls=None):
        super().__init__(cls)
        self.items = set()
     
    def add(self,item,itemType=None):
        if (not super().canBeHandled(item,itemType)):
            raise TypeError
        with self._lock:
            self.items.add(item)

    def remove(self,item,itemType=None):
        with self._lock:
            if (not self.canBeHandled(item,itemType) or  item not in self.item ):
                raise TypeError
            self.items.remove(item)

    def getItem(self,index):
        if index < len(self.items):
            raise IndexError
        return self.items[index]

class Dict(Iterable):

    def __init__(self,kcls=None,vcls=None):
        super().__init__()
        self.addItemType("key",kcls)
        self.addItemType("value",vcls)
        pass

    def add(self,key,value):
        if (not self.canBeHandled(key,"key") or not self.canBeHandled(value,"value")):
            raise TypeError
        with self._lock:
            self.items.put(key,value)

    def remove(self,key):
        with self._lock:
            if key not in self.items:
                raise KeyError
            self.items.remove(key)

    def getItem(self,key):
        if (key not in self.items):
            raise KeyError
        return self.items[key]
        
