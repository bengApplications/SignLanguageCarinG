import os
from trunk import get_dataset_path

def run(folderName):
    #print(f"Received input: '{folderName}'")
    create_subfolder(folderName) 

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
        # Return list of folder names only (tags)
        return [f for f in os.listdir(rootFolder) if os.path.isdir(os.path.join(rootFolder, f))]
    except FileNotFoundError:
        return []