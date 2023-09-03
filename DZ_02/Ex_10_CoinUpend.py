# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты 
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
# Input: 5 -> 1 0 1 1 0
# Output: 2

n = int(input('Введите количество монет: '))
count = 0
for i in range(n):
    side = int(input(f'Введите положение монеты {i+1}: '))
    if side == 0:
        count += 1
print(count)