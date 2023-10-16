import tkinter as tk
from tkinter import ttk

def show_no_window(): 
    no_root = tk.Tk()
    label = ttk.label(no_root,text="No Mientas y Descansa")
    label.pack()
    no_root.mainloop()