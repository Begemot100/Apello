import os
from PIL import Image, ImageDraw, ImageFont
from tkinter import Tk, font

from PIL.ImageFont import truetype #I can make the libraries needed to run automatically load

font.root = Tk()
# print(font.families())

def image_signature(directory):
    for file in os.listdir(directory): # loop through the folder
        if file.endswith(".jpg", ".HEIC"):
            name = os.path.splitext(file)[0].replace("-", ' ').title()  # format the file name
            image = Image.open(directory + "/" + file)
            image.load() # loading the library
            font = truetype('Avenir',size=15)
            draw_text = ImageDraw.Draw(image)
            draw_text.text((image.size[0] - 100,image.size[1] - 50), name,fill='white',font=font)
            image.save(directory + "/" + file) # save the result
            image.show()


print('This script signs images from the file name')
directory = input('Enter the path to the folder with files:')
image_signature(directory)
print('Ready!')
