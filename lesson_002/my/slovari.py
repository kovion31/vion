# Словари - изменяемый объект
my_box = {}

my_box["слон"] = "Элифан"
print(my_box["слон"])
my_box['машина'] = "nissan"
print(my_box["машина"])
print(my_box)

print("слон" in my_box)

print(my_box.setdefault("кот", "Мурзик"))
print(my_box)

# Множества
set()

my_set = set([1,2,3,4,2,5,3,5,6,22,3,1,5])
print(my_set)

other_set = {3,6,8,5,4,3,7,5,9,22}
print(other_set)
# объединение
print(my_set | other_set)
# пересечения
print(my_set & other_set)
# вычитание
print(my_set - other_set)
print(other_set - my_set)