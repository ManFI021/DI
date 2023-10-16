import tkinter as tk
from PIL import Image, ImageTk


class Cell():
    def __init__(self, title, path,description):
        self.title = title
        self.path = path
        self.image_tk = self.load_and_resize_image()
        self.description = description
#funcion de resize de imagenes
    def load_and_resize_image(self):
        original_image = Image.open(self.path)
        resized_image = original_image.resize((100,100),Image.LANCZOS)
        image_tk = ImageTk.PhotoImage(resized_image)
        return image_tk