# coding=utf-8

import os
import re
import ImageFilter
import ImageEnhance
import numpy as np
from base import open_image
from PIL import Image

'''
    1、透明图像的alpha通道值为0-255,0为透明， 255为100%
'''


# 获取图片主体
def get_main_image(img):
    try:
        width, height = img.size
        r, g, b = img.split()
        alpha = b.point(lambda x: 300-x)
        main_alpha = alpha.getdata()
        p_list = [p for p in main_alpha]
        first_p = main_alpha[0]
        for h_i, h in enumerate(range(height)):
            for w_i, w in enumerate(range(width)):
                # 确定主体范围
                if alpha.getpixel((w, h)) > first_p:
                    # 进入边界
                    first_i = w
                    # 边界到行末端值一致为出边界
                    min_w = h_i*width+first_i
                    max_w = (h_i+1)*width
                    for i in range(min_w, max_w):
                        main_set = set(p_list[i:max_w])
                        if len(main_set) == 0 and main_set[0] == first_p and main_alpha[i-1] > first_p:
                            print min_w, i
                            continue
    except Exception as e:
        print e


# 测试简单白底图片转换为透明
def convert_trans_pic(img):
    try:
        with open_image(img) as image:
            new_img = image.im
            if new_img.mode == 'RGB':
                r, g, b = new_img.split()
                a = b.point(lambda x: 300-x)
                a_img = Image.merge('RGBA', (r, g, b, a))
                a_img.save('test.png')
    except Exception as e:
        print e

if __name__ == '__main__':
    # convert_trans_pic('leaf_2.jpg')
    with open_image('leaf_2.jpg') as image:
        get_main_image(image.im)
