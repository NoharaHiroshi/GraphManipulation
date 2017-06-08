# coding=utf-8

import os
import numpy as np
import matplotlib.image as mpimg
from base import open_image
from PIL import Image

convert_char = [u'█', u'▉', u'▊', u'▌', u'▍', u'▎', u'▏']


def base_image(img):
    try:
        with open_image(img) as image:
            new_img = image.im.convert('1').resize((128, 128))
            width, height = new_img.size
            # 逐行扫描，高度为0,1,2,3。。。
            for h in range(height):
                row = list()
                for w in range(width):
                    pixel = new_img.getpixel((w, h))
                    con = len(convert_char) - 1
                    flag = pixel // (255 // con)
                    row.append(u'%s(%s)' % (convert_char[flag], flag))
                print ' '.join(row)
    except Exception as e:
        print e

if __name__ == '__main__':
    base_image(u'img.png')