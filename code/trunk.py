import os

def run():
    read_files()

def get_dataset_path():
    current_dir = os.path.dirname(__file__)
    return os.path.join(current_dir, 'dataset')

def read_files():
    path = get_dataset_path()
    print("Dataset path:", path)

    files = [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]