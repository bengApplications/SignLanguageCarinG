
import tkinter as tk
from tkinter import ttk

from cont import Cont
from camera import Camera

class View:
    def __init__(self):
        # layzi initialization
        self.shared_listbox = None  # Placeholder for the listbox to be shared across methods

        # immidiate initialization
        self.cont = Cont()
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
        print("💡 fill_taglist called")
        tags = Cont.get_tags()
        print("Tags:", tags)
    
        scrollbar = tk.Scrollbar(self.frames["frame_1"], orient=tk.VERTICAL)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.shared_listbox = tk.Listbox(self.frames["frame_1"])
        self.shared_listbox.pack(fill=tk.BOTH, expand=True)

        for tag in tags:
            self.shared_listbox.insert(tk.END, tag) 

        # default
        if tags:
            self.shared_listbox.selection_set(0)    

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
        button_capture = tk.Button(buttonFrame_capture, text="capture Image", command=lambda: self.on_capture())
        button_capture.pack(side=tk.LEFT, padx=5)
       
        buttonFrame_train = tk.Frame(self.frames["frame_3"])
        buttonFrame_train.pack(pady=10)
        button_train = tk.Button(buttonFrame_capture, text="train tag", command=lambda: self.on_train())
        button_train.pack(side=tk.LEFT, padx=5)

        buttonFrame_detect = tk.Frame(self.frames["frame_3"])
        buttonFrame_detect.pack(pady=10)
        button_detect = tk.Button(buttonFrame_capture, text="detect", command=lambda: self.on_detect())
        button_detect.pack(side=tk.LEFT, padx=5)

    def on_capture(self):
        selection_tuple = self.shared_listbox.curselection()
        if not selection_tuple:
            import tkinter.messagebox as messagebox
            messagebox.showwarning("No selection", "Please select a tag before capturing.")
            return

        index = selection_tuple[0]       
        selected_tag = self.shared_listbox.get(index)

        # Capture image from camera
        frame = self.camera.capture_image()
        if Cont.save_image(frame, selected_tag):
           pass #self.refresh_thumbnails()
        pass

    def on_train(self):
        tag = self.get_current_tag(self)
        self.cont.train(tag)

    def on_detect(self):
        tag = self.get_current_tag()
        self.cont.detect(tag, self.camera.provide_capturedFrames)

    def get_current_tag(self):
        return self.shared_listbox.get(self.shared_listbox.curselection()) if self.shared_listbox.curselection() else None  
