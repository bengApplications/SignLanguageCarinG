import os

from trainer import Trainer  


def run():
    read_files()

def get_dataset_path():
    current_dir = os.path.dirname(__file__)
    return os.path.join(current_dir, 'dataset')

def read_files():
    path = get_dataset_path()
    print("Dataset path:", path)

    files = [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

def train(path_tagFolder):
    model_path = os.path.join(path_tagFolder, 'handpose_classifier.pkl')
    
    trainer = Trainer(path_tagFolder)  # Pass only the dataset path, as expected
    trainer.model_path = model_path    # Set the model path explicitly after initialization
    
    trainer.load_data()
    trainer.train()
    
    print(f"Model trained and saved to {model_path}")
    return model_path

