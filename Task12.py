# Задача 12
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя
# делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

def Clue(mult, sum):
    y = 1
    while y * y - sum * y + mult != 0:
        if y > mult:
            break
        if y == sum:
            break
        y += 1
    if y > mult or y == sum:
        return 0
    x = sum - y
    return x, y

userMultiplication = int(input('Подскажите Кате чему равно произведение загаданных чисел > '))
userSum = int(input('Подскажите Кате чему равна сумма загаданных чисел > '))
if Clue(userMultiplication, userSum) == 0:
    print('Таких чисел не существует')
else:
    print(f' Кате загадали числа {Clue(userMultiplication, userSum)}')
