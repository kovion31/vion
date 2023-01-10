# -*- coding: utf-8 -*-


import simple_draw as sd


def rainbow():
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

    radius = 900
    for color in rainbow_colors:
        point = sd.get_point(400, -100)
        sd.circle(point, radius, color, 5)
        radius += -5
