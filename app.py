import tkinter as tk
from tkinter import ttk
import encrypt


# Needed functions in this module

def sendToConsole():
    text = entry.get()
    encrypt.test(text)


# GUI
window = tk.Tk()

window.geometry("500x500")
window.title('Test App')

# Instruction
ttk.Label(master=window, text = 'Enter the text you would like to encrypt.').pack()

# Message Entry Box
entry = tk.Entry(master = window)
entry.pack()

# Button to Encrypt
encryptButton = ttk.Button(master = window, text = 'Encrypt', command=sendToConsole)
encryptButton.pack()

window.mainloop()
