"""Invert, binarize and skeletonize input image"""
import cv2
import numpy as np
from skimage.morphology import skeletonize

def invert(image):
    """Input: filename for image to be inverted.
    Returns inverted image (does not save)"""
    im_in = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    th, im_th = cv2.threshold(im_in, 220, 255, cv2.THRESH_BINARY_INV)
    im_floodfill = im_th.copy()
    h, w = im_th.shape[:2]
    mask = np.zeros((h+2, w+2), np.uint8)
    cv2.floodFill(im_floodfill, mask, (0,0), 255);
    im_floodfill_inv = cv2.bitwise_not(im_floodfill)
    im_out = im_th | im_floodfill_inv
    return im_out

def im2binary(inverted_image):
    (thresh, im_bw) = cv2.threshold(inverted_image, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    cv2.imwrite('binary.png', im_bw)

def im2skeleton(inbinary_image, out_name):
    binary_image = cv2.imread(inbinary_image)
    skeleton = skeletonize(binary_image)
    cv2.imwrite(out_name, skeleton)


for num1 in range(1, 50):
    for num2 in range(1, 11):
        im_name = './data/images-transformed/' + str(num1) + '_' + str(num2) + '.png'
        try:
            img = cv2.imread(im_name, cv2.IMREAD_GRAYSCALE)
            binary = im2binary(img)
            out_name = './data/image-skeletons/' + str(num1) + '_' + str(num2) + 'skel.png'
            im2skeleton('binary.png', out_name)

        except:
            print(im_name)
