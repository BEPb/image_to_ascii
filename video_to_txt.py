"""
Python 3.10 программа преобразования видео в текст
видео можно загрузить как из файла так и из интернета
Название файла video_to_txt.py

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-02-11
"""
import cv2
from PIL import Image
import numpy as np
import time
import sys

abc = '@MWNHB8$06XFVYZ27>1jli!;:,. '
l = 256 / len(abc)

def remove_transparency(im, bg_colour=(255, 255, 255)):
    if im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info):
        alpha = im.convert('RGBA').split()[-1]
        bg = Image.new("RGBA", im.size, bg_colour + (255,))
        bg.paste(im, mask=alpha)
        return bg

    else:
        return im

def img2pixel(img, charwidth=100):
    img = img.convert("L")
    w, h = img.size
    img = img.resize((charwidth, int(charwidth * (h / w) / 2.4)))
    data = np.array(img)
    return data


def pixel2char(data):
    chars = '\n\n'
    for row in data:
        for pixel in row:
            a = abc[int(pixel / l)]
            chars += a
        chars += '\n'
    return chars + '\n'


def main(args):
    start = time.time()
    if len(args) != 3:
        return
    vcap = cv2.VideoCapture(args[1])
    width = vcap.get(cv2.CAP_PROP_FRAME_WIDTH)  # вещественное число
    height = vcap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # вещественное число
    fps = vcap.get(cv2.CAP_PROP_FPS)
    print(width, height, fps)

    currentframe = 0
    while (True):
        t1 = time.time()
        ret, frame = vcap.read()
        if ret:
            pilimg = Image.fromarray(frame)
            data = img2pixel(pilimg, charwidth=int(args[2]))
            s = pixel2char(data=data)
            print(s)
            currentframe += 1
        else:
            break

        time2sleep = (1 / fps) - (time.time() - t1)
        if time2sleep > 0: time.sleep(time2sleep)

    # Освободите пространство и окна
    vcap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
