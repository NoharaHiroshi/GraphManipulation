# coding=utf-8

import os
import re
import ImageFilter
import ImageEnhance
from base import open_image
from PIL import Image

'''
    1、透明图像的alpha通道值为0-255,0为透明， 255为100%
'''


# 获取图片主体
def get_main_image(img, value):
    try:
        width, height = img.size
        r, g, b = img.split()
        alpha = b
        main_alpha = alpha.getdata()
        first_p = main_alpha[0]
        for h in range(height):
            start = 0
            end = 0
            for w in range(width):
                pixel = alpha.getpixel((w, h))
                if pixel < first_p - value:
                    start = w
                    break
            for _w in range(width)[::-1]:
                pixel = alpha.getpixel((_w, h))
                if pixel < first_p - value:
                    end = _w
                    break
            pixel_start_list = range(0, start)
            pixel_end_list = range(end, width)
            pixel_list = range(start, end)
            for p in pixel_start_list:
                alpha.putpixel((p, h), 0)
            for p in pixel_end_list:
                alpha.putpixel((p, h), 0)
            for p in pixel_list:
                alpha.putpixel((p, h), 255)
        return alpha
    except Exception as e:
        print e


# 测试简单白底图片转换为透明
def convert_trans_pic(img):
    try:
        with open_image(img) as image:
            new_img = image.im.resize((500, 431))
            if new_img.mode == 'RGB':
                r, g, b = new_img.split()
                a = get_main_image(new_img, 40)
                a_img = Image.merge('RGBA', (r, g, b, a))
                a_img.save('test.png')
    except Exception as e:
        print e

if __name__ == '__main__':
    convert_trans_pic('leaf_2.jpg')
