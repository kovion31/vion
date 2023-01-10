# -*- coding: utf-8 -*-
import random

import simple_draw as sd
from random import randint

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# TODO здесь ваш код

# delta = 30



def draw_branches(point, angle, length):
    delta = randint(int(30 - (30 * .4)), int(30 + (30 * .4)))
    deviation_length = (randint(int(75 - (75 * .2)), int(75 + (75 * .2))))/100
    if length > 10:
        color = sd.COLOR_WHITE
    if length < 10:
        color = sd.COLOR_GREEN
    if length < 2:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, )
    v1.draw(color=color)
    next_point = v1.end_point
    next_angle_1 = angle - delta
    next_angle_2 = angle + delta
    next_length = length * deviation_length
    draw_branches(point=next_point, angle=next_angle_1, length=next_length)
    draw_branches(point=next_point, angle=next_angle_2, length=next_length)


# for delta


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()
