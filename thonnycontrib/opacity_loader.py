from tkinter import Label, Text, Toplevel
import tkinter as tk
from thonny import get_workbench
from thonnycontrib.oc.pages.Login.page import LoginPage



def param():
    loginPage = LoginPage(get_workbench())
    loginPage.run() 
    
def load_plugin():
    get_workbench().add_command(command_id="opacity_contests_menu",
                                menu_name="tools",
                                command_label="OC Profile",
                                handler=param)


#content = get_workbench().get_editor_notebook().get_current_editor_content() 