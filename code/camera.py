# camera.py
import cv2
from PIL import Image, ImageTk

class CameraManager:
    def __init__(self, label_widget, max_cams=5):
        self.label_widget = label_widget  # Tkinter Label for preview
        self.max_cams = max_cams
        self.cameras = self._detect_cameras()
        self.selected_index = None
        self.cap = None
        self.preview_running = False

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

    def start_preview(self):
        if self.selected_index is None:
            return
        self.cap = cv2.VideoCapture(self.selected_index)
        self.preview_running = True
        self._update_preview()

    def stop_preview(self):
        self.preview_running = False
        if self.cap:
            self.cap.release()
            self.cap = None

    def _update_preview(self):
        if not self.preview_running or not self.cap:
            return

        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            img = img.resize((200, 200))
            imgtk = ImageTk.PhotoImage(image=img)
            self.label_widget.imgtk = imgtk
            self.label_widget.config(image=imgtk)

        # Schedule next update
        self.label_widget.after(30, self._update_preview)

    def capture_image(self):
        if not self.cap or not self.cap.isOpened():
            return None
        ret, frame = self.cap.read()
        return frame if ret else None
    