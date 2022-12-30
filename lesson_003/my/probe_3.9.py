zoo_pets = [
    'lion', 'monkey', 'skunk',
    # 'elephant', 'horse',
]
for animal in zoo_pets:
    if animal == 'skunk':
        print('Фууу...')
        continue
    print('Сейчас переменная animal указывает на', animal)
    if animal == 'elephant':
        print('Нашли слона! :)')
        break
    print('Это не слон....')
else:
    print('Тут слона нет...')
print('Выход из цикла')