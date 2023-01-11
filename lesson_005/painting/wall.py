# -*- coding: utf-8 -*-

import simple_draw as sd


def brick_paint(point_x1, point_y1, brick_width, brick_height):
    start_point = sd.get_point(point_x1, point_y1)
    v1 = sd.get_vector(start_point=start_point, angle=0, length=brick_width)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=90, length=brick_height)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=180, length=brick_width)
    v3.draw()
    v4 = sd.get_vector(start_point=v3.end_point, angle=270, length=brick_height)
    v4.draw()


def wall_paint(point_x1, point_y1, brick_width, brick_height):
    shift = brick_width / 2
    wall_width = 400
    wall_height = 200
    for brick_y in range(point_y1, point_y1 + wall_height, brick_height):
        for brick_x in range(point_x1, point_x1 + wall_width, brick_width):
            brick_paint(brick_x + shift, brick_y, brick_width, brick_height)
        if shift == 0:
            shift = brick_width / 2
        else:
            shift = 0
    start_point = sd.get_point(point_x1, point_y1)
    v1 = sd.get_vector(start_point=start_point, angle=0, length=wall_width + shift)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=90, length=wall_height)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=180, length=wall_width + shift)
    v3.draw()
    v4 = sd.get_vector(start_point=v3.end_point, angle=270, length=wall_height)
    v4.draw()
