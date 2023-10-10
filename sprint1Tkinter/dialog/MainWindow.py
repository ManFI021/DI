from tkinter import ttk, Tk, messagebox
from Cell import Cell
import tkinter as tk
from detail_window import new_ventana_desc

class MainWindow:
    image_references = []
    def on_button_clicked(self, cell):
        new_ventana_desc(cell)

    def __init__(self, root):
        root.title("MainWindow")
        self.cells = [
            Cell("Victini", "C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\data\\unedited\\victini.png","""Las referencias a Pokemon en clase me hicieron poner esta imagen,Victini, el encantador Pokémon de la victoria, irradia alegría y poder. Con orejas en forma de V , canaliza energía positiva para impulsar la fortuna y éxito.
                 Su presencia trae suerte a entrenadores, brindándoles vitalidad y determinación en sus desafíos. Un compañero inspirador."""),
            Cell("Meme 1", "C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\data\\unedited\\meme1.jpg","""El meme de -Press Any Key- de Los Simpson satiriza la simplicidad tecnológica. Homer busca la tecla -Any Key-,
                 resaltando humorísticamente la confusión ante instrucciones básicas, resonando con las experiencias cotidianas de usuarios tecnológicamente desafiantes."""),
            Cell("Meme 2", "C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\data\\unedited\\meme2.jpg","""Meme que se hizo viral tras la llegada de las elecciones en diferentes países,incluyendo España"""),
            Cell("Meme 3", "C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\data\\unedited\\meme3.jpg","""El propio meme se autodefine,(llevo mucho tiempo con el ejercicio por culpa de un espacio en blanco)"""),
            Cell("Bmo", "C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\data\\unedited\\bmo.png","""Es una consola adorable y multifuncional con conciencia propia. Su personalidad juguetona y versatilidad hacen de él un entrañable amigo para Finn y Jake,los protagonistas,
                  fusionando tecnología avanzada con encanto infantil en el extravagante mundo de Ooo.""")
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