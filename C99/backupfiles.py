import os
import shutil
src = input("Enter source folder name:")
dest = input("Enter destination folder name:")
src = src + "/"
dest = dest + "/"
listOfFIles = os.listdir(src)
for file in listOfFIles:
    shutil.copy((src + file), dest)