import tkinter as tk
class Watcher():

    PRESSED=1
    RELEASED=2


    def __init__(self,editor):
        self.codeview = editor.get_code_view()
        self.text = editor.get_text_widget()
        self.editor = editor
        # list to store keycode of currently pressed keys
        self._keys_stat = dict()
        self._combinations = dict()
        self.text.bind("<KeyPress>",self.key_pressed,True)
        self.text.bind("<KeyRelease>",self.key_released,True)
        pass

    def key_pressed(self,k):
        self._keys_stat[k.keycode] = Watcher.PRESSED
 

    def _define_combinations(self):
        # on Copy action
        def _on_copy(self):
            self
        copy = Watcher.key_combination(53,54,)
        
    def _copy_action():
        pass
    def key_released(self,event,k):
        self._keys_stat[k.keycode] = Watcher.RELEASED


    class key_combination():
        
        def __init__(self,keycode1,keycode2,runnable):
            self.keycode1 = keycode1
            self.keycode2 = keycode2
            self.runnable = runnable
    
