import pathlib
import tkinter as tk
import tkinter.ttk as ttk
import pygubu

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "design.ui"


class LoginPage:

    def __init__(self, master=None):

        # 3: Create Builder
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)

        # 2: Load an ui file
        builder.add_from_file(PROJECT_UI)

        # 3: Create the mainwindow
        self.mainwindow = builder.get_object('oc_login', master)

        # 4: Connect callbacks
        builder.connect_callbacks(self)
        master.update()
        self.mainwindow.geometry("+%d+%d" % (master.winfo_x() + (master.winfo_width()/4),
                                            master.winfo_y() + (master.winfo_height()/4)))

    def run(self):
        self.mainwindow.mainloop()

 