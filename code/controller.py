import os
from trunk import get_dataset_path

def run(folderName):
    #print(f"Received input: '{folderName}'")
    create_subfolder(folderName) 

def get_tagFolder(tag):
    folder_root = get_dataset_path()
    folder_tag = os.path.join(folder_root, tag)
    return folder_tag

def create_subfolder(folderName):     
    if not folderName:
       # messagebox.showwarning("Input Error", "Please enter a folder name.")
        return

    rootFolder = get_dataset_path()
    folderPath = os.path.join(rootFolder, folderName)
    try:
        os.makedirs(folderPath, exist_ok=False)
        #messagebox.showinfo("Success", f"Folder '{folderName}' created in 'dataset/'.")
    except FileExistsError:
        pass
        #messagebox.showwarning("Exists", f"Folder '{folderName}' already exists.")

def list_tags():
    rootFolder = get_dataset_path()
    try:
        return [f for f in os.listdir(rootFolder) if os.path.isdir(os.path.join(rootFolder, f))]
    except FileNotFoundError:
        return []
    
def get_images_for_tag(tag):
    folder_tag = get_tagFolder(tag)
    if not os.path.isdir(folder_tag):
        return []

    image_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".gif")
    images = [
        os.path.join(folder_tag, f)
        for f in os.listdir(folder_tag)
        if f.lower().endswith(image_extensions)
    ]
    return images 