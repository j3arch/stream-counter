import tkinter as tk
import os

def read_text_file(path, fallback) -> str:
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read().strip() or fallback
    except OSError:
        return fallback

def timer_gui() -> None:
    timer_text = read_text_file("timer.txt", "00:00:00")
    milestones_text = read_text_file("milestones.txt", "0")


    time_label.config(text=timer_text)
    milestones_label.config(text=f"{milestones_text}")
    root.after(1000, timer_gui)

root = tk.Tk()
root.title("Stream counter")
root.geometry("600x400")

time_label = tk.Label(
    root, 
    text="Loading...", 
    font=("Helvetica", 48, "bold"), 
    bg="#2c3e50", 
    fg="#ecf0f1"
)

milestones_label = tk.Label(
    root, 
    text="Loading...", 
    font=("Helvetica", 48, "bold"), 
    bg="#2c3e50", 
    fg="#ecf0f1"
)

time_label.pack(expand=True)
milestones_label.pack(expand=True)

timer_gui()
root.mainloop()