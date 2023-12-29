import pyautogui
import threading
import keyboard  
import tkinter as tk
from tkinter.font import Font

class AutoClicker:
    def __init__(self, app):
        self.app = app
        self.is_clicking = False
        self.click_thread = None
        self.infinite_mode = False
        self.num_clicks_var = tk.StringVar(app, '0') 

    def toggle_clicking(self, event=None):
        if self.is_clicking:
            self.stop_clicking()
        else:
            self.start_clicking()

    def start_clicking(self):
        try:
            clicks_per_pack = int(click_pack.get("1.0", "end-1c"))
            delay = float(click_delay.get("1.0", "end-1c"))
            if not self.infinite_mode:
                total_clicks = int(number_of_clicks.get("1.0", "end-1c")) * clicks_per_pack
            else:
                total_clicks = float('inf')
        except ValueError:
            print("Por favor, insira números válidos.")
            return

        self.is_clicking = True
        self.click_thread = threading.Thread(target=self.perform_clicking, args=(clicks_per_pack, delay, total_clicks))
        self.click_thread.daemon = True
        self.click_thread.start()

    def stop_clicking(self):
        self.is_clicking = False

    def perform_clicking(self, clicks_per_pack, delay, total_clicks):
        num_clicked = 0
        while self.is_clicking and (self.infinite_mode or num_clicked < total_clicks):
            for _ in range(clicks_per_pack):
                if not self.is_clicking:
                    return
                pyautogui.click()
                num_clicked += 1
                self.app.after(0, self.num_clicks_var.set, str(num_clicked))
                if not self.infinite_mode and num_clicked >= total_clicks:
                    return
            pyautogui.sleep(delay)

    def toggle_infinite_mode(self):
        self.infinite_mode = not self.infinite_mode
        if not self.infinite_mode:
            self.num_clicks_var.set('0')  

def on_enter_press():
    auto_clicker.toggle_clicking()

app = tk.Tk()
app.title("Só os Lagados")
app.geometry("220x270")

solFont = Font(family="Helvetica", size=16)

auto_clicker = AutoClicker(app)

name_label = tk.Label(app, text="SoL - Auto Clicker", font=solFont)
name_label.place(x=20, y=10)

click_pack_label = tk.Label(app, text="Cliques por Pacote")
click_pack_label.place(x=10, y=40)
click_pack = tk.Text(app, height=1, width=5)
click_pack.place(x=150, y=40)

click_delay_label = tk.Label(app, text="Delay entre Pacotes (s)")
click_delay_label.place(x=10, y=70)
click_delay = tk.Text(app, height=1, width=5)
click_delay.place(x=150, y=70)

number_of_clicks_label = tk.Label(app, text="Número Total de Pacotes")
number_of_clicks_label.place(x=10, y=100)
number_of_clicks = tk.Text(app, height=1, width=5)
number_of_clicks.place(x=150, y=100)

clicks_label = tk.Label(app, text="Cliques dados:")
clicks_count_label = tk.Label(app, textvariable=auto_clicker.num_clicks_var)
clicks_label.place(x=10, y=160)
clicks_count_label.place(x=100, y=160)

infinite_mode_var = tk.BooleanVar()
infinite_checkbox = tk.Checkbutton(app, text="Modo Infinito", variable=infinite_mode_var, command=auto_clicker.toggle_infinite_mode)
infinite_checkbox.place(x=55, y=130)

start_button = tk.Button(app, text="[ENTER]", command=auto_clicker.toggle_clicking)
start_button.place(x=10, y=190)

use_mode_label = tk.Label(app, text="Iniciar / Parar")
use_mode_label.place(x=70, y=193)

italic_font = Font(family="Helvetica", size=10, slant="italic")

created_by_label = tk.Label(app, text="By: [SoL] Inhumanity", font=italic_font)
created_by_label.place(x=45, y=240)

keyboard.add_hotkey('enter', on_enter_press)

app.mainloop()

keyboard.remove_hotkey('enter')
