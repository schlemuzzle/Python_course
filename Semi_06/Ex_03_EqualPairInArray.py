# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных строках.
# Input: 1 2 3 2 3
#        1 2 1 2 2 2 3 4
# Output: 2
#         7

from random import randint


def pairarr(list):
    count = 0
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] == list[j]:
                count += 1
    return count 

#or
def para(list):
    count = 0
    for i in range(len(list)):
        if list[i] == list[i:]:
            count += 1
    return count

#or

def count_p(list):
    count = 0
    for i, el in enumerate(list):
        count += list[i + 1:].count(el)
    return count

list1 = [randint(1, 20) for _ in range(int(input("Количество элементов в списке: ")))]
print(list1)
print(pairarr(list1))
print(count_p(list1))
list11 = [1, 2, 1, 2, 2, 2, 3, 4]
print(para(list11))






