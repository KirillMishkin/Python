# -*- coding: utf-8 -*-
# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день
# спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который общий
# результат спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b и
# выводить одно натуральное число — номер дня.
#
# Например: a = 2, b = 3.
#
# Результат:
#
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22

a_km = int(input())  # первый день количество километров
b_km = int(input())  # за определенный день количество километров больше или равна введенному числу
day = 1
print(f'{day}-й день: {a_km}')  # Вывожу данные за первый день

while a_km < b_km:
    day += 1
    a_km = a_km + (a_km * 0.1)
    print(f'{round(day, 2)}-й день: {round(a_km, 2)}')
