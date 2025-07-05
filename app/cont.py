import tag as tagManager

class Cont:
    def __init__(self):
        pass

    @staticmethod
    def get_tags():
        return tagManager.get_tags()

    @staticmethod
    def save_image(frame, tag):
        if frame is None:
            return False
        return tagManager.save_image(frame, tag)
    
    def train(self, tag):
        tagManager.train_tag(tag)

    def detect(self, tag, capturedFrames):
        tagManager.detect_tag(tag, capturedFrames)