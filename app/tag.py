import os
import numpy as np
import cv2
from PIL import Image

from repository import create_folder
from pathing import getPaths_tags, getPath_tag, getPath_modelFile
from trainer import Trainer
from detector import Detector

def get_tags():
    paths_tags = getPaths_tags()
    tags = [os.path.basename(path) for path in paths_tags if isinstance(path, str) and os.path.basename(path)]
    return tags

def save_image(frame, tag):
    if frame is None:
        return False
    
    path_tag = getPath_tag(tag)
    if not os.path.exists(path_tag):
        create_folder(path_tag)
    
    path_imageFile = os.path.join(path_tag, f"{tag}_{len(os.listdir(path_tag)) + 1}.jpg")

    try:
        if isinstance(frame, np.ndarray):
            converted_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # convert color format
            image = Image.fromarray(converted_frame)  # convert to PIL Image
        else:
            image = frame  # already PIL Image or something else

        image.save(path_imageFile)
        return True
    except Exception as e:
        print(f"Error saving image: {e}")
        return False

def train_tag(tag):
    path_tag = getPath_tag(tag)
    path_modelFile = getPath_modelFile
    trainer = Trainer(tag, path_tag, path_modelFile)
    trainer.run()

def detect_tag(tag, capture):
    path_modelFile = getPath_modelFile(tag)
    
    detector = Detector(path_modelFile, capture)
    detector.run()