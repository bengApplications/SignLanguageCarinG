# camera.py
import cv2

class CameraManager:
    def __init__(self, max_cams=5):
        self.max_cams = max_cams
        self.cameras = self._detect_cameras()
        self.selected_index = None

    def _detect_cameras(self):
        available = []
        for i in range(self.max_cams):
            cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)  # Use cv2.CAP_DSHOW on Windows
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

    def get_selected_index(self):
        return self.selected_index

    def capture_frame(self):
        if self.selected_index is None:
            return None
        cap = cv2.VideoCapture(self.selected_index)
        ret, frame = cap.read()
        cap.release()
        return frame if ret else None
