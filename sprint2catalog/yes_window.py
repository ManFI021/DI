import tkinter as tk
from tkinter import ttk


def show_yes_window(): 
    yes_root = tk.Tk()
    label = ttk.Label(yes_root,text="Estoy Cansado Jefe")
    label.pack()
    yes_root.mainloop()