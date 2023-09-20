# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива.
# Input: 7 -> 3 1 3 4 2 4 12
#        6 -> 4 15 43 1 15 1
# Output: 3 3 2 12

from random import randint

def dif_lists(list_1, list_2):
    return [el for el in list_1 if el not in list_2]

n = int(input('Введите n: '))
m = int(input('Введите m: '))
list_1 = [randint(1, 20) for i in range(n)]
print(list_1)
list_2 = [randint(1, 20) for i in range(m)]
print(list_2)
list_3 = dif_lists(list_1, list_2)
print(list_3)