# coding=utf-8
import os
from PIL import Image, ImageDraw, ImageFont

directory = raw_input('Enter the path : ')
num = raw_input('Enter the number you want add: ')

def resize_addnum(name,nums):
    try:
        image = Image.open(directory + name)
    except IOError:
        print 'Cannot open the file'
        exit()
    new_image = image.resize( (240, 200) )
    rename = "Shrinked_" + name
    x,y = new_image.size
    draw = ImageDraw.Draw(new_image)
    myfont = ImageFont.truetype( 'arial.ttf', x/8)
    draw.text(( 7*x/9, 0), nums, fill = 'blue', font = myfont)
    new_image.save(rename)

pic_list = os.listdir(directory)
count = 0

for file in pic_list:
    if file.endswith('.jpg') or file.endswith('.png') :
        count = count + 1
        resize_addnum(file,num)

print count, "picture(s) had been resized and added by a number"

