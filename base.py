# coding=utf-8

import os
import contextlib
from PIL import Image


@contextlib.contextmanager
def open_image(file_name):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    img_dir = os.path.join(base_dir, u'GraphManipulation\Images')
    file_dir = os.path.join(img_dir, file_name)
    im = Image.open(file_dir)
    try:
        yield im
    except Exception as e:
        print e
    finally:
        pass

if __name__ == '__main__':
    pass