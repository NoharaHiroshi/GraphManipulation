# coding=utf-8

import os
import numpy as np
from base import open_image
from PIL import Image

convert_char = [u'█', u'▉', u'▊', u'▌', u'▍', u'▎', u'▏']


def base_image(img):
    try:
        with open_image(img) as image:
            new_img = image.im.convert('RGBA')
            new_img = new_img.resize((128, 128))
            print new_img.mode
            width, height = new_img.size
            # 逐行扫描，高度为0,1,2,3。。。
            for h in range(height):
                row = list()
                for w in range(width):
                    r, g, b, a = new_img.getpixel((w, h))
                    con = len(convert_char) - 1
                    gary = int(r*0.299 + g*0.587 + b*0.114)
                    flag = gary // (255 // con)
                    row.append(u'%s(%s)' % (convert_char[flag], flag))
                print ' '.join(row)
            new_img.show()
    except Exception as e:
        print e

if __name__ == '__main__':
    base_image(u'img.png')