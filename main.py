import tkinter as tk
from PIL import Image, ImageTk
import random
import sys
from os import listdir
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # Temporary folder used by PyInstaller
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

folder_path = resource_path("patrick_img")
icon_path = resource_path("./patrick_img/patrick_icon.ico")

patrick_list = [patrick for patrick in listdir(folder_path) if (patrick.endswith(".PNG") or patrick.endswith(".png"))]
loaded_images = [Image.open(f"{folder_path}/{patrick}") for patrick in patrick_list]

default_patricks = 100


if len(sys.argv) > 1:
    try:
        default_patricks = int(sys.argv[1])
    except ValueError:
        print("Invalid number of Patricks. Using default value.")

def show_image():
    img = random.choice(loaded_images)
    x = random.randint(0, 1520)  # Random x position
    y = random.randint(0, 680)  # Random y position

    new_window = tk.Toplevel(root)

    new_window.iconbitmap(icon_path)
    random_width = random.randint(50, 800)
    random_height = random.randint(50, 800)
    new_window.geometry(f"{random_width}x{random_height}+{x}+{y}")
    
    img = img.resize((random_width, random_height))  
    tk_img = ImageTk.PhotoImage(img)

    label = tk.Label(new_window, image=tk_img)
    label.image = tk_img 
    label.pack()

def gradual_pop(index=0, total=default_patricks, delay=10000):
    if index < total:
        show_image()
        if not delay < 4:
            delay = delay - 1/2*delay
        root.after(int(delay), gradual_pop, index + 1, total, int(delay))
    else:
        root.after(delay, root.destroy)

root = tk.Tk()
root.geometry("400x400")
root.title("Patrick")

root.withdraw()
root.after(1000, gradual_pop)

root.mainloop()

