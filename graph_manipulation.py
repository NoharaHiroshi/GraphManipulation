# coding=utf-8

import os
import numpy as np
import matplotlib.image as mpimg
from base import open_image
from PIL import Image


def base_image(img):
    try:
        with open_image(img) as image:
            new_img = image.im
            img_arr = np.array(new_img)
            con_img = Image.fromarray(img_arr)
            con_img.show()
    except Exception as e:
        print e

if __name__ == '__main__':
    img = mpimg.imread(u'Images/cat_1.jpg')
    img *= 255
    im = Image.fromarray(np.uint8(img))
    im.show()