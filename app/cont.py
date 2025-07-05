import tag as tagManager
from trainer import Trainer

class Cont:
    def __init__(self):
        pass

    @staticmethod
    def get_tags():
        return tagManager.get_tags()

    @staticmethod
    def save_image(frame, tag_name):
        if frame is None:
            return False
        return tagManager.save_image(frame, tag_name)
    
    def train(self, tag):
        tagManager.train_tag(tag) 