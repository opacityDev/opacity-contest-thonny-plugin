import tkinter as tk
class Watcher():
    PRESSED=1
    RELEASED=2


    def __init__(self,text):
        
        # list to store keycode of currently pressed keys
        self._keys_stat = dict()
        self._combinations = dict()
        text.bind("<KeyPress>",self.key_pressed,True)
        text.bind("<KeyRelease>",self.key_released,True)
        pass

    def key_pressed(self,k):
        self._keys_stat[k.keycode] = Watcher.PRESSED
 

    def _define_combinations(self):
        copy = Watcher.key_combination(53,54)
        
    def _copy_action():
        pass
    def key_released(self,event,k):
        self._keys_stat[k.keycode] = Watcher.RELEASED


    class key_combination():
        
        def __init__(self,keycode1,keycode2):
            self.keycode1 = 
    