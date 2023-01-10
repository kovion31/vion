# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw
from random import random, randint


# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# TODO здесь ваш код

def smile(x1, y1, x2, y2):
    for _ in range(1):
        x = randint(int(x1), int(x2 - 100))
        y = randint(int(y1), int(y2 - 50))
        point = simple_draw.get_point(x, y)
        point_2 = simple_draw.get_point(x + 100, y + 50)
        point_3 = simple_draw.get_point(x + 25, y + 15)
        point_4 = simple_draw.get_point(x + 75, y + 15)
        color = simple_draw.random_color()
        simple_draw.ellipse(point, point_2, width=1, color=color)
        simple_draw.circle(simple_draw.get_point(x + 25, y + 30), radius=5, color=color)
        simple_draw.circle(simple_draw.get_point(x + 75, y + 30), radius=5, color=color)
        simple_draw.line(point_3, point_4, color=color)
