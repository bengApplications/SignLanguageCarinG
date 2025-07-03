import os

from pathing import getPaths_tags

def get_tags():
    paths_tags = getPaths_tags()
    tags = [os.path.basename(path) for path in paths_tags if isinstance(path, str) and os.path.basename(path)]
    return tags