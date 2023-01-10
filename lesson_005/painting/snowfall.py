# -*- coding: utf-8 -*-

import simple_draw as sd


def snowfall(x1, y1, x2, y2):
    N = 50
    x = []
    y = []
    length = []
    while True:
        # sd.clear_screen()
        sd.start_drawing()
        i = 0
        while i < N:
            x.append(sd.random_number(x1, x2))
            y.append(sd.random_number(y1, y2))
            length.append(sd.random_number(5, 25))
            if y[i] > y1:
                point = sd.get_point(x[i], y[i])
                sd.snowflake(center=point, length=length[i], color=sd.background_color)
            else:
                y[i] += y2

            y[i] -= 10
            x[i] = x[i] + sd.random_number(0, 20)
            if x[i] > x2:
                x[i] = 0
            point = sd.get_point(x[i], y[i])
            sd.snowflake(center=point, length=length[i], color=sd.COLOR_WHITE)
            i += 1
        sd.finish_drawing()
        sd.sleep(0.1)
        if sd.user_want_exit():
            break
