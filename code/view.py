
import tkinter as tk

def run():
    rootWindow = get_rootWindow()
    frames = get_frames(rootWindow)
    rootWindow.mainloop()

def get_rootWindow():
    root = tk.Tk()
    root.title("second")
    root.geometry("800x600")  # Set a default size for the window
    root.resizable(True, True)  # Allow resizing in both directions
    return root

def get_frames(rootWindow):
    main_frame = tk.Frame(rootWindow)
    main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    verticalFrame_1 = tk.Frame(main_frame)
    verticalFrame_1.pack(fill=tk.BOTH, expand=True, pady=5)

    verticalFrame_2 = tk.Frame(main_frame)
    verticalFrame_2.pack(fill=tk.BOTH, expand=True, pady=5)

    verticalFrame_3 = tk.Frame(main_frame)
    verticalFrame_3.pack(fill=tk.BOTH, expand=True, pady=5)

    return {
        "main": main_frame,
        "verticalFrame_1": verticalFrame_1,
        "verticalFrame_2": verticalFrame_2,
        "verticalFrame_3": verticalFrame_3
    }


