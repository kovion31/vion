my_pets = ['lion', 'dog', 'skunk', 'hamster', 'cat', 'monkey']
i = -1
while i < len(my_pets):
    i += 1
    if i == 2:
        continue
    pet = my_pets[i]
    print('Проверяем ', pet)
    if pet == 'cat':
        print('Ура, кот найден!')
        break
print('дотвиданя!')