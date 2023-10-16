import threading
import requests
import tkinter as tk
from tkinter import ttk
from MainWindow import MainWindow
class LoadingWindow:
    def __init__(self,root) -> None:
        self.root = root
        self.root.title("Cargando...")
        self.root.resizable(False,False)

        self.label = tk.Label(self.root,text="Cargando datos...",font=("Arial",14))
        self.label.pack(side=tk.TOP,pady=10)

        label_bg_color = self.label.cget("bg")

        self.canvas = tk.Cancas(self.root,width=60,height=60,bg=label_bg_color)
        self.canvas.pack()

        self.progress = 0

        self.draw_progress_circle(self.progress)

        self.update_progress_circle()

        self.thread = threading.Thread(target=self.fetxh_json_data)
        self.thread.start()

    def draw_progress_circle(self,progress):
       self.canvas.delete("progress")
       angle = int(360 *(progress/100)) 
       self.canvas.create_arc(10,10,35,35,start=0,extent=angle,tags="progress",outline='green',width=4,style=tk.ARC)

    def update_progres_circle(self):
        if self.progress < 100:
            self.progress +=10
        else:
            self.progress = 0
        self.draw_progress_circle(self.progress)
        self.root.after(100,self.update_progres_circle)      
    def fetch_json_data(self):
        response = requests.get("")
        if response.status_code==200:
            json_data = response.json
            self.root.quit()
            launch_main_window(json_data)
def launch_main_window(json_data):
    root=tk.Tk()
    app=MainWindow(root,json_data)
    root.mainloop()                 
