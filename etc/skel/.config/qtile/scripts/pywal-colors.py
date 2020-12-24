#!/usr/bin/env python
import os
import random
wallpaper_list = []

d = "/usr/share/wallpapers/garuda-wallpapers"
for path in os.listdir(d):
    full_path = os.path.join(d, path)
    if os.path.isfile(full_path):
        wallpaper_list.append(full_path)

#Add your own wallpapers directory
#e = "/home/rohit/mydata/Pictures/wallpapers"
#for path in os.listdir(e):
#    full_path = os.path.join(e, path)
#    if os.path.isfile(full_path):
#        wallpaper_list.append(full_path)


wallpaper = random.choice(wallpaper_list)


os.system("wal -i " + wallpaper)

#print(wallpaper_list)
