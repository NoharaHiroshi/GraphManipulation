# coding=utf-8

import os
import re
import ImageFilter
import ImageEnhance
from base import open_image, calculate_by_time
from PIL import Image

'''
    1、透明图像的alpha通道值为0-255,0为透明， 255为100%
'''


# 获取图片主体(横)
def get_row_main_image(img, value):
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


# 获取图片主体(纵)
def get_col_main_image(img, value):
    try:
        width, height = img.size
        r, g, b = img.split()
        alpha = b
        main_alpha = alpha.getdata()
        first_p = main_alpha[0]
        for w in range(width):
            start = 0
            end = 0
            for h in range(height):
                pixel = alpha.getpixel((w, h))
                if pixel < first_p - value:
                    start = h
                    break
            for _h in range(height)[::-1]:
                pixel = alpha.getpixel((w, _h))
                if pixel < first_p - value:
                    end = _h
                    break
            pixel_start_list = range(0, start)
            pixel_end_list = range(end, height)
            pixel_list = range(start, end)
            for p in pixel_start_list:
                alpha.putpixel((w, p), 0)
            for p in pixel_end_list:
                alpha.putpixel((w, p), 0)
            for p in pixel_list:
                alpha.putpixel((w, p), 255)
        return alpha
    except Exception as e:
        print e


def get_main_image(img, value):
    row_alpha = get_row_main_image(img, value)
    col_alpha = get_col_main_image(img, value)
    width, height = img.size
    for h in range(height):
        for w in range(width):
            row_pixel = row_alpha.getpixel((w, h))
            col_pixel = col_alpha.getpixel((w, h))
            if row_pixel != col_pixel:
                col_alpha.putpixel((w, h), 0)
    alpha = col_alpha
    return alpha


# 测试简单白底图片转换为透明
def convert_trans_pic(img):
    try:
        with open_image(img) as image:
            new_img = image.im
            if new_img.mode == 'RGB':
                r, g, b = new_img.split()
                a = get_main_image(new_img, 20)
                a_img = Image.merge('RGBA', (r, g, b, a))
                a_img.save('test.png')
            else:
                print 'not RGB mode'
    except Exception as e:
        print e

if __name__ == '__main__':
    convert_trans_pic('flower_1.jpg')
