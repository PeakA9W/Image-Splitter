from PIL import Image # pip install Pillow 
import os
import sys


def imgsplit(imagepath, Vrow, Hrow, ImgFormat, suffix):
    # opening the image as an image object from the pillow module
    try:
        image = Image.open(rf'{imagepath}')
    except Exception:
        return 0
    
    # making the export directory 
    directory = imagepath.split("\\")[-1].split('.')[0]
    parent_dir = imagepath.split(directory)[0]
    path = os.path.join(parent_dir, (directory + suffix))
    if not os.path.exists(path):
        os.mkdir(path)

    imagename = directory

    w = image.size[0]
    h = image.size[1]
    new_w = int(w / Hrow)
    new_h = int(h / Vrow)
    
    top_y = -new_h
    bottom_y = 0

    for i in range(Vrow):
        top_y += new_h
        bottom_y += new_h
        left_x = -new_w
        right_x = 0
        for j in range(Hrow):
            right_x += new_w
            left_x += new_w
            img = image.crop((left_x, top_y, right_x, bottom_y))

            # export the image to the path of the export directory 
            try:
                img.save(path + rf'\{imagename}_{i+1}_{j+1}.{ImgFormat}')
            except Exception:
                return 0

suffix = ''  # default suffix 
while True:
    try:
        Vrow = int(input("How many Vertical Rows? \t"))
        break
    except:
        print("Only Numbers Allowed")

while True:
    try:
        Hrow = int(input("How many Horizontal Rows? \t"))
        break
    except:
        print("Only Numbers Allowed")

ImgFormat = input("please type the format of the exported images\t")
Suffix = input("please type a Suffix for the export folder name (leave it empty for no suffix)")

for arg in sys.argv[1:]:  
    if imgsplit(arg, Vrow, Hrow, ImgFormat, suffix) == 0:
        print("Invalid Image Format")
        input("Press any key to leave..")

    




        
