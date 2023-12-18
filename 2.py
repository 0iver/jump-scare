from PIL import Image, ImageTk
import random 
import os 
import time
import tkinter

def show_image(image_path): 
    window = tkinter.Tk()

    img = Image.open(image_path)
    img = ImageTk.PhotoImage(img)
    panel = tkinter.Label(window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")

    time.sleep(random.randint(1, 15) * 1000)

    window.destroy()

def get_random_image():
    image_folder_path = os.path.join(os.getcwd(), "img")
    image_files = [f for f in os.listdir(image_folder_path) if os.path.isfile(os.path.join(image_folder_path, f))]
    image_path = os.path.join(image_folder_path, random.choice(image_files))

    return image_path

def init():
    show_image(get_random_image())
    
    time.sleep(random.randint(60, 120) * 1000)
    
    init()


