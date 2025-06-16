import os
import ctypes
import random
import time

wall_folder = r"C:\Users\hussa\OneDrive\Desktop\Walls"
change_interval = 10

def change_wallpaper():
    wallies = [os.path.join(wall_folder, f) for f in os.listdir(wall_folder) if f.endswith(('.jpg', '.png'))]
    if wallies:
        chosen = random.choice(wallies)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, chosen, 3)
        print(f"Setting wallpaper: {chosen}")

while True:
    change_wallpaper()
    time.sleep(change_interval)

