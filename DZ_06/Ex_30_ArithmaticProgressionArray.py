# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов 
# нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Input: 7 2 5
# Output: 7 9 11 13 15

def progarr(a, d, n):
    result = []
    for i in range(1, n + 1):
        result.append(a + (i - 1) * d)
    return result

a = int(input('Введите первый элемент прогрессии: '))
d = int(input('Введите разность прогрессии: '))
n = int(input('Введите количество элементов прогрессии: '))
print(progarr(a, d, n))