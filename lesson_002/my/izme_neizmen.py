# неизменяеые объекты
valve = 42
print(id(valve))

mass = valve
print(id(mass))

mass = mass + 1
print('valve id =', id(valve))
print('mass id =', id(mass))

car = 'nissan'
print(id(car))
my_car = car
print(id(my_car))
my_car = my_car + ' terrano'
print(id(car), id(my_car))
print(car)
print(my_car)