# coding=utf-8

import os
import re
import contextlib
from PIL import Image


@contextlib.contextmanager
def open_image(file_name, auto_save=True, image_type=None):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    img_dir = os.path.join(base_dir, u'GraphManipulation\Images')
    file_dir = os.path.join(img_dir, file_name)
    im = Image.open(file_dir)
    try:
        yield im
    except Exception as e:
        print e
    finally:
        if auto_save:
            pre_file = u'new_%s' % re.search(u'\w+', file_name).group()
            file_suffix = re.search(u'\.\w+', file_name).group()
            if image_type:
                new_name = u'%s%s' % (pre_file, image_type)
            else:
                new_name = u'%s%s' % (pre_file, file_suffix)
            new_img = os.path.join(img_dir, new_name)
            im.save(new_img)

if __name__ == '__main__':
    pass