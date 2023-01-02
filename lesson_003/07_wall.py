# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код
for point_y in [0, 100, 200, 300, 400, 500]:
    point_start = simple_draw.get_point(0, point_y)
    point_end = simple_draw.get_point(600, point_y)
    simple_draw.line(point_start, point_end)
    for point_x in [100, 200, 300, 400, 500]:
        point_start = simple_draw.get_point(point_x, point_y)
        point_end = simple_draw.get_point(point_x, point_y + 50)
        simple_draw.line(point_start, point_end)
for point_y in [50, 150, 250, 350, 450, 550]:
    point_start = simple_draw.get_point(0, point_y)
    point_end = simple_draw.get_point(600, point_y)
    simple_draw.line(point_start, point_end)
    for point_x in [50, 150, 250, 350, 450, 550]:
        point_start = simple_draw.get_point(point_x, point_y)
        point_end = simple_draw.get_point(point_x, point_y + 50)
        simple_draw.line(point_start, point_end)

simple_draw.pause()
