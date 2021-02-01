import os

wallpaper_list = []
dir_list = []

def add_dir(dir_path):
    dir_list.append(dir_path)
    for path in os.listdir(dir_path):
        full_path = os.path.join(dir_path, path)
        if os.path.isfile(full_path):
            wallpaper_list.append(full_path)
def print_dirs():
    print(dir_list)

add_dir("/usr/share/wallpapers/garuda-wallpapers")
