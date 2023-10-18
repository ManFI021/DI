import threading
import requests
import tkinter as tk
from tkinter import ttk
from MainWindow import launch_main_window


class LoadingWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Cargando...")
        self.root.resizable(False, False)

        self.label = tk.Label(self.root, text="Cargando datos...", font=("Arial", 14))
        self.label.pack(side=tk.TOP, pady=10)

        label_bg_color = self.label.cget("bg")

        self.canvas = tk.Canvas(self.root, width=60, height=60, bg=label_bg_color)
        self.canvas.pack()

        self.progress = 0

        self.draw_progress_circle(self.progress)

        self.update_progress_circle()
        self.start_fetching_thread()
        self.fetch_json_data()
        self.check_thread()
       

    def draw_progress_circle(self, progress):
        self.canvas.delete("progress")
        angle = int(360 * (progress / 100))
        self.canvas.create_arc(10, 10, 35, 35, start=0, extent=angle, tags="progress", outline='green', width=4,
                               style=tk.ARC)

    def update_progress_circle(self):
        if self.progress < 104:
            self.progress += 14        
        else:
            self.progress = 0
        self.draw_progress_circle(self.progress)
        self.root.after(100, self.update_progress_circle)
    
    def fetch_json_data(self):
        response = requests.get("https://raw.githubusercontent.com/ManFI021/DI/main/catalog.json")
        if response.status_code == 200:
            self.json_data = response.json()
            self.finished = True

    
    def start_fetching_thread(self):
        fetch_thread = threading.Thread(target=self.fetch_json_data)
        fetch_thread.start()

    def check_thread(self):
        if self.finished:
            self.root.destroy()
            launch_main_window(self.json_data)
        else:
            self.root.after(100,self.check_thread)              