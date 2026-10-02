import tkinter as tk
import os
from shortcut_service import terminal_controller

def timer_gui() -> None:
    file_path = "timer.txt"

    try:
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as file:
                timer_text = file.read().strip()
        else:
            timer_text = "file not found"
    except OSError:
        timer_text = "error reading file"

    if not timer_text:
        timer_text = "0"

    time_label.config(text=timer_text)
    root.after(1000, timer_gui)

root = tk.Tk()
root.title("Strem counter")
root.geometry("600x400")

time_label = tk.Label(
    root, 
    text="Loading...", 
    font=("Helvetica", 48, "bold"), 
    bg="#2c3e50", 
    fg="#ecf0f1"
)

terminal = terminal_controller()
terminal.pack(expand=True, fill="both", padx=5, pady=5)
time_label.pack(expand=True)


timer_gui()
root.mainloop()