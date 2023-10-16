from tkinter import ttk,Button
from yes_window import show_yes_window
from no_window import show_no_window

class MainWindow:
    def on_button_click(self):
        pass
    def __init__(self,root):
       self.root = root
       #Creacion boton si
       self.button = ttk.Button(self.root,text="Si",command=show_yes_window)
       self.button.pack()
       #Creacion boton no
       self.button = ttk.Button(self.root,text="No",command=show_no_window)
       self.button.pack()