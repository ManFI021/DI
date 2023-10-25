from tkinter import Frame, ttk, Tk, messagebox, Canvas, Scrollbar
from Cell import Cell
import tkinter as tk
from detail_window import new_ventana_desc
from PIL import Image,ImageTk
from io import BytesIO
import requests

class MainWindow:
    image_references = []
    def on_button_clicked(self, cell):
        #cell argument error arreglado (self)
        new_ventana_desc(self,cell)

    def __init__(self,root,json_data):
        self.root = root
        self.root.title("MainWindow")
        
        # Canvas para scrolling
        self.canvas = Canvas(root)
        self.scrollbar= Scrollbar(self.root,orient="vertical",command=self.canvas.yview)
        self.scrollable_frame = Frame(self.canvas)
        
        # ScrollBar Configuracion
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        
        # Frame dentro del canvas para cada celda
        self.canvas.create_window((0,0),window=self.scrollable_frame,anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
         #for each crea celdas por objeto json
        self.cells = [Cell(cell['name'], load_image_from_url(cell['image_url']), cell['description']) for cell in json_data]
        
        for i, cell in enumerate(self.cells):
            label = ttk.Label(self.scrollable_frame, image=cell.image_tk, text=cell.title, compound=tk.BOTTOM)
            label.grid(row=i, column=0)
            label.bind("<Button-1>", lambda event, celda=cell: self.on_button_clicked(celda))
        
        self.canvas.grid(row=0,column=0,sticky="nsew")
        self.scrollbar.grid(row=0,column=1,sticky="ns")

        self.root.grid_rowconfigure(0,weight=1)
        self.root.grid_columnconfigure(0,weight=1)

        # Centrar celdas
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2
        self.root.geometry(f"+{int(x)}+{int(y)}")
       
        barra_menus = tk.Menu()
        # Crear el primer menú.
        menu_archivo = tk.Menu(barra_menus, tearoff=False)
        menu_archivo.add_command(
        label="Acerca de",
            accelerator="",
            #funcion descriptiva del desarrollador
            command=mensaje_extres
        )
        # Asociar el atajo del teclado del menú "Acerca de".
        root.bind_all("<Control-n>", mensaje_extres)
        # Agregarlo a la barra.
        barra_menus.add_cascade(menu=menu_archivo, label="Ayuda")
        root.config(menu=barra_menus)


def mensaje_extres(event=None):
    messagebox.showinfo("Mensaje","Lo que llevo sufrido en este boletín no tiene nombre :)")
       

if __name__ == "__main__":
    root = Tk()
    app = MainWindow(root)
    
    root.mainloop()

def load_image_from_url(url):
    response = requests.get(url)
    img_data = Image.open(BytesIO(response.content))
    img = ImageTk.PhotoImage(img_data)
    return img
