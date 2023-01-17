# -*- coding: utf-8 -*-

from random import randint


# Реализуем модель человека.
# Человек может есть, работать, играть, ходить в магазин.
# У человека есть степень сытости, немного еды и денег.
# Если сытость < 0 единиц, человек умирает.
# Человеку надо прожить 365 дней.
from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')
            self.fullness -= 5
            self.shopping()

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 10
        self.fullness -= 5

    def cleaning(self):
        cprint('{} Убрал мусор в доме'.format(self.name), color='blue')
        self.house.mud = 100
        self.fullness -= 5

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money > 0:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            # self.house.money -= 50
            self.house.food = self.house.money
            self.house.money = 0
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')
            self.work()

    def shopping_pets(self):
        if self.house.money > 0:
            cprint('{} сходил в магазин за едой для животных'.format(self.name), color='magenta')
            # self.house.money -= 50
            self.house.food_pet = self.house.money
            self.house.money = 0
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')
            self.work()

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def act(self):
        if self.fullness < 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food_pet < 5:
            self.shopping_pets()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif self.house.mud <= 0:
            self.cleaning()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 20
        self.house = None

    def __str__(self):
        return 'Кот - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food_pet >= 0:
            cprint('Кот {} поел'.format(self.name), color='yellow')
            self.fullness += 5
            self.house.food_pet -= 5
        else:
            cprint('Кот {} нет еды'.format(self.name), color='red')
            self.sleep()

    def sleep(self):
        cprint('Кто {} спал целый день'.format(self.name), color='green')
        self.fullness -= 5

    def play(self):
        cprint('Кто {} играл целый день'.format(self.name), color='green')
        self.fullness -= 5

    def tear_wallpaper(self):
        cprint('Кто {} Дерет обои'.format(self.name), color='green')
        self.fullness -= 5
        self.house.mud -= 10

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 5
        cprint('Кот {} Вьехал в дом'.format(self.name), color='cyan')

    def act(self):
        if self.fullness < 0:
            cprint('Кот {} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 5:
            self.eat()
        elif dice == 1:
            self.play()
        elif dice == 2:
            self.eat()
        elif dice == 3:
            self.tear_wallpaper()
        else:
            self.sleep()


class House:

    def __init__(self):
        self.food = 50
        self.food_pet = 0
        self.money = 0
        self.mud = 100

    def __str__(self):
        return 'В доме еды осталось {}, еды для питомцев {}, денег осталось {}, чистота {}%'.format(
            self.food, self.food_pet, self.money, self.mud)


citizens = [
    Man(name='Бивис'),
    Man(name='Батхед'),
    Man(name='Кенни'),
]

pets = [
    Cat(name='Барсик'),
    Cat(name='Персик')
]


my_sweet_home = House()
for citisen in citizens:
    citisen.go_to_the_house(house=my_sweet_home)
for pet in pets:
    pet.go_to_the_house(house=my_sweet_home)


for day in range(1, 366):
    cprint('================ день {} =================='.format(day), color='yellow')
    for citisen in citizens:
        citisen.act()
    for pet in pets:
        pet.act()
    print('--- в конце дня ---')
    for citisen in citizens:
        print(citisen)
    for pet in pets:
        print(pet)
    print(my_sweet_home)

# Создадим двух людей, живущих в одном доме - Бивиса и Батхеда
# Нужен класс Дом, в нем должн быть холодильник с едой и тумбочка с деньгами
# Еда пусть хранится в холодильнике в доме, а деньги - в тумбочке.
