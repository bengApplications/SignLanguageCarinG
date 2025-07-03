
import tkinter as tk
from tkinter import ttk

import cont
from camera import Camera

def run():
    rootWindow = get_rootWindow()
    frames = get_frames(rootWindow)
    fill_frames(frames)
    rootWindow.mainloop()

def get_rootWindow():
    root = tk.Tk()
    root.title("second")
    root.geometry("800x600")  # Set a default size for the window
    root.resizable(True, True)  # Allow resizing in both directions
    return root

def get_frames(rootWindow):
    main_frame = tk.Frame(rootWindow)
    main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    verticalFrame_1 = tk.Frame(main_frame)
    verticalFrame_1.pack(fill=tk.BOTH, expand=True, pady=5)

    verticalFrame_2 = tk.Frame(main_frame)
    verticalFrame_2.pack(fill=tk.BOTH, expand=True, pady=5)

    verticalFrame_3 = tk.Frame(main_frame)
    verticalFrame_3.pack(fill=tk.BOTH, expand=True, pady=5)

    return {
        "main": main_frame,
        "verticalFrame_1": verticalFrame_1,
        "verticalFrame_2": verticalFrame_2,
        "verticalFrame_3": verticalFrame_3
    }

def fill_frames(frames):
    fill_taglist(frames)
    fill_cameraSelection(frames)

def fill_cameraSelection(frames):
    camera = Camera()
    cameras = camera.get_camera_names()
    camera_asString = tk.StringVar()

    camera_dropdown = ttk.Combobox(frames["verticalFrame_2"], textvariable=camera_asString, values=cameras, state="readonly")
    camera_dropdown.pack(padx=10, pady=10)
    camera_dropdown.bind("<<ComboboxSelected>>", on_camera_select)

def fill_taglist(frames):
    #data
    tags = cont.get_tags()
    # Create a vertical scrollbar for the Listbox 
    scrollbar = tk.Scrollbar(frames["verticalFrame_1"], orient=tk.VERTICAL)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    # Create a Listbox in verticalFrame_1
    listbox = tk.Listbox(frames["verticalFrame_1"])
    listbox.pack(fill=tk.BOTH, expand=True)

    for tag in tags:
        listbox.insert(tk.END, tag)

def on_camera_select(event):
    # Placeholder function for camera selection event
    selected_camera = event.widget.get()
    print(f"Camera selected: {selected_camera}")
