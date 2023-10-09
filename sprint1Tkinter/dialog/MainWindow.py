import tkinter as tk
from tkinter import ttk, Tk, messagebox
from PIL import Image, ImageTk
from Cell import Cell

class MainWindow:
    image_references = []

    def on_button_clicked(self, cell):
        message = "Has hecho clic en la celda " + cell.title
        messagebox.showinfo("Informacion", message)

    def __init__(self, root):
        root.title("MainWindow")
        #Ruta Imagenes edited
        self.cells = [
            Cell("Victini", r"C:\msys64\home\Alumno\DI\sprint1Tkinter\catalog\data\edited\169px-Victini_(20_aniversario)_resized.png"),
            Cell("Meme 1", r"C:\msys64\home\Alumno\DI\sprint1Tkinter\catalog\data\edited\IMG_20231004_140354_resized.jpg"),
            Cell("Meme 2", r"C:\msys64\home\Alumno\DI\sprint1Tkinter\catalog\data\edited\IMG_20231004_140344_resized.jpg"),
            Cell("Meme 3", r"C:\msys64\home\Alumno\DI\sprint1Tkinter\catalog\data\edited\a62e3935390bcf16d136c4760f087ad0_resized.jpg"),
            Cell("Bmo", r"C:\msys64\home\Alumno\DI\sprint1Tkinter\catalog\data\edited\25f68acc5bfc7e5f149a714c6a660353_resized.png"),
        ]

        for i, cell in enumerate(self.cells):
            image_tk = ImageTk.PhotoImage(file=cell.path)
            self.image_references.append(image_tk)
            #Añadir la referencia de la imagen correspondiente para evitar PhotoImage Error
            label = ttk.Label(root, image=image_tk, text=cell.title, compound=tk.BOTTOM)
            label.grid(row=i, column=0)
            label.bind("<Button-1>", lambda event, celda=cell: self.on_button_clicked(celda))

if __name__ == "__main__":
    root = Tk()
    app = MainWindow(root)
    root.mainloop()