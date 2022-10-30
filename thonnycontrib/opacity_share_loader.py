from re import X
from tkinter import Label, Text, Toplevel
import tkinter as tk
from thonny import get_workbench 
from thonnycontrib.opacity_share.lib.watcher import Watcher

def param():
    editor_notebook = get_workbench().get_editor_notebook()
    text_widget = editor_notebook.get_current_editor().get_text_widget()
    w1 = Watcher(text_widget)
    pass  
 

 
def load_plugin():
    get_workbench().add_command(command_id="opacity_contests_menu",
                                menu_name="tools",
                                command_label="OC Profile",
                                handler=param)
    pass


#content = get_workbench().get_editor_notebook().get_current_editor_content() 