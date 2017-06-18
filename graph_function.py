# coding=utf-8

import os
import re
import ImageFilter
import ImageEnhance
from base import open_image
from PIL import Image


# 创建新的图片
def new_image(mode, size, color):
    try:
        img = Image.new(mode, size, color)
        img.show()
    except Exception as e:
        print e


# 合并图像(将两张图片以相同的透明度合并)
def blend_image(img1, img2, alpha):
    try:
        with open_image(img1) as image:
            new_img1 = image.im.resize((200, 200))
        with open_image(img2) as image:
            new_img2 = image.im.resize((200, 200))
        blend_img = Image.blend(new_img1, new_img2, alpha)
        blend_img.show()
    except Exception as e:
        print e


# 合并图片
def composite_image(img1, img2):
    try:
        with open_image(img1) as image:
            new_img1 = Image.new('L', (200, 200))
        with open_image(img2) as image:
            new_img2 = image.im.resize((200, 200))
            m = new_img2.convert('L')
        comp_img = Image.composite(new_img1, new_img2, m)
        comp_img.show()
    except Exception as e:
        print e


# 对每个像素进行处理
def eval_image(img):
    try:
        with open_image(img) as image:
            new_img = image.im
            new_img = Image.eval(new_img, lambda x: x*2)
            new_img.show()
    except Exception as e:
        print e


if __name__ == "__main__":
    eval_image('cat.jpg')