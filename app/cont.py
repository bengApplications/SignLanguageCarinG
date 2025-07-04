import tag 

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