from lib2to3.pgen2.token import NEWLINE
import tkinter as tk
import time
class Watcher():

    PRESSED=1
    RELEASED=2


    def __init__(self,editor):
        self.codeview = editor.get_code_view()
        self.text = editor.get_text_widget()
        self.editor = editor
        # list to store keycode of currently pressed keys
        self.keys_stat = dict()
        self._controls = list()
        self._define_controls()
        self.text.bind("<KeyPress>",self.key_pressed,True)
        self.text.bind("<KeyRelease>",self.key_released,True)
        self._releasing = False 
    def key_pressed(self,k):
        
        if k.keycode not in self.keys_stat:
            self.keys_stat[k.keycode] = {"last_pressed":time.time(),
                                        "last_released":-1,
                                        "stat":Watcher.PRESSED
                                        }
        else:
            self.keys_stat[k.keycode]["stat"] = Watcher.PRESSED
            self.keys_stat[k.keycode]["last_pressed"] = time.time()

        index = self.text.index("insert")
        if index and "." in index:
                line, col = index.split(".")    
                print(("Key [{}] [{}] pressed @  {} : {}".format(k.char,k.keycode,line, int(col) + 1)))
        


    def _define_controls(self):
        # on Copy action
        def _on_copy(self)
            tk.messagebox.showinfo(title=None,message="You copied sth i see you")
        def on_myster(self):
            tk.messagebox.showinfo(title=None,message="You did run the myster sth i see you")
        self.add_control(Watcher.Combo(_on_copy,37,58))
    def key_released(self,event):
 
        index = self.text.index("insert")
        if index and "." in index:
                line, col = index.split(".")    
                print(("Key [{}] [{}] released @  {} : {}".format(event.char,event.keycode,line, int(col) + 1)))
         
        if event.keycode not in self.keys_stat:
            self.keys_stat[event.keycode] = {"last_pressed":-1,
                                        "last_released":time.time(),
                                        "stat":Watcher.RELEASED
                                        }
        else:
            self.keys_stat[event.keycode]["stat"] = Watcher.RELEASED
            self.keys_stat[event.keycode]["last_released"] = time.time()
             
        for control in self._controls:
            control.check(self,event ) 
         
    def add_control(self,control):
        self._controls.append(control)
    
    class Combo():

        TIMEGAP = 0.09
        
        def __init__(self,action,*keys):
            self.keys = keys
            self.action = action
            print("New Combo added {}".format(self.keys))

        def check(self,watcher,event):
            for i in range(0,len(self.keys)):
                key = self.keys[i]
                if (key not in watcher.keys_stat):
                    return 
                key_stat = watcher.keys_stat[key] 
                is_pressed = (
                    key_stat["stat"] == Watcher.PRESSED 
                    or time.time() - key_stat["last_released"] < float(Watcher.Combo.TIMEGAP)
                )
                if (not is_pressed):
                    return
                if (i!=0):
                    prev_key_stat = watcher.keys_stat[self.keys[i-1]]
                    if (key_stat['last_pressed'] < prev_key_stat['last_pressed']):
                        return
            print(key_stat['last_released'],prev_key_stat['last_released'])
            self.action(watcher)

