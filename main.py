from PIL import Image, ImageTk
import random 
import os 
import time
import tkinter as tk

def show_image(image_path):
    window = tk.Tk()
    window.title("Image Display")

    img = Image.open(image_path)
    tk_img = ImageTk.PhotoImage(img)
    panel = tk.Label(window, image=tk_img)
    panel.image = tk_img 
    panel.pack(side="bottom", fill="both", expand="yes")

    random_time = random.randint(1, 15)

    print("Waiting for", random_time, "seconds before closing window")
    
    window.after(random_time * 1000, window.destroy)

    window.mainloop()

def get_random_image():
    image_folder_path = os.path.join(os.getcwd(), "img")
    image_files = [f for f in os.listdir(image_folder_path) if os.path.isfile(os.path.join(image_folder_path, f))]
    image_random_selected = random.choice(image_files)
    image_path = os.path.join(image_folder_path, image_random_selected)

    print("Image Selected", image_random_selected)

    return image_path

def init():
    while True:
        show_image(get_random_image())
        
        random_sleep_amount = random.randint(60, 120)

        print("Waiting for", random_sleep_amount, "seconds")

        time.sleep(random_sleep_amount)
        
        print("Restarting Cycle")

init()
