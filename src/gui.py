import tkinter as tk
from timer_service import Timer, run_timer
from main import main

def gui():
    pass

root = tk.Tk()
root.title("Strem counter")
root.geometry("300x150")

time_label = tk.Label(root, text="00:00", font=("Arial", 40))
time_label.pack(expand=True)


root.mainloop()