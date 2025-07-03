import os
import cv2
import numpy as np
import mediapipe as mp
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report
import joblib

class Trainer:
    def __init__(self, path_tagFolder, model_path='handpose_classifier.pkl'):
      
        self.dataset_path = path_tagFolder
        self.model_path = model_path
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(static_image_mode=True, max_num_hands=1)
        self.data = []
        self.labels = []

    def extract_landmarks(self, image):
        results = self.hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        if results.multi_hand_landmarks:
            landmarks = []
            for lm in results.multi_hand_landmarks[0].landmark:
                landmarks.extend([lm.x, lm.y, lm.z])
            return landmarks
        return None

    def load_data(self):
        for label in os.listdir(self.dataset_path):
            class_dir = os.path.join(self.dataset_path, label)
            if not os.path.isdir(class_dir):
                continue
            for filename in os.listdir(class_dir):
                filepath = os.path.join(class_dir, filename)
                img = cv2.imread(filepath)
                if img is None:
                    continue
                landmarks = self.extract_landmarks(img)
                if landmarks:
                    self.data.append(landmarks)
                    self.labels.append(label)
        self.data = np.array(self.data)
        self.labels = np.array(self.labels)
        print(f"Loaded {len(self.data)} samples.")

    def train(self):
        if not self.data:
            self.load_data()
        X_train, X_test, y_train, y_test = train_test_split(
            self.data, self.labels, test_size=0.2, random_state=42
        )
        self.model = SVC(kernel='rbf', probability=True)
        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)
        print(classification_report(y_test, y_pred))
        joblib.dump(self.model, self.model_path)
        print(f"Model saved to {self.model_path}")
