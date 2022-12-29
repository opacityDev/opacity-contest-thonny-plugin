from lib import Coordinator
from lib.Observers import SingleObserver
from thonny import get_workbench 

def main():
    editor_notebook = get_workbench().get_editor_notebook()
    coordinator1 = Coordinator(editor_notebook.get_current_editor())
    coordinator1.listenTo("keypress")
    
    pass