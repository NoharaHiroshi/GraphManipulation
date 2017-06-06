# coding=utf-8

from base import open_image


def base_image(img):
    try:
        with open_image(img) as image:
            image.convert("1")
            print image.mode
    except Exception as e:
        print e

if __name__ == '__main__':
    base_image(u'img.jpg')
