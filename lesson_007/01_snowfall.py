# -*- coding: utf-8 -*-

import simple_draw as sd


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    def __init__(self):
        self.x = sd.random_number(0, 600)
        self.y = sd.random_number(0, 600)
        self.length = sd.random_number(5, 25)

    def clear_previous_picture(self):
        center = sd.get_point(x=self.x, y=self.y)
        sd.snowflake(center=center, length=self.length, color=sd.background_color)

    def move(self):
        self.x += sd.random_number(-5, 5)
        self.y -= sd.random_number(5, 10)

    def draw(self):
        center = sd.get_point(x=self.x, y=self.y)
        sd.snowflake(center=center, length=self.length)

    def can_fall(self):
        if self.y < 0:
            self.y += 600
            # fallen_flakes += 1
        if self.x > 600:
            self.x -= 600


def get_flakes(count):
    i = 0
    new_flakes = []
    while i < N:
        new_flakes.append(Snowflake())
        i += 1
    return new_flakes


# def get_fallen_flakes():
#     if flake.y < 0:
#         return 1


# flake = Snowflake()

# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     flake.can_fall()
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
N = 100
fallen_flakes = 0
flakes = get_flakes(count=N)  # создать список снежинок
while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
        flake.can_fall()
        # fallen_flakes += get_fallen_flakes()  # подчитать сколько снежинок уже упало
    # if fallen_flakes:
    #     append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
