# coding=utf-8

import os
import contextlib
import datetime
from PIL import Image


class NewImage:
    def __init__(self, file_name):
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.img_file_dir = os.path.join(self.base_dir, u'GraphManipulation\Images')
        self.file_dir = os.path.join(self.img_file_dir, file_name)
        self.im = Image.open(self.file_dir)


@contextlib.contextmanager
def open_image(file_name):
    new_im = NewImage(file_name)
    try:
        yield new_im
    except Exception as e:
        print e
    finally:
        pass

if __name__ == '__main__':
    pass


def calculate_by_time(func):
    def wrapper(*args, **kwargs):
        begin = datetime.datetime.now()
        func(*args, **kwargs)
        end = datetime.datetime.now()
        time = end - begin
        print u'运行时间：%s s' % time
    return wrapper