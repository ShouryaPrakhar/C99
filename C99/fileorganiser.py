import os
import shutil
path = input("Enter the nme of directory to be sorted:")
listOfFIles = os.listdir(path)
for file in listOfFIles:
    name , ext = os.path.splitext(file)
    ext = ext[1:]
    if ext == "" :
        continue
    if os.path.exists(path + "/" + ext):
        shutil.move(path + "/" + file , path + "/" + ext + "/" + file)
    else :
        os.makedirs(path + "/" + ext)
        shutil.move(path + "/" + file , path + "/" + ext + "/" + file)