from wall import wall_paint
import simple_draw as sd
from math import sin, cos, pi
from smile import smile



def house_paint(house_point_x, house_point_y):
    house_width = 400
    house_height = 200
    brick_width = 50
    brick_height = 25

    # Стена (стартовая точка по Х, стартовая точка по Y, ширина кирпича, высота кирпича)
    wall_paint(house_point_x, house_point_y, brick_width, brick_height)

    # Крыша
    start_point = sd.get_point((house_point_x - 25), (house_point_y + house_height))
    v1 = sd.get_vector(start_point=start_point, angle=0, length=house_width + 75)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=150, length=(((house_width + 75) / 2) / cos(pi / 6)))
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=210, length=(((house_width + 75) / 2) / sin(pi / 3)))
    v3.draw()

    # Окно
    left_bottom_point_x = house_point_x + brick_width / 4 + house_width / 4
    left_bottom_point_y = house_point_y + house_height / 4
    right_top_point_x = house_point_x + brick_width / 4 + house_width * 3 / 4
    right_top_point_y = house_point_y + house_height * 3 / 4
    left_bottom = sd.get_point(left_bottom_point_x, left_bottom_point_y)
    right_top = sd.get_point(right_top_point_x, right_top_point_y)
    sd.rectangle(left_bottom=left_bottom, right_top=right_top)

    # Смайлик
    smile(x1=left_bottom_point_x, y1=left_bottom_point_y, x2=right_top_point_x, y2=right_top_point_y)
