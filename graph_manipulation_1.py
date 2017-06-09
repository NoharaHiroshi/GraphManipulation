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


# Create Thumbnail
def create_thumbnail(img, rate=None, resize=None):
    status = u'success'
    try:
        with open_image(img) as image:
            new_img = image.im
            new_size = new_img.size
            width, height = new_size
            if resize:
                if isinstance(resize, tuple):
                    new_size = resize
                else:
                    status = u'fail'
                    return status
            elif rate:
                if isinstance(rate, (int, float)):
                    _width = int(width * rate)
                    _height = int(height * rate)
                    new_size = _width, _height
                else:
                    status = u'fail'
                    return status
            else:
                status = u'fail'
                return status
            new_img.thumbnail(new_size)
            new_img.show()
        return status
    except Exception as e:
        print e


if __name__ == '__main__':
    create_thumbnail(u'img.png', resize=(200, 200))