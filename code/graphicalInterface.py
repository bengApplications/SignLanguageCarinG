import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

from camera import CameraManager
from tkinter import ttk

from controller import run as run_controller
from controller import list_tags, get_images_for_tag  # You must have this function
from controller import save_image

def run():
    root = tk.Tk()
    root.title("first title")

    # --- Layout ---
    main_frame = tk.Frame(root)
    main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    left_frame = tk.Frame(main_frame)
    left_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

    right_frame = tk.Frame(main_frame)
    right_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.Y)

    # New frame below main_frame for thumbnails
    bottom_frame = tk.Frame(root)
    bottom_frame.pack(padx=10, pady=(0, 10), fill=tk.BOTH, expand=True)

    # Canvas + Scrollbar for thumbnail gallery
    canvas = tk.Canvas(bottom_frame, height=200)
    scrollbar = tk.Scrollbar(bottom_frame, orient="horizontal", command=canvas.xview)
    canvas.configure(xscrollcommand=scrollbar.set)

    scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
    canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    thumbnail_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=thumbnail_frame, anchor="nw")

    # --- Left side widgets ---
    label = tk.Label(left_frame, text="first label")
    label.pack(padx=20, pady=5)

    entry = tk.Entry(left_frame, width=30)
    entry.pack(padx=10, pady=5)

    def get_input():
        return entry.get()

    def onButtonPress_tag():
        run_controller(get_input())
        refresh_tags()

    def refresh_tags():
        tag_listbox.delete(0, tk.END)
        tags = list_tags()
        for tag in tags:
            tag_listbox.insert(tk.END, tag)

    button_tag = tk.Button(left_frame, text="Create Tag", command=onButtonPress_tag)
    button_tag.pack(padx=10, pady=10)

    tag_listbox = tk.Listbox(left_frame, width=40, height=10)
    tag_listbox.pack(padx=10, pady=10)
    refresh_tags()

    # --- Right side widgets ---

    image_label = tk.Label(right_frame)
    image_label.pack(padx=10, pady=10)
    
    # camera
    camera_var = tk.StringVar()
    camera_dropdown = None  # placeholder

    # Create CameraManager with image_label as preview area
    cam_manager = CameraManager(image_label)
    camera_names = cam_manager.get_camera_names()

    if camera_names:
        camera_var.set(camera_names[0])
        cam_manager.select_camera(camera_names[0])
        cam_manager.start_preview()
    else:
        camera_var.set("No camera found")

    def on_camera_select(event=None):
        selected = camera_var.get()
        cam_manager.stop_preview()
        cam_manager.select_camera(selected)
        cam_manager.start_preview()

    camera_dropdown = ttk.Combobox(right_frame, textvariable=camera_var, values=camera_names, state="readonly")
    camera_dropdown.pack(padx=10, pady=10)
    camera_dropdown.bind("<<ComboboxSelected>>", on_camera_select)

    def on_take_example():
        # Check if a tag is selected
        if not tag_listbox.curselection():
            messagebox.showwarning("No Tag", "Please select a tag first.")
            return

        # Get selected tag name
        index = tag_listbox.curselection()[0]
        selected_tag = tag_listbox.get(index)

        # Capture image from camera
        frame = cam_manager.capture_image()
        if save_image(frame, selected_tag):
            refresh_tags()

    button_example = tk.Button(right_frame, text="Take example pic for tag", command=on_take_example)
    button_example.pack(padx=10, pady=10)

    # Keep references to prevent garbage collection
    displayed_image = {"img": None}
    thumbnails = []

    def on_tag_select(event):
        nonlocal thumbnails
        thumbnails.clear()

        for widget in thumbnail_frame.winfo_children():
            widget.destroy()

        if not tag_listbox.curselection():
            return

        index = tag_listbox.curselection()[0]
        selected_tag = tag_listbox.get(index)

        image_paths = get_images_for_tag(selected_tag)
        if image_paths:
            # Show first image large
            try:
                img = Image.open(image_paths[0])
                img.thumbnail((200, 200))
                photo = ImageTk.PhotoImage(img)
                image_label.config(image=photo)
                displayed_image["img"] = photo
            except Exception as e:
                messagebox.showerror("Error", f"Could not load image: {e}")
                image_label.config(image='')
                displayed_image["img"] = None

            # Show all thumbnails
            for i, path in enumerate(image_paths):
                try:
                    thumb_img = Image.open(path)
                    thumb_img.thumbnail((80, 80))
                    thumb_photo = ImageTk.PhotoImage(thumb_img)

                    # Define click handler in closure
                    def on_thumbnail_click(event, p=path):
                        try:
                            full_img = Image.open(p)
                            full_img.thumbnail((200, 200))
                            full_photo = ImageTk.PhotoImage(full_img)
                            image_label.config(image=full_photo)
                            displayed_image["img"] = full_photo
                        except Exception as e:
                            messagebox.showerror("Error", f"Could not load image: {e}")

                    lbl = tk.Label(thumbnail_frame, image=thumb_photo, cursor="hand2")
                    lbl.image = thumb_photo  # keep reference
                    lbl.grid(row=0, column=i, padx=5, pady=5)
                    lbl.bind("<Button-1>", on_thumbnail_click)

                    thumbnails.append(thumb_photo)
                except Exception as e:
                    print(f"Skipping image {path}: {e}")


        else:
            image_label.config(image='')
            displayed_image["img"] = None

        # Resize canvas scroll region
        thumbnail_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    tag_listbox.bind("<<ListboxSelect>>", on_tag_select)

    root.mainloop()
