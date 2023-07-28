import tkinter as tk
from tkinter import ttk

# GUI
window = tk.Tk()


# Instruction
ttk.Label(master=window, text = 'GPT').pack()

# Message Entry Box
entry = tk.Entry(master = window)
entry.pack()

window.mainloop()