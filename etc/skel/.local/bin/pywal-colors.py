#!/usr/bin/env python
import os
import random
import wallist
import sys



walpl = os.environ['HOME'] + "/.local/bin/wallist.py"

if len(sys.argv) > 1:
    if sys.argv[1] == "--dirs":
        wallist.print_dirs()
    elif sys.argv[1] == "--add":
        dir_path = input("Enter full path of directory: ")
        with open(walpl, "a") as f:
            f.write('\nadd_dir("{}")'.format(dir_path))
else:         
    wallpaper = random.choice(wallist.wallpaper_list)
    os.system("wal -i " + wallpaper)

#print(wallist.wallpaper_list)

