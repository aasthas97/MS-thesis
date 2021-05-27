"""Inverts image and create scalar, rotational and combined transforms.
Writes transformation details to transforminfo.txt"""

import cv2
import imutils
import random
import PIL
from PIL import Image

def invert(image):
    im_in = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    im_out = cv2.bitwise_not(im_in)
    cv2.imwrite('inverted.png', im_out)

def rotate(image, type_transform, out_name):
    im_in = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    angle = random.randint(0, 360)
    global transform_details
    transform_details.append(angle)
    rotated = imutils.rotate_bound(im_in, angle)
    if type_transform == 'both': # if both scalar and rotational transformations, save temporarily as 'rotate.png'
        cv2.imwrite('rotate.png', rotated)
    elif type_transform == 'rotational': # if only rotational transformation, save with the right name
        cv2.imwrite(out_name, rotated)

def resize(image, out_name):
    img = Image.open(image)
    basewidth = random.randint(300, 1500)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    foo = 'basewidth: ' + str(basewidth) + ', ' + 'hsize: ' + str(hsize)
    global transform_details
    transform_details.append(foo)
    img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    img.save(out_name)


transform_details = []

for num in range(1, 50):
    im_name = './data/images/%d.png' % num
#     print(im_name)
    transform_details.append(im_name + '\n')

    for transform_index in range(1, 11):
        out_name = './data/images-transformed/%d_%d.png' % (num, transform_index)
        if transform_index <= 4:
            inverted = invert(im_name)
            resize('inverted.png', out_name)

        elif transform_index > 4 and transform_index <= 8:
            invert(im_name)
            rotate('inverted.png', 'rotational', out_name)

        elif transform_index > 8 and transform_index <= 10:
            invert(im_name)
            rotate('inverted.png', 'both', out_name)
            resize('rotate.png', out_name)


transform_details = [str(element) for element in transform_details]
with open('transforminfo.txt', 'w') as writefile:
    data = '\n'.join(transform_details)
    writefile.write(data)
