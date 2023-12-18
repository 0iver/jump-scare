import tkinter as tk
import random
import os
import time
import logging

# Correct path to the folder containing images
image_folder_path = 'Users\Olive\OneDrive\Documents\GitHub\jump-scare\img'

# Get all image files from the folder
image_files = [f for f in os.listdir(image_folder_path) if os.path.isfile(os.path.join(image_folder_path, f))]

logger = logging.getLogger("logging_tryout2")
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s")

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

def show_image():
    # Choose a random image
    img_path = os.path.join(image_folder_path, random.choice(image_files))

    # Create a full-screen window
    window = tk.Tk()
    # window.attributes('-fullscreen', True)

    # Load and display the image
    img = Image.open(img_path)
    img = ImageTk.PhotoImage(img)
    panel = tk.Label(window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")

    # Function to close the window
    def close_window():
        window.destroy()

    # Schedule window to close after 10000 ms (10 seconds)
    window.after(10000, close_window)

    # Start the main event loop
    window.mainloop()


while True:
    show_image()

    random_slepe = random.randint(1,15) * 60000

    time.sleep(random_slepe)  
