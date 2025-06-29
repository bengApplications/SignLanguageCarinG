import tkinter as tk
from tkinter import messagebox

from controller import run as run_controller
from controller import list_tags

def run():
    root = tk.Tk()
    root.title("first title")

    # Create two main frames: left and right
    main_frame = tk.Frame(root)
    main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    left_frame = tk.Frame(main_frame)
    left_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

    right_frame = tk.Frame(main_frame)
    right_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.Y)

    # Left side widgets
    label = tk.Label(left_frame, text="first label")
    label.pack(padx=20, pady=5)

    entry = tk.Entry(left_frame, width=30)
    entry.pack(padx=10, pady=5)

    def get_input():
        return entry.get()

    def onButtonPress_tag():
        run_controller(get_input())
        refresh_tags()

    def refresh_tags():
        tag_listbox.delete(0, tk.END)
        tags = list_tags()
        for tag in tags:
            tag_listbox.insert(tk.END, tag)

    button_tag = tk.Button(left_frame, text="Create Tag", command=onButtonPress_tag)
    button_tag.pack(padx=10, pady=10)

    tag_listbox = tk.Listbox(left_frame, width=40, height=10)
    tag_listbox.pack(padx=10, pady=10)
    refresh_tags()

    # Right side widgets
    def on_take_example():
        messagebox.showinfo("Example", "Take example clicked")

    button_example = tk.Button(right_frame, text="Take Example", command=on_take_example)
    button_example.pack(padx=10, pady=10)

    root.mainloop()
