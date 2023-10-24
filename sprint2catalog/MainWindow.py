from tkinter import ttk, Tk, messagebox
from Cell import Cell
import tkinter as tk
from detail_window import new_ventana_desc
from PIL import Image,ImageTk
from io import BytesIO
import requests

class MainWindow:
    image_references = []
    def on_button_clicked(self, cell):
        new_ventana_desc(self,cell)

    def __init__(self,root,json_data):
        self.root = root
        self.root.title("MainWindow")        
        #for each crea celdas por objeto json
        self.cells = [Cell(cell['name'],load_image_from_url(cell['image_url']),cell['description']) for cell in json_data]
        for i, cell in enumerate(self.cells):
            self.image_references.append(cell.image_tk)
            label = ttk.Label(root, image=cell.image_tk, text=cell.title, compound=tk.BOTTOM)
            label.grid(row=i, column=0)
            label.bind("<Button-1>", lambda event, celda=cell: self.on_button_clicked(celda))
        #redimension de Mainwindow 
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth())/2
        y = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth())/2
        self.root.geometry(f"+{int(x)}+{int(y)}")
if __name__ == "__main__":
    root = Tk()
    app = MainWindow(root)
    root.mainloop()
def load_image_from_url(url):
    response = requests.get(url)
    img_data = Image.open(BytesIO(response.content))
    img = ImageTk.PhotoImage(img_data)
    return img


# x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth())/2
# y = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth())/2
# self.root.geometry(f"+{int(x)}+{int(y)}")