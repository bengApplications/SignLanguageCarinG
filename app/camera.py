# camera.py
import cv2
from PIL import Image, ImageTk

class Camera:
    def __init__(self, max_cams=99):
        self.max_cams = max_cams
        self.cameras = self._detect_cameras()
        self.selected_index = None
        self.cap = None
        self.canvas = None
        self.is_displaying = False

    def _detect_cameras(self):
        available = []
        for i in range(self.max_cams):
            cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
            if cap is not None and cap.isOpened():
                ret, _ = cap.read()
                if ret:
                    available.append((f"Camera {i}", i))
                cap.release()
        return available

    def get_camera_names(self):
        return [name for name, _ in self.cameras]

    def select_camera(self, name):
        for cam_name, index in self.cameras:
            if cam_name == name:
                self.selected_index = index
                return index
        return None

    def start_display(self):
        self.cap = cv2.VideoCapture(self.selected_index, cv2.CAP_DSHOW)
        self.is_displaying = True
        self.update_display()

    def stop_display(self):
        self.is_displaying = False
        if self.cap:
            self.cap.release()
            self.cap = None

    def update_display(self):
        if not self.is_displaying or not self.cap:
            return

        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            img = img.resize((200, 200))
            imgtk = ImageTk.PhotoImage(image=img)

            # ✅ Keep reference to avoid garbage collection
            self.canvas.imgtk = imgtk
            self.canvas.config(image=imgtk)

        self.canvas.after(30, self.update_display)

    def capture_image(self):
        if not self.cap or not self.cap.isOpened():
            return None
        ret, frame = self.cap.read()
        return frame if ret else None
    
    def release(self):
        if self.cap is not None:
            self.cap.release()
            self.cap = None
            print("Camera released.")

    def set_canvas(self, label):
        self.canvas = label

    def __del__(self):
        print("⚠️ Camera instance was garbage collected.")

    def provide_capture(self):
        return self.cap    