# coding=utf-8

import os
import re
from base import open_image
from PIL import Image


# Check Picture Information
# 输出图片属性
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
# 转换图片格式
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
# 创建缩略图
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
# 裁剪中心图像并旋转
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
# 分割通道并合并
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


# Resize Picture
# 图形几何变换
def resize_picture(img, size):
    status = u'success'
    try:
        with open_image(img) as image:
            new_img = image.im
            if isinstance(size, tuple):
                new_img = new_img.resize(size)
            else:
                status = u'fail'
            new_img.show()
            print status
    except Exception as e:
        print e


# Rotate Picture
# 旋转图形
def rotate_picture(img, angle):
    try:
        with open_image(img) as image:
            new_img = image.im
            new_img = new_img.rotate(angle)
            new_img.show()
    except Exception as e:
        print e


# Transpose Picture
# 旋转图形（水平反转）
def transpose_picture(img):
    try:
        with open_image(img) as image:
            new_image = image.im
            new_image = new_image.transpose(Image.FLIP_LEFT_RIGHT)
            new_image = new_image.transpose(Image.ROTATE_90)
            new_image = new_image.transpose(Image.ROTATE_180)
            new_image.show()
    except Exception as e:
        print e

if __name__ == '__main__':
    transpose_picture(u'img.png')