# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

# TODO здесь ваш код
colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]
colors_ru = ['Красный', 'Оранжевый', 'Желтый', 'Зеленый', 'Голубоу', 'Синий', 'Фиолетовый']

print("Возможные цвета:")
for i, color_ru in enumerate(colors_ru):
    print(i, ':', color_ru)

user_input = input('Введите номер желаемый цвет: ')
color = colors[int(user_input)]
print('Вы выбрали ', colors_ru[int(user_input)])


length = 100
width = 2
angle = 20
point = sd.get_point(100, 100)

v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
v1.draw(color=color)

v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=width)
v2.draw(color=color)

v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=width)
v3.draw(color=color)

# - квадрат
point = sd.get_point(400, 100)

v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
v1.draw(color=color)

v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=length, width=width)
v2.draw(color=color)

v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=length, width=width)
v3.draw(color=color)

v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 270, length=length, width=width)
v4.draw(color=color)

# - пятиугольник
point = sd.get_point(100, 400)

v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
v1.draw(color=color)

v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=length, width=width)
v2.draw(color=color)

v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 72 * 2, length=length, width=width)
v3.draw(color=color)

v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 72 * 3, length=length, width=width)
v4.draw(color=color)

v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 72 * 4, length=length, width=width)
v5.draw(color=color)

# - шестиугольника
point = sd.get_point(400, 400)

v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
v1.draw(color=color)

v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length, width=width)
v2.draw(color=color)

v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=length, width=width)
v3.draw(color=color)

v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=length, width=width)
v4.draw(color=color)

v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=length, width=width)
v5.draw(color=color)

sd.line(start_point=v5.end_point, end_point=point, width=width, color=color)

sd.pause()
