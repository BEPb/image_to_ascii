"""
Python 3.10 программа преобразования картинки в текст
Картинку можно загрузить как из файла так и из интернета
Название файла img_to_txt_rus.py

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-02-11
"""

from PIL import Image
import numpy as np
import requests
import sys

txt_file = f'texts/out.txt'
# img_file = ['-', f'pictures/superman.jpg', 90]  # указываем адрес файла изображения для обработки и его конечный размер
img_file = ['-', f'pictures/py.jpg', 80]  # указываем адрес файла изображения для обработки и его конечный размер

abc = '##@@MMBB88NNHHOOGGPPEEXXFFVVYY22ZZCC77LLjjll11rrii;;;:::....  '
l = 256 / len(abc)

# функция определяет тип изображения
def remove_transparency(im, bg_colour=(255, 255, 255)):
    # Обрабатывать только в том случае, если изображение имеет прозрачность
    if im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info):

        # Необходимо преобразовать в RGBA, если формат LA из-за ошибки в PIL
        alpha = im.convert('RGBA').split()[-1]

        # Создайте новое фоновое изображение нашего матового цвета.
        # Должен быть RGBA, потому что вставка требует, чтобы оба изображения имели одинаковый формат
        bg = Image.new("RGBA", im.size, bg_colour + (255,))
        bg.paste(im, mask=alpha)
        return bg
    else:
        return im

# преобразование картинки
def pixel_to_black(fp, weight):
    try:
        img = Image.open(fp)
    except:
        print('Введите правильный путь или URL изображения, пожалуйста.')
        return
    img = remove_transparency(img)
    img = img.convert("L")
    im_w, im_h = img.size
    img = np.array(img)
    h, w = img.shape
    # ширина
    weight_w = weight if w >= weight else w
    weight_h = weight if h >= weight else h
    weight = weight_w if weight_w < weight_h else weight_h
    # Максимальная ширина символа
    t_w = weight
    # Максимальная высота символов
    t_h = weight / (im_w / im_h) / 2
    width_times = int(w / t_w) if int(w / t_w) != 0 else 1
    high_times = int(h / t_h) if int(h / t_h) != 0 else 1

    tmp_high = []
    for high_index in range(int(h / high_times)):
        tmp_width = []
        for width_index in range(int(w / width_times)):
            tmp_block = []
            for y in range((high_index * high_times), ((high_index + 1) * high_times)):
                for x in range(width_index * width_times, (width_index + 1) * width_times):
                    tmp_block.append(img[y, x])
            avg_tmp_block = sum(tmp_block) / len(tmp_block)
            tmp_width.append(avg_tmp_block)
        tmp_high.append(tmp_width)
    return tmp_high


def black_to_alphabet(rgb_list):
    tmp_high = ''
    for i in rgb_list:
        tmp_width = ''
        for ii in i:
            a = abc[int(ii / l)]
            tmp_width += a
        tmp_width += '\n'
        tmp_high += tmp_width
    return tmp_high

# функция преобразования изображения в текст
def paint(uri, weight):
    if uri.startswith('http'):  # если указана ссылка в интернете, то скачиваем изображение
        print('Распознана ссылка')
        img = get_img(uri)
    else:  # иначе указана ссылка на локальное изображение (файл)
        print('Распознан файл')
        img = uri
    rgb_list = pixel_to_black(img, weight)
    if not rgb_list:
        return
    s = black_to_alphabet(rgb_list)
    with open(txt_file, 'w', encoding='utf-8') as f:
        f.write(s)
    return s

# функция взятия изображения
def get_img(url):
    print('Загрузка изображения из Интернета, пожалуйста, подождите.')
    response = requests.get(url)
    if response.status_code == 200:
        with open(f'pictures/temp.png', 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
            return f'pictures/temp.png'

'''Главная функция'''
def main(args):  # функция принимает аргументы
    try:
        print('Ваша ссылка принята')
        uri = args[1]
        assert type(uri) == str
    except:
        # изображение по умолчанию, в случае если не задано иное
        print('Вы не указали ссылку на скачивание, по этой причине будет загружено изображение по умолчанию...')
        uri = 'https://i.postimg.cc/t4Cmn7wC/py.png'
    try:
        weight = int(args[2])  # второй аргумент, это ширина изображения текста в символах
        assert type(weight) == int  # проверяем что заданное число - целое
    except:
        weight = 80  # если ширина не задана, то по умолчанию 80 символов
    s = paint(uri, weight=weight)
    if not s:
        return
    print(s)  # печать в командной строке преобразованного изображения в текст

# проверка на главную программу и запуск главной функции
if __name__ == '__main__':
    main(sys.argv)  # запускаем главную функцию с аргументами при запуске программы
    # main(img_file)  # запускаем главную функцию с картинкой из папки
