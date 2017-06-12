# coding=utf-8

import os
import re
import ImageFilter
import ImageEnhance
from base import open_image
from PIL import Image


# Point Operation
# 点操作:对图像中的每个点进行某种变换
def point_operation(img):
    try:
        with open_image(img) as image:
            new_img = image.im
            # point(lambda x)
            new_img = new_img.point(lambda i: i * 2)
            new_img.show()
    except Exception as e:
        print e


# Single Channel Operation
# 单个通道的处理
def single_channel_operation(img):
    try:
        with open_image(img) as image:
            new_img_channels = image.im.split()
            r, g, b = range(3)
            red_channel = new_img_channels[r].point(lambda i: i < 100 and 255)
            green_channel = new_img_channels[g].point(lambda i: i * 0.7)
            green_channel.paste(green_channel, None, red_channel)
            new_img = Image.merge(image.im.mode, new_img_channels)
            new_img.show()
    except Exception as e:
        print e


# Enhance Picture
# 增强图片
def ehance_picture(img):
    try:
        with open_image(img) as image:
            new_img = ImageEnhance.Contrast(image.im)
            new_img.enhance(1.8).show("30% more contrast")
    except Exception as e:
        print e

if __name__ == '__main__':
    ehance_picture(u'cat_1.jpg')