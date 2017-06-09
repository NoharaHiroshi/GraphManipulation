# coding=utf-8

from PIL import Image, ImageDraw


def main():
    im = Image.new("RGBA", (800, 800))
    draw = ImageDraw.Draw(im)
    draw.rectangle((0, 0, 200, 200), fill=(255, 0, 0, 128))
    draw.rectangle((400, 400, 600, 600), fill=(255, 0, 0))

    im2 = Image.new("RGBA", (800, 800))
    draw2 = ImageDraw.Draw(im2)
    draw2.rectangle((100, 100, 300, 300), fill=(0, 255, 0, 128))
    draw2.rectangle((500, 500, 700, 700), fill=(0, 255, 0))

    # merge two images using blend
    blend = Image.blend(im, im2, 128)
    # drawf = ImageDraw.Draw(blend)
    # drawf.rectangle((500, 100, 600, 200), fill=(255, 0, 0))
    # drawf.rectangle((600, 200, 700, 300), fill=(0, 255, 0))
    blend.show()

    # merge two images using composite
    ones = Image.new("RGBA", (800, 800))
    _draw = ImageDraw.Draw(ones)
    _draw.rectangle((0, 0, 800, 800), fill=(255, 255, 255, 128))
    final = Image.composite(im, im2, ones)
    final.show()


if __name__ == '__main__':
    main()