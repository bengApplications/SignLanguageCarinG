# camera.py
import cv2
from PIL import Image, ImageTk

class Camera:
    def __init__(self, max_cams=99):
        self.max_cams = max_cams
        self.cameras = self._detect_cameras()
        self.selected_index = None
        self.cap = None
        self.previewLabel = None
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
        #self.cap = cv2.VideoCapture(self.selected_index)
        self.cap = cv2.VideoCapture(self.selected_index, cv2.CAP_DSHOW)
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

            # ✅ Keep reference to avoid garbage collection
            self.previewLabel.imgtk = imgtk
            self.previewLabel.config(image=imgtk)

        # ✅ Schedule next update
        self.previewLabel.after(30, self._update_preview)

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

    def set_previewLabel(self, label):
        self.previewLabel = label

    def __del__(self):
        print("⚠️ Camera instance was garbage collected.")
    