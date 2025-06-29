import tkinter as tk
from tkinter import messagebox

from controller import run as run_controller
from controller import list_tags

def run():
    root = tk.Tk()
    root.title("first title")
    label = tk.Label(root, text="first label")
    label.pack(padx=20, pady=20)
    
    #gui elements
    entry = tk.Entry(root, width=30)
    entry.pack(padx=10, pady=5)
    
    def get_input():
        return entry.get()

    def on_create_folder():
        enteredFolderName = entry.get()
        run_controller(enteredFolderName)

    def onButtonPress_tag():
        run_controller(get_input())

    def refresh_tags():
        tag_listbox.delete(0, tk.END)  # Clear existing entries
        tags = list_tags()
        for tag in tags:
            tag_listbox.insert(tk.END, tag)

    create_button = tk.Button(root, text="Create Folder", command=on_create_folder)
    create_button.pack(padx=10, pady=10)

    button_tag = tk.Button(root, text="Create Tag", command=onButtonPress_tag)
    button_tag.pack(padx=10, pady=10)

    #tags
    tag_listbox = tk.Listbox(root, width=40, height=10)
    tag_listbox.pack(padx=10, pady=10)
    refresh_tags()  

    root.mainloop()



