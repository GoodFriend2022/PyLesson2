# Задача 14
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

def PowerTwo(number):
    count = 0
    power = []
    while 2 ** count <= number:
        power.append(2 ** count)
        count += 1
    return power

userNumber = int(input('Введите натуральное число > '))
print(PowerTwo(userNumber))

