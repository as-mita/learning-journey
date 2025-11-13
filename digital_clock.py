# digital_clock.py — Simple Tkinter Digital Clock
import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("⏰ Digital Clock")

label = tk.Label(root, font=("Arial", 50, "bold"), background="black", foreground="cyan")
label.pack(anchor="center")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

time()
root.mainloop()
