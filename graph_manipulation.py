# coding=utf-8

import os
from base import open_image


def base_image(img):
    try:
        with open_image(img) as image:
            new_img = image.im.convert("1")
            new_dir = os.path.join(image.img_dir, 'new_img.jpg')
            new_img.save(new_dir)
    except Exception as e:
        print e

if __name__ == '__main__':
    base_image(u'img.jpg')
