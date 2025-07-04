import tag
from trainer import Trainer

class Cont:
    def __init__():
        pass

    @staticmethod
    def get_tags():
        return tag.get_tags()

    @staticmethod
    def save_image(frame, tag_name):
        if frame is None:
            return False
        return tag.save_image(frame, tag_name)
    
    def train(tag):
        trainer = Trainer()
        return trainer.train(tag) 