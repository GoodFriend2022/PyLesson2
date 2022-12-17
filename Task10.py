# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки 
# были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

import random
def SideCoins(amountCoins):
    sides = []
    for i in range(amountCoins):
        side = random.randint(0, 1)
        sides.append(side)
    return sides

def CoinFlip(sidesCoins):
    firstSide = 0
    for i in sidesCoins:
        firstSide += i
    secondSide = len(sidesCoins) - firstSide
    if firstSide > secondSide:
        return secondSide
    return firstSide

userAmountCoins = int(input('Введите количество монет > '))
coins = SideCoins(userAmountCoins)
print(coins)
if CoinFlip(coins) == 0:
    print('Переворачивать ничего не надо')
else: print(f'Минимальное количество монет, которые необходимо перевернуть - {CoinFlip(coins)}')

