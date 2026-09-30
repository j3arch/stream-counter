import tkinter as tk
import os

def timer_gui():
    file_path = "timer.txt"

    try:
        if os.path.exist(file_path):
            with open(file_path, "r") as file:
                timer_text = file.read()

        else:
            timer_text = "file not found"
    except Exception as e:
        timer_text = "error reading file"

    if not timer_text:
        timer_text = "0"

    time_label.config(text=timer_text)
    root.after(1000, timer_gui)

root = tk.Tk()
root.title("Strem counter")
root.geometry("300x150")

time_label = tk.Label(
    root, 
    text="Loading...", 
    font=("Helvetica", 48, "bold"), 
    bg="#2c3e50", 
    fg="#ecf0f1"
)
time_label.pack(expand=True)

timer_gui()


root.mainloop()