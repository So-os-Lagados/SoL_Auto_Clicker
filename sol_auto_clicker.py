import pyautogui
import tkinter as tk
from threading import Thread
import time

class AutoclickerApp:
    def __init__(self, master):
        self.master = master
        master.title("Autoclicker")

        self.running = False

        self.start_button = tk.Button(master, text="Iniciar", command=self.toggle_autoclicker, width=20)
        self.start_button.pack()

        self.quit_button = tk.Button(master, text="Sair", command=master.quit, width=20)
        self.quit_button.pack()


        master.bind('<Return>', self.handle_keypress)

    def toggle_autoclicker(self):
        if not self.running:
            self.running = True
            self.start_button.config(text="Parar")
            self.start_autoclicker()
        else:
            self.running = False
            self.start_button.config(text="Iniciar")

    def start_autoclicker(self):
        cliques_por_grupo = 5
        tempo_de_espera = 1  

        def autoclick():
            while self.running:
                for _ in range(cliques_por_grupo):
                    pyautogui.click()
                    time.sleep(tempo_de_espera) 

        autoclick_thread = Thread(target=autoclick)
        autoclick_thread.start()

    def handle_keypress(self, event):
        self.toggle_autoclicker()

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoclickerApp(root)
    root.mainloop()
