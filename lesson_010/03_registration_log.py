# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

# TODO здесь ваш код

class NotNameError(Exception):
    pass

class NotEmailError(Exception):
    pass

class NotAgeError(Exception):
    pass

def registrations_bad(line, exc):
    file_name = 'registrations_bad.log'
    file = open(file_name, mode='a', encoding='UTF8')
    file.write(f'{line}, {exc}')
    file.write('\n')
    file.close()

# error = 0
error_line = 0
error_age = 0
error_name = 0
error_email = 0
total_error = 0

with open('registrations.txt', 'r', encoding='UTF8') as ff:
    for line in ff:
        line = line[:-1]
        try:
            # print(f'Read line {line}', flush=True)
            name, email, age = line.split(' ')
            print(f'Данные корректны {line}')
            age = int(age)
            if age < 10 or age > 99:
                raise NotAgeError(f'Возраст {age}')
            if email.find('@') == -1:
                raise NotEmailError(f'Email {email} указан не верно ')
            i = 9
            while i > 0:
                i_str = str(i)
                if name.find(i_str) != -1:
                    raise NotNameError(f'Имя {name} введено не верно')
                i -= 1
            file_name = 'registrations_good.log'
            file = open(file_name, mode='a', encoding='UTF8')
            file.write(line)
            file.write('\n')
            file.close()
        except NotNameError as exc:
            print(f'Неверное значение {exc}')
            error_name += 1
            registrations_bad(line, exc)
        except NotEmailError as exc:
            print(f'Неверное значение {exc}')
            error_email += 1
            registrations_bad(line, exc)
        except NotAgeError as exc:
            print(f'Неверное значение {exc}')
            error_age += 1
            registrations_bad(line, exc)
        except:
            print(f'Ошибка в данных в строке {line}')
            error_line += 1
            registrations_bad(line, exc='Ошибка в данных')
print(f'Ошибка имени в {error_name} строках')
print(f'Ошибка email в {error_email} строках')
print(f'Ошибка возраста в {error_age} строках')
print(f'Ошибка данных в {error_line} строках')
total_error = error_name + error_age + error_line + error_email
print(f'Всего ошибок в {total_error} строках')