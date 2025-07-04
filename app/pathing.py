import os

path_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def getPath_root():
    return path_root

def getPath_tags():
    return os.path.join(path_root, 'tags')

def getPaths_tags():
    path_tags = getPath_tags()
    paths_tags = [f for f in os.listdir(path_tags) if os.path.isdir(os.path.join(path_tags, f))]
    return [os.path.join(path_root, tag) for tag in paths_tags]

def getPath_tag(tag):
    return os.path.join(path_root, getPath_tags(), tag)
