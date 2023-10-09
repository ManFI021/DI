import tkinter as tk
from PIL import Image, ImageTk

class Cell():
    def __init__(self, title, path):
        self.title = title
        self.path = path
        self.image_tk = self.load_image()

    def load_image(self):
        image = Image.open(self.path)
        image_tk = ImageTk.PhotoImage(image)
        return image_tk