# coding=utf-8

import os
import re
from base import open_image


# Check Picture Information
def check_picture_image(img):
    try:
        with open_image(img) as image:
            new_img = image.im
            return {
                u'mode': new_img.mode,
                u'size': new_img.size,
                u'format': new_img.format
            }
    except Exception as e:
        print e


# Transition Picture format
def transition_picture_format(img, img_type):
    try:
        with open_image(img) as image:
            file_name = re.search(u'^\w+', img).group()
            file_dir = image.img_file_dir
            new_img = image.im
            new_img_dir = os.path.join(file_dir, u'%s.%s' % (file_name, img_type))
            new_img.save(new_img_dir)
            new_img.show()
    except Exception as e:
        print e

if __name__ == '__main__':
    transition_picture_format(u'cat.jpg', u'png')