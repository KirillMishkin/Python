# -*- coding: utf-8 -*-
# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.


number = int(input('введите целое положительное число '))

while number < 0:
    print('Ваше число меньше 0. Повторите попытку!')
    number = int(input('введите целое положительное число '))
else:
    number = str(number)

print(max(list(number)))
