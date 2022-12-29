from lib2to3.pgen2.token import NEWLINE
import tkinter as tk
import time
class Watcher():

    PRESSED=1
    RELEASED=2


    def __init__(self):
        pass

    def set_editor_notebook(self,editor_notebook):
        editor = editor_notebook.get_current_editor()
        self.codeview = editor.get_code_view()
        self.text = editor.get_text_widget()
        self.editor = editor
        self.editor_notebook = editor_notebook
        # list to store keycode of currently pressed keys
        self.keys_stat = dict()
        self._controls = list()
        self._define_controls()
        self.text.bind("<KeyPress>",self.key_pressed,True)
        self.text.bind("<KeyRelease>",self.key_released,True)
        self.text.bind("<<Undo>>", self._on_undo, True)
        self.text.bind("<<Redo>>", self._on_redo, True)
        self.text.bind("<<Cut>>", self._on_cut, True)
        self.text.bind("<<Copy>>", self._on_copy, True)
        self._releasing = False 
        
        def test(selfo,*args):
            if not hasattr(self,"second_editor"):
                return

            print("a7a " + f'{args}')
            self.second_editor.get_code_view()._vertical_scrollbar_update(selfo,args)
            editor.get_code_view()._vertical_scrollbar_update(selfo,args)
        self.text["yscrollcommand"]=test

        self.text.bind()

    def get_second_editor(self):
        self.second_editor=self.editor_notebook.get_current_editor()    

    def key_pressed(self,k):
        
        if k.keycode not in self.keys_stat:
            self.keys_stat[k.keycode] = {"last_pressed":time.time(),
                                        "last_released":-1,
                                        "stat":Watcher.PRESSED
                                        }
        else:
            self.keys_stat[k.keycode]["stat"] = Watcher.PRESSED
            self.keys_stat[k.keycode]["last_pressed"] = time.time()

        for control in self._controls:
            control.check(self,k) 
        index = self.text.index("insert")
        if index and "." in index:
                line, col = index.split(".")    
                print(("Key [{}] [{}] pressed @  {} : {}".format(k.char,k.keycode,line, int(col) + 1)))
        
    def _on_copy(self,e):
        print("copy")

    def _on_paste(self,e):
        print("paste")

    def _on_undo(self,e):
        print("undo")

    def _on_redo(self,e):
        print("redo")

    def _on_cut(self):
        pass

    def _on_tab(self):
        pass

    def _on_selection(self):
        pass

    def on_insert(self):
        
        pass

    def _define_controls(self):
        # on Copy action
        def _on_copy(self):
            tk.messagebox.showinfo(title=None,message="You copied sth i see you")
        def _on_myster(self):
            tk.messagebox.showinfo(title=None,message="You did run the myster sth i see you")
        self.add_control(Watcher.Combo(_on_myster,37,58))
        self.add_control(Watcher.Combo(_on_copy,37,55))

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
                    prev_key = self.keys[i-1]
                    prev_key_stat = watcher.keys_stat[prev_key] 
                    if (key_stat['last_pressed'] < prev_key_stat['last_pressed']):
                        return
                  
                    
            print(key_stat['last_released'],prev_key_stat['last_released'])
            self.action(watcher)

