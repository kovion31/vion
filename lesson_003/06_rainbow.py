# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код
point_start_x = 50
point_end_x = 350
for color in rainbow_colors:
    point_start = sd.get_point(point_start_x, 50)
    point_end = sd.get_point(point_end_x, 450)
    sd.line(point_start, point_end, color, 4)
    point_start_x += 5
    point_end_x += 5

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код
# radius = 700
# for color in rainbow_colors:
#     point = sd.get_point(400, -200)
#     sd.circle(point, radius, color, 4)
#     radius += -5


sd.pause()
