import cv2
import joblib
import mediapipe as mp
import numpy as np

class Detector:
    def __init__(self, path_modelFile, capture):
        self.model = joblib.load(path_modelFile)
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(static_image_mode=False, max_num_hands=1)
        self.capture = capture

    def extract_landmarks(self, image):
        results = self.hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        if results.multi_hand_landmarks:
            landmarks = []
            for lm in results.multi_hand_landmarks[0].landmark:
                landmarks.extend([lm.x, lm.y, lm.z])
            return landmarks
        return None

    def run(self):
        while True:
            ret, frame = self.capture.read()
            if not ret:
                break

            landmarks = self.extract_landmarks(frame)
            if landmarks:
                prediction = self.model.predict([landmarks])[0]  # 1 for in-class, -1 for outlier

                label = "MATCH" if prediction == 1 else "NOT MATCH"
                color = (0, 255, 0) if prediction == 1 else (0, 0, 255)

                cv2.putText(frame, label, (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 2)

            cv2.imshow("Pose Recognizer", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        self.capture.release()
        cv2.destroyAllWindows()
