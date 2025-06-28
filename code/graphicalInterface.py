import tkinter as tk
from tkinter import messagebox

from controller import run as run_controller

def run():
    root = tk.Tk()
    root.title("first title")
    label = tk.Label(root, text="first label")
    label.pack(padx=20, pady=20)
    
    #gui elements
    entry = tk.Entry(root, width=30)
    entry.pack(padx=10, pady=5)


    def on_create_folder():
        enteredFolderName = entry.get()
        run_controller(enteredFolderName)


    create_button = tk.Button(root, text="Create Folder", command=on_create_folder)
    create_button.pack(padx=10, pady=10)

    root.mainloop()



