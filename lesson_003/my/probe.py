x, y = 10, 29

if x < 0:
    print('Х меньше нуля')
    z = x**2 + y
else:
    print('Х больше нуля')
    z = x - y
print('Результат', z)


print('Здравствуйте')
my_family = ['Мама', 'Папа', 'Сестра']
my_family_height = [
    [my_family[0], 172],
    [my_family[1], 185],
    [my_family[2], 144]
]
print('Рост отца -', my_family_height[1][1], 'см')

total_heiding = my_family_height[0][1]
total_heiding += my_family_height[1][1]
total_heiding += my_family_height[2][1]
print('Общий рост моей семьи -', total_heiding, 'см')
