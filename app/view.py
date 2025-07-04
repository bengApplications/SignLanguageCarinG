
import tkinter as tk
from tkinter import ttk

import cont
from camera import Camera

class View:
    def __init__(self):
        self.rootWindow = self.create_rootWindow()
        self.camera = Camera()
        self.frames = self.create_frames()
        self.fill_frames()

        self.rootWindow.protocol("WM_DELETE_WINDOW", self.on_close)

    def run(self):
        self.rootWindow.mainloop()
        
    def on_close(self):
        self.camera.release()
        self.rootWindow.destroy()

    def create_rootWindow(self):
        root = tk.Tk()
        root.title("second")
        root.geometry("800x600")  # Set a default size for the window
        root.resizable(True, True)  # Allow resizing in both directions
        return root

    def create_frames(self):
        frame_main = tk.Frame(self.rootWindow)
        frame_main.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        frame_1 = tk.Frame(frame_main)
        frame_1.pack(fill=tk.BOTH, expand=True, pady=5)

        frame_2 = tk.Frame(frame_main)
        frame_2.pack(fill=tk.BOTH, expand=True, pady=5)

        frame_3 = tk.Frame(frame_main)
        frame_3.pack(fill=tk.BOTH, expand=True, pady=5)

        return {
            "main": frame_main,
            "frame_1": frame_1,
            "frame_2": frame_2,
            "frame_3": frame_3
        }

    def fill_frames(self):
        self.fill_taglist()
        self.fill_cameraSelection()
        self.fill_cameraPreview()
        self.create_buttons()

    def fill_taglist(self):
        tags = cont.get_tags()
    
        scrollbar = tk.Scrollbar(self.frames["frame_1"], orient=tk.VERTICAL)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        listbox = tk.Listbox(self.frames["frame_1"])
        listbox.pack(fill=tk.BOTH, expand=True)

        for tag in tags:
            listbox.insert(tk.END, tag)    

    def fill_cameraSelection(self):
        cameras = self.camera.get_camera_names()
        camera_asString = tk.StringVar()

        camera_dropdown = ttk.Combobox(self.frames["frame_2"], textvariable=camera_asString, values=cameras, state="readonly")
        camera_dropdown.pack(padx=10, pady=10)
        camera_dropdown.bind("<<ComboboxSelected>>", self.on_camera_select)
        
        #default
        if cameras:
            self.camera.select_camera(cameras[0]) #for openCV Videocapture
            camera_asString.set(cameras[0])
            camera_dropdown.current(0)

    def fill_cameraPreview(self):
        camera_previewLabel = tk.Label(self.frames["frame_2"], text="Camera Preview")
        camera_previewLabel.pack(padx=10, pady=10)
        self.camera.set_previewLabel(camera_previewLabel)
        camera_previewLabel.after(100, self.camera.start_preview)   

    def on_camera_select(self, event):
        # Placeholder function for camera selection event
        selected_camera = event.widget.get()

    def create_buttons(self):
        buttonFrame_capture = tk.Frame(self.frames["frame_2"])
        buttonFrame_capture.pack(pady=10)

        button_capture = tk.Button(buttonFrame_capture, text="Capture Image", command=lambda: on_capture())
        button_capture.pack(side=tk.LEFT, padx=5)

        def on_capture(self):
            # if not listbox.curselection():
            #     messagebox.showwarning("No Tag", "Please select a tag first.")
            #     return

            # # Get selected tag name
            # index = tag_listbox.curselection()[0]
            # selected_tag = tag_listbox.get(index)

            # # Capture image from camera
            # frame = cam_manager.capture_image()
            # if save_image(frame, selected_tag):
            #     refresh_tags()
            pass
