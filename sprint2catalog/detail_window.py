import tkinter as tk
from tkinter import ttk

def new_ventana_desc(self,cell):
    root = tk.Toplevel()
    label1 = ttk.Label(root,image=cell.image_tk)
    label2 = ttk.Label(root,text=cell.title)
    label3 = ttk.Label(root,text=cell.description)
    label1.pack()
    label2.pack()
    label3.pack()
    root.mainloop()
