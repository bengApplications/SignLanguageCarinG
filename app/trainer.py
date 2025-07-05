import os
import cv2
import numpy
import mediapipe as mp
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report
import joblib

class Trainer:
    def __init__(self, tag, path_tagFolder, path_modelFile):
      
        self.tag = tag
        self.path_tagfolder = path_tagFolder
        self.path_modelFile = path_modelFile
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(static_image_mode=True, max_num_hands=1)

        # filled by loading trainingData
        self.trainingData = []
        self.trainingData_tags = []

    def run(self):
        self.load_trainingData()
        self.train()

    def extract_landmarks(self, image):
        results = self.hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        if results.multi_hand_landmarks:
            landmarks = []
            for lm in results.multi_hand_landmarks[0].landmark:
                landmarks.extend([lm.x, lm.y, lm.z])
            return landmarks
        return None

    def load_trainingData(self):
        allFilesInTagFolder = os.listdir(self.path_tagfolder)

        for file in allFilesInTagFolder:
            path_file = os.path.join(self.path_tagfolder, file)
            image = cv2.imread(path_file)
            if image is None:
                print(f"Warning: Could not read image {path_file}. Skipping.")
                continue

            landmarks = self.extract_landmarks(image)

            if landmarks:
                self.trainingData.append(landmarks)
                self.trainingData_tags.append(self.tag)
            else:
                print(f"⚠️ No hand detected in {file}. Skipped.")

    def train(self):

        X_train, X_test, y_train, y_test = train_test_split(
            self.trainingData, self.trainingData_tags, test_size=0.2, random_state=42
        )
        self.model = SVC(kernel='rbf', probability=True)
        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)
        print(classification_report(y_test, y_pred))
        joblib.dump(self.model, self.path_modelFile)
        print(f"Model saved to {self.path_modelFile}")
