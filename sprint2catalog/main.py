from tkinter import Tk
from MainWindow import MainWindow
from ventana_de_carga import LoadingWindow

if __name__ == "__main__":
    root = Tk()
    # Crear e iniciar la ventana de carga
    loading_window = LoadingWindow(root)
    root.mainloop()