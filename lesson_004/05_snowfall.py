# -*- coding: utf-8 -*-

from random import randint

import simple_draw as sd

sd.resolution = (1200, 600)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 200

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

# TODO здесь ваш код
x = []
y = []
length = []

# y = 500
# x = 100

# y2 = 450
# x2 = 150
while True:
    # sd.clear_screen()
    sd.start_drawing()
    i = 0
    while i < N:
        x.append(sd.random_number(0, 1200))
        y.append(sd.random_number(0, 600))
        length.append(sd.random_number(5, 25))
        if y[i] > 50:
            point = sd.get_point(x[i], y[i])
            sd.snowflake(center=point, length=length[i], color=sd.background_color)
        else:
            y[i] += 600

        y[i] -= 10
        x[i] = x[i] + sd.random_number(0, 50)
        if x[i] > 1200:
            x[i] = 0

        point = sd.get_point(x[i], y[i])
        sd.snowflake(center=point, length=length[i], color=sd.COLOR_WHITE)

        i += 1

    # point2 = sd.get_point(x2, y2)
    # sd.snowflake(center=point2, length=30)
    # y2 -= 10
    # if y2 < 50:
    #    break
    # x2 = x2 + 20
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


