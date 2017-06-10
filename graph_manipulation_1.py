# coding=utf-8

import os
import re
from base import open_image
from PIL import Image


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


# Operation Picture
def operation_picture(img, r_size):
    try:
        with open_image(img) as image:
            new_img = image.im.convert('RGBA')
            m_width, m_height = [i//2 for i in new_img.size]
            r_size //= 2
            box = (m_width-r_size, m_height-r_size, m_width+r_size, m_height+r_size)
            region = new_img.crop(box)
            region = region.transpose(Image.ROTATE_180)
            new_img.paste(region, box)
            new_img.show()
    except Exception as e:
        print e


# Split And Merge Channel
def operation_channel(img):
    try:
        with open_image(img) as image:
            new_img = image.im
            if new_img.mode == 'RGB':
                r, g, b = new_img.split()
                change_image = Image.merge("GRB", (g, b, r))
            elif new_img.mode == 'RGBA':
                r, g, b, a = new_img.split()
                change_image = Image.merge("GRBA", (g, b, r, a))
            else:
                change_image = new_img
            change_image.show()
    except Exception as e:
        print e

if __name__ == '__main__':
    operation_channel(u'img.png')