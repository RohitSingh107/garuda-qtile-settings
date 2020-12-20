import os

wallpaper_list = []

d = "/usr/share/wallpapers/garuda-wallpapers"
for path in os.listdir(d):
    full_path = os.path.join(d, path)
    if os.path.isfile(full_path):
        wallpaper_list.append(full_path)
