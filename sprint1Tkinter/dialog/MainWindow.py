from tkinter import ttk, Tk, messagebox
from Cell import Cell
import tkinter as tk

class MainWindow:
    image_references = []

    def on_button_clicked(self, cell):
        message = "Has hecho clic en la celda " + cell.title
        messagebox.showinfo("Informacion", message)

    def __init__(self, root):
        root.title("MainWindow")
        self.cells = [
            Cell("Victini", "C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\data\\unedited\\victini.png"),
            Cell("Meme 1", "C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\data\\unedited\\meme1.jpg"),
            Cell("Meme 2", "C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\data\\unedited\\meme2.jpg"),
            Cell("Meme 3", "C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\data\\unedited\\meme3.jpg"),
            Cell("Bmo", "C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\data\\unedited\\bmo.png")
        ]

        for i, cell in enumerate(self.cells):
            self.image_references.append(cell.image_tk)

            label = ttk.Label(root, image=cell.image_tk, text=cell.title, compound=tk.BOTTOM)
            label.grid(row=i, column=0)
            label.bind("<Button-1>", lambda event, celda=cell: self.on_button_clicked(celda))

if __name__ == "__main__":
    root = Tk()
    app = MainWindow(root)
    root.mainloop()