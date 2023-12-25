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

    random_time = random.randint(1, 15) 

    print("Waiting for", random_time, "seconds")

    time.sleep(random_time)

    print("Destorying Window")

    window.destroy()

def get_random_image():
    image_folder_path = os.path.join(os.getcwd(), "img")
    image_files = [f for f in os.listdir(image_folder_path) if os.path.isfile(os.path.join(image_folder_path, f))]
    image_random_selected = random.choice(image_files)
    image_path = os.path.join(image_folder_path, image_random_selected)

    print("Image Selected", image_random_selected)

    return image_path

def init():
    show_image(get_random_image())
    
    random_sleep_amount = random.randint(60, 120)

    print("Waiting for", random_sleep_amount, "Seconds")
    
    time.sleep(random_sleep_amount)
    
    print("Restarying Cycle")

    init()

init()

