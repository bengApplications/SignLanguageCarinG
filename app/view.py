
import tkinter as tk
from tkinter import ttk

import cont
from camera import Camera

def run():
    rootWindow = get_rootWindow()

    camera = Camera()
    def on_close():
        camera.release()
        rootWindow.destroy()
    rootWindow.protocol("WM_DELETE_WINDOW", on_close)

    frames = get_frames(rootWindow)
    fill_frames(frames, camera)

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

def fill_frames(frames, camera):
    fill_taglist(frames)

    fill_cameraSelection(frames, camera)
    fill_cameraPreview(frames, camera)

def fill_taglist(frames):
    tags = cont.get_tags()
   
    scrollbar = tk.Scrollbar(frames["verticalFrame_1"], orient=tk.VERTICAL)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    listbox = tk.Listbox(frames["verticalFrame_1"])
    listbox.pack(fill=tk.BOTH, expand=True)

    for tag in tags:
        listbox.insert(tk.END, tag)    

def fill_cameraSelection(frames, camera):
    cameras = camera.get_camera_names()
    camera_asString = tk.StringVar()

    camera_dropdown = ttk.Combobox(frames["verticalFrame_2"], textvariable=camera_asString, values=cameras, state="readonly")
    camera_dropdown.pack(padx=10, pady=10)
    camera_dropdown.bind("<<ComboboxSelected>>", on_camera_select)
    
    #default
    if cameras:
       camera.select_camera(cameras[0]) #for openCV Videocapture
       camera_asString.set(cameras[0])
       camera_dropdown.current(0)

def fill_cameraPreview(frames, camera):
    camera_previewLabel = tk.Label(frames["verticalFrame_2"], text="Camera Preview")
    camera_previewLabel.pack(padx=10, pady=10)
    camera.set_previewLabel(camera_previewLabel)
    camera_previewLabel.after(100, camera.start_preview)   

def on_camera_select(event):
    # Placeholder function for camera selection event
    selected_camera = event.widget.get()
