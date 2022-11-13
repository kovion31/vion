car = 'nissan'
my_list = []

my_list = [1, 2, 3, 'qwerty', 5]

print(my_list[:3])
print(my_list[::2])
print(my_list[-1])

my_list.append(77)
print(my_list)

my_list.extend([5, 5, 5])
print(my_list)

my_list.insert(3, 'aaa')
print(my_list)

del my_list[6]
print(my_list)

my_list.remove(5)
print(my_list)

my_list.append(car)
print(my_list)

print(my_list + [6,7,8])

print(my_list * 3)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[1][1])

print([1,2,3] > [1,2,4])

print(id(my_list))

print(my_list.count(5))

del my_list[3]
print(my_list)

my_list[1] = 300
print(my_list)

# список
print(list(range(10)))

print(list(range(0, 100, 5)))