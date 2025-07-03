import os

def getPath_dataset():
    folder_current = os.path.dirname(__file__)
    return os.path.join(folder_current, 'dataset')

def getPath_tag(tag):
    folder_root = getPath_dataset
    folder_tag = os.path.join(folder_root, tag)
    return folder_tag