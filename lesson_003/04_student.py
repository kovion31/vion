# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000

# TODO здесь ваш код
user_input = input("Введите, пожалуйста, количество месяцев: ")
month = int(user_input)
print('Вы ввели', month)

total_educational_grant = 0
total_expenses = 0
i = 1
while i <= month:
    total_educational_grant = educational_grant * i
    if i != 1:
        expenses += expenses * 0.03
    total_expenses += expenses
    i = i + 1
ask = total_expenses - total_educational_grant
print("Траты за", month, "месяцев", total_expenses, "рублей")
print("Стипендия за", month, "месяцев", total_educational_grant, "рублей")
print("Студенту надо попросить", ask, "рублей")

