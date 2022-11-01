from re import X
from tkinter import Label, Text, Toplevel
import tkinter as tk
from thonny import get_workbench 
from opacity_share.lib.watcher import Watcher
w1=Watcher()
def param():
    editor_notebook = get_workbench().get_editor_notebook() 
    w1.set_editor_notebook(editor_notebook)
 
def set_second_editor():
    w1.get_second_editor()
 
def load_plugin():
    get_workbench().add_command(command_id="opacity_contests_menu",
                                menu_name="tools",
                                command_label="OC Profile",
                                handler=param)
    get_workbench().add_command(command_id="opacity_second_editor",
                                menu_name="tools",
                                command_label="Set second editor",
                                handler=set_second_editor)
    pass


#content = get_workbench().get_editor_notebook().get_current_editor_content() 