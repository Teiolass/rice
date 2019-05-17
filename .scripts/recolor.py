#!/usr/bin/env python3

from PIL import Image
# import argparse


name = 'albero'
extension = 'png'
img_path = '/home/teiolass/Downloads/'
full_img_path = img_path + name + '.' + extension
save_path = img_path + name + '-recolored.' + extension

theme = 'creme'

screen_size = (1920, 1080)


if theme == 'gruvbox':
    color1 = [40, 40, 40]
    color2 = [215, 153, 33]
if theme == 'creme':
    color1 = [247, 217, 105]
    color2 = [166, 32, 106]

resize_ratio = 0.7

def blend(ca, cb, pt):
    r = []
    for h1, h2 in zip(ca, cb):
        h = int((h1 * pt + h2 * (255 - pt)) / 255)
        r.append(h)
    return tuple(r)

def hard_blend(ca, cb, pt):
    if pt > 20:
        return tuple(ca)
    else:
        return tuple(cb)


# parser = argparse.ArgumentParser(description='Recolor images for beautiful ' \
#         'desktops')
# parser.add_argument('image', help='The path to the image you want to recolor')
# args = parser.parse_args()
# 
# full_img_path = args.image


im = Image.open(full_img_path)
im = im.convert('L')
im = im.resize((int(resize_ratio*im.size[0]),int(resize_ratio*im.size[1])), Image.ANTIALIAS)
newimdata = []
for color in im.getdata():
   newimdata.append(blend(color1, color2, color))
   # newimdata.append((color,color,color))
newim = Image.new('RGB', im.size)
newim.putdata(newimdata)

fin = Image.new('RGB', screen_size, tuple(color1))
offx = int(0.5*(screen_size[0] - im.width))
offy = int(0.5*(screen_size[1] - im.height))
fin.paste(newim, (offx, offy))

fin.save(save_path)


